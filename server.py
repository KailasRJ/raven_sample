from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hey, it's the Python server speaking!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    