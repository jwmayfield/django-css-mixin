Overview
========

There has been more than one occasion in which I've needed to specify attributes on models to tie in with CSS, so I've abstracted that small bit of functionality into a simple Django model mixin (aka abstract base class).

Installation
============

::

pip install git://github.com/jwmayfield/django-css-mixin.git

Usage
=====

models.py::

  from django.db import models
  from django_css_mixin.models import CSSMixin


  class MyModel(CSSMixin, ...):
    ...

some template code::

  {% for object in object_list %}
    <div id="{{ object.attr_id }}" class="{{ object.attr_class }}" style="{{ object.attr_style }}">{{ object }}</div>
  {% endfor %}
