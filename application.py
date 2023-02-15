from flask import Flask, render_template

application = Flask(__name__)

app = application

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()