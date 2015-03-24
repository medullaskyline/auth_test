## auth_test

Comparison of [django-userena](https://github.com/bread-and-pepper/django-userena) and [django-allauth](https://github.com/pennersr/django-allauth).

#### django-userena

Live site is [here](http://http://test-authentic.appspot.com/userena_app).

##### how to run locally

Create a mysql database called userena_db with a root password 'password'.

Run migrations on userena, userena_app, guardian, and easy_thumbnails.

To use email verification, run the add_site_ids script and start the application with one of the following commands:
```
$ dev_appserver.py
$ python manage.py runserver 8080
$ SETTINGS_MODE='prod' python manage.py runserver 8080
```

When run locally, the SITE_ID settings variable is 3, which should correspond to localhost:8080.

if /userena_app/signup gives the error "Permission matching query does not exist", run permissions_fix.


##### dependencies

Instructions for installing userena are [here](http://django-userena.readthedocs.org/en/latest/installation.html).

##### issues

* disabled accounts


#### django-allauth

##### dependencies

Instructions for installing django-allauth are [here](http://django-allauth.readthedocs.org/en/latest/installation.html).