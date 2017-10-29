# django-indonesia-regions
[![Build Status](https://travis-ci.org/Keda87/django-indonesia-regions.svg?branch=master)](https://travis-ci.org/Keda87/django-indonesia-regions)

Pluggable django apps provide indonesian regions database. 

The data originally was from [Wilayah Administratif Indonesia](https://github.com/edwardsamuel/Wilayah-Administratif-Indonesia).

# Quick Start
1. Install it through pip.
        
        $ pip install django-indonesia-regions --upgrade
2. Add `djindonesiaregions` to your `INSTALLED_APPS` setting like this.

        INSTALLED_APPS = [
            ...
            'djindonesiaregions',
        ]
3. Run `python manage.py migrate` to create the region models and load the data.

# ER Schema

![ER Schema][erd]

[erd]: screenshots/erd.png
