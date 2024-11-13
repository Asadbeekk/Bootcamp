from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/family")
def family():
    family_member = ['Avazbek', 'Dostonbek', 'Zulfiya']
    return render_template("family.html", family_member=family_member)

if __name__ == "__main__":
    app.run(debug=True)
