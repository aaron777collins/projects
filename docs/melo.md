# melo

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/melo)

## 📊 Project Details

- **Primary Language:** TypeScript
- **Languages Used:** TypeScript, JavaScript, Shell, CSS, Dockerfile
- **License:** None
- **Created:** February 17, 2026
- **Last Updated:** February 17, 2026

## 📝 About

# Melo v2 CI/CD Pipeline

This directory contains GitHub Actions workflows for automated testing, building, and deployment of Melo v2.

## Workflows

### 1. PR Tests (`pr-tests.yml`)
**Trigger:** Pull requests to `master` branch

**Steps:**
- ✅ Checkout code
- ✅ Setup Node.js 18 and pnpm
- ✅ Cache pnpm dependencies
- ✅ Install dependencies
- ✅ Run ESLint (`pnpm lint`)
- ✅ Build application (`pnpm build`)
- ✅ Run Playwright E2E tests (`pnpm test:e2e`)
- ✅ Upload test results as artifacts

**Purpose:** Ensures all pull requests pass quality checks before merging.

### 2. Build and Deploy (`deploy.yml`)
**Trigger:** Pushes to `master` branch

**Steps:**
1. **Test Job:**
   - Same as PR tests but with production build
   - Upload build artifacts

2. **Deploy Job:**
   - Download build artifacts from test job
   - Deploy to dev2.aaroncollins.info via SSH
   - Restart application using PM2
   - Run health check

**Environment:** `development` (GitHub environment with protection rules)

### 3. Docker Build (`docker.yml`)
**Trigger:** Pushes to `master` and tags starting with `v*`

**Steps:**
- ✅ Build Docker image
- ✅ Push to GitHub Container Registry (ghcr.io)
- ✅ Tag with branch name or version
- ✅ Use GitHub Actions cache for faster builds

## Environment Configuration

### Development (`.env.development`)
- Local development settings
- Debug mode enabled
- Uses file-based SQLite database

### Production (`.env.production`)
- Production optimizations
- PostgreSQL database
- Security configurations
- Deployed to dev2.aaroncollins.info

## Deployment Setup

### PM2 Configuration (`ecosystem.config.js`)
- Application name: `melo-v2`
- Single instance (can be scaled later)
- Memory limit: 1GB
- Structured logging to `./logs/`

### Required GitHub Secrets

For deployment to work, set these in your repository settings:

```
DEV2_HOST=dev2.aaroncollins.info
DEV2_USERNAME=deploy
DEV2_SSH_KEY=<private SSH key>
```

### Server Prerequisites

On dev2.aaroncollins.info:
1. Node.js 18+ installed
2. pnpm installed globally
3. PM2 installed globally
4. SSH access configured for deploy user
5. Repository cloned to `/var/www/melo-v2`
6. Environment variables configured

## Health Monitoring

### Health Check Endpoint
The deploy workflow includes a health check that verifies the application is running:
```bash
curl -f https://dev2.aaroncollins.info/api/health
```

This uses the health endpoint from task `p12-5-health-endpoints`.

## Usage

### Automatic Deployments
1. Push code to `master` branch
2. CI runs tests and builds application
3. If tests pass, deploys to dev2.aaroncollins.info
4. PM2 reloads the application
5. Health check verifies deployment

### Manual Operations

**Check deployment status:**
```bash
pm2 status melo-v2
pm2 logs melo-v2
```

**Manual restart:**
```bash
pm2 restart melo-v2
```

**View build logs:**
Check GitHub Actions tab for detailed build/deploy logs.

## Troubleshooting

### Common Issues

**Build failures:**
- Check Node.js/pnpm versions match CI
- Ensure all dependencies are in pnpm-lock.yaml
- Verify TypeScript compilation passes locally

**Deployment failures:**
- Check SSH key permissions
- Verify server disk space and memory
- Check PM2 process status
- Review server logs in `./logs/`

**Test failures:**
- Run tests locally: `pnpm test:e2e`
- Check Playwright browser dependencies
- Review test artifacts in GitHub Actions

### Logs and Monitoring

- **CI Logs:** GitHub Actions tab
- **Application Logs:** `/var/www/melo-v2/logs/` on server
- **PM2 Logs:** `pm2 logs melo-v2`
- **Health Status:** `https://dev2.aaroncollins.info/api/health`

