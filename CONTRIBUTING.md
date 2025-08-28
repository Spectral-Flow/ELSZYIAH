# Contributing to Elysia Concierge

Welcome to the Elysia Concierge project! This guide will help you get started with contributing to The Avant's AI-powered concierge system.

## 🎯 Project Overview

Elysia Concierge is a sophisticated AI-powered concierge system designed for The Avant luxury apartments in Centennial, Colorado. Our goal is to provide residents with an exceptional living experience through intelligent automation and personalized service.

## 🚀 Quick Start

### Prerequisites

- **Python**: 3.9+ (recommended: 3.11)
- **Node.js**: 20+ 
- **Git**: Latest version
- **Code Editor**: VS Code recommended with Python and TypeScript extensions

### 1. Environment Setup

```bash
# Clone the repository
git clone https://github.com/Spectral-Flow/ELSZYIAH.git
cd ELSZYIAH

# Copy environment template
cp .env.example .env

# Edit .env file with your configuration
# At minimum, set:
# - SECRET_KEY (generate a secure random string)
# - Database URLs (or use defaults for development)
```

### 2. Backend Setup

```bash
# Create virtual environment
cd backend
python -m venv venv

# Activate virtual environment
# Windows:
.\\venv\\Scripts\\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements-ci.txt

# Run development server
python -m uvicorn elysia_lite:app --reload --host 0.0.0.0 --port 8000
```

### 3. Frontend Setup (Optional)

```bash
cd frontend
npm install
npm run dev
```

### 4. Install Development Tools

```bash
# Install pre-commit hooks (Python tools)
pip install pre-commit
pre-commit install

# Install Node.js tools globally (optional)
npm install -g eslint prettier typescript
```

## 🛠️ Development Workflow

### Branch Strategy

We use a feature branch workflow:

```bash
# Create feature branch
git checkout -b feature/elysia-amenity-booking
git checkout -b fix/maintenance-request-validation
git checkout -b docs/api-documentation-update

# Make your changes...

# Commit with conventional commit format
git commit -m "feat(amenities): add pool booking functionality"
git commit -m "fix(maintenance): validate unit number format"
git commit -m "docs(api): update endpoint documentation"

# Push and create pull request
git push origin feature/elysia-amenity-booking
```

### Commit Message Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `ci`: CI/CD changes
- `build`: Build system changes

**Scopes:**
- `api`: API endpoints
- `ai`: AI/ML functionality
- `auth`: Authentication
- `db`: Database
- `ui`: User interface
- `amenities`: Amenity booking
- `maintenance`: Maintenance requests
- `residents`: Resident management

**Examples:**
```
feat(amenities): add fitness center booking API
fix(maintenance): resolve duplicate request creation
docs(api): update OpenAPI specification
test(ai): add unit tests for response generation
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest tests -v

# Run specific test file
pytest tests/test_api.py -v

# Run tests with coverage
pytest tests --cov=backend --cov-report=html

# Run tests for specific functionality
pytest tests -k "test_amenities" -v
```

### Writing Tests

Create tests in the `tests/` directory:

```python
# tests/test_new_feature.py
import pytest
from fastapi.testclient import TestClient
from backend.elysia_lite import app

client = TestClient(app)

def test_new_endpoint():
    response = client.get("/api/new-endpoint")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

@pytest.mark.asyncio
async def test_async_functionality():
    # Test async code here
    pass
```

### Test Categories

- **Unit Tests**: Test individual functions/classes
- **Integration Tests**: Test component interactions
- **API Tests**: Test HTTP endpoints
- **End-to-End Tests**: Test complete user workflows

## 🎨 Code Style

### Python

We use the following tools for Python code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **bandit**: Security scanning

```bash
# Format code
black backend/ tests/
isort backend/ tests/

# Check code quality
flake8 backend/ tests/
mypy backend/

# Security scan
bandit -r backend/
```

### Frontend (TypeScript/JavaScript)

- **ESLint**: Linting
- **Prettier**: Code formatting
- **TypeScript**: Type checking

```bash
cd frontend
npm run lint
npm run format
npm run type-check
```

### Pre-commit Hooks

Pre-commit hooks automatically run code quality checks:

```bash
# Install pre-commit
pip install pre-commit
pre-commit install

# Run manually
pre-commit run --all-files
```

## 📝 Documentation

### API Documentation

API documentation is automatically generated from FastAPI:
- Development: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

### Code Documentation

- Use docstrings for all functions and classes
- Follow Google/NumPy docstring format
- Include type hints

```python
def process_resident_request(
    request: ResidentRequest, 
    ai_model: str = "mock"
) -> ConciergeResponse:
    """Process a resident request through Elysia AI.
    
    Args:
        request: The resident's request containing message and metadata
        ai_model: AI model to use for processing ("mock", "llamacpp", etc.)
        
    Returns:
        ConciergeResponse containing the AI's response and metadata
        
    Raises:
        ValidationError: If request data is invalid
        AIServiceError: If AI processing fails
    """
    # Implementation here
    pass
```

## 🏗️ Architecture Guidelines

### Backend Structure

```
backend/
├── __init__.py
├── elysia_lite.py         # Main FastAPI application
├── elysia_concierge.py    # Full-featured version
├── models/                # Data models
├── services/              # Business logic
├── utils/                 # Utility functions
└── config/                # Configuration
```

### Key Principles

1. **Separation of Concerns**: Keep AI, API, and business logic separate
2. **Type Safety**: Use Pydantic models and type hints
3. **Error Handling**: Implement comprehensive error handling
4. **Configuration**: Use environment variables for all configuration
5. **Security**: Never commit secrets, validate all inputs
6. **Performance**: Consider async/await for I/O operations

### AI Integration

When working with AI models:

- Support multiple AI backends (mock, llama-cpp, OpenAI, Azure)
- Use environment variables for model selection
- Implement fallback mechanisms
- Add proper error handling for model failures

## 🛡️ Security Guidelines

### Environment Variables

- Never commit `.env` files
- Use strong, unique secrets
- Rotate secrets regularly
- Use different secrets for different environments

### Input Validation

- Validate all user inputs
- Sanitize data before processing
- Use Pydantic models for request validation
- Implement rate limiting

### Dependencies

- Keep dependencies updated
- Run security scans regularly
- Review dependency licenses
- Use known, trusted packages

## 🚀 Deployment

### Development

```bash
# Start development server
npm run dev:backend

# Or with specific AI model
ELYSIA_USE_LLAMACPP=true npm run dev:backend
```

### Production

- Use environment-specific configuration
- Enable security headers
- Set up monitoring and logging
- Use HTTPS
- Implement health checks

## 🐛 Reporting Issues

### Bug Reports

When reporting bugs, include:

1. **Environment**: OS, Python version, Node.js version
2. **Steps to Reproduce**: Detailed steps
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **Error Messages**: Full error messages and stack traces
6. **Configuration**: Relevant environment variables (no secrets!)

### Feature Requests

For feature requests, include:

1. **Use Case**: Why is this needed?
2. **Proposed Solution**: How should it work?
3. **Alternatives**: Other solutions considered
4. **Impact**: Who would benefit?

## 📞 Getting Help

- **Issues**: GitHub Issues for bugs and feature requests
- **Discussions**: GitHub Discussions for questions
- **Documentation**: Check docs/ directory
- **API Reference**: http://localhost:8000/docs when running locally

## 🏆 Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project documentation

Thank you for contributing to Elysia Concierge! Your efforts help create an exceptional living experience for The Avant residents.

---

*This project is maintained by Kairoi Residential Technology Team*