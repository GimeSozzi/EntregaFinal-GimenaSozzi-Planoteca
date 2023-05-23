# Entrega Final - Gimena Sozzi
# Planoteca

PLANOTECA es un sitio web creado con Django donde los arquitectos pueden subir los planos de sus proyectos arquitectónicos. Los usuarios deben registrarse y, una vez iniciada la sesión, pueden ver los proyectos, descargar los planos, crear, buscar, editar y eliminar proyectos, enviar y recibir mensajes y editar su perfil.


## Funcionalidades implementadas

- Ver proyectos: Cualquier persona que visite la página puede ver los proyectos.
- Buscar proyecto: Cualquier persona que visite la página puede buscar proyectos.
- Registrarse: Los usuarios pueden registrarse en el sitio web.
- Iniciar sesión: Los usuarios pueden iniciar sesión en el sitio web.
- Editar perfil: Los usuarios pueden editar su perfil.
- Cambiar contraseña: Los usuarios pueden cambiar su contraseña.
- Cerrar sesión: Los usuarios pueden cerrar su sesión.
- Crear proyecto: Los usuarios registrados y logueados pueden crear proyectos.
- Editar proyecto: Los usuarios registrados y logueados pueden editar proyectos.
- Eliminar proyecto: Los usuarios registrados y logueados pueden eliminar proyectos propios.
- Enviar mensaje: Los usuarios registrados y logueados pueden enviar mensajes a otros usuarios que sean autores de proyectos.
- Responder mensaje: Los autores pueden responder mensajes enviados por otros usarios o autores.
- Lista de conversaciones: Los usuarios registrados y logueados pueden ver su lista de conversaciones.
- Ver conversación: Los usuarios registrados y logueados pueden ver una conversación en particular.
- Interfaz de admin.

## Dependencias

Para instalar las dependencias de Planoteca, es recomendable utilizar un entorno virtual (Virtualenv) y luego instalarlas utilizando el archivo requirements.txt. Pasos a seguir:

1. Crear un entorno virtual y activarlo.

2. Instalar las dependencias desde el archivo requirements.txt:

`pip install -r requirements.txt`

## Ejecución

Después de instalar las dependencias, es necesario inicializar la base de datos. Para ello, ejecutar los siguientes comandos:

1. Aplicar las migraciones para crear la base de datos sqlite:

`python manage.py migrate`

2. Iniciar el servidor de desarrollo de Django con el siguiente comando:

`python manage.py runserver`

Luego, podrás acceder al sistema ingresando en tu navegador a la dirección http://localhost:8000/.

## Admin

El proyecto cuenta con una interface de admin en donde se puede acceder a todos los modelos del proyecto.

Para usar el admin, es necesario crear un superusuario, ejecutando el siguiente comando en la terminal:

`python manage.py createsuperuser`

Luego, se te pedirán los datos del superusuario, como nombre de usuario, correo electrónico y contraseña.

Una vez que hayas creado el superusuario, puedes acceder al panel de administración en la dirección: /admin/

## Video demostración

https://youtu.be/K4qJUJXgD2w

## Contribuyentes

- Gimena Sozzi

¡Espero que te sea útil este archivo README.md!
