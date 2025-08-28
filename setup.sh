#!/bin/bash

# =============================================================================
# Elysia Concierge - Legendary Setup Script
# The Avant - Kairoi Residential
# =============================================================================

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Emojis for visual appeal
ROCKET="🚀"
CHECK="✅"
CROSS="❌"
WARNING="⚠️"
INFO="ℹ️"
SPARKLES="✨"
GEAR="🔧"
SHIELD="🛡️"
DOCS="📚"

echo -e "${PURPLE}${SPARKLES}=============================================================${SPARKLES}${NC}"
echo -e "${PURPLE}${ROCKET} Elysia Concierge - Legendary Setup ${ROCKET}${NC}"
echo -e "${PURPLE}${SPARKLES} The Avant - Kairoi Residential ${SPARKLES}${NC}"
echo -e "${PURPLE}${SPARKLES}=============================================================${SPARKLES}${NC}"
echo ""

# =============================================================================
# Helper Functions
# =============================================================================

log_info() {
    echo -e "${BLUE}${INFO} $1${NC}"
}

log_success() {
    echo -e "${GREEN}${CHECK} $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}${WARNING} $1${NC}"
}

log_error() {
    echo -e "${RED}${CROSS} $1${NC}"
}

check_command() {
    if command -v "$1" &> /dev/null; then
        log_success "$1 is installed"
        return 0
    else
        log_error "$1 is not installed"
        return 1
    fi
}

# =============================================================================
# System Requirements Check
# =============================================================================

log_info "Checking system requirements..."

# Check Python
if check_command python3; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    log_info "Python version: $PYTHON_VERSION"
    
    # Check if Python version is 3.9+
    if python3 -c "import sys; sys.exit(0 if sys.version_info >= (3, 9) else 1)"; then
        log_success "Python version is 3.9+ ✓"
    else
        log_error "Python 3.9+ is required. Please upgrade Python."
        exit 1
    fi
else
    log_error "Python 3 is required. Please install Python 3.9+."
    exit 1
fi

# Check Node.js (optional but recommended)
if check_command node; then
    NODE_VERSION=$(node --version)
    log_info "Node.js version: $NODE_VERSION"
else
    log_warning "Node.js not found. Install Node.js 20+ for full development experience."
fi

# Check pip
if check_command pip; then
    log_success "pip is available"
elif check_command pip3; then
    log_success "pip3 is available"
    alias pip=pip3
else
    log_error "pip is required. Please install pip."
    exit 1
fi

# Check make
if check_command make; then
    log_success "make is available for automation"
else
    log_warning "make not found. You can still use manual commands."
fi

echo ""

# =============================================================================
# Project Setup
# =============================================================================

log_info "Setting up Elysia Concierge project..."

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    log_info "Creating .env file from template..."
    cp .env.example .env
    log_success "Created .env file"
    log_warning "Please edit .env file with your configuration"
else
    log_info ".env file already exists"
fi

# Create virtual environment
log_info "Setting up Python virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    log_success "Created virtual environment"
else
    log_info "Virtual environment already exists"
fi

# Activate virtual environment
log_info "Activating virtual environment..."
source venv/bin/activate
log_success "Virtual environment activated"

# Upgrade pip
log_info "Upgrading pip..."
pip install --upgrade pip

# Install Python dependencies
log_info "Installing Python dependencies..."
pip install -r backend/requirements-ci.txt
log_success "Python dependencies installed"

# Install development tools
log_info "Installing development tools..."
pip install black isort flake8 pre-commit bandit safety
log_success "Development tools installed"

# Install pre-commit hooks
log_info "Setting up pre-commit hooks..."
pre-commit install
log_success "Pre-commit hooks installed"

echo ""

# =============================================================================
# Validation Tests
# =============================================================================

log_info "Running validation tests..."

# Test imports
log_info "Testing Python imports..."
python3 -c "
import fastapi
import uvicorn
import pydantic
print('Core dependencies imported successfully')
"
log_success "Python imports working"

# Run tests
log_info "Running test suite..."
if pytest tests -v --tb=short; then
    log_success "All tests passed!"
else
    log_warning "Some tests failed, but setup continues..."
fi

echo ""

# =============================================================================
# Quick Start Demo
# =============================================================================

log_info "Testing development server..."

# Start server in background
log_info "Starting development server..."
python3 -m uvicorn backend.elysia_lite:app --host 0.0.0.0 --port 8000 &
SERVER_PID=$!

# Wait for server to start
sleep 5

# Test health endpoint
log_info "Testing health endpoint..."
if curl -f http://localhost:8000/health > /dev/null 2>&1; then
    log_success "Health endpoint working!"
    
    # Test API endpoints
    log_info "Testing API endpoints..."
    if curl -f http://localhost:8000/api/elysia/amenities > /dev/null 2>&1; then
        log_success "API endpoints working!"
    else
        log_warning "API endpoints may have issues"
    fi
else
    log_warning "Health endpoint not responding"
fi

# Stop server
kill $SERVER_PID 2>/dev/null || true
log_info "Development server stopped"

echo ""

# =============================================================================
# Final Instructions
# =============================================================================

echo -e "${GREEN}${SPARKLES}=============================================================${SPARKLES}${NC}"
echo -e "${GREEN}${CHECK} Elysia Concierge Setup Complete! ${CHECK}${NC}"
echo -e "${GREEN}${SPARKLES}=============================================================${SPARKLES}${NC}"
echo ""

echo -e "${CYAN}${ROCKET} Quick Start Commands:${NC}"
echo ""
echo -e "${YELLOW}  Development:${NC}"
echo -e "    make dev                 # Start with mock AI"
echo -e "    make dev-llamacpp        # Start with llama-cpp"  
echo -e "    make dev-bloom           # Start with BLOOM"
echo -e "    make health              # Check application health"
echo -e "    make demo                # Run demo sequence"
echo ""
echo -e "${YELLOW}  Testing:${NC}"
echo -e "    make test                # Run all tests"
echo -e "    make test-cov            # Run tests with coverage"
echo ""
echo -e "${YELLOW}  Code Quality:${NC}"
echo -e "    make format              # Format code"
echo -e "    make lint                # Run linting"
echo -e "    make security            # Security scan"
echo ""
echo -e "${YELLOW}  Docker (Alternative):${NC}"
echo -e "    docker-compose up        # Start full environment"
echo -e "    docker-compose down      # Stop environment"
echo ""

echo -e "${CYAN}${DOCS} Documentation:${NC}"
echo -e "  • API Docs: http://localhost:8000/docs"
echo -e "  • Redoc: http://localhost:8000/redoc" 
echo -e "  • CONTRIBUTING.md for development guidelines"
echo -e "  • README.md for detailed setup instructions"
echo ""

echo -e "${CYAN}${GEAR} Next Steps:${NC}"
echo -e "  1. Edit .env file with your configuration"
echo -e "  2. Review CONTRIBUTING.md for development workflow"
echo -e "  3. Run 'make dev' to start development server"
echo -e "  4. Visit http://localhost:8000/docs for API documentation"
echo -e "  5. Run 'make demo' to test functionality"
echo ""

echo -e "${PURPLE}${SPARKLES} Welcome to The Avant's AI Concierge System! ${SPARKLES}${NC}"
echo -e "${PURPLE}Building the future of luxury apartment living... ${ROCKET}${NC}"
echo ""

# Deactivate virtual environment
deactivate 2>/dev/null || true