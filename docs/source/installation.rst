.. _ref-installation:

============
Installation
============

Requirements
================

   - Python2, Python2.7

   - Django 1.6, 1.7, 1.8

   - sass 3.4+ (不是必须)

Setup
===============

1. 通过pip进行安装 ::

   pip install django-dynamic-cabinetmaps

2. 在settings.py进行添加 ::


   INSTALLED_APPS = (
    ......

    'cabinet_structure',

    ......
   )

3. 安装好之后,需要通过一些配置,详情请看'Usage'.