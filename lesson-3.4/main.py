from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name", "Flask")
    return render_template("hello.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
