# 🚀 Deployment Guide

## Elysia Concierge - The Avant Deployment

This guide covers all deployment options for the Elysia Concierge system.

## 📋 Prerequisites

- **Backend**: Python 3.9+, pip
- **Frontend**: Node.js 20+, npm
- **Database**: PostgreSQL 15+ (production), SQLite (development)
- **Cache**: Redis 7+ (optional, recommended for production)

## 🔧 Local Development

### Quick Start

```bash
# 1. Clone and setup
git clone https://github.com/Spectral-Flow/ELSZYIAH.git
cd ELSZYIAH
npm run setup:dev

# 2. Environment configuration
cp .env.example .env
# Edit .env with your settings

# 3. Start all services
npm run dev:all
```

### Individual Services

```bash
# Backend only (API on :8000)
npm run dev:backend

# Frontend only (Web on :3000)
npm run dev:frontend

# Mobile development
npm run dev:mobile
```

## ☁️ Vercel Deployment (Recommended)

### Automatic Deployment

1. **Fork the repository** to your GitHub account
2. **Connect to Vercel** at [vercel.com](https://vercel.com)
3. **Import your fork** - Vercel will auto-detect the configuration
4. **Set environment variables** in Vercel dashboard:
   ```
   ENVIRONMENT=production
   PROPERTY_NAME=Your Property Name
   PROPERTY_LOCATION=Your City, State
   ```
5. **Deploy** - Vercel will automatically deploy on every push to main

### Manual Deployment

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

### Environment Variables for Vercel

Required variables in Vercel dashboard:
- `ENVIRONMENT=production`
- `PROPERTY_NAME=Your Property Name`
- `PROPERTY_LOCATION=Your City, State`
- `SECRET_KEY=your-production-secret-key`

Optional (for AI features):
- `OPENAI_API_KEY=your-openai-key`
- `AZURE_OPENAI_API_KEY=your-azure-key`

## 🐳 Docker Deployment

### Single Container

```bash
# Build image
docker build -t elysia-concierge .

# Run container
docker run -p 8000:8000 \
  -e ENVIRONMENT=production \
  -e PROPERTY_NAME="Your Property" \
  elysia-concierge
```

### Docker Compose (Full Stack)

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## 🖥️ Traditional Server Deployment

### Ubuntu/Debian Server

```bash
# 1. System dependencies
sudo apt update
sudo apt install python3.11 python3.11-venv nginx postgresql redis-server

# 2. Application setup
git clone https://github.com/Spectral-Flow/ELSZYIAH.git
cd ELSZYIAH
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Database setup
sudo -u postgres createdb elysia_concierge
sudo -u postgres createuser elysia

# 4. Environment configuration
cp .env.example .env
# Edit .env with production settings

# 5. Run with gunicorn
pip install gunicorn
gunicorn backend.elysia_lite:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Systemd Service

```ini
# /etc/systemd/system/elysia-concierge.service
[Unit]
Description=Elysia Concierge API
After=network.target

[Service]
Type=exec
User=elysia
Group=elysia
WorkingDirectory=/opt/elysia-concierge
Environment=PATH=/opt/elysia-concierge/venv/bin
ExecStart=/opt/elysia-concierge/venv/bin/gunicorn backend.elysia_lite:app -w 4 -k uvicorn.workers.UvicornWorker --bind 127.0.0.1:8000
Restart=always

[Install]
WantedBy=multi-user.target
```

### Nginx Configuration

```nginx
# /etc/nginx/sites-available/elysia-concierge
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## 🔒 Security Configuration

### Production Environment Variables

```bash
# Generate secure secret key
python -c "import secrets; print(secrets.token_urlsafe(32))"

# Required security settings
ENVIRONMENT=production
DEBUG=false
SECRET_KEY=your-generated-secret-key
CORS_ORIGINS=https://your-domain.com
```

### Database Security

```sql
-- Create dedicated database user
CREATE USER elysia WITH ENCRYPTED PASSWORD 'secure-password';
CREATE DATABASE elysia_concierge OWNER elysia;
GRANT ALL PRIVILEGES ON DATABASE elysia_concierge TO elysia;
```

### Firewall Configuration

```bash
# Allow only necessary ports
sudo ufw allow 22    # SSH
sudo ufw allow 80    # HTTP
sudo ufw allow 443   # HTTPS
sudo ufw enable
```

## 📊 Monitoring & Logging

### Health Checks

```bash
# API health check
curl https://your-domain.com/health

# Database connectivity
curl https://your-domain.com/api/health/db

# Redis connectivity
curl https://your-domain.com/api/health/redis
```

### Log Files

```bash
# Application logs
tail -f logs/elysia.log

# Nginx logs
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log

# System logs
journalctl -u elysia-concierge -f
```

## 🔄 Backup & Recovery

### Database Backup

```bash
# Create backup
pg_dump elysia_concierge > backup_$(date +%Y%m%d_%H%M%S).sql

# Restore backup
psql elysia_concierge < backup_20241228_120000.sql
```

### Application Backup

```bash
# Backup application files
tar -czf elysia_backup_$(date +%Y%m%d).tar.gz \
  /opt/elysia-concierge \
  --exclude=venv \
  --exclude=__pycache__ \
  --exclude=.git
```

## 🎯 Environment-Specific Configurations

### Development
- SQLite database
- Debug mode enabled
- Hot reloading
- Mock AI responses

### Staging
- PostgreSQL database
- Production-like configuration
- Real AI integration testing
- SSL certificates

### Production
- Optimized database settings
- Caching enabled
- Monitoring and alerting
- SSL/TLS encryption
- Automated backups

## 🚨 Troubleshooting

### Common Issues

**Port already in use:**
```bash
lsof -i :8000
kill -9 PID
```

**Database connection failed:**
```bash
# Check PostgreSQL status
sudo systemctl status postgresql

# Check connection
psql -h localhost -U elysia -d elysia_concierge
```

**Permission denied:**
```bash
# Fix file permissions
sudo chown -R elysia:elysia /opt/elysia-concierge
chmod +x scripts/*.sh
```

### Performance Tuning

**Database optimization:**
```sql
-- PostgreSQL optimization
ALTER SYSTEM SET shared_buffers = '256MB';
ALTER SYSTEM SET effective_cache_size = '1GB';
SELECT pg_reload_conf();
```

**Application tuning:**
```bash
# Increase worker processes
gunicorn backend.elysia_lite:app -w 8 -k uvicorn.workers.UvicornWorker

# Enable Redis caching
export REDIS_URL=redis://localhost:6379/0
```

## 📞 Support

- **Documentation**: [GitHub Wiki](https://github.com/Spectral-Flow/ELSZYIAH/wiki)
- **Issues**: [GitHub Issues](https://github.com/Spectral-Flow/ELSZYIAH/issues)
- **Community**: [Discussions](https://github.com/Spectral-Flow/ELSZYIAH/discussions)