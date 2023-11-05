# Usar la imagen base de Python
FROM python:3.9

# Copiar el script Python al contenedor
COPY import.py /usr/src/app/import.py

# Instalar la biblioteca redis-py
RUN pip install redis

# Establecer el directorio de trabajo
WORKDIR /usr/src/app

# Ejecutar el script Python al iniciar el contenedor
CMD ["python", "import.py"]

