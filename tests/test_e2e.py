"""
End-to-end tests for FastAPI Calculator web interface.
Tests user interactions using Playwright.
"""
import pytest
import asyncio
import uvicorn
import threading
import time
from playwright.async_api import async_playwright
from app.main import app

class TestServer:
    """Test server helper for E2E tests."""
    
    def __init__(self):
        self.server = None
        self.thread = None
        self.port = 8001  # Use different port to avoid conflicts
    
    def start(self):
        """Start the test server in a separate thread."""
        def run_server():
            uvicorn.run(app, host="127.0.0.1", port=self.port, log_level="error")
        
        self.thread = threading.Thread(target=run_server, daemon=True)
        self.thread.start()
        
        # Wait for server to start
        time.sleep(2)
    
    def stop(self):
        """Stop the test server."""
        # Server will stop when main thread exits due to daemon=True
        pass

@pytest.fixture(scope="session")
def test_server():
    """Fixture to start and stop test server for E2E tests."""
    server = TestServer()
    server.start()
    yield server
    server.stop()

@pytest.fixture(scope="session")
async def browser():
    """Fixture to start and stop browser for E2E tests."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        yield browser
        await browser.close()

@pytest.fixture
async def page(browser, test_server):
    """Fixture to create a new page for each test."""
    page = await browser.new_page()
    await page.goto(f"http://127.0.0.1:{test_server.port}")
    yield page
    await page.close()

class TestCalculatorInterface:
    """Test cases for calculator web interface."""
    
    @pytest.mark.asyncio
    async def test_page_loads(self, page):
        """Test that the calculator page loads correctly."""
        # Check page title
        title = await page.title()
        assert "FastAPI Calculator" in title
        
        # Check main heading
        heading = await page.text_content("h1")
        assert "FastAPI Calculator" in heading
        
        # Check display is present
        display = await page.query_selector("#display")
        assert display is not None
        
        # Check buttons are present
        buttons = await page.query_selector_all(".btn")
        assert len(buttons) > 0
    
    @pytest.mark.asyncio
    async def test_number_input(self, page):
        """Test entering numbers into the calculator."""
        # Click number buttons
        await page.click('button:has-text("1")')
        await page.click('button:has-text("2")')
        await page.click('button:has-text("3")')
        
        # Check display shows the numbers
        display_value = await page.input_value("#display")
        assert display_value == "123"
    
    @pytest.mark.asyncio
    async def test_clear_function(self, page):
        """Test the clear function."""
        # Enter some numbers
        await page.click('button:has-text("5")')
        await page.click('button:has-text("6")')
        
        # Verify numbers are displayed
        display_value = await page.input_value("#display")
        assert display_value == "56"
        
        # Click clear button
        await page.click('button:has-text("C")')
        
        # Verify display is cleared
        display_value = await page.input_value("#display")
        assert display_value == "0"
    
    @pytest.mark.asyncio
    async def test_addition_calculation(self, page):
        """Test addition calculation through UI."""
        # Enter: 5 + 3 =
        await page.click('button:has-text("5")')
        await page.click('button:has-text("+")')
        await page.click('button:has-text("3")')
        await page.click('button:has-text("=")')
        
        # Wait for calculation to complete
        await page.wait_for_timeout(1000)
        
        # Check result is displayed
        result_text = await page.text_content("#result")
        assert "5 + 3 = 8" in result_text
        
        # Check display shows result
        display_value = await page.input_value("#display")
        assert display_value == "8"
    
    @pytest.mark.asyncio
    async def test_subtraction_calculation(self, page):
        """Test subtraction calculation through UI."""
        # Enter: 10 - 4 =
        await page.click('button:has-text("1")')
        await page.click('button:has-text("0")')
        await page.click('button:has-text("-")')
        await page.click('button:has-text("4")')
        await page.click('button:has-text("=")')
        
        # Wait for calculation to complete
        await page.wait_for_timeout(1000)
        
        # Check result is displayed
        result_text = await page.text_content("#result")
        assert "10 - 4 = 6" in result_text
    
    @pytest.mark.asyncio
    async def test_multiplication_calculation(self, page):
        """Test multiplication calculation through UI."""
        # Enter: 6 * 7 =
        await page.click('button:has-text("6")')
        await page.click('button:has-text("×")')
        await page.click('button:has-text("7")')
        await page.click('button:has-text("=")')
        
        # Wait for calculation to complete
        await page.wait_for_timeout(1000)
        
        # Check result is displayed
        result_text = await page.text_content("#result")
        assert "6 × 7 = 42" in result_text
    
    @pytest.mark.asyncio
    async def test_division_calculation(self, page):
        """Test division calculation through UI."""
        # Enter: 15 / 3 =
        await page.click('button:has-text("1")')
        await page.click('button:has-text("5")')
        await page.click('button:has-text("÷")')
        await page.click('button:has-text("3")')
        await page.click('button:has-text("=")')
        
        # Wait for calculation to complete
        await page.wait_for_timeout(1000)
        
        # Check result is displayed
        result_text = await page.text_content("#result")
        assert "15 ÷ 3 = 5" in result_text
    
    @pytest.mark.asyncio
    async def test_power_calculation(self, page):
        """Test power calculation through UI."""
        # Enter: 2 ^ 3 =
        await page.click('button:has-text("2")')
        await page.click('button:has-text("^")')
        await page.click('button:has-text("3")')
        await page.click('button:has-text("=")')
        
        # Wait for calculation to complete
        await page.wait_for_timeout(1000)
        
        # Check result is displayed
        result_text = await page.text_content("#result")
        assert "2 ^ 3 = 8" in result_text
    
    @pytest.mark.asyncio
    async def test_modulo_calculation(self, page):
        """Test modulo calculation through UI."""
        # Enter: 10 % 3 =
        await page.click('button:has-text("1")')
        await page.click('button:has-text("0")')
        await page.click('button:has-text("%")')
        await page.click('button:has-text("3")')
        await page.click('button:has-text("=")')
        
        # Wait for calculation to complete
        await page.wait_for_timeout(1000)
        
        # Check result is displayed
        result_text = await page.text_content("#result")
        assert "10 % 3 = 1" in result_text
    
    @pytest.mark.asyncio
    async def test_decimal_numbers(self, page):
        """Test calculations with decimal numbers."""
        # Enter: 2.5 + 3.7 =
        await page.click('button:has-text("2")')
        await page.click('button:has-text(".")')
        await page.click('button:has-text("5")')
        await page.click('button:has-text("+")')
        await page.click('button:has-text("3")')
        await page.click('button:has-text(".")')
        await page.click('button:has-text("7")')
        await page.click('button:has-text("=")')
        
        # Wait for calculation to complete
        await page.wait_for_timeout(1000)
        
        # Check result is displayed
        result_text = await page.text_content("#result")
        assert "2.5 + 3.7 = 6.2" in result_text
    
    @pytest.mark.asyncio
    async def test_division_by_zero_error(self, page):
        """Test division by zero shows error."""
        # Enter: 5 / 0 =
        await page.click('button:has-text("5")')
        await page.click('button:has-text("÷")')
        await page.click('button:has-text("0")')
        await page.click('button:has-text("=")')
        
        # Wait for calculation to complete
        await page.wait_for_timeout(1000)
        
        # Check error is displayed
        result_text = await page.text_content("#result")
        assert "Error" in result_text
        assert "Division by zero" in result_text
        
        # Check result div has error styling
        result_class = await page.get_attribute("#result", "class")
        assert "error" in result_class
    
    @pytest.mark.asyncio
    async def test_modulo_by_zero_error(self, page):
        """Test modulo by zero shows error."""
        # Enter: 5 % 0 =
        await page.click('button:has-text("5")')
        await page.click('button:has-text("%")')
        await page.click('button:has-text("0")')
        await page.click('button:has-text("=")')
        
        # Wait for calculation to complete
        await page.wait_for_timeout(1000)
        
        # Check error is displayed
        result_text = await page.text_content("#result")
        assert "Error" in result_text
        assert "Modulo by zero" in result_text
    
    @pytest.mark.asyncio
    async def test_multiple_calculations(self, page):
        """Test performing multiple calculations in sequence."""
        # First calculation: 3 + 2 = 5
        await page.click('button:has-text("3")')
        await page.click('button:has-text("+")')
        await page.click('button:has-text("2")')
        await page.click('button:has-text("=")')
        await page.wait_for_timeout(1000)
        
        result_text = await page.text_content("#result")
        assert "3 + 2 = 5" in result_text
        
        # Clear for next calculation
        await page.click('button:has-text("C")')
        
        # Second calculation: 8 * 3 = 24
        await page.click('button:has-text("8")')
        await page.click('button:has-text("×")')
        await page.click('button:has-text("3")')
        await page.click('button:has-text("=")')
        await page.wait_for_timeout(1000)
        
        result_text = await page.text_content("#result")
        assert "8 × 3 = 24" in result_text
    
    @pytest.mark.asyncio
    async def test_keyboard_input(self, page):
        """Test keyboard input functionality."""
        # Focus on the page
        await page.focus("body")
        
        # Type a calculation using keyboard
        await page.keyboard.type("5+3")
        await page.keyboard.press("Enter")
        
        # Wait for calculation to complete
        await page.wait_for_timeout(1000)
        
        # Check result is displayed
        result_text = await page.text_content("#result")
        assert "5 + 3 = 8" in result_text
    
    @pytest.mark.asyncio
    async def test_api_info_section(self, page):
        """Test API information section is displayed."""
        # Check API info section exists
        api_info = await page.query_selector(".api-info")
        assert api_info is not None
        
        # Check API endpoints are listed
        api_text = await page.text_content(".api-info")
        assert "POST /add" in api_text
        assert "POST /subtract" in api_text
        assert "POST /multiply" in api_text
        assert "POST /divide" in api_text
        assert "POST /power" in api_text
        assert "POST /modulo" in api_text
        assert "GET /docs" in api_text
        assert "GET /health" in api_text

class TestResponsiveDesign:
    """Test cases for responsive design."""
    
    @pytest.mark.asyncio
    async def test_mobile_viewport(self, browser, test_server):
        """Test calculator works on mobile viewport."""
        # Create mobile page
        page = await browser.new_page()
        await page.set_viewport_size({"width": 375, "height": 667})  # iPhone SE
        await page.goto(f"http://127.0.0.1:{test_server.port}")
        
        # Test basic functionality
        await page.click('button:has-text("2")')
        await page.click('button:has-text("+")')
        await page.click('button:has-text("3")')
        await page.click('button:has-text("=")')
        
        await page.wait_for_timeout(1000)
        
        result_text = await page.text_content("#result")
        assert "2 + 3 = 5" in result_text
        
        await page.close()
    
    @pytest.mark.asyncio
    async def test_tablet_viewport(self, browser, test_server):
        """Test calculator works on tablet viewport."""
        # Create tablet page
        page = await browser.new_page()
        await page.set_viewport_size({"width": 768, "height": 1024})  # iPad
        await page.goto(f"http://127.0.0.1:{test_server.port}")
        
        # Test basic functionality
        await page.click('button:has-text("4")')
        await page.click('button:has-text("×")')
        await page.click('button:has-text("6")')
        await page.click('button:has-text("=")')
        
        await page.wait_for_timeout(1000)
        
        result_text = await page.text_content("#result")
        assert "4 × 6 = 24" in result_text
        
        await page.close()