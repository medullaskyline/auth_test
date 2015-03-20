## auth_test

Comparison of [django-userena](https://github.com/bread-and-pepper/django-userena) and [django-allauth](https://github.com/pennersr/django-allauth).

#### django-userena

##### how to run

Currently the site_id is set to 2, where the site is localhost:8888.  
Run the program on port 8888.

Uncomment 'guardian', 'easy_thumbnails', and 'userena' in INSTALLED_APPS in auth_test/settings.py, migrate the database, then re-comment them.

To use email verification, run add_site_ids.py.

##### dependencies

Instructions for installing userena are [here](http://django-userena.readthedocs.org/en/latest/installation.html).