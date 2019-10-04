from flask import Flask
app  = Flask(__name__)

# 如果访问 /,返回 Index Page
@app.route('/')
def index():
    return 'Index Page'

# 如果访问 /hello，返回 Hello, World!
@app.route('/hello')
def hello():
    return 'Hello, World!'