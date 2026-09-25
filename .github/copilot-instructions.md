# AI Agent Starter - Deployment Instructions

## Overview
This is a starter AI agent project with Python, OpenAI function calling, and a simple FastAPI interface. These instructions guide automated deployment.

## Prerequisites
- Python 3.8+
- pip package manager
- OpenAI API key
- FastAPI dependencies

## Deployment Steps

### 1. Environment Setup
```bash
# Clone the repository
git clone https://github.com/bdbest-spec/ai-agent-starter.git
cd ai-agent-starter

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration
```bash
# Set environment variables
export OPENAI_API_KEY=your_openai_api_key_here
export ENVIRONMENT=production
export HOST=0.0.0.0
export PORT=8000
```

### 3. Run the Application
```bash
# Start FastAPI server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Production deployment (with Gunicorn)
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000
```

### 4. Verify Deployment
```bash
# Check API health
curl http://localhost:8000/health

# View API documentation
# Visit http://localhost:8000/docs (Swagger UI)
# Visit http://localhost:8000/redoc (ReDoc)
```

## GitHub Actions Automation

The deployment is automated via GitHub Actions. Workflows trigger on:
- Push to `main` branch
- Pull request creation
- Manual workflow dispatch

### Workflow Files Location
`.github/workflows/` directory contains CI/CD pipeline configurations.

## Continuous Deployment (CD)

The following steps run automatically:
1. **Install Dependencies** - pip install from requirements.txt
2. **Run Tests** - Execute test suite
3. **Build** - Package application
4. **Deploy** - Deploy to hosting platform

## Rollback Procedure

If deployment fails:
```bash
# Revert to previous commit
git revert HEAD

# Push changes
git push origin main
```

## Monitoring & Logs

Check deployment status:
- GitHub Actions: `.github/workflows/` outputs
- Application logs: Check FastAPI console output
- API health: `GET /health` endpoint

## Support

For issues:
1. Check GitHub Actions workflow logs
2. Review application error logs
3. Verify environment variables are set correctly
4. Ensure OpenAI API key is valid

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
