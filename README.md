# Elysia Concierge 🏗️✨

**AI-powered concierge system for The Avant luxury apartments - Kairoi Residential**

[![CI/CD](https://github.com/Spectral-Flow/ELSZYIAH/actions/workflows/ci.yml/badge.svg)](https://github.com/Spectral-Flow/ELSZYIAH/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-Proprietary-red.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> **🎯 Mission**: Transform ordinary apartment living into an extraordinary lifestyle experience through AI-powered hospitality and intelligent automation.

## 🌟 What Makes This Legendary

- **🧠 Multi-AI Engine Support**: Mock, llama-cpp, BLOOM, OpenAI, Azure OpenAI
- **🏗️ Production-Ready Architecture**: FastAPI, PostgreSQL, Redis, Docker
- **🔒 Security First**: Pre-commit hooks, security scanning, environment validation
- **🧪 Comprehensive Testing**: Unit, integration, API, and performance tests  
- **📦 One-Command Setup**: Automated development environment configuration
- **🐳 Docker Support**: Full containerized development stack
- **📊 Monitoring & Health**: Built-in health checks and observability
- **🔄 CI/CD Pipeline**: Automated testing, security, and deployment

## 🚀 Lightning-Fast Setup

### Option 1: Automated Setup (Recommended)

```bash
# Clone and setup in one go
git clone https://github.com/Spectral-Flow/ELSZYIAH.git
cd ELSZYIAH
./setup.sh
```

### Option 2: Manual Setup

```bash
# Clone repository
git clone https://github.com/Spectral-Flow/ELSZYIAH.git
cd ELSZYIAH

# Quick setup
make install-dev
source venv/bin/activate

# Start development server
make dev
```

### Option 3: Docker Setup

```bash
# Full environment with database
docker-compose up --build

# API only
docker-compose up elysia-api
```

## 🎮 Quick Commands

| Command | Description |
|---------|-------------|
| `make dev` | Start with mock AI (instant) |
| `make dev-llamacpp` | Start with llama-cpp models |
| `make dev-bloom` | Start with BLOOM models |
| `make test` | Run comprehensive test suite |
| `make demo` | Interactive demo sequence |
| `make health` | Check system health |
| `make format` | Auto-format code |
| `make security` | Security scan |

## 🏗️ Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Mobile App    │    │   API Gateway   │
│  (SvelteKit)    │    │ (React Native)  │    │   (FastAPI)     │
└─────────┬───────┘    └─────────┬───────┘    └─────────┬───────┘
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 │
                    ┌─────────────┴───────────┐
                    │    Elysia AI Core      │
                    │  (Multi-Engine Support) │
                    └─────────────┬───────────┘
                                 │
          ┌──────────────────────┼──────────────────────┐
          │                      │                      │
┌─────────▼───────┐    ┌─────────▼───────┐    ┌─────────▼───────┐
│   PostgreSQL    │    │      Redis      │    │   External APIs │
│   (Database)    │    │     (Cache)     │    │ (Property Mgmt) │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🎯 AI Engine Options

### 🚀 Instant Development (Default)
```bash
make dev  # Uses intelligent mock AI
```

### 🧠 Local AI Models  
```bash
# BLOOM (smallest, fastest)
make dev-bloom

# llama-cpp (GGUF models, powerful)
make dev-llamacpp
```

### ☁️ Cloud AI Services
```bash
# Hosted Hugging Face
ELYSIA_USE_HOSTED=true make dev

# Azure OpenAI (production recommended)
ELYSIA_USE_AZURE_OPENAI=true make dev
```

## 🏠 The Avant Features

### 🤖 AI Concierge Capabilities
- **Maintenance Requests**: "My kitchen faucet is leaking"
- **Amenity Booking**: "Reserve the fitness center for 7 AM"
- **Package Inquiries**: "Is my Amazon delivery ready?"
- **Guest Access**: "Add visitor access for John Smith today"
- **Community Events**: "What's happening this weekend?"
- **Local Recommendations**: Cherry Creek, Centennial area knowledge

### 🏢 Property Management
- **280 Units** across 12 floors
- **Premium Amenities**: Fitness center, pool, clubhouse, coworking
- **Smart Building**: IoT integration, access control
- **Location Intelligence**: Centennial, CO area expertise

## 🧪 Testing Strategy

```bash
# Run all tests
make test

# Coverage report
make test-cov

# Integration tests
make test-integration

# API endpoint tests  
make test-api

# Watch mode for development
make test-watch
```

## 🔒 Security & Quality

### Automated Code Quality
- **Black**: Code formatting
- **isort**: Import sorting  
- **flake8**: Linting
- **mypy**: Type checking
- **bandit**: Security scanning
- **pre-commit**: Git hooks

### Security Features
- Environment variable validation
- SQL injection prevention
- CORS configuration
- Rate limiting ready
- Secrets detection

## 📊 Monitoring & Health

### Health Checks
```bash
# Application health
curl http://localhost:8000/health

# API status  
curl http://localhost:8000/api/elysia/amenities

# System check
make health
```

### Observability
- Structured logging
- Prometheus metrics ready
- Health check endpoints
- Error tracking integration

## 🐳 Docker Development

### Full Stack
```bash
# Complete environment
docker-compose --profile frontend --profile admin up

# Database admin at http://localhost:5050
# Redis admin at http://localhost:8081
```

### Services Available
- **elysia-api**: Main application
- **postgres**: Database
- **redis**: Cache  
- **pgadmin**: Database admin
- **redis-commander**: Redis admin

## 🌍 Environment Configuration

Copy `.env.example` to `.env` and customize:

```bash
# Core Settings
ENVIRONMENT=development
DEBUG=true
SECRET_KEY=your-secure-secret-key

# AI Configuration  
ELYSIA_USE_LLAMACPP=false
ELYSIA_USE_BLOOM=false
AZURE_OPENAI_API_KEY=your-key-here

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/elysia
REDIS_URL=redis://localhost:6379/0
```

## 📚 API Documentation

### Interactive Documentation
- **Swagger UI**: http://localhost:8000/docs
- **Redoc**: http://localhost:8000/redoc

### Key Endpoints
- `POST /api/elysia/request` - Submit resident request
- `GET /api/elysia/amenities` - Get amenity information
- `GET /api/elysia/community` - Community & building info
- `GET /health` - Application health check

### Example Request
```bash
curl -X POST "http://localhost:8000/api/elysia/request" \
  -H "Content-Type: application/json" \
  -d '{
    "resident_id": "AVT-RES-304-001",
    "unit_number": "304", 
    "request_type": "maintenance",
    "message": "Kitchen faucet is leaking",
    "priority": "medium"
  }'
```

## 🚀 Deployment

### Development
```bash
make dev                    # Local development
docker-compose up          # Containerized development
```

### Production
```bash
# Vercel (API deployment)
vercel --prod

# Docker (full stack)
docker-compose -f docker-compose.prod.yml up
```

### Environment Variables for Production
Set these in your deployment platform:

```bash
ENVIRONMENT=production
SECRET_KEY=your-production-secret
DATABASE_URL=your-production-db-url
AZURE_OPENAI_API_KEY=your-production-ai-key
SENTRY_DSN=your-error-tracking-dsn
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:

- Development workflow
- Code style guidelines  
- Testing requirements
- Pull request process

### Quick Contribution Setup
```bash
git clone https://github.com/Spectral-Flow/ELSZYIAH.git
cd ELSZYIAH
./setup.sh
make dev
# Make your changes
make test
make format
git commit -m "feat: your amazing feature"
```

## 📋 Project Structure

```
ELSZYIAH/
├── backend/              # FastAPI application
│   ├── elysia_lite.py   # Main application
│   ├── elysia_concierge.py  # Full version
│   └── requirements*.txt
├── frontend/            # SvelteKit frontend (planned)
├── mobile/              # React Native app (planned)
├── tests/               # Test suite
├── docs/                # Documentation
├── scripts/             # Automation scripts
├── docker-compose.yml   # Development environment
├── Makefile            # Task automation
├── pyproject.toml      # Python configuration
└── .env.example        # Environment template
```

## 🏆 Success Metrics

### Resident Experience
- **Response Time**: < 2 seconds for AI responses
- **Resolution Rate**: > 90% first-contact resolution
- **Satisfaction**: > 4.5/5.0 average rating
- **Engagement**: > 80% monthly active users

### Technical Performance
- **Uptime**: 99.9% availability SLA
- **API Performance**: < 500ms response times
- **Scalability**: 500+ concurrent users
- **Security**: Zero data breaches

## 📞 Support & Resources

- **Documentation**: [docs/](docs/)
- **API Reference**: http://localhost:8000/docs
- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions
- **Security**: Report privately to security team

## 📄 License

This project is proprietary software owned by Kairoi Residential. All rights reserved.

---

**🏗️ Built with ❤️ for The Avant residents by Kairoi Residential Technology Team**

*Transforming apartment living through AI-powered hospitality and innovation* ✨