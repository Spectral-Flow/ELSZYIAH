# 🛠️ Developer Guide

## Elysia Concierge Development

Comprehensive guide for developers working on the Elysia Concierge system.

## 🚀 Quick Start

```bash
# Clone and setup
git clone https://github.com/Spectral-Flow/ELSZYIAH.git
cd ELSZYIAH
npm run setup:dev

# Start development
npm run dev:all
```

## 📁 Project Structure

```
ELSZYIAH/
├── backend/                 # Python FastAPI backend
│   ├── elysia_lite.py      # Main API server
│   ├── elysia_concierge.py # Full-featured version
│   └── requirements*.txt   # Python dependencies
├── frontend/               # Web dashboard
│   ├── index.html          # Main HTML file
│   ├── package.json        # Frontend dependencies
│   └── vite.config.js      # Build configuration
├── mobile/                 # React Native mobile app
│   ├── src/App.tsx         # Main app component
│   └── package.json        # Mobile dependencies
├── tests/                  # Test suites
│   ├── test_api.py         # API tests
│   └── test_*_adapter.py   # AI adapter tests
├── docs/                   # Documentation
├── scripts/                # Deployment scripts
├── .github/workflows/      # CI/CD pipelines
├── docker-compose.yml      # Local development stack
├── Dockerfile              # Container definition
├── pyproject.toml          # Python project configuration
├── .env.example            # Environment template
└── package.json            # Root workspace configuration
```

## 🔧 Development Setup

### Environment Configuration

1. **Copy environment template:**
   ```bash
   cp .env.example .env
   ```

2. **Edit configuration:**
   ```bash
   # Required settings
   ENVIRONMENT=development
   DEBUG=true
   PROPERTY_NAME="Your Property Name"
   
   # AI Configuration (choose one)
   ELYSIA_USE_MOCK=true          # Mock responses (default)
   ELYSIA_USE_LLAMACPP=true      # Local GGUF models
   ELYSIA_USE_BLOOM=true         # Hugging Face BLOOM
   ELYSIA_USE_HOSTED=true        # OpenAI/Azure OpenAI
   ```

### Development Scripts

```bash
# Setup all dependencies
npm run setup:dev

# Start all services
npm run dev:all

# Individual services
npm run dev:backend    # API server on :8000
npm run dev:frontend   # Web app on :3000
npm run dev:mobile     # React Native development

# Code quality
npm run lint:all       # Run all linters
npm run format         # Format all code
npm run test:all       # Run all tests
```

## 🏗️ Backend Development

### API Structure

The backend uses FastAPI with the following key components:

- **elysia_lite.py**: Lightweight version for Vercel deployment
- **elysia_concierge.py**: Full-featured version with all capabilities
- **AI Adapters**: Pluggable AI backends (mock, llama-cpp, BLOOM, hosted)

### Adding New Endpoints

```python
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1")

class NewRequest(BaseModel):
    data: str

@router.post("/new-endpoint")
async def new_endpoint(request: NewRequest):
    return {"status": "success", "data": request.data}

# Add to main app
app.include_router(router)
```

### AI Backend Integration

```python
# Create new AI adapter
class CustomAIAdapter:
    async def generate_response(self, request: ResidentRequest) -> str:
        # Your AI logic here
        return "AI generated response"

# Register adapter
from elysia_lite import AIEngine
engine = AIEngine()
engine.register_adapter("custom", CustomAIAdapter())
```

### Testing Backend

```bash
# Run all tests
npm run test:backend

# Run specific test file
python -m pytest tests/test_api.py -v

# Run with coverage
python -m pytest tests/ --cov=backend --cov-report=html
```

## 🎨 Frontend Development

### Technology Stack

- **Build Tool**: Vite
- **Styling**: Modern CSS with CSS Grid/Flexbox
- **API Integration**: Fetch API with proxy configuration

### Development Server

```bash
cd frontend
npm run dev
```

The frontend runs on http://localhost:3000 with API proxy to backend.

### Adding New Features

```html
<!-- Add to index.html -->
<div class="new-feature">
    <h3>New Feature</h3>
    <button onclick="handleNewFeature()">Click Me</button>
</div>

<script>
async function handleNewFeature() {
    try {
        const response = await fetch('/api/new-endpoint', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({data: 'test'})
        });
        const result = await response.json();
        console.log(result);
    } catch (error) {
        console.error('Error:', error);
    }
}
</script>
```

## 📱 Mobile Development

### React Native Setup

```bash
cd mobile
npm install

# iOS (requires macOS and Xcode)
npm run ios

# Android (requires Android Studio)
npm run android
```

### Adding New Screens

```tsx
// mobile/src/screens/NewScreen.tsx
import React from 'react';
import {View, Text, StyleSheet} from 'react-native';

const NewScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>New Screen</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
  },
});

export default NewScreen;
```

## 🧪 Testing

### Backend Testing

