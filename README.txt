Ningún comando lleva las comillas ("")

Primero debemos instalar python3 y pip3 (depende del sistema operativo)

Una vez instalados, con pip3 instalaremos virtualenv y virtualenvwrapper

"pip3 install virtualenv virtualenvwrapper"

Modificaremos el archivo .bashrc o .zshrc (depende de tu sistema) que se encuentra en raíz (~/)

Dentro pondremos las siguientes líneas

" PYTHON_BIN_PATH="$(python3 -m site --user-base)/bin"
PATH="$PATH:$PYTHON_BIN_PATH"

# Exports 
export WORKON_HOME="~/.envs" # Carpeta dónde vendrán nuestros imports
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENV_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
"

Una vez hecho esto, guardaremos y reiniciaremos la terminal o haremos (aquí depende de cuál estés ocupando si bashrc o zshrc

"source .zshrc"

"source .bashrc"

Procedemos a crear nuestro entorno virtual con 
mkvirtualenv <nombre-entorno>
// para salir del entorno virutal hacemos "deactivate"
// para volver a entrar "workon <nombre-entorno>"

Entramos al proyecto que hemos clonado y hacemos
"pip install -r requirements.txt"

Ahora tenemos que instalar postgres
sudo apt install postgresql
sudo apt install libpq-dev (o su equivalente dependiendo del sistema)

Configuramos la base de datos de postgres
psql -d postgres
Una vez dentro, nos aparecerá una pantalla con postgres y hacemos lo siguiente
\du
Veremos una lista con los usuarios, nuestro usuario debe tener los permisos de superusuario, crear rol y crear db
Si no los tiene, haremos
ALTER ROLE <user> WITH SUPERUSER;
ALTER ROLE <user> WITH CREATEDB;
ALTER ROLE <user> WITH CREATEROLE;

Después crearemos la base de datos
CREATE DATABASE online_market;

Nos movemos a la base de datos con 
\c online_market

Creamos el usuario para esa base de datos
CREATE ROLE market_user;

Agregamos contraseña al usuario
ALTER ROLE market_user WITH PASSWORD '123456'

Podemos iniciar el proyecto con
"python manage.py runserver"

Luego podremos entrar a localhost:8000 en nuestro navegador para acceder a cualquier página

Para realizar migraciones
"python manage.py makemigrations"
"python manage.py migrate"

Para crear un superusuario
"python manage.py createsuperuser"
Les pedirá sus datos y los pondrán y podrán acceder a 
localhost:8000/admin

Para crear una aplicación (dentro de la carpeta applications)
"django-admin startapp <nombre-app>"

Casi siempre será una app por modelo
Al agregar una app, hay que entrar a la carpeta con el nombre de la app
y cambiar el name, por ejemplo
name = "home"
por 
name = "applications.home"

Si necesitan instalar la app
Hay que entrar a la carpeta "online_market/settings/base.py"
Y agregar en OWN_APPS la aplicación de la siguiente forma (solo si es aplicación propia)

OWN_APPS = [
	'applications.home'
]

Si es de django agregar a DJANGO_APPS, o THIRD_PARTY_APPS si es de terceros (instalada con pip)

Hay que agregar un archivo urls.py en cada aplicación creada por nosotros
y luego reconfigurar cómo se hizo en la app home

Las vistas son intermediarios(Controladores) entre lo que se muestra al usuario(templates html) y 
la lógica de nuestro programa(models.py)

Para crear un modelo, en models.py hay que crear una clase
class NombreTabla(models.Model):
	attr_1 = models.CharField('nombre-columna', max_length=100)
	attr_2 = models.ImageField('nombre-columna', upload_to, blank=True, null=True)
	Pueden checar todos los tipos que hay en internet o más tarde los subiré aquí mismo

Se pueden crear vistas genéricas(controladores genéricos) 
https://ccbv.co.uk/ (Aquí viene documentación sobre todas las vistas genéricas)
Las más básicas son:
TemplateView (Te permite mostrar un template html), se ocupan con herencia en python de la sig forma.

class HomeView(TemplateView):
	template_name = 'home/home.html' # La carpeta se configuro en el settings/base.py para que lo revisen

ListView (Te permite mostrar un template y pasarle una lista a ese template)
class HomeListView(ListView):
	template_name = 'home/lista.html'
	context_object_name = 'nombre_mostrado_en_html'
	queryset = [1, 2, 3, 4, 5] # Lista mostrada en html
	# model = Person # Aquí también se pueden mostrar todos los datos de un módelo (Tabla en postgres)

En el html se ve algo así
	<ul>
		{% for el in nombre_mostrado_en_html %}
		<li>{{ el }}</li>
		{% endfor %}
	</ul>
	Se mostraría una lista con los elementos del 1 al 5

Hay más modelos, que agregaré más adelante

En html se pueden hacer includes de html completo y también se pueden hacer bloques para tener un 
archivo base.html y no repetir tanto código (veáse en los archivos templates/base.html, 
templates/home/home.html y templates/includes/navbar.html)

Utilizaremos bootstrap para diseñar la página

Cualquier cosa extra, pueden preguntar y la contestaré lo más rápido que pueda

