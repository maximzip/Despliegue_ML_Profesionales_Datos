# Funciones predecir(), cargar_modelo(), normalizar_country()
import joblib
import pandas as pd
import os

pwd = os.path.dirname(os.path.abspath(__file__))

PAISES_CONOCIDOS = {'Australia', 'Brazil', 'Canada', 'France', 'Germany', 'India',
                     'Italy', 'Netherlands', 'Otros', 'Poland', 'Spain', 'Ukraine',
                     'United Kingdom of Great Britain and Northern Ireland',
                     'United States of America'}


def normalizar_country(country):
    return country if country in PAISES_CONOCIDOS else 'Otros'


def cargar_modelo():
    return joblib.load(os.path.join(pwd, "modelo_final.joblib"))


modelo = cargar_modelo()


def predecir(data: dict) -> dict:
    data = data.copy()
    data["Country"] = normalizar_country(data["Country"])

    X = pd.DataFrame([data])  # construye el DataFrame de una fila

    prediccion = int(modelo.predict(X)[0])
    probabilidad = float(modelo.predict_proba(X)[0][0])

    return {
        "prediction": prediccion,          
        "probabilidad_no_usa_ia": probabilidad
    }