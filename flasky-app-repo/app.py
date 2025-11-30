# app.py
from flask import Flask, render_template

app = Flask(__name__)

# 定义一个路由来处理根URL (/)
@app.route('/')
def home():
    # 使用 render_template() 来渲染 templates/index.html
    return render_template('index.html')

if __name__ == '__main__':
    # 在本地运行应用
    app.run(debug=True)
