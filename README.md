# keto guru

## dev setup

requires: 

- python3.7
- pipenv
- SpatiaLite - <https://docs.djangoproject.com/en/3.0/ref/contrib/gis/install/spatialite/>

install:

    pipenv install

run: 

    pipenv shell
    cd ketoguru
    python ./manage.py migrate
    python ./manage.py runserver
