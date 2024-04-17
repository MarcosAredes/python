from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/Base_Python")
def python_page():
    return render_template("BP.html")


@app.route("/Data_Science")
def data_science_page():
    return render_template("DS.html")


@app.route("/Machine_Learning")
def machine_learning_page():
    return render_template("ML.html")


if __name__ == "__main__":
    app.run(debug=True)
