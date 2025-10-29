"""
FastAPI Calculator Application.
Provides REST API endpoints for calculator operations.
"""
import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from typing import Union
import uvicorn

from app.operations import (
    add, subtract, multiply, divide, power, modulo, CalculatorError
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Calculator API",
    description="A simple calculator API with basic arithmetic operations",
    version="1.0.0"
)

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Pydantic models for request/response
class CalculationRequest(BaseModel):
    a: Union[int, float] = Field(..., description="First number")
    b: Union[int, float] = Field(..., description="Second number")
    
    class Config:
        json_schema_extra = {
            "example": {
                "a": 10,
                "b": 5
            }
        }

class CalculationResponse(BaseModel):
    result: Union[int, float] = Field(..., description="Result of the calculation")
    operation: str = Field(..., description="Operation performed")
    operands: dict = Field(..., description="Input operands")
    
    class Config:
        json_schema_extra = {
            "example": {
                "result": 15,
                "operation": "addition",
                "operands": {"a": 10, "b": 5}
            }
        }

class ErrorResponse(BaseModel):
    error: str = Field(..., description="Error message")
    operation: str = Field(..., description="Operation that failed")

# Root endpoint - serve calculator web interface
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serve the calculator web interface."""
    logger.info("Serving calculator web interface")
    return templates.TemplateResponse("calculator.html", {"request": request})

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint."""
    logger.info("Health check requested")
    return {"status": "healthy", "service": "Calculator API"}

# Addition endpoint
@app.post("/add", response_model=CalculationResponse)
async def add_numbers(request: CalculationRequest):
    """Add two numbers."""
    try:
        logger.info(f"Addition requested: {request.a} + {request.b}")
        result = add(request.a, request.b)
        return CalculationResponse(
            result=result,
            operation="addition",
            operands={"a": request.a, "b": request.b}
        )
    except CalculatorError as e:
        logger.error(f"Addition failed: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error in addition: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Subtraction endpoint
@app.post("/subtract", response_model=CalculationResponse)
async def subtract_numbers(request: CalculationRequest):
    """Subtract two numbers."""
    try:
        logger.info(f"Subtraction requested: {request.a} - {request.b}")
        result = subtract(request.a, request.b)
        return CalculationResponse(
            result=result,
            operation="subtraction",
            operands={"a": request.a, "b": request.b}
        )
    except CalculatorError as e:
        logger.error(f"Subtraction failed: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error in subtraction: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Multiplication endpoint
@app.post("/multiply", response_model=CalculationResponse)
async def multiply_numbers(request: CalculationRequest):
    """Multiply two numbers."""
    try:
        logger.info(f"Multiplication requested: {request.a} * {request.b}")
        result = multiply(request.a, request.b)
        return CalculationResponse(
            result=result,
            operation="multiplication",
            operands={"a": request.a, "b": request.b}
        )
    except CalculatorError as e:
        logger.error(f"Multiplication failed: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error in multiplication: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Division endpoint
@app.post("/divide", response_model=CalculationResponse)
async def divide_numbers(request: CalculationRequest):
    """Divide two numbers."""
    try:
        logger.info(f"Division requested: {request.a} / {request.b}")
        result = divide(request.a, request.b)
        return CalculationResponse(
            result=result,
            operation="division",
            operands={"a": request.a, "b": request.b}
        )
    except CalculatorError as e:
        logger.error(f"Division failed: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error in division: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Power endpoint
@app.post("/power", response_model=CalculationResponse)
async def power_numbers(request: CalculationRequest):
    """Raise a number to a power."""
    try:
        logger.info(f"Power requested: {request.a} ^ {request.b}")
        result = power(request.a, request.b)
        return CalculationResponse(
            result=result,
            operation="power",
            operands={"a": request.a, "b": request.b}
        )
    except CalculatorError as e:
        logger.error(f"Power operation failed: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error in power operation: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Modulo endpoint
@app.post("/modulo", response_model=CalculationResponse)
async def modulo_numbers(request: CalculationRequest):
    """Calculate modulo of two numbers."""
    try:
        logger.info(f"Modulo requested: {request.a} % {request.b}")
        result = modulo(request.a, request.b)
        return CalculationResponse(
            result=result,
            operation="modulo",
            operands={"a": request.a, "b": request.b}
        )
    except CalculatorError as e:
        logger.error(f"Modulo operation failed: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error in modulo operation: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Exception handlers
@app.exception_handler(CalculatorError)
async def calculator_exception_handler(request: Request, exc: CalculatorError):
    """Handle calculator-specific exceptions."""
    logger.error(f"Calculator error: {exc}")
    return HTTPException(status_code=400, detail=str(exc))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)