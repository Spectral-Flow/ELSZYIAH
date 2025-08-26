#!/bin/bash

# Elysia Concierge Setup Script
# Kairoi Residential - The Avant, Centennial CO
# Cross-platform development environment setup

echo "🏢 Elysia Concierge Setup - The Avant"
echo "Kairoi Residential Technology Initiative"
echo "========================================="

# Detect platform
PLATFORM="unknown"
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    PLATFORM="windows"
elif [[ "$OSTYPE" == "linux-android"* ]]; then
    PLATFORM="termux"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    PLATFORM="linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    PLATFORM="macos"
fi

echo "Detected platform: $PLATFORM"

# Platform-specific setup
case $PLATFORM in
    "windows")
        echo "Setting up for Windows development..."
        # Check for Python
        if ! command -v python &> /dev/null; then
            echo "❌ Python not found. Please install Python 3.9+ from python.org"
            exit 1
        fi
        
        # Check for Node.js
        if ! command -v node &> /dev/null; then
            echo "❌ Node.js not found. Please install Node.js 20+ from nodejs.org"
            exit 1
        fi
        ;;
        
    "termux")
        echo "Setting up for Termux (Android) development..."
        # Update packages
        pkg update && pkg upgrade -y
        
        # Install required packages
        pkg install -y python nodejs-lts git rust clang make cmake
        ;;
        
    *)
        echo "Setting up for $PLATFORM..."
        # Assume standard Unix-like environment
        ;;
esac

# Create project structure
echo "📁 Creating project structure..."
mkdir -p {backend,frontend,mobile,docs,models,audio,logs,tests}

# Backend setup
echo "🐍 Setting up Python backend..."
cd backend

# Create virtual environment
if [ ! -d "venv" ]; then
    python -m venv venv
fi

