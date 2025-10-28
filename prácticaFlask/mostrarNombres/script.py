from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def mostrar_nombres():
    if request.method == "POST":
        nombre = request.form["nombre"]
        return redirect(url_for("usuarios", nombres=nombre))
    return render_template("index.html", nombre="visitante")

@app.route("/<nombres>")
def usuarios(nombres):
    return render_template("index.html", nombre=nombres)

if __name__ == "__main__":
    app.run(debug=True)
