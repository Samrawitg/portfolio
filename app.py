from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    with open("projects.json") as f:
        projects = json.load(f)
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)