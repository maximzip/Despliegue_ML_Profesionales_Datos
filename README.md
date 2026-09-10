# API de predicción — uso de IA en profesionales de datos

Modelo de clasificación (LogisticRegression) que predice si un profesional de datos
usa IA en su trabajo, a partir de datos demográficos y laborales (Stack Overflow
Developer Survey 2025). Objetivo: estimar necesidades de formación en una plantilla.

## Endpoints

- `GET /` — interfaz web para probar el modelo manualmente.
- `POST /predict` — predicción de una persona. Body JSON con 12 campos (ver ejemplo abajo).
- `GET /predict_get` — igual que `/predict` pero vía query string (solo para pruebas rápidas).
- `POST /predict_batch` — predicción de una plantilla completa. Body JSON = lista de personas.
  Devuelve el conteo y porcentaje de personas que no usan IA.

## Ejemplo de uso

\`\`\`bash
curl -X POST https://<tu-app>.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{"Age": "25-34 years old", "EdLevel": "...", ...}'
\`\`\`

## Variables de entrada

| Campo | Tipo | Valores posibles / ejemplo |
|---|---|---|
| Age | categórico | "18-24 years old" … "65 years or older" |
| EdLevel | categórico | "Bachelor’s degree (B.A., B.S., B.Eng., etc.)", etc. |
| Employment | categórico | "Employed", "Student", "Retired", etc. |
| WorkExp | numérico (años) | 4.0 |
| LearnCodeChoose | categórico | "Yes, I am new to coding or currently a student", etc. |
| DevType | categórico | "Data scientist", "AI/ML engineer", etc. |
| OrgSize | categórico | "100 to 499 employees", "10,000 or more employees", etc. |
| ICorPM | categórico | "Individual contributor", "People manager" |
| RemoteWork | categórico | "Remote", "In-person", "Hybrid...", etc. |
| Industry | categórico | "Software Development", "Fintech", etc. |
| Country | categórico | "Spain", "Germany", ... "Otros" (para países no frecuentes) |
| ConvertedCompYearly | numérico (dólares) | 45000 |

Todas las opciones exactas están disponibles como `<select>` en la interfaz web (`/`),
para evitar errores de tecleo en valores categóricos.

## Instalación local

\`\`\`bash
pip install -r requirements.txt
python app.py
\`\`\`

## Despliegue

Desplegado en Render. Build: `pip install -r requirements.txt`. Start: `gunicorn app:app`.

## Desarrollador

Maksym Chaika Palamaryuk
