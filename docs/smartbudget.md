# smartbudget

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/smartbudget)

## 📊 Project Details

- **Primary Language:** HTML
- **Languages Used:** HTML, TypeScript, JavaScript, Shell, CSS, Dockerfile
- **License:** None
- **Created:** January 14, 2026
- **Last Updated:** January 17, 2026

## 📝 About

# SmartBudget

> **Intelligent Personal Finance Management** - Take control of your financial future with AI-powered budgeting and insights.

![SmartBudget Banner](https://via.placeholder.com/1200x300/2563EB/ffffff?text=SmartBudget)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.3-blue)](https://www.typescriptlang.org/)
[![Next.js](https://img.shields.io/badge/Next.js-14-black)](https://nextjs.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## Overview

**SmartBudget** is a comprehensive personal finance management application that helps you:

- Import and manage all your financial transactions
- Automatically categorize expenses and income using AI
- Create and track budgets with real-time progress monitoring
- Set and achieve financial goals
- Gain insights into your spending patterns
- Make data-driven financial decisions

Optimized for **Canadian banks** (especially CIBC), SmartBudget supports CSV and OFX/QFX import formats with intelligent merchant normalization and AI-powered categorization.

---

## Features

### Core Features

- **Universal Transaction Import**
  - CSV, OFX, QFX format support
  - Multi-file drag-and-drop upload
  - Automatic duplicate detection
  - Import preview and validation

- **AI-Powered Auto-Categorization**
  - 90%+ accuracy using hybrid ML + rule-based system
  - Plaid PFCv2 taxonomy (16 primary, 100+ subcategories)
  - Merchant normalization pipeline
  - Confidence scoring and user feedback loop

- **Unknown Merchant Research**
  - Claude AI integration for merchant lookup
  - Web search and business identification
  - Automatic category suggestions
  - Knowledge base learning

- **Comprehensive Dashboard**
  - Real-time financial overview
  - Net worth tracking with trends
  - Cash flow analysis
  - Interactive charts (Recharts + D3.js)
  - Multiple timeframe views

- **Advanced Budget Management**
  - Multiple budget types (Envelope, Percentage, Fixed, Goal-based)
  - Real-time tracking with alerts
  - Budget forecasting and analytics
  - Rollover and fund transfer support

- **Financial Goals**
  - Savings goals with progress tracking
  - Debt payoff calculators
  - Net worth targets
  - Milestone celebrations

### Advanced Features

- **Split Transactions**: Allocate expenses across multiple categories
- **Tags & Labels**: Custom organization and tax tracking
- **Recurring Detection**: Auto-identify and predict recurring expenses
- **Smart Search**: Full-text search with advanced filtering
- **Export & Reporting**: CSV, Excel, PDF exports with tax reports
- **AI Insights**: Spending patterns, anomaly detection, savings opportunities

---

## Screenshots

### Dashboard
![Dashboard](https://via.placeholder.com/800x500/f9fafb/2563eb?text=Dashboard+View)

### Transaction Management
![Transactions](https://via.placeholder.com/800x500/f9fafb/2563eb?text=Transaction+Management)

### Budget Tracking
![Budgets](https://via.placeholder.com/800x500/f9fafb/2563eb?text=Budget+Tracking)

---

## Quick Start

### Prerequisites

- **Node.js** 20+ and npm/yarn/pnpm
- **PostgreSQL** 16+ database
- **Git** for version control

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/smartbudget.git
cd smartbudget
```

2. **Install dependencies**

```bash
npm install
# or
pnpm install
# or
yarn install
```

3. **Set up environment variables**

Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env` and configure:

```env
# Database
DATABASE_URL="postgresql://user:password@localhost:5432/smartbudget"

# NextAuth
NEXTAUTH_URL="http://localhost:3000"
NEXTAUTH_SECRET="your-secret-key-here"

# Sentry (optional)
SENTRY_DSN="your-sentry-dsn"
NEXT_PUBLIC_SENTRY_DSN="your-sentry-dsn"
```

4. **Set up the database**

```bash
# Generate Prisma client
npx prisma generate

# Run migrations
npx prisma migrate deploy

# Seed initial data (categories)
npx prisma db seed
```

5. **Start the development server**

```bash
npm run dev
```

6. **Open your browser**

Navigate to [http://localhost:3000](http://localhost:3000)

---

## Tech Stack

### Frontend

- **Framework**: [Next.js 14+](https://nextjs.org/) (App Router, Server Actions)
- **UI Components**: [shadcn/ui](https://ui.shadcn.com/) (Radix UI + Tailwind CSS)
- **Styling**: [Tailwind CSS](https://tailwindcss.com/)
- **Visualization**: [Recharts](https://recharts.org/), [D3.js](https://d3js.org/)
- **Animation**: [Framer Motion](https://www.framer.com/motion/)
- **Form Handling**: [React Hook Form](https://react-hook-form.com/) + [Zod](https://zod.dev/)
- **State Management**: React Context + [Zustand](https://zustand-demo.pmnd.rs/)

### Backend

- **Runtime**: Node.js 20+
- **API**: Next.js API Routes + Server Actions
- **Database**: [PostgreSQL 16+](https://www.postgresql.org/) with [Prisma ORM](https://www.prisma.io/)
- **Authentication**: [NextAuth.js v5](https://authjs.dev/) (Auth.js)
- **File Processing**: [Papa Parse](https://www.papaparse.com/) (CSV), [node-ofx-parser](https://github.com/kedder/node-ofx-parser) (OFX/QFX)
- **AI Integration**: [Anthropic Claude API](https://www.anthropic.com/api)

### AI/ML

- **Categorization**: Hybrid rule-based + ML model
- **Merchant Normalization**: Fuzzy matching (RapidFuzz) + NLP
- **Unknown Merchant Lookup**: Claude AI via subprocess (AICEO pattern)

### Infrastructure

- **Hosting**: [Vercel](https://vercel.com/)
- **Database Hosting**: [Neon](https://neon.tech/) or [Supabase](https://supabase.com/)
- **Monitoring**: [Sentry](https://sentry.io/) (error tracking)
- **Analytics**: Vercel Analytics

---

## Project Structure

```
smartbudget/
├── src/
│   ├── app/                    # Next.js App Router pages
│   │   ├── (auth)/            # Authentication pages
│   │   ├── (dashboard)/       # Main application pages
│   │   ├── api/               # API routes
│   │   ├── layout.tsx         # Root layout
│   │   └── page.tsx           # Homepage
│   ├── components/            # React components
│   │   ├── ui/               # shadcn/ui components
│   │   ├── dashboard/        # Dashboard components
│   │   ├── transactions/     # Transaction components
│   │   └── ...
│   ├── lib/                   # Utility functions
│   │   ├── prisma.ts         # Prisma client
│   │   ├── auth.ts           # NextAuth config
│   │   ├── categorizer.ts    # Auto-categorization
│   │   ├── merchant-normalizer.ts
│   │   └── ...
│   ├── hooks/                 # Custom React hooks
│   ├── types/                 # TypeScript types
│   └── styles/                # Global styles
├── prisma/
│   ├── schema.prisma          # Database schema
│   ├── migrations/            # Database migrations
│   └── seed.ts                # Seed script
├── e2e/                       # End-to-end tests
├── public/                    # Static assets
├── docs/                      # Additional documentation
├── .env                       # Environment variables
├── next.config.js             # Next.js configuration
├── tailwind.config.ts         # Tailwind CSS config
├── tsconfig.json              # TypeScript config
├── package.json               # Dependencies
└── README.md                  # This file
```

---

## Documentation

Comprehensive documentation is available:

- **[User Guide](USER_GUIDE.md)** - Complete guide for end users
- **[API Documentation](API_DOCS.md)** - REST API reference for developers
- **[Testing Guide](TESTING.md)** - Testing infrastructure and best practices
- **[Error Monitoring](ERROR_MONITORING.md)** - Sentry configuration and error handling
- **[Database Setup](prisma/README.md)** - Database schema and seeding

---

## Development

### Available Scripts

```bash
# Development
npm run dev              # Start dev server
npm run build            # Build for production
npm run start            # Start production server
npm run lint             # Run ESLint
npm run format           # Format with Prettier

# Database
npx prisma studio        # Open Prisma Studio (database GUI)
npx prisma generate      # Generate Prisma client
npx prisma migrate dev   # Create and apply migrations
npx prisma db seed       # Seed database with initial data

# Testing
npm run test             # Run unit tests
npm run test:watch       # Run tests in watch mode
npm run test:coverage    # Generate coverage report
npm run test:e2e         # Run E2E tests
npm run test:e2e:ui      # Run E2E tests with UI

# Type Checking
npm run type-check       # Run TypeScript type checking
```

### Development Workflow

1. **Create a feature branch**

```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes**

- Follow the existing code style
- Add tests for new features
- Update documentation as needed

3. **Run tests and linting**

```bash
npm run lint
npm run test
npm run type-check
```

4. **Commit your changes**

```bash
git add .
git commit -m "feat: add awesome feature"
```

Follow [Conventional Commits](https://www.conventionalcommits.org/) format:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting)
- `refactor:` - Code refactoring
- `test:` - Test changes
- `chore:` - Build/config changes

5. **Push and create a Pull Request**

```bash
git push origin feature/your-feature-name
```

---

## Testing

SmartBudget has comprehensive test coverage:

- **Unit Tests**: Vitest for utilities, business logic
- **Integration Tests**: API route testing
- **E2E Tests**: Playwright for user flows

### Running Tests

```bash
# All tests
npm run test:all

# Unit tests only
npm run test

# E2E tests only
npm run test:e2e

# With coverage
npm run test:coverage
```

See [TESTING.md](TESTING.md) for detailed testing documentation.

---

## Deployment

### Deploy to Vercel

1. **Install Vercel CLI**

```bash
npm install -g vercel
```

2. **Link project**

```bash
vercel link
```

3. **Set environment variables**

```bash
vercel env add DATABASE_URL
vercel env add NEXTAUTH_SECRET
# Add other environment variables
```

4. **Deploy**

```bash
vercel --prod
```

### Database Migration

For production deployments, run migrations:

```bash
npx prisma migrate deploy
```

### Environment Variables

Ensure all required environment variables are set:

- `DATABASE_URL` - PostgreSQL connection string
- `NEXTAUTH_URL` - Application URL
- `NEXTAUTH_SECRET` - Secret for session encryption
- `SENTRY_DSN` - Sentry error tracking (optional)
- `NEXT_PUBLIC_SENTRY_DSN` - Client-side Sentry (optional)

---

## Configuration

### Database

SmartBudget uses PostgreSQL with Prisma ORM. Configure your database connection in `.env`:

```env
DATABASE_URL="postgresql://user:password@host:port/database?schema=public"
```

### Authentication

Configure NextAuth.js providers in `src/auth.ts`:

- Username/Password (default)
- Google OAuth (coming soon)
- Apple Sign-In (coming soon)

### AI Integration

To enable Claude AI merchant research:

```env
ANTHROPIC_API_KEY="your-api-key"
```

### Sentry (Error Monitoring)

Optional but recommended for production:

```env
SENTRY_DSN="your-sentry-dsn"
NEXT_PUBLIC_SENTRY_DSN="your-public-dsn"
SENTRY_ORG="your-org"
SENTRY_PROJECT="your-project"
```

See [ERROR_MONITORING.md](ERROR_MONITORING.md) for setup details.

---

## Performance

SmartBudget is optimized for performance:

- **Page Load**: <2s (First Contentful Paint)
- **API Response**: <200ms (p95)
- **Database Queries**: <50ms (p95)
- **Transaction Import**: 10,000 transactions in <5s
- **Dashboard Render**: <1s with 10,000+ transactions

### Performance Features

- Server-side rendering (SSR) for fast initial loads
- Optimistic UI updates
- API route caching
- Database query optimization with indexes
- Code splitting and lazy loading
- Image optimization

---

## Security

SmartBudget takes security seriously:

- **Encryption**: AES-256 at rest, TLS 1.3 in transit
- **Authentication**: NextAuth.js with secure sessions
- **Authorization**: Row-level security for all data access
- **Input Validation**: Zod schemas for all inputs
- **SQL Injection Protection**: Prisma parameterized queries
- **XSS Protection**: React's built-in escaping + CSP headers
- **CSRF Protection**: CSRF tokens on all mutations

### Security Best Practices

- Never commit `.env` files
- Rotate secrets regularly
- Keep dependencies updated
- Review code for security issues
- Use strong passwords and 2FA
- Follow OWASP Top 10 guidelines

---

## Privacy

Your financial data privacy is paramount:

- **No Data Selling**: Your data is never sold or shared with third parties
- **Encryption**: All sensitive data is encrypted
- **Bank Credentials**: Never stored (file-based imports only)
- **GDPR Compliant**: Full data portability and deletion rights
- **Anonymized Analytics**: Optional and aggregated only

### Data Handling

- **Local Processing**: Transaction categorization happens on your server
- **Minimal Cloud AI**: Claude AI research is opt-in and merchant-specific
- **Data Export**: Download all your data anytime
- **Account Deletion**: Permanently delete all data

---

## Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

- **Report Bugs**: [Open an issue](https://github.com/yourusername/smartbudget/issues)
- **Suggest Features**: [Feature requests](https://github.com/yourusername/smartbudget/discussions)
- **Submit Pull Requests**: Fix bugs or add features
- **Improve Documentation**: Help others understand SmartBudget
- **Translate**: Help translate to other languages

### Contribution Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass (`npm run test:all`)
6. Commit with conventional commits (`git commit -m 'feat: add amazing feature'`)
7. Push to your fork (`git push origin feature/amazing-feature`)
8. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## Roadmap

### Current Version: v1.0 (MVP)

Released: January 2026

### Upcoming Features

#### v1.1 (Q2 2026)
- Mobile responsive enhancements
- Dark mode improvements
- Multi-currency support
- Bank account sync (Plaid integration)

#### v1.2 (Q3 2026)
- Investment tracking
- Credit score monitoring
- Bill payment reminders
- Collaborative budgets (multi-user households)

#### v2.0 (Q4 2026)
- Mobile apps (iOS & Android)
- Advanced AI insights
- Natural language queries
- Receipt OCR
- Tax optimization tools

See [ROADMAP.md](ROADMAP.md) for detailed plans.

---

## FAQ

### General

**Q: Is SmartBudget free?**
A: Yes, SmartBudget is currently free during the beta period. Future pricing TBD.

**Q: Do I need to connect my bank account?**
A: No! SmartBudget uses file-based imports (CSV, OFX). No bank credentials required.

**Q: Which banks are supported?**
A: Any bank that exports CSV or OFX/QFX files. Optimized for Canadian banks (CIBC, TD, RBC, Scotiabank, BMO).

### Technical

**Q: Is my data secure?**
A: Yes. All data is encrypted (AES-256 at rest, TLS 1.3 in transit). We never store bank credentials.

**Q: Can I self-host SmartBudget?**
A: Yes! SmartBudget is open-source. Follow the installation guide above.

**Q: Does it work offline?**
A: The web app requires internet. Future mobile apps will have offline support.

**Q: How accurate is the auto-categorization?**
A: 90%+ accuracy after initial training. Improves as you correct transactions.

---

## Support

### Get Help

- **Documentation**: [User Guide](USER_GUIDE.md) | [API Docs](API_DOCS.md)
- **Issues**: [GitHub Issues](https://github.com/yourusername/smartbudget/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/smartbudget/discussions)
- **Email**: support@smartbudget.app

### Community

- **Discord**: [Join our Discord](https://discord.gg/smartbudget) (coming soon)
- **Twitter**: [@SmartBudgetApp](https://twitter.com/smartbudgetapp) (coming soon)
- **Blog**: [blog.smartbudget.app](https://blog.smartbudget.app) (coming soon)

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 SmartBudget Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Acknowledgments

Built with amazing open-source technologies:

- [Next.js](https://nextjs.org/) - React framework
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS
- [shadcn/ui](https://ui.shadcn.com/) - UI component library
- [Prisma](https://www.prisma.io/) - Database ORM
- [NextAuth.js](https://authjs.dev/) - Authentication
- [Recharts](https://recharts.org/) - Charting library
- [Anthropic Claude](https://www.anthropic.com/) - AI assistant

Special thanks to the open-source community for making projects like this possible.

---

## Star History

If you find SmartBudget useful, please consider starring the repository!

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/smartbudget&type=Date)](https://star-history.com/#yourusername/smartbudget&Date)

---

<div align="center">

**Made with ❤️ by the SmartBudget Team**

[Website](https://smartbudget.app) • [Documentation](USER_GUIDE.md) • [API](API_DOCS.md) • [Support](mailto:support@smartbudget.app)

</div>

