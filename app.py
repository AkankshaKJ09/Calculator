from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
        <h1>Basic Calculator</h1>
        <form action="/calculate" method="POST">
            <input type="number" name="num1" placeholder="Enter first number" required>
            <select name="operation" required>
                <option value="add">+</option>
                <option value="subtract">-</option>
                <option value="multiply">*</option>
                <option value="divide">/</option>
            </select>
            <input type="number" name="num2" placeholder="Enter second number" required>
            <button type="submit">Calculate</button>
        </form>
    """)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero"

        return render_template_string("""
            <h1>Result: {{ result }}</h1>
            <a href="/">Go Back</a>
        """, result=result)

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)