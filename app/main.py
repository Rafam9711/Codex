from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import fitz
from typing import Dict

app = FastAPI()

class PolizaRequest(BaseModel):
    numero_credito: str
    nombre_archivo: str

@app.post("/analizar-poliza")
async def analizar_poliza(data: PolizaRequest) -> Dict[str, str]:
    archivo_path = f"polizas/{data.nombre_archivo}"
    try:
        with fitz.open(archivo_path) as pdf:
            texto = "\n".join(page.get_text() for page in pdf)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al abrir PDF: {e}")

    texto_lower = texto.lower()

    contiene_poliza = "póliza" in texto_lower or "poliza" in texto_lower
    contiene_vigente = "vigente" in texto_lower
    contiene_credito = "crédito" in texto_lower or "credito" in texto_lower
    duplicado = "duplicado" in texto_lower

    estado = "vigente" if contiene_vigente else "no vigente"

    recomendacion = (
        "No requiere acción" if contiene_poliza and contiene_vigente and contiene_credito and not duplicado
        else "Revisar la póliza"
    )

    return {
        "numero_credito": data.numero_credito,
        "estado": estado,
        "duplicado": duplicado,
        "recomendacion": recomendacion,
    }
