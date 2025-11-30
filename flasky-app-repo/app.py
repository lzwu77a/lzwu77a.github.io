from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    expression = ""
    if request.method == "POST":
        expression = request.form.get("expression")
        if expression == "C":
            result = ""
        elif expression == "=":
            try:
                result = eval(request.form.get("current_expression"))
            except Exception as e:
                result = "Error"
        else:
            result = expression

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
