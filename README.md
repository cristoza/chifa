# 🥢 Chifa-Bot: Asistente Inteligente con Rastreo de Auditoría

Este proyecto es un chatbot especializado para un Chifa, capaz de responder a 50 consultas frecuentes sobre el menú, precios y servicios. Está diseñado como un **widget inyectable** que puede integrarse en cualquier sitio web existente sin alterar su estructura original.

## 🚀 Características Técnicas
* **Inyección No Invasiva:** Interfaz de usuario flotante (Burbuja) mediante CSS y JS.
* **Backend Robusto:** Servidor API REST construido con Python y Flask.
* **Base de Datos Relacional:** Almacenamiento en PostgreSQL para gestión de respuestas y auditoría.
* **Rastreo de Seguridad:** El sistema registra automáticamente la **IP del cliente, fecha y hora exacta** de cada consulta realizada.

## 🛠️ Requisitos e Instalación

### 1. Base de Datos (PostgreSQL)
Antes de correr el servidor, debes configurar las tablas y los datos.
* Abre tu gestor de base de datos (pgAdmin o psql).
* Crea una base de datos llamada `chifa_db`.
* Ejecuta el script contenido en el archivo `setup.sql`.

### 2. Frontend (Html)
Agrega la Burbuja del chatbot copiado el contenido de 'inyector.html' antes de cerrar su body en el html central con eso deberia funcionar de manera correcta 
### 3. Backend (Python)
Instala todas las librerías necesarias con un solo comando:
```bash
pip install -r requirements.txt

