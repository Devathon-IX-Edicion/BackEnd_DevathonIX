# 🧙‍♂️ Platos Mágicas de Hufflepuff - Backend

![Hufflepuff Banner](https://media.discordapp.net/attachments/1349453635850993767/1354637021317959690/Leonardo_Phoenix_10_Design_a_heraldic_shield_with_a_majestic_b_0.png?ex=67eb4989&is=67e9f809&hm=c9c18748dc85b648085248ab12d026ae92ecbf039a484efffbdc742c77b0cb3c&=&format=webp&quality=lossless&width=648&height=648)

> *"Los buenos Hufflepuff son leales y justos, pacientes y verdaderos, y no temen el trabajo duro."* - El Sombrero Seleccionador

## 📜 Sobre el Proyecto

Bienvenidos al backend del **MVP de platos Mágicas de Hufflepuff**, nuestro proyecto para el Devathon con temática de Harry Potter. Como buenos Hufflepuff, hemos trabajado arduamente para crear una plataforma donde los magos pueden experimentar con ingredientes mágicos, crear platos únicas y descubrir efectos sorprendentes.

Este proyecto está construido con **Django REST Framework**, una potente herramienta para crear APIs que conectarán nuestra aplicación frontend con la base de datos donde almacenaremos todas las recetas, ingredientes y resultados mágicos.

## 🌱 Características Principales

- Gestión de ingredientes mágicos por categorías
- Sistema de creación y combinación de platos
- Registro de efectos mágicos y resultados
- Historial de intentos para cada sesión de usuario
- Listado de recetas descubiertas con posibilidad de marcarlas como favoritas

## 🧪 Guía de Instalación y Configuración

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### 1. Clonar el Repositorio

```bash
git clone https://github.com/hufflepuff-team/magical-potions-backend.git
cd magical-potions-backend
```

### 2. Crear y Activar un Entorno Virtual

#### En Windows:
```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
venv\Scripts\activate
```

#### En macOS/Linux:
```bash
# Crear el entorno virtual
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate
```

Una vez activado, deberías ver `(venv)` al inicio de tu línea de comandos.

### 3. Instalar Dependencias

```bash
pip install django djangorestframework django-cors-headers
```

### 4. Configurar el Proyecto

```bash
django-admin startproject hufflepuff_potions .
cd hufflepuff_potions
django-admin startapp potions_api
cd ..
```

No olvides añadir 'rest_framework', 'corsheaders' y 'hufflepuff_potions.potions_api' a INSTALLED_APPS en settings.py.

### 5. Configurar la Base de Datos

Para el MVP, utilizaremos SQLite que viene integrado con Django:

```python
# En hufflepuff_potions/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### 6. Crear Modelos

Implementa los modelos en `potions_api/models.py` según el esquema DBML que definimos:
- Category
- Ingredient
- Effect
- Recipe
- RecipeIngredient
- AttemptHistory
- AttemptIngredient
- FavoriteRecipe

### 7. Realizar Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Estructura de la API

Nuestra API sigue una arquitectura RESTful utilizando los componentes de Django REST Framework:

- **Serializers**: Convierten los modelos a JSON y viceversa
- **ViewSets**: Manejan las operaciones CRUD para cada modelo
- **Routers**: Configuran automáticamente las URLs para los endpoints

### 9. Endpoints Principales

```
/api/categories/     # Categorías de ingredientes
/api/ingredients/    # Ingredientes mágicos
/api/effects/        # Efectos mágicos
/api/recipes/        # Recetas de platos
/api/attempts/       # Historial de intentos
/api/favorites/      # Recetas favoritas
```

### 10. Iniciar el Servidor

```bash
python manage.py runserver
```

El servidor estará disponible en [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 🧙‍♂️ Datos de Prueba (Opcional)

Para crear algunos datos iniciales:

```bash
# Crear un superusuario para acceder al admin
python manage.py createsuperuser

# Accede al admin en:
# http://127.0.0.1:8000/admin/
```

## Manual de documentación de la API con drf-yasg

### Requisitos
- Django ≥ 2.2 y Django REST Framework ≥ 3.10  
- drf-yasg instalado:
  ```bash
  pip install drf-yasg
Esto levantará tu API en http://127.0.0.1:8000/.
Django REST Framework

Abre tu navegador web favorito
Puede ser Chrome, Firefox, Safari, Edge, etc.

Visita Swagger UI

 URL: http://127.0.0.1:8000/swagger/

        drf-yasg

    Visita ReDoc

        URL: http://127.0.0.1:8000/redoc/

        Qué verás: documentación alternativa optimizada para lectura, con menú lateral y secciones plegables.
        drf-yasg

    Consulta el esquema crudo (OpenAPI)

        JSON: http://127.0.0.1:8000/swagger.json

        YAML: http://127.0.0.1:8000/swagger.yaml

## 🦡 Equipo Hufflepuff

Estamos orgullosos de representar a la casa Hufflepuff en este Devathon. Como auténticos Hufflepuff, hemos puesto nuestro esfuerzo, dedicación y trabajo duro en este proyecto.

## 🛠️ Próximos Pasos

- Implementar sistema de autenticación (para futura versión)
- Añadir más tests unitarios
- Optimizar consultas a la base de datos
- Implementar cache para mejorar rendimiento

---

*Desarrollado con 💛🖤 por el equipo Hufflepuff para el Devathon 2025*