# Activate virtual environment
if [[ "$PLATFORM" == "windows" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Create basic configuration
cat > .env << EOF
# Elysia Concierge Environment Configuration
# The Avant - Centennial, Colorado

# Application Settings
APP_NAME="Elysia Concierge"
APP_VERSION="1.0.0"
ENVIRONMENT="development"
DEBUG=true

# Property Information
PROPERTY_NAME="The Avant"
PROPERTY_LOCATION="Centennial, Colorado"
PROPERTY_UNITS=280
MANAGEMENT_COMPANY="Kairoi Residential"

# API Configuration
API_HOST="0.0.0.0"
API_PORT=8000
API_WORKERS=4

# Database Configuration
DATABASE_URL="postgresql://elysia:secure_password@localhost:5432/elysia_concierge"
REDIS_URL="redis://localhost:6379/0"

# AI Model Configuration
MODEL_PATH="./models/mistral-7b.gguf"
MODEL_TYPE="mistral"
MAX_TOKENS=512
TEMPERATURE=0.7

# Authentication
SECRET_KEY="your-secret-key-change-this-in-production"
ACCESS_TOKEN_EXPIRE_MINUTES=1440

# External Integrations
PROPERTY_MANAGEMENT_API_URL=""
PROPERTY_MANAGEMENT_API_KEY=""

# Notification Settings
SENDGRID_API_KEY=""
TWILIO_ACCOUNT_SID=""
TWILIO_AUTH_TOKEN=""

# Monitoring
SENTRY_DSN=""
LOG_LEVEL="INFO"
EOF

cd ..

# Frontend setup
echo "⚛️ Setting up SvelteKit frontend..."
cd frontend

# Create package.json for frontend
cat > package.json << EOF
{
  "name": "elysia-concierge-frontend",
  "version": "1.0.0",
  "description": "The Avant resident portal - Elysia Concierge interface",
  "scripts": {
    "dev": "vite dev --host 0.0.0.0 --port 3000",
    "build": "vite build",
    "preview": "vite preview",
    "test": "vitest",
    "lint": "eslint .",
    "format": "prettier --write ."
  },
  "devDependencies": {
    "@sveltejs/adapter-auto": "^2.0.0",
    "@sveltejs/kit": "^1.20.4",
    "@typescript-eslint/eslint-plugin": "^6.0.0",
    "@typescript-eslint/parser": "^6.0.0",
    "eslint": "^8.28.0",
    "eslint-config-prettier": "^8.5.0",
    "eslint-plugin-svelte": "^2.30.0",
    "prettier": "^2.8.0",
    "prettier-plugin-svelte": "^2.10.1",
    "svelte": "^4.0.5",
    "svelte-check": "^3.4.3",
    "typescript": "^5.0.0",
    "vite": "^4.4.2",
    "vitest": "^0.34.0"
  },
  "type": "module",
  "dependencies": {
    "date-fns": "^2.30.0",
    "lucide-svelte": "^0.290.0"
  }
}
EOF

cd ..

# Mobile setup
echo "📱 Setting up React Native mobile app..."
cd mobile

# Create package.json for mobile
cat > package.json << EOF
{
  "name": "ElysiaConciergeMobile",
  "version": "1.0.0",
  "description": "The Avant resident mobile app - Elysia Concierge",
  "main": "index.js",
  "scripts": {
    "android": "react-native run-android",
    "ios": "react-native run-ios", 
    "start": "react-native start",
    "test": "jest",
    "lint": "eslint . --ext .js,.jsx,.ts,.tsx",
    "build:android": "cd android && ./gradlew assembleRelease",
    "build:ios": "cd ios && xcodebuild -workspace ElysiaConciergeMobile.xcworkspace -scheme ElysiaConciergeMobile -configuration Release"
  },
  "dependencies": {
    "react": "18.2.0",
    "react-native": "0.72.6",
    "@react-native-async-storage/async-storage": "^1.19.3",
    "@react-navigation/native": "^6.1.7",
    "@react-navigation/stack": "^6.3.17",
    "react-native-gesture-handler": "^2.13.1",
    "react-native-safe-area-context": "^4.7.2",
    "react-native-screens": "^3.25.0",
    "react-native-vector-icons": "^10.0.0",
    "react-native-voice": "^3.2.4"
  },
  "devDependencies": {
    "@babel/core": "^7.20.0",
    "@babel/preset-env": "^7.20.0",
    "@babel/runtime": "^7.20.0",
    "@react-native/eslint-config": "^0.72.2",
    "@react-native/metro-config": "^0.72.11",
    "@tsconfig/react-native": "^3.0.0",
    "@types/react": "^18.0.24",
    "@types/react-test-renderer": "^18.0.0",
    "babel-jest": "^29.2.1",
    "eslint": "^8.19.0",
    "jest": "^29.2.1",
    "metro-react-native-babel-preset": "0.76.8",
    "prettier": "^2.4.1",
    "react-test-renderer": "18.2.0",
    "typescript": "4.8.4"
  },
  "engines": {
    "node": ">=18"
  }
}
EOF

cd ..

# Create documentation
echo "📚 Creating documentation..."
cat > docs/DEPLOYMENT.md << EOF
# Elysia Concierge Deployment Guide
## The Avant - Kairoi Residential

### Production Deployment Checklist

#### Infrastructure Requirements
- [ ] Ubuntu 22.04 LTS server (minimum 4GB RAM, 2 vCPU)
- [ ] PostgreSQL 15+ database
- [ ] Redis 7+ cache server
- [ ] SSL certificate for HTTPS
- [ ] Domain name configured
- [ ] Backup strategy implemented

#### Security Configuration
- [ ] Environment variables configured (no secrets in code)
- [ ] Database credentials secured
- [ ] API rate limiting enabled
- [ ] CORS properly configured
- [ ] Security headers implemented
- [ ] Access logs enabled

#### The Avant Specific Setup
- [ ] Property management system integration tested
- [ ] Resident data migration completed
- [ ] Amenity booking system connected
- [ ] Emergency contact configuration verified
- [ ] Staff training completed

#### Go-Live Steps
1. Deploy backend to production server
2. Configure database and run migrations
3. Deploy frontend to CDN/hosting
4. Configure mobile app builds
5. Test all integrations
6. Monitor logs and performance
7. Announce to residents

#### Post-Launch Monitoring
- [ ] Performance monitoring (response times < 2s)
- [ ] Error tracking and alerting
- [ ] User satisfaction surveys
- [ ] Usage analytics review
- [ ] Regular backup verification

### Support Contacts
- Technical Support: tech@kairoi.com
- Property Management: management@theavant.com
- Emergency: 303-555-EMERGENCY
EOF

# Create development workflow
cat > docs/DEVELOPMENT.md << EOF
# Development Workflow
## Elysia Concierge - The Avant

### Daily Development Process

1. **Start Development Environment**
   \`\`\`bash
   npm run dev:all
   \`\`\`

2. **Check Elysia Status**
   \`\`\`bash
   npm run elysia:status
   \`\`\`

3. **View Live Logs**
   \`\`\`bash
   npm run elysia:logs
   \`\`\`

### Testing The Avant Features

#### Resident Request Types
- Maintenance: "My faucet is leaking in unit 304"
- Amenities: "Book the fitness center for tomorrow 7 AM"
- Packages: "Is my Amazon delivery ready for pickup?"
- Guest Access: "Add guest access for John Smith visiting today"
- Community: "What events are happening this weekend?"

#### Property-Specific Testing
- Unit numbers: 101-280 (fictional for testing)
- Amenities: Fitness center, pool, clubhouse, coworking
- Local knowledge: Centennial, Cherry Creek, RTD light rail

### Code Quality Standards
- Python: Black formatting, isort imports, 90%+ test coverage
- Frontend: ESLint, Prettier, TypeScript strict mode
- Mobile: React Native best practices, accessibility compliance

### Git Workflow
1. Feature branches: \`feature/elysia-amenity-booking\`
2. Pull requests required for main branch
3. Automated testing on all PRs
4. Code review by senior developer
5. Deployment only from main branch
EOF

echo "✅ Elysia Concierge setup complete!"
echo ""
echo "Next steps:"
echo "1. Start the development environment: npm run dev:all"
echo "2. Visit http://localhost:3000 for the resident portal"
echo "3. API documentation: http://localhost:8000/docs"
echo "4. Review deployment guide: docs/DEPLOYMENT.md"
echo ""
echo "🏢 Ready to serve The Avant residents with Elysia Concierge!"
echo "For support: tech@kairoi.com"
