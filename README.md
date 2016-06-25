# django-indonesia-regions

Pluggable django apps provide indonesian regions data. 

The data originally was from [https://github.com/edwardsamuel/Wilayah-Administratif-Indonesia](https://github.com/edwardsamuel/Wilayah-Administratif-Indonesia)

# Quick Start

1. Add "djindonesiaregions" to your INSTALLED_APPS setting like this::

        INSTALLED_APPS = [
            ...
            'djindonesiaregions',
        ]
2. Run `python manage.py migrate` to create the region models and load the data.

# ER Schema

![ER Schema][erd]

[erd]: screenshots/erd.png

# License

- The package license under [MIT](http://opendatacommons.org/licenses/odbl/1-0/)
- The data (CSV) license under [ODBL v1.0](http://opendatacommons.org/licenses/odbl/1-0/)