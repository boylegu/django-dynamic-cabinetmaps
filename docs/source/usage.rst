.. _ref-usage:

============
Usage
============

API
================

首先你需要在你APP的views中，继承CabinetViews类，该类提供三个API。


template_name
_____________

用于指定渲染机柜的模版

cabinet_cells
_____________

提供总共需要多少个机柜

rack_rows
_________

   :default: ``42``

提供每个机柜总共有多少个导轨

example
_______

::

  from cabinet_structure.views import CabinetViews

  class MyViews(CabinetViews):

     template_name = 'MyAPP/MyAPP.html'
     cabinet_cells = 8
     # rack_rows = 42


.. note::
  cabinet_cells可以手工填写；但更推荐从数据库中进行计算.

CSS
=========
需要引入bootstrap框架以及本项目有关的样式套件cabinet_style.css

example
_______
::

 {% load staticfiles %}
 ......
 <head>
 ......
   <link href="{% static '....bootstrap.min.css' %}" rel="stylesheet">
   <link rel="stylesheet" href="{% static 'cabinetmaps/css/cabinet_style.css' %}">
 ......
 </head>

Templates
==========

example
_______
::

 ....

 <div ....>

        {{ cabinet_data }}
 </div>

 ....


{{ cabinet_data }}
___________________
在模版中指定一下标签变量{{ cabinet_data }}, 该标签涵盖了所有生成后的机柜HTML信息

查看机柜编号
______________
生成后的机柜图,通过HTML可以查看,如下所示

1. 机柜编号

::

 <tr><td class="jgtable" ......>
         <font class="jgtitle"><p>A1</p></font></td>
 </tr>
 ......

 <tr><td class="jgtable" ......>
         <font class="jgtitle"><p>A9</p></font></td>
 </tr>

2. 机柜上的的导轨编号

::

 .......
 <tr><td class='jgtable' align='center' height='8' valign='bottom' id='4'></td></tr>
 .......
 <tr><td class='jgtable' align='center' height='8' valign='bottom' id='12'></td></tr>

.. note::
  在之后的版本中,对于机柜编号的定制会得到加强,并提供数据填充的API.

Settings
===============

.. currentmodule:: django.conf.settings

.. attribute:: MAX_CABINET_ROWS_NUM

   :default: ``6``

   用于指定页面每行中显示多少个机柜::

      # in settings.py

      MAX_CABINET_ROWS_NUM = 7


   .. warning::

      目前'开发测试版'中,试图设置该参数,会导致前端样式的显示问题,在之后的版本中会修复,请多关注!

Demo
===============

1. 从git上克隆 https://github.com/boylegu/django-dynamic-cabinetmaps.git

2. 然后进入``demoapp``

3. ``python manage runserver``

.. note::
  目前demo是需要django 1.6运行