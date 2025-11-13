from flask import Flask, request, render_template_string

app = Flask(__name__)

# Operation functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error: Division by zero" if y == 0 else x / y

OPERATIONS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# HTML template with embedded CSS
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background-color: #f4f4f4;
        }
        input, select, button {
            margin: 10px;
            padding: 10px;
            font-size: 16px;
        }
        .result { color: green; font-weight: bold; }
        .error { color: red; }
    </style>
</head>
<body>
    <h1>🧮 Calculator</h1>
    <form method="POST">
        <input type="text" name="x" placeholder="First number" required>
        <select name="operation">
            <option value="+">+</option>
            <option value="-">−</option>
            <option value="*">×</option>
            <option value="/">÷</option>
        </select>
        <input type="text" name="y" placeholder="Second number" required>
        <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
        <p class="result">Result: {{ result }}</p>
    {% endif %}
    {% if error %}
        <p class="error">{{ error }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        try:
            x = float(request.form['x'])
            y = float(request.form['y'])
            op = request.form['operation']
            if op in OPERATIONS:
                result = OPERATIONS[op](x, y)
            else:
                error = "Invalid operation"
        except ValueError:
            error = "Please enter valid numbers"

    return render_template_string(HTML_TEMPLATE, result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
