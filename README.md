```text
# Ejercicios de Programación Orientada a Objetos en Python
## Proyecto: Sistema de Adopción de Animales - Python Orientado a Objetos

Este proyecto contiene el desarrollo de un sistema para gestionar la adopción de animales, implementado en Python con un enfoque orientado a objetos. Incluye clases para representar animales, refugios, hogares de tránsito, usuarios y un sistema central que coordina todo.

---

## Estructura del proyecto
/ejercicios
├── 01_Modelos/             # Carpeta con las clases principales
│   ├── _oldies/            # Versiones anteriores y borradores de código
│   ├── animal.py
│   ├── perro.py
│   ├── gato.py
│   ├── refugio.py
│   ├── hogar_transito.py
│   ├── sistema.py
│   └── usuario.py
├── clase1/                 # Ejercicios y materiales de la cursada
├── clase2/
├── clase3/
├── clase4/
├── main.py                 # Script principal para pruebas y demostraciones
├── readme.md               # Este archivo :P
├── tp_final/               # Proyecto Django para la interfaz web 
   ├── manage.py
   ├── .env
   ├── .gitignore
   │
   ├── tp_final/               ← Configuración del proyecto (settings, urls, etc.)
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   │
   ├── the_pawject/            ← Mi app 
   │   ├── __init__.py
   │   ├── admin.py
   │   ├── apps.py
   │   ├── models.py
   │   ├── views/
   │   │   ├── __init__.py
   │   │   ├── usuario_views.py
   │   │   ├── refugio_views.py
   │   │   ├── hogar_views.py
   │   │   └── animal_views.py
   │   ├── forms/
   │   │   ├── __init__.py
   │   │   ├── usuario_form.py
   │   │   ├── refugio_form.py
   │   │   ├── hogar_form.py
   │   │   └── animal_form.py
   │   ├── templates/
   │   │   ├── base.html
   │   │   ├── home.html
   │   │   ├── login.html
   │   │   ├── registro.html
   │   │   ├── usuario/
   │   │   │   └── editar_usuario.html
   │   │   ├── refugio/
   │   │   │   └── crear_refugio.html
   │   │   ├── hogar_transito/
   │   │   │   └── crear_hogar.html
   │   │   └── animal/
   │   │       └── lista_animales.html
   │   ├── urls.py
   │   └── tests.py
   │
   ├── static/                 ← Para CSS, JS, imágenes personalizadas
   │   ├── css/
   │   └── js/
   │
   └── media/                  ← Para archivos subidos (como imágenes)


---

### Proyecto Django: Interfaz Web de Adopciones (`tp_final/`)

Este módulo corresponde a la interfaz web del sistema de adopciones de animales, construida con Django.

#### Funcionalidades:

* Formulario para crear usuarios con validaciones
* Autocompletado de dirección usando la **API de Google Maps**
* Estilos básicos con **Bootstrap 5**
* Variables sensibles protegidas mediante `.env` (no incluidas en el repositorio, usando un .gitignore para proteger la g-api)

#### Cómo correr el proyecto

1. Entrá a la carpeta `tp_final`:

   ```bash
   cd tp_final
   ```

2. Creá y activá un entorno virtual:

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. Instalá Django y dotenv:

   ```bash
   pip install django python-dotenv
   ```

4. Creá el archivo `.env` en la raíz de `tp_final/` con el siguiente contenido:

   ```
   GOOGLE_API_KEY=tu_clave_real
   ```

5. Aplicá migraciones:

   ```bash
   python manage.py migrate
   ```

6. Corré el servidor:

   ```bash
   python manage.py runserver
   ```

#### Verificá que la API funcione

Entrá a:

```
http://localhost:8000/test-api/
```

Deberías ver tu clave de Google Maps si fue cargada correctamente desde `.env`.

