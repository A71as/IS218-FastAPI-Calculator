// Calculator JavaScript

let currentExpression = '';
let firstOperand = null;
let currentOperator = null;
let waitingForOperand = false;

function appendToDisplay(value) {
    const display = document.getElementById('display');
    
    if (waitingForOperand) {
        display.value = value;
        waitingForOperand = false;
    } else {
        display.value = display.value === '0' ? value : display.value + value;
    }
    
    currentExpression += value;
}

function clearDisplay() {
    document.getElementById('display').value = '0';
    document.getElementById('result').textContent = 'Ready for calculation';
    document.getElementById('result').className = 'result-display';
    currentExpression = '';
    firstOperand = null;
    currentOperator = null;
    waitingForOperand = false;
}

async function calculate() {
    const expression = document.getElementById('display').value;
    const resultDiv = document.getElementById('result');
    
    if (!expression || expression === '0') {
        showResult('Please enter a calculation', 'error');
        return;
    }
    
    try {
        // Parse the expression to extract operands and operator
        const parsed = parseExpression(expression);
        if (!parsed) {
            showResult('Invalid expression format', 'error');
            return;
        }
        
        const { a, b, operation } = parsed;
        
        // Make API call based on operation
        const response = await makeCalculationRequest(operation, a, b);
        
        if (response.error) {
            showResult(`Error: ${response.error}`, 'error');
        } else {
            showResult(`${a} ${getOperatorSymbol(operation)} ${b} = ${response.result}`, 'success');
            document.getElementById('display').value = response.result;
        }
        
    } catch (error) {
        console.error('Calculation error:', error);
        showResult(`Error: ${error.message}`, 'error');
    }
}

function parseExpression(expression) {
    // Remove spaces
    expression = expression.replace(/\s/g, '');
    
    // Find the last operator in the expression
    const operators = ['+', '-', '*', '/', '^', '%'];
    let operatorIndex = -1;
    let operator = null;
    
    // Look for operators from right to left (except for negative numbers)
    for (let i = expression.length - 1; i > 0; i--) {
        if (operators.includes(expression[i])) {
            // Skip if this might be a negative sign
            if (expression[i] === '-' && (i === 0 || operators.includes(expression[i-1]))) {
                continue;
            }
            operatorIndex = i;
            operator = expression[i];
            break;
        }
    }
    
    if (operatorIndex === -1) {
        return null;
    }
    
    const a = parseFloat(expression.substring(0, operatorIndex));
    const b = parseFloat(expression.substring(operatorIndex + 1));
    
    if (isNaN(a) || isNaN(b)) {
        return null;
    }
    
    const operationMap = {
        '+': 'add',
        '-': 'subtract',
        '*': 'multiply',
        '/': 'divide',
        '^': 'power',
        '%': 'modulo'
    };
    
    return {
        a: a,
        b: b,
        operation: operationMap[operator]
    };
}

function getOperatorSymbol(operation) {
    const symbolMap = {
        'add': '+',
        'subtract': '-',
        'multiply': '×',
        'divide': '÷',
        'power': '^',
        'modulo': '%'
    };
    return symbolMap[operation] || operation;
}

async function makeCalculationRequest(operation, a, b) {
    try {
        const response = await fetch(`/${operation}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ a: a, b: b })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            return { error: data.detail || 'Calculation failed' };
        }
        
        return data;
    } catch (error) {
        return { error: 'Network error: ' + error.message };
    }
}

function showResult(message, type = 'success') {
    const resultDiv = document.getElementById('result');
    resultDiv.textContent = message;
    resultDiv.className = `result-display ${type}`;
}

// Keyboard support
document.addEventListener('keydown', function(event) {
    const key = event.key;
    
    if (key >= '0' && key <= '9' || key === '.') {
        appendToDisplay(key);
    } else if (key === '+') {
        appendToDisplay('+');
    } else if (key === '-') {
        appendToDisplay('-');
    } else if (key === '*') {
        appendToDisplay('*');
    } else if (key === '/') {
        event.preventDefault();
        appendToDisplay('/');
    } else if (key === '%') {
        appendToDisplay('%');
    } else if (key === '^') {
        appendToDisplay('^');
    } else if (key === 'Enter' || key === '=') {
        event.preventDefault();
        calculate();
    } else if (key === 'Escape' || key === 'c' || key === 'C') {
        clearDisplay();
    }
});

// Initialize display
clearDisplay();