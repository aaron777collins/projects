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
- ✅ Upload test results as ar

