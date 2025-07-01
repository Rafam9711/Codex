# Codex

Este proyecto contiene un ejemplo sencillo de una API REST creada con FastAPI.

## Uso

1. Instalar las dependencias (si se dispone de acceso a Internet):
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecutar el servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

La API expone un único endpoint POST en `/analizar-poliza` que recibe un JSON con el número de crédito y el nombre del archivo PDF ubicado en la carpeta `polizas/`. El servicio extrae el texto del PDF con **PyMuPDF** y verifica si contiene las palabras clave "póliza", "vigente" y "crédito" para determinar el estado de la póliza.
