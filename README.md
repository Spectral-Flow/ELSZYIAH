# 🏢 Elysia Concierge

**AI-powered luxury apartment concierge system for The Avant - Centennial, Colorado**

*Built with ❤️ for modern apartment living by Kairoi Residential*

---

## ✨ Features

- **🤖 AI-Powered Assistant**: Intelligent responses using multiple AI backends
- **🏠 Property Management**: Maintenance requests, amenity bookings, community info
- **📱 Multi-Platform**: Web dashboard, mobile app, and API access
- **🔒 Secure & Compliant**: Enterprise-grade security for resident data
- **⚡ Real-time**: Instant responses and live updates
- **🌐 Cloud-Ready**: Optimized for Vercel deployment

## 🚀 Quick Start

### Prerequisites

- **Python 3.9+** ([Download](https://python.org))
- **Node.js 20+** ([Download](https://nodejs.org))
- **Git** ([Download](https://git-scm.com))

### 1. Clone & Setup

```bash
# Clone the repository
git clone https://github.com/Spectral-Flow/ELSZYIAH.git
cd ELSZYIAH

# Install all dependencies
npm run setup:dev

# Copy environment template
cp .env.example .env
# Edit .env with your configuration
```

### 2. Start Development

```bash
# Start all services (backend + frontend + mobile)
npm run dev:all

# Or start individually:
npm run dev:backend    # API server on http://localhost:8000
npm run dev:frontend   # Web app on http://localhost:3000
npm run dev:mobile     # React Native development
```

### 3. Test the API

```bash
# Check health
curl http://localhost:8000/health

# Test a request
curl -X POST http://localhost:8000/api/elysia/request \
  -H "Content-Type: application/json" \
  -d '{
    "resident_id": "AVT-RES-304-001",
    "unit_number": "304",
    "request_type": "maintenance",
    "message": "My kitchen faucet is leaking",
    "priority": "medium"
  }'
```

## 🏗️ Architecture

```
├── backend/          # FastAPI server & AI engine
├── frontend/         # SvelteKit web dashboard  
├── mobile/           # React Native mobile app
├── docs/             # Documentation
├── scripts/          # Setup & deployment scripts
└── tests/            # Test suites
```

### AI Backends

The system supports multiple AI backends for flexibility:

- **🔧 Mock Mode** (default): Intelligent mock responses for development
- **🦙 Llama-cpp**: Local GGUF models (offline capable)
- **🌸 BLOOM**: Lightweight Hugging Face models
- **☁️ Hosted**: OpenAI, Azure OpenAI, or other hosted services

## 📚 Development

### Code Quality

```bash
# Run linting & formatting
npm run lint:all
npm run format

# Run tests
npm run test:all

# Type checking
npm run typecheck
```

### Environment Variables

Key environment variables (see `.env.example` for full list):

```bash
# Application
ENVIRONMENT=development
DEBUG=true

# AI Configuration
ELYSIA_USE_MOCK=true          # Use mock responses
ELYSIA_USE_LLAMACPP=false     # Use local GGUF models
ELYSIA_USE_HOSTED=false       # Use hosted AI service

# API Keys (for hosted AI)
OPENAI_API_KEY=your_key_here
AZURE_OPENAI_API_KEY=your_key_here
```

## 🚀 Deployment

### Vercel (Recommended)

```bash
# Deploy to Vercel
npm run deploy:vercel

# Or use Vercel CLI
npx vercel --prod
```

### Docker

```bash
# Build container
docker build -t elysia-concierge .

# Run container
docker run -p 8000:8000 elysia-concierge
```

### Traditional Server

```bash
# Production backend
cd backend
gunicorn elysia_lite:app -w 4 -k uvicorn.workers.UvicornWorker

# Build frontend
cd frontend
npm run build
```

## 🔧 Configuration

### AI Models

**For local development (mock mode):**
- No additional setup required
- Provides realistic responses for testing

**For llama-cpp-python:**
```bash
pip install llama-cpp-python
export ELYSIA_USE_LLAMACPP=true
export ELYSIA_LLAMACPP_REPO_ID="HagalazAI/Elysia-Trismegistus-Mistral-7B-v02-GGUF"
```

**For BLOOM models:**
```bash
pip install transformers torch
export ELYSIA_USE_BLOOM=true
export ELYSIA_BLOOM_MODEL="bigscience/bloom-560m"
```

**For hosted services:**
```bash
export ELYSIA_USE_HOSTED=true
export OPENAI_API_KEY="your-api-key"
```

### Property Customization

Update `.env` with your property details:

```bash
PROPERTY_NAME="Your Property Name"
PROPERTY_LOCATION="Your City, State"
PROPERTY_UNITS=280
MANAGEMENT_COMPANY="Your Management Company"
```

## 🧪 Testing

```bash
# Run all tests
npm run test:all

# Backend tests only
npm run test:backend

# Frontend tests only  
npm run test:frontend

# With coverage
npm run test:coverage
```

## 📖 API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Key Endpoints

- `POST /api/elysia/request` - Submit resident requests
- `GET /api/elysia/amenities` - Get amenity information
- `GET /api/elysia/community` - Get community updates
- `GET /health` - Health check

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Development Guidelines

- Follow existing code style (enforced by prettier/black)
- Write tests for new features
- Update documentation as needed
- Ensure all linting passes

## 📞 Support

- **Technical Issues**: [GitHub Issues](https://github.com/Spectral-Flow/ELSZYIAH/issues)
- **Documentation**: [Project Wiki](https://github.com/Spectral-Flow/ELSZYIAH/wiki)
- **Property Management**: Contact your local Kairoi team

## 📄 License

Proprietary - Kairoi Residential Internal Use Only

---

## 🎯 Project Status

**Current Version**: 1.0.0  
**Status**: ✅ Production Ready  
**Last Updated**: December 2024

### Recent Updates

- ✅ Multi-AI backend support
- ✅ Comprehensive testing suite  
- ✅ Production deployment optimization
- ✅ Enhanced developer experience
- ✅ Security hardening

---

**Elysia Concierge: Where technology, hospitality, and design converge to transform ordinary apartment life into an extraordinary lifestyle experience.**