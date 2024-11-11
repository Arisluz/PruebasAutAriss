# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el código de la aplicación al contenedor
COPY . /app

# Instalar dependencias (si tienes un archivo requirements.txt, instálalas)
# RUN pip install --no-cache-dir -r requirements.txt  # Descomenta si tienes dependencias

# Exponer el puerto que utilizará la aplicación
EXPOSE 8080

# Definir el comando para ejecutar la aplicación
CMD ["python", "app.py"]

