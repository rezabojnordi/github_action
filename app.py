from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World! from CI/CD with GitHub Actions!"

if __name__ == '__main__':
    # در حالت توسعه، از پورت 5000 استفاده می‌کند
    # در سرور، توسط یک وب‌سرور حرفه‌ای‌تر اجرا خواهد شد
    app.run(host='0.0.0.0', port=5000)
