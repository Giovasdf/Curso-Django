# Django y MariaDB Esencial! CRUD y API


![](imagenesReadme/udemyLogo.png)

## 🗒️ Software a utilizar

* [Python](https://www.python.org/)
* [MariaDB](https://mariadb.org/download/?t=mariadb&p=mariadb&r=10.10.0)
* [VSCode](https://code.visualstudio.com/)
* [Django](https://pypi.org/project/Django/)
* [Django Rest Framework](https://pypi.org/project/djangorestframework/)



## 🚀 Configuracion de Mariadb en Django
* [Link de DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04)

Archivo por defecto

```sh
. . .

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

. . .
```

Archivo MariaDB a editar con datos de la BD

```sh
. . .

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

. . .
```
