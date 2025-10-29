# FastAPI Calculator

A comprehensive FastAPI-based calculator application with unit, integration, and end-to-end testing, complete with CI/CD pipeline and web interface.

![FastAPI Calculator](https://img.shields.io/badge/FastAPI-Calculator-blue)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Tests](https://img.shields.io/badge/Tests-Unit%20%7C%20Integration%20%7C%20E2E-green)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-green)

## 🚀 Features

- **REST API Calculator**: Complete arithmetic operations via REST endpoints
- **Web Interface**: Interactive calculator with modern UI
- **Comprehensive Testing**: Unit, integration, and end-to-end tests
- **Logging**: Detailed operation tracking and error logging
- **CI/CD Pipeline**: Automated testing and deployment with GitHub Actions
- **Code Quality**: Linting, formatting, and type checking
- **Security Scanning**: Automated vulnerability detection
- **API Documentation**: Interactive Swagger/OpenAPI docs

## 📋 Supported Operations

- ➕ **Addition**: Add two numbers
- ➖ **Subtraction**: Subtract two numbers  
- ✖️ **Multiplication**: Multiply two numbers
- ➗ **Division**: Divide two numbers (with zero-division protection)
- 🔢 **Power**: Raise a number to a power
- 📐 **Modulo**: Calculate remainder of division

## 🛠️ Technology Stack

- **Backend**: FastAPI, Python 3.11+
- **Frontend**: HTML5, CSS3, JavaScript
- **Testing**: pytest, pytest-asyncio, Playwright
- **Code Quality**: Black, Flake8, isort, mypy
- **CI/CD**: GitHub Actions
- **Documentation**: Swagger/OpenAPI

## 📁 Project Structure

```
IS218docker/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   └── operations.py        # Calculator operations
├── tests/
│   ├── __init__.py
│   ├── test_operations.py   # Unit tests
│   ├── test_main.py         # Integration tests
│   └── test_e2e.py          # End-to-end tests
├── templates/
│   └── calculator.html      # Web interface
├── static/
│   ├── styles.css           # Stylesheet
│   └── script.js            # JavaScript
├── .github/
│   └── workflows/
│       └── ci-cd.yml        # GitHub Actions workflow
├── requirements.txt         # Python dependencies
├── pyproject.toml          # Tool configurations
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🚦 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd IS218docker
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers** (for E2E tests)
   ```bash
   playwright install chromium
   ```

### Running the Application

1. **Start the server**
   ```bash
   python -m uvicorn app.main:app --reload
   ```

2. **Access the application**
   - Web Interface: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - Alternative Docs: http://localhost:8000/redoc

## 🧪 Testing

### Run All Tests
```bash
pytest -v
```

### Run Specific Test Types

**Unit Tests**
```bash
pytest tests/test_operations.py -v
```

**Integration Tests**
```bash
pytest tests/test_main.py -v
```

**End-to-End Tests**
```bash
pytest tests/test_e2e.py -v
```

### Coverage Report
```bash
pytest --cov=app --cov-report=html
```

## 🔌 API Endpoints

### Health Check
```http
GET /health
```

### Calculator Operations

All calculation endpoints accept JSON requests with `a` and `b` parameters:

```json
{
  "a": 10,
  "b": 5
}
```

#### Addition
```http
POST /add
```

#### Subtraction
```http
POST /subtract
```

#### Multiplication
```http
POST /multiply
```

#### Division
```http
POST /divide
```

#### Power
```http
POST /power
```

#### Modulo
```http
POST /modulo
```

### Example Response
```json
{
  "result": 15,
  "operation": "addition",
  "operands": {
    "a": 10,
    "b": 5
  }
}
```

### Error Response
```json
{
  "detail": "Division by zero is not allowed"
}
```

## 🎯 Usage Examples

### Using cURL

**Addition**
```bash
curl -X POST "http://localhost:8000/add" \
     -H "Content-Type: application/json" \
     -d '{"a": 10, "b": 5}'
```

**Division with Error Handling**
```bash
curl -X POST "http://localhost:8000/divide" \
     -H "Content-Type: application/json" \
     -d '{"a": 10, "b": 0}'
```

### Using Python Requests

```python
import requests

# Addition
response = requests.post(
    "http://localhost:8000/add",
    json={"a": 10, "b": 5}
)
print(response.json())  # {"result": 15, "operation": "addition", ...}

# Division by zero (error case)
response = requests.post(
    "http://localhost:8000/divide",
    json={"a": 10, "b": 0}
)
print(response.status_code)  # 400
print(response.json())  # {"detail": "Division by zero is not allowed"}
```

## 🔧 Development

### Code Quality Tools

**Format code**
```bash
black app tests
```

**Sort imports**
```bash
isort app tests
```

**Lint code**
```bash
flake8 app tests
```

**Type checking**
```bash
mypy app
```

### Pre-commit Hooks

Run all quality checks:
```bash
# Format, lint, and type check
black app tests && isort app tests && flake8 app tests && mypy app
```

## 🚀 CI/CD Pipeline

The GitHub Actions workflow (`ci-cd.yml`) includes:

1. **Test Job**
   - Code quality checks (linting, formatting, type checking)
   - Unit tests with coverage
   - Integration tests
   - End-to-end tests
   - Coverage reporting

2. **Security Job**
   - Dependency vulnerability scanning
   - Code security analysis

3. **Build Job**
   - Application startup testing
   - Build verification

4. **Deploy Jobs**
   - Staging deployment (develop branch)
   - Production deployment (main branch)

### Workflow Triggers

- Push to `main` or `develop` branches
- Pull requests to `main` branch

## 📊 Test Coverage

The application includes comprehensive test coverage:

- **Unit Tests**: 100% coverage of operations.py functions
- **Integration Tests**: All API endpoints with various scenarios
- **End-to-End Tests**: Complete user workflow testing with Playwright

### Coverage Areas

- ✅ All arithmetic operations
- ✅ Error handling (division by zero, invalid inputs)
- ✅ API endpoint functionality
- ✅ Request/response validation
- ✅ Web interface interactions
- ✅ Keyboard input support
- ✅ Responsive design testing

## 🔒 Security

Security measures implemented:

- Input validation using Pydantic models
- Error handling to prevent information leakage
- Automated security scanning in CI/CD
- Dependency vulnerability monitoring

## 📝 Logging

The application implements comprehensive logging:

- Operation tracking with input/output logging
- Error logging with detailed context
- Structured logging format for analysis
- Different log levels for development and production

## 🐳 Docker Support

To run with Docker:

```bash
# Build image
docker build -t fastapi-calculator .

# Run container
docker run -p 8000:8000 fastapi-calculator
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

### Development Workflow

1. Run tests locally before committing
2. Follow code formatting standards (Black, isort)
3. Update documentation for new features
4. Ensure CI/CD pipeline passes

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [pytest Documentation](https://docs.pytest.org/)
- [Playwright Documentation](https://playwright.dev/python/)

## 📞 Support

For questions and support:

1. Check the [GitHub Issues](../../issues)
2. Review the API documentation at `/docs`
3. Run the test suite to verify setup

---

**Built with ❤️ using FastAPI and modern Python development practices**