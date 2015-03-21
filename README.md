## auth_test

Comparison of [django-userena](https://github.com/bread-and-pepper/django-userena) and [django-allauth](https://github.com/pennersr/django-allauth).

#### django-userena

Live site is [here](http://http://test-authentic.appspot.com/).

##### how to run locally

To use email verification, run add_site_ids.py.
When run locally, the site_id will be 3, where the site is localhost:8080.

Create a mysql database called userena_db with a root password 'password'.

Run migrations on userena, userena_app, guardian, and easy_thumbnails.

It can be run with 
* dev_appserver.py
* python manage.py runserver 8080
* SETTINGS_MODE='prod' python manage.py runserver 8080

go to 
* /userena_app to see a list of profiles
* /userena_app/signup to create a profile
* /userena_app/signin to sign in
* /userena_app/signout to sign out

if /userena_app/signup gives the error "Permission matching query does not exist", run permissions_fix.py.


##### dependencies

Instructions for installing userena are [here](http://django-userena.readthedocs.org/en/latest/installation.html).