from flask import Flask, request, jsonify, render_template
from model import cargar_modelo, predecir 



app = Flask(__name__)
modelo = cargar_modelo()

# Lista de campos que el modelo necesita
CAMPOS_REQUERIDOS = ['Age', 'EdLevel', 'Employment', 'WorkExp', 'LearnCodeChoose',
    'DevType', 'OrgSize', 'ICorPM', 'RemoteWork', 'Industry',
    'Country', 'ConvertedCompYearly']

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/app")
def home():
    return render_template("index.html")

def _procesar(data: dict) -> tuple[dict, int]:
    """Valida y predice. Devuelve (resultado_o_error, status_code)."""
    faltantes = [c for c in CAMPOS_REQUERIDOS if not (data or {}).get(c)]
    if faltantes:
        return {"error": f"Faltan campos: {faltantes}"}, 400

    try:
        data["ConvertedCompYearly"] = float(data["ConvertedCompYearly"])
        data["WorkExp"] = float(data["WorkExp"])
    except (ValueError, TypeError):
        return {"error": "ConvertedCompYearly y WorkExp deben ser numéricos"}, 400

    return predecir(data), 200

# 1er ENDPOINT. POST con JSON con los 12 campos y devuelve predicción de una persona
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    resultado, status = _procesar(data)
    return jsonify(resultado), status

# 2º ENDPOINT. GET de prueba con query string
@app.route("/predict_get", methods=["GET"])
def predict_get():
    data = {campo: request.args.get(campo) for campo in CAMPOS_REQUERIDOS}
    resultado, status = _procesar(data)
    return jsonify(resultado), status

# 3er ENDPOINT. POST con JSON de datos plantilla (se despliega en la presentación)
# El cliente sube un archivo JSON con los datos de cada trabajador de su plantilla con cada variable 
# sería como una lista como la siguiente: [{...trabajador1...}, {...trabajador2...}]
@app.route("/predict_batch", methods=["POST"])
def predict_batch():
    lista_empleados = request.get_json()
    if not isinstance(lista_empleados, list):
        return jsonify({"error": "Se espera una lista de empleados"}), 400

    validos = []
    errores = []
    for emp in lista_empleados:
        resultado, status = _procesar(emp)
        (validos if status == 200 else errores).append(resultado)

    no_usa_ia = sum(1 for r in validos if r.get("prediction") == 0)

    return jsonify({
        "total_empleados": len(lista_empleados),
        "procesados_correctamente": len(validos),
        "con_error": len(errores),
        "no_usan_ia": no_usa_ia,
        "porcentaje": round(no_usa_ia / len(validos) * 100, 1) if validos else 0
    })


if __name__ == "__main__":
    app.run(port=5000, debug=False)