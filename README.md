# django-indonesia-regions

Pluggable django apps provide indonesian regions data. 

The data originally was from [https://github.com/edwardsamuel/Wilayah-Administratif-Indonesia](https://github.com/edwardsamuel/Wilayah-Administratif-Indonesia)

# Quick Start
1. Install it through pip.
        
        $ pip install django-indonesia-regions --upgrade
2. Add "djindonesiaregions" to your INSTALLED_APPS setting like this.

        INSTALLED_APPS = [
            ...
            'djindonesiaregions',
        ]
3. Run `python manage.py migrate` to create the region models and load the data.

# ER Schema

![ER Schema][erd]

[erd]: screenshots/erd.png

# License

```
The MIT License

Copyright (c) 2016 Adiyat Mubarak

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```