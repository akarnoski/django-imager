[![Build Status](https://travis-ci.org/adriennekarnoski/django-imager.svg?branch=front-end-4)](https://travis-ci.org/adriennekarnoski/django-imager)
# ImagerSite

**Authors**: [Mark Reynoso](https://github.com/markreynoso), [Adrienne Karnoski](https://github.com/adriennekarnoski)

**Version**: 1.0.0

## Overview
```django-imager``` is a simple django application where a user can register to create a photo library and display their best photograhpy work, as well as see the work of their fellow imagers.

## Website
[Check it out] tbd

## Getting Started
- Clone down the repository to your local machine:
```
$ git clone https://github.com/adriennekarnoski/django-imager.git
```
- Once your download is complete, cd into the ```django-imager``` repository:
```
$ cd django-imager
```
- Create a new virtual environment with Python 3 and activate it:
```
django-imager $ python3 -m venv ENV
django-imager $ . ENV/bin/activate
```
- Install the project in editable mode along with its testing requirements, via pip:
```
(ENV) django-imager $ pip install -e .[testing]
```
- Once your environment is complete, cd into the ```imagersite``` directory:
```
(ENV) cd imagersite
```
- Test your project:
```
(ENV) ./manage.py tests
```
- Begin serving your application, via the ```runserver``` command:
```
(ENV) ./manage.py runserver
```
- Visit your site from your browser:
```
http://localhost/8000
```

## Routes:

| Route | Route Name | Description |
| --- | --- | --- |
| /  | homepage | The home page |
| /login | login | Login for existing users |
| /logout | logout | Logout for a logged in user |
| /accounts/register | registration_register | Registration page for a new user |
| /images | images | All public photos on app |
| /images/album| album | All public albums on app |
| /images/album/<pk> | albumphoto | All photos from one album |
| /images/library | library | All photos and albums from one user |


## Built With:

- [Django Framework](https://djangoproject.com)

- [Start Bootstrap](https://startbootstrap.com/template-overviews/bare/)
