from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ──────────────────────────────────────────
#  BASE DE DATOS FALSA  (lista en memoria)
#  Se reinicia cada vez que reinicias Flask
# ──────────────────────────────────────────
productos = [
    {"id": 1, "nombre": "Cuaderno",    "marca": "Norma",     "cantidad": 50,  "precio": 2.50},
    {"id": 2, "nombre": "Lapiz HB",    "marca": "Faber-Castell", "cantidad": 100, "precio": 0.30},
    {"id": 3, "nombre": "Borrador",    "marca": "Pelikan",   "cantidad": 80,  "precio": 0.50},
    {"id": 4, "nombre": "Boligrafo",   "marca": "Bic",       "cantidad": 90,  "precio": 0.60},
    {"id": 5, "nombre": "Colores",     "marca": "Crayola",   "cantidad": 120, "precio": 4.00},
    {"id": 6, "nombre": "Cartuchera",  "marca": "Totto",     "cantidad": 70,  "precio": 6.00},
    {"id": 7, "nombre": "Pegante",     "marca": "Colbon",    "cantidad": 50,  "precio": 2.00},
    {"id": 8, "nombre": "Marcadores",  "marca": "Sharpie",   "cantidad": 30,  "precio": 3.00},
]
siguiente_id = 9


# ── READ ──────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html", productos=productos)


# ── CREATE ────────────────────────────────
@app.route("/agregar", methods=["POST"])
def agregar():
    global siguiente_id
    productos.append({
        "id":       siguiente_id,
        "nombre":   request.form["nombre"],
        "marca": request.form["marca"],
        "cantidad": int(request.form["cantidad"]),
        "precio":   float(request.form["precio"]),
    })
    siguiente_id += 1
    return redirect(url_for("index"))


# ── UPDATE ────────────────────────────────
@app.route("/editar/<int:id>", methods=["POST"])
def editar(id):
    for p in productos:
        if p["id"] == id:
            p["nombre"]   = request.form["nombre"]
            p["marca"] = request.form["marca"]
            p["cantidad"] = int(request.form["cantidad"])
            p["precio"]   = float(request.form["precio"])
    return redirect(url_for("index"))


# ── DELETE ────────────────────────────────
@app.route("/eliminar/<int:id>")
def eliminar(id):
    productos[:] = [p for p in productos if p["id"] != id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
