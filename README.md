# 🐾 FastAPI Veterinaria CRUD

Este es un proyecto que implementa un CRUD para gestionar animales en una veterinaria, utilizando **FastAPI** como framework backend y **SQLAlchemy** como ORM para conectarse a una base de datos relacional.

Fue hecho para practicar la creación de APIs REST con validaciones, dependencias y operaciones CRUD.

🔗 Link de Uso
https://fastapi-practice-production-abb6.up.railway.app/docs

🔗 Puedes acceder a la documentación automática desplegada por FastAPI en los siguientes enlaces:

- 📚 http://127.0.0.1:8000/docs
- 📚 http://127.0.0.1:8000/redoc

---

## 📁 Estructura del Proyecto

```
├── main.py             # Contiene las rutas y lógica del CRUD para los animales
├── models.py           # Define los modelos y enums de la base de datos
├── database.py         # Configuración de conexión a la base de datos y sesión
├── requirements.txt    # Dependencias necesarias del entorno
├── procfile            # Configuración para despliegue en Railway
├── README.md           # Este archivo 📘
└── .env                # Variables de entorno 
```

---

## ⚙️ Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/Zers04/fastAPI-practice.git
cd fastapi-practice
```

2. (Opcional) Crea un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución

Ejecuta el servidor con el siguiente comando:

```bash
uvicorn main:app --reload
```

Esto levantará el servidor local en `http://127.0.0.1:8000`.

---

## 🔁 Endpoints disponibles

| Método | Endpoint               | Descripción                             |
|--------|------------------------|-----------------------------------------|
| GET    | `/animales/`           | Obtener todos los animales              |
| GET    | `/animales/{id}`       | Obtener un animal por su ID             |
| POST   | `/animales/`           | Registrar un nuevo animal               |
| PUT    | `/animales/{id}`       | Actualizar los datos de un animal       |
| DELETE | `/animales/{id}`       | Eliminar un animal de la base de datos  |

---

## 🧠 Aprendizajes y prácticas

Este proyecto permite aprender y poner en práctica:

- Creación de APIs REST con FastAPI
- Conexión a bases de datos usando SQLAlchemy
- Organización de dependencias y rutas limpias

---

## 👥 Integrantes

- Juan David Cataño Castillo – 202160227 
- Valentina Londoño Dueñas – 202160173
