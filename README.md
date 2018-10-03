

# moneyflow demo

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    $ python3 -m venv venv
    $ . venv/bin/activate
    $ export DJANGO_SETTINGS_MODULE=conf.settings.dev

Install all dependencies for development:

    $ pip install -r requirements/dev.txt

Copy local.sample.env to .env file for development in conf/settings.

Run migrations (if needed)

    $ python manage.py migrate

Start redis
    $ docker run -p 6379:6379 -d redis:2.8

Start Server
    $ python manage.py runserver

