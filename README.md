# consecionariaLP# Sistema de Gestión para una Concesionaria de Autos

## Descripción del Proyecto

Este proyecto es una aplicación web desarrollada en Django que permite gestionar las operaciones clave de una concesionaria de autos. El sistema está diseñado para manejar de manera eficiente la información relacionada con vehículos, clientes, y comentarios, asegurando que tanto el personal de la concesionaria como los clientes puedan interactuar con la plataforma de forma segura y organizada.

### Funcionalidades Principales

- **Gestión de Vehículos**: La aplicación permite registrar, actualizar y eliminar vehículos, junto con sus marcas, modelos, y categorías. Además, es posible subir imágenes de los vehículos, lo cual es obligatorio para mantener una galería visual actualizada.

- **Administración de Usuarios**: El sistema distingue entre dos tipos de usuarios: staff y no staff. Los usuarios staff tienen acceso a un panel de administración donde pueden gestionar vehículos y revisar comentarios. Los usuarios no staff, por otro lado, pueden interactuar con los vehículos dejando comentarios, los cuales pueden editar y eliminar si son los autores.

- **Autenticación y Seguridad**: Se implementa un sistema de autenticación robusto que incluye registro y login de usuarios. Las vistas críticas están protegidas, permitiendo el acceso solo a usuarios autenticados y restringiendo acciones según el rol del usuario.

- **Comentarios y Moderación**: Los usuarios pueden comentar sobre los vehículos. Los comentarios pueden ser revisados por el personal de la concesionaria, quien tiene la capacidad de eliminarlos si es necesario, aun[text](recent:/604bc532c87909765eb7b91166b964a6)que no pueden editarlos. Esto garantiza que el contenido publicado en la plataforma se mantenga relevante y respetuoso.

- **Proyecto**:
![Pagina Principal](./home/static/home/pagina_inicio.jpeg)
![Vista imagen vehiculo](./home/static/home/imagen_vehiculo.jpeg)


### Tecnologías Utilizadas

- **Django 4.x**: El proyecto está construido sobre la versión más reciente de Django, aprovechando sus capacidades para desarrollar aplicaciones web seguras y escalables.
- **Base de Datos Relacional**: El sistema incluye una estructura de datos robusta, con múltiples modelos interrelacionados que permiten una gestión integral de la información.
- **Gestión de Archivos y Media**: Las imágenes de los vehículos son gestionadas mediante un sistema de archivos bien configurado, asegurando su almacenamiento y visualización eficiente.

### Estructura del Proyecto

El proyecto sigue una arquitectura MVC (Modelo-Vista-Controlador) utilizando las mejores prácticas de Django, lo que facilita su mantenimiento y escalabilidad. Los formularios están diseñados para validar datos de manera efectiva, y se utilizan vistas basadas en clases para garantizar un código modular y reutilizable.

### Funcionalidades Adicionales

- **Navegación Pública**: Aunque ciertas funcionalidades están reservadas para usuarios autenticados, cualquier visitante puede explorar el catálogo de vehículos.


Este proyecto representa una solución completa para la gestión de una concesionaria de autos, combinando una interfaz amigable con un backend potente y seguro.

## Instalación y Configuración

1. Clona el repositorio en la carpeta deseada:
    ```bash
    git clone git@github.com:GeronimoTorresOrtiz/concesionariaLP.git
    ```
2. Ingresa a la carpeta del proyecto:
    ```bash
    cd concesionariaLP
    ```
3. Crea un entorno virtual:
    ```bash
    python3 -m venv env
    ```
4. Activa el entorno virtual:
    ```bash
    source env/bin/activate
    ```
5. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ``` 
6. Ingresa a la carpeta del proyecto:
    ```bash
    cd concesionaria
    ```
7. Realiza las migraciones para crear las tablas de la base de datos:
    ```bash
    python3 manage.py migrate
    ```
8. Carga los datos iniciales en la base de datos:
    ```bash
    python3 manage.py load_data
    ```
9. Crea un superusuario para entrar al admin:
    ```bash
    python3 manage.py createsuperuser --username <nombre de tu usuario>
    ``` 
       
10. Inicia el servidor de desarrollo:
    ```bash
    python3 manage.py runserver
    ``` 
