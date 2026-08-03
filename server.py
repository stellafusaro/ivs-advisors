from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
	return render_template("projects.html")

@app.route("/consultant")
def consultant():
	return render_template("consultant.html")

@app.route("/cde")
def cde():
         return render_template("cde.html")

@app.route("/banker")
def banker():
         return render_template("banker.html")

if __name__ == "__main__":
    app.run(debug=True)

