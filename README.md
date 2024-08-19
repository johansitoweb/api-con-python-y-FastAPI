# api-con-python-y-FastAPI
Esta es una api contruida con python y FastAPI
Instrucciones para Ejecutar la API
Ejecuta la API:

En la terminal, navega al directorio donde se encuentra main.py y ejecuta:


uvicorn main:app --reload
Esto iniciará el servidor en http://127.0.0.1:8000.

Interactúa con la API:

Puedes usar herramientas como Postman o curl para interactuar con la API.

Crear un ítem:


curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{"id": 1, "name": "Item 1", "description": "Este es el primer ítem."}'
Leer todos los ítems:


curl -X GET "http://127.0.0.1:8000/items/"
Leer un ítem específico:


curl -X GET "http://127.0.0.1:8000/items/1"
Eliminar un ítem:


curl -X DELETE "http://127.0.0.1:8000/items/1"
Documentación Automática:

