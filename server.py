from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
app.secret_key = "hello"

@app.route("/")
def form():
    
    return render_template("index.html")

@app.route("/process", methods=["GET", "POST"])
def process():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]
    print(request.form)
    return redirect(url_for("result"))

@app.route("/result")
def result():

    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True)