```bash
# All tests
python -m pytest tests/ -v

# Specific test
python -m pytest tests/test_api.py::test_health -v

# With coverage
python -m pytest tests/ --cov=backend --cov-report=term-missing
```

### Writing Tests

```python
# tests/test_new_feature.py
import pytest
from fastapi.testclient import TestClient
from backend.elysia_lite import app

client = TestClient(app)

def test_new_endpoint():
    response = client.post("/api/new-endpoint", 
                          json={"data": "test"})
    assert response.status_code == 200
    assert response.json()["status"] == "success"
```

### Frontend Testing

```bash
cd frontend
npm test
```

## 🔍 Code Quality

### Linting and Formatting

```bash
# Python
black backend/              # Format code
isort backend/              # Sort imports
mypy backend/               # Type checking
flake8 backend/             # Linting

# JavaScript/TypeScript
eslint frontend/ --fix      # Lint and fix
prettier --write frontend/  # Format

# All at once
npm run lint:all
npm run format
```

### Pre-commit Hooks

Pre-commit hooks automatically run on `git commit`:

```bash
# Install hooks
npm run setup:tools

# Run manually
npx lint-staged
```

### Code Style Guidelines

**Python:**
- Follow PEP 8
- Use Black for formatting (88 character line length)
- Use type hints
- Write docstrings for functions

**TypeScript/JavaScript:**
- Use Prettier for formatting
- Follow ESLint rules
- Use meaningful variable names
- Add JSDoc comments for complex functions

## 📊 Debugging

### Backend Debugging

```bash
# Enable debug mode
export DEBUG=true

# Start with reload
python -m uvicorn backend.elysia_lite:app --reload --log-level debug

# View logs
tail -f logs/elysia.log
```

### API Testing

```bash
# Health check
curl http://localhost:8000/health

# Submit request
curl -X POST http://localhost:8000/api/elysia/request \
  -H "Content-Type: application/json" \
  -d '{
    "resident_id": "test-001",
    "unit_number": "101",
    "request_type": "maintenance",
    "message": "Test request",
    "priority": "low"
  }'

# Interactive API docs
open http://localhost:8000/docs
```

### Database Inspection

```bash
# SQLite (development)
sqlite3 elysia.db ".tables"
sqlite3 elysia.db "SELECT * FROM requests LIMIT 5;"

# PostgreSQL (production)
psql elysia_concierge -c "SELECT * FROM requests LIMIT 5;"
```

## 🔄 Git Workflow

### Branch Strategy

```bash
# Feature development
git checkout -b feature/new-feature
git commit -m "Add new feature"
git push origin feature/new-feature

# Create PR on GitHub
```

### Commit Messages

Follow conventional commits:

```bash
feat: add new API endpoint for amenity booking
fix: resolve authentication token validation
docs: update deployment guide
test: add unit tests for AI adapters
chore: update dependencies
```

## 🚀 CI/CD

### GitHub Actions

The repository includes automated CI/CD:

- **Code Quality**: Linting, formatting, type checking
- **Testing**: Unit tests, integration tests
- **Security**: Vulnerability scanning
- **Deployment**: Automatic Vercel deployment on main branch

### Running CI Locally

```bash
# Simulate CI checks
npm run lint:check
npm run test:all

# Security scanning
pip install safety bandit
safety check -r requirements.txt
bandit -r backend/
```

## 📦 Deployment

### Development Deployment

```bash
# Docker development
docker-compose up -d

# Check status
docker-compose ps
docker-compose logs -f elysia-backend
```

### Production Deployment

See [DEPLOYMENT.md](./DEPLOYMENT.md) for comprehensive deployment guide.

## 🤝 Contributing

### Pull Request Process

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Add** tests for new functionality
5. **Ensure** all tests pass
6. **Submit** a pull request

### Code Review Checklist

- [ ] Code follows style guidelines
- [ ] Tests added for new features
- [ ] Documentation updated
- [ ] No breaking changes
- [ ] Performance impact considered

## 🆘 Troubleshooting

### Common Issues

**Import errors:**
```bash
# Add project root to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

**Port conflicts:**
```bash
# Find process using port
lsof -i :8000
kill -9 PID
```

**Dependencies issues:**
```bash
# Clean install
rm -rf node_modules package-lock.json
npm install

# Python dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### Getting Help

- **GitHub Issues**: [Create an issue](https://github.com/Spectral-Flow/ELSZYIAH/issues/new)
- **Discussions**: [GitHub Discussions](https://github.com/Spectral-Flow/ELSZYIAH/discussions)
- **Wiki**: [Project Wiki](https://github.com/Spectral-Flow/ELSZYIAH/wiki)

## 📚 Resources

- **FastAPI**: https://fastapi.tiangolo.com/
- **React Native**: https://reactnative.dev/
- **Vite**: https://vitejs.dev/
- **Docker**: https://docs.docker.com/
- **Vercel**: https://vercel.com/docs