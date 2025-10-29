"""
Integration tests for FastAPI Calculator endpoints.
Tests all API endpoints in app/main.py
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

# Create test client
client = TestClient(app)

class TestHealthEndpoint:
    """Test cases for health check endpoint."""
    
    def test_health_check(self):
        """Test health check endpoint returns correct status."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["service"] == "Calculator API"

class TestRootEndpoint:
    """Test cases for root endpoint serving web interface."""
    
    def test_root_endpoint(self):
        """Test root endpoint serves HTML page."""
        response = client.get("/")
        assert response.status_code == 200
        assert "text/html" in response.headers["content-type"]
        assert "FastAPI Calculator" in response.text

class TestAdditionEndpoint:
    """Test cases for addition endpoint."""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers via API."""
        response = client.post("/add", json={"a": 5, "b": 3})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 8
        assert data["operation"] == "addition"
        assert data["operands"] == {"a": 5, "b": 3}
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers via API."""
        response = client.post("/add", json={"a": -5, "b": -3})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == -8
        assert data["operation"] == "addition"
    
    def test_add_floats(self):
        """Test adding floating point numbers via API."""
        response = client.post("/add", json={"a": 2.5, "b": 3.7})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == pytest.approx(6.2)
        assert data["operation"] == "addition"
    
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers via API."""
        response = client.post("/add", json={"a": 10, "b": -4})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 6
    
    def test_add_invalid_input(self):
        """Test addition with invalid input."""
        response = client.post("/add", json={"a": "invalid", "b": 5})
        assert response.status_code == 422  # Validation error

class TestSubtractionEndpoint:
    """Test cases for subtraction endpoint."""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers via API."""
        response = client.post("/subtract", json={"a": 10, "b": 4})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 6
        assert data["operation"] == "subtraction"
        assert data["operands"] == {"a": 10, "b": 4}
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers via API."""
        response = client.post("/subtract", json={"a": -5, "b": -8})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 3
    
    def test_subtract_result_negative(self):
        """Test subtraction resulting in negative number."""
        response = client.post("/subtract", json={"a": 3, "b": 8})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == -5
    
    def test_subtract_floats(self):
        """Test subtracting floating point numbers via API."""
        response = client.post("/subtract", json={"a": 7.5, "b": 2.3})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == pytest.approx(5.2)

class TestMultiplicationEndpoint:
    """Test cases for multiplication endpoint."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers via API."""
        response = client.post("/multiply", json={"a": 6, "b": 7})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 42
        assert data["operation"] == "multiplication"
        assert data["operands"] == {"a": 6, "b": 7}
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero via API."""
        response = client.post("/multiply", json={"a": 5, "b": 0})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 0
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers via API."""
        response = client.post("/multiply", json={"a": -4, "b": -3})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 12
    
    def test_multiply_mixed_signs(self):
        """Test multiplying numbers with different signs."""
        response = client.post("/multiply", json={"a": -4, "b": 3})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == -12
    
    def test_multiply_floats(self):
        """Test multiplying floating point numbers via API."""
        response = client.post("/multiply", json={"a": 2.5, "b": 4.0})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 10.0

class TestDivisionEndpoint:
    """Test cases for division endpoint."""
    
    def test_divide_positive_numbers(self):
        """Test dividing positive numbers via API."""
        response = client.post("/divide", json={"a": 15, "b": 3})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 5
        assert data["operation"] == "division"
        assert data["operands"] == {"a": 15, "b": 3}
    
    def test_divide_by_zero(self):
        """Test division by zero returns error."""
        response = client.post("/divide", json={"a": 5, "b": 0})
        assert response.status_code == 400
        data = response.json()
        assert "Division by zero is not allowed" in data["detail"]
    
    def test_divide_negative_numbers(self):
        """Test dividing negative numbers via API."""
        response = client.post("/divide", json={"a": -12, "b": -4})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 3
    
    def test_divide_mixed_signs(self):
        """Test dividing numbers with different signs."""
        response = client.post("/divide", json={"a": -12, "b": 4})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == -3
    
    def test_divide_floats(self):
        """Test dividing floating point numbers via API."""
        response = client.post("/divide", json={"a": 7.5, "b": 2.5})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 3.0
    
    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        response = client.post("/divide", json={"a": 0, "b": 5})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 0

class TestPowerEndpoint:
    """Test cases for power endpoint."""
    
    def test_power_positive_numbers(self):
        """Test power operation with positive numbers via API."""
        response = client.post("/power", json={"a": 2, "b": 3})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 8
        assert data["operation"] == "power"
        assert data["operands"] == {"a": 2, "b": 3}
    
    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        response = client.post("/power", json={"a": 5, "b": 0})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 1
    
    def test_power_negative_base(self):
        """Test power with negative base."""
        response = client.post("/power", json={"a": -2, "b": 3})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == -8
    
    def test_power_fractional_exponent(self):
        """Test power with fractional exponent."""
        response = client.post("/power", json={"a": 4, "b": 0.5})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 2.0

class TestModuloEndpoint:
    """Test cases for modulo endpoint."""
    
    def test_modulo_positive_numbers(self):
        """Test modulo operation with positive numbers via API."""
        response = client.post("/modulo", json={"a": 10, "b": 3})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 1
        assert data["operation"] == "modulo"
        assert data["operands"] == {"a": 10, "b": 3}
    
    def test_modulo_by_zero(self):
        """Test modulo by zero returns error."""
        response = client.post("/modulo", json={"a": 5, "b": 0})
        assert response.status_code == 400
        data = response.json()
        assert "Modulo by zero is not allowed" in data["detail"]
    
    def test_modulo_even_division(self):
        """Test modulo with even division."""
        response = client.post("/modulo", json={"a": 15, "b": 5})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 0
    
    def test_modulo_negative_numbers(self):
        """Test modulo with negative numbers."""
        response = client.post("/modulo", json={"a": -7, "b": 3})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == 2
    
    def test_modulo_floats(self):
        """Test modulo with floating point numbers."""
        response = client.post("/modulo", json={"a": 7.5, "b": 2.5})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == pytest.approx(0.0)

class TestErrorHandling:
    """Test cases for error handling across endpoints."""
    
    def test_missing_parameters(self):
        """Test endpoints with missing parameters."""
        response = client.post("/add", json={"a": 5})
        assert response.status_code == 422
        
        response = client.post("/subtract", json={"b": 3})
        assert response.status_code == 422
    
    def test_invalid_data_types(self):
        """Test endpoints with invalid data types."""
        response = client.post("/multiply", json={"a": "invalid", "b": 5})
        assert response.status_code == 422
        
        response = client.post("/divide", json={"a": 5, "b": "invalid"})
        assert response.status_code == 422
    
    def test_empty_request_body(self):
        """Test endpoints with empty request body."""
        response = client.post("/add", json={})
        assert response.status_code == 422
        
        response = client.post("/power", json={})
        assert response.status_code == 422

class TestAPIDocumentation:
    """Test cases for API documentation endpoints."""
    
    def test_openapi_schema(self):
        """Test OpenAPI schema is accessible."""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        schema = response.json()
        assert "openapi" in schema
        assert "paths" in schema
    
    def test_docs_endpoint(self):
        """Test interactive documentation is accessible."""
        response = client.get("/docs")
        assert response.status_code == 200
        assert "swagger" in response.text.lower()
    
    def test_redoc_endpoint(self):
        """Test ReDoc documentation is accessible."""
        response = client.get("/redoc")
        assert response.status_code == 200
        assert "redoc" in response.text.lower()