# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize result to an empty string for the initial GET request
    result = ''
    
    # Check if the form was submitted (POST request)
    if request.method == 'POST':
        try:
            # 1. Retrieve data from the submitted form
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))
            operation = request.form.get('operation')

            # 2. Perform the calculation based on the selected operation
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    result = "Error: Division by zero!"
                else:
                    result = num1 / num2
            else:
                result = "Error: Invalid operation."
                
            # Optional: Round the result for cleaner display
            if isinstance(result, (float)):
                 result = round(result, 4)

        except (ValueError, TypeError):
            # Handle cases where inputs are not valid numbers
            result = "Error: Please enter valid numbers."
        
    # Render the HTML template, passing the latest result to it
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Run the application locally
    app.run(debug=True)
