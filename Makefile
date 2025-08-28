# Elysia Concierge - Development Automation
# The Avant - Kairoi Residential
# Usage: make <target>

.PHONY: help install dev test lint format clean docs build deploy health

# =============================================================================
# Help & Information
# =============================================================================

help: ## Show this help message
	@echo "🏗️  Elysia Concierge - The Avant Development Commands"
	@echo ""
	@echo "Available commands:"
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z_-]+:.*##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
	@echo ""
	@echo "Environment Variables:"
	@echo "  ELYSIA_USE_LLAMACPP=true    - Enable llama-cpp-python"
	@echo "  ELYSIA_USE_BLOOM=true       - Enable BLOOM model"
	@echo "  ELYSIA_USE_HOSTED=true      - Enable hosted inference"
	@echo "  DEBUG=true                  - Enable debug mode"

# =============================================================================
# Environment Setup
# =============================================================================

.env: ## Create .env file from template
	@if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo "✅ Created .env file from template"; \
		echo "📝 Please edit .env with your configuration"; \
	else \
		echo "⚠️  .env file already exists"; \
	fi

install-dev: .env ## Install all development dependencies
	@echo "🔧 Installing Python development dependencies..."
	cd backend && python -m pip install --upgrade pip
	cd backend && pip install -r requirements-ci.txt
	@echo "🔧 Installing pre-commit hooks..."
	pip install pre-commit
	pre-commit install
	@echo "✅ Development environment ready!"

install-full: .env ## Install full production dependencies
	@echo "🔧 Installing Python production dependencies..."
	cd backend && python -m pip install --upgrade pip
	cd backend && pip install -r requirements.txt
	@echo "✅ Production environment ready!"

install-frontend: ## Install frontend dependencies
	@if [ -d "frontend" ] && [ -f "frontend/package.json" ]; then \
		echo "🔧 Installing frontend dependencies..."; \
		cd frontend && npm install; \
		echo "✅ Frontend dependencies installed!"; \
	else \
		echo "ℹ️  No frontend package.json found, skipping"; \
	fi

install-mobile: ## Install mobile dependencies
	@if [ -d "mobile" ] && [ -f "mobile/package.json" ]; then \
		echo "🔧 Installing mobile dependencies..."; \
		cd mobile && npm install; \
		echo "✅ Mobile dependencies installed!"; \
	else \
		echo "ℹ️  No mobile package.json found, skipping"; \
	fi

install: install-dev install-frontend install-mobile ## Install all dependencies

# =============================================================================
# Development
# =============================================================================

dev: .env ## Start development server with mock AI
	@echo "🚀 Starting Elysia Concierge development server..."
	cd backend && python -m uvicorn elysia_lite:app --reload --host 0.0.0.0 --port 8000

dev-llamacpp: .env ## Start development server with llama-cpp
	@echo "🚀 Starting Elysia with llama-cpp-python..."
	cd backend && ELYSIA_USE_LLAMACPP=true python -m uvicorn elysia_lite:app --reload --host 0.0.0.0 --port 8000

dev-bloom: .env ## Start development server with BLOOM
	@echo "🚀 Starting Elysia with BLOOM model..."
	cd backend && ELYSIA_USE_BLOOM=true python -m uvicorn elysia_lite:app --reload --host 0.0.0.0 --port 8000

dev-hosted: .env ## Start development server with hosted inference
	@echo "🚀 Starting Elysia with hosted inference..."
	@echo "⚠️  Make sure ELYSIA_HF_API_KEY is set in .env"
	cd backend && ELYSIA_USE_HOSTED=true python -m uvicorn elysia_lite:app --reload --host 0.0.0.0 --port 8000

# =============================================================================
# Testing
# =============================================================================

test: ## Run all tests
	@echo "🧪 Running tests..."
	pytest tests -v

test-cov: ## Run tests with coverage report
	@echo "🧪 Running tests with coverage..."
	pytest tests --cov=backend --cov-report=html --cov-report=term-missing

test-unit: ## Run unit tests only
	@echo "🧪 Running unit tests..."
	pytest tests -m "not integration" -v

test-integration: ## Run integration tests only
	@echo "🧪 Running integration tests..."
	pytest tests -m integration -v

test-api: ## Test API endpoints
	@echo "🧪 Testing API endpoints..."
	pytest tests/test_api.py -v

test-watch: ## Run tests in watch mode
	@echo "🧪 Running tests in watch mode..."
	pytest-watch tests

# =============================================================================
# Code Quality
# =============================================================================

lint: ## Run all linting tools
	@echo "🔍 Running linting tools..."
	black --check backend/ tests/
	isort --check-only backend/ tests/
	flake8 backend/ tests/
	mypy backend/

format: ## Format code with black and isort
	@echo "🎨 Formatting code..."
	black backend/ tests/
	isort backend/ tests/
	@echo "✅ Code formatted!"

format-check: ## Check code formatting without changes
	@echo "🔍 Checking code formatting..."
	black --check backend/ tests/
	isort --check-only backend/ tests/

security: ## Run security scans
	@echo "🛡️  Running security scans..."
	bandit -r backend/ -f json -o bandit-report.json || true
	@echo "📋 Security report saved to bandit-report.json"

pre-commit: ## Run pre-commit hooks on all files
	@echo "🔍 Running pre-commit hooks..."
	pre-commit run --all-files

# =============================================================================
# Health Checks
# =============================================================================

health: ## Check application health
	@echo "🩺 Checking application health..."
	curl -f http://localhost:8000/health || echo "❌ Health check failed"

status: ## Check Elysia status and amenities
	@echo "📊 Checking Elysia status..."
	curl -s http://localhost:8000/api/elysia/amenities | python -m json.tool || echo "❌ Status check failed"

logs: ## Show application logs
	@echo "📋 Application logs:"
	@if [ -f "backend/elysia_concierge.log" ]; then \
		tail -n 50 backend/elysia_concierge.log; \
	else \
		echo "No log file found"; \
	fi

# =============================================================================
# Documentation
# =============================================================================

docs: ## Generate and serve documentation
	@echo "📚 Serving documentation..."
	@echo "API Docs: http://localhost:8000/docs"
	@echo "Redoc: http://localhost:8000/redoc"
	@echo "Development docs:"
	cd docs && python -m http.server 8080

docs-build: ## Build documentation
	@echo "📚 Building documentation..."
	@echo "ℹ️  Documentation build target not implemented yet"

# =============================================================================
# Database
# =============================================================================

db-reset: ## Reset database (development only)
	@echo "🗃️  Resetting database..."
	@echo "⚠️  This will delete all data!"
	@read -p "Are you sure? (y/N): " confirm && [ "$$confirm" = "y" ]
	# Add database reset commands here when implemented

db-migrate: ## Run database migrations
	@echo "🗃️  Running database migrations..."
	# Add migration commands here when implemented

# =============================================================================
# Cleanup
# =============================================================================

clean: ## Clean up temporary files
	@echo "🧹 Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	rm -f bandit-report.json
	@echo "✅ Cleanup complete!"

clean-all: clean ## Clean everything including dependencies
	@echo "🧹 Deep cleaning..."
	rm -rf backend/venv/
	rm -rf frontend/node_modules/
	rm -rf mobile/node_modules/
	@echo "✅ Deep cleanup complete!"

# =============================================================================
# Quick Tests
# =============================================================================

quick-test: ## Quick API test
	@echo "⚡ Quick API test..."
	curl -X POST "http://localhost:8000/api/elysia/request" \
		-H "Content-Type: application/json" \
		-d '{"resident_id": "AVT-RES-304-001", "unit_number": "304", "request_type": "maintenance", "message": "Test request from Makefile", "priority": "medium"}' | python -m json.tool

demo: ## Run a demo sequence
	@echo "🎬 Running Elysia demo..."
	@echo "1️⃣  Testing amenities endpoint..."
	curl -s http://localhost:8000/api/elysia/amenities | python -m json.tool
	@echo ""
	@echo "2️⃣  Testing maintenance request..."
	curl -X POST "http://localhost:8000/api/elysia/request" \
		-H "Content-Type: application/json" \
		-d '{"resident_id": "AVT-RES-101-001", "unit_number": "101", "request_type": "maintenance", "message": "Demo: Kitchen faucet is dripping", "priority": "low"}' | python -m json.tool
	@echo ""
	@echo "🎉 Demo complete!"

# =============================================================================
# Development Utilities
# =============================================================================

shell: ## Open Python shell with app context
	@echo "🐍 Opening Python shell..."
	cd backend && python -c "from elysia_lite import app; import IPython; IPython.embed()"

requirements: ## Update requirements files
	@echo "📦 Updating requirements..."
	cd backend && pip-compile requirements.in
	@echo "✅ Requirements updated!"

check-env: ## Check environment configuration
	@echo "🔍 Environment check:"
	@echo "Python: $(shell python --version)"
	@echo "Node.js: $(shell node --version 2>/dev/null || echo 'Not installed')"
	@echo "Current directory: $(shell pwd)"
	@echo "Virtual environment: $(shell echo $$VIRTUAL_ENV || echo 'None')"
	@test -f .env && echo ".env file: ✅" || echo ".env file: ❌"

# =============================================================================
# Default
# =============================================================================

.DEFAULT_GOAL := help