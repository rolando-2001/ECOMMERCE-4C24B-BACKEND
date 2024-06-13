# Clona el repositorio y tiene que estar dentro de esa carpeta ECOMMERCE-4C24B-BACKEND
# Crea y activa un entorno virtual (venv) en la carpeta del proyecto:

# python -m venv venv venv\Scripts\activate

# Instala las dependencias del proyecto utilizando el archivo requirements.txt:
# pip install -r requirements.txt

# Esto instalará todas las dependencias necesarias
# En el archivo settings.py, comenta o elimina la siguiente línea:
# DATABASES = { 'default': dj_database_url.config() }

# Agrega la configuración de tu base de datos MySQL en settings.py:
# python DATABASES = { 'default': { 'ENGINE': 'django.db.backends.mysql', 'NAME': 'prueba', 'USER': 'root', 'PASSWORD': '', 'HOST': 'localhost', 'PORT': '3306', } }

# Asegúrate de reemplazar 'NAME', 'USER', 'PASSWORD' con los valores correspondientes a tu base de datos MySQL.
# Finalmente, aplica las migraciones para crear las tablas en tu base de datos:
# python manage.py migrate