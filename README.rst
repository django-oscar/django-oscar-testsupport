===========================
Testing utilities for Oscar
===========================

A simple package to allow the test utils from Oscar to be used by other
packages.

Contents:

* A ``@dataProvider`` decorator for feeding test methods with different
  datasets.  This is a port of a useful PHPUnit feature.

* A ``ClientTestCase`` which provides useful boilerplate functionality for when
  working with Django's test client.  It can set-up users as part of the
  ``setUp`` method.

* A ``WebTestCase``, similar to the ``ClientTestCase`` but for working with
  WebTest.

* Various factory methods for creating orders, products, offers and vouchers.

Install
------

Install with::

   pip install django-oscar-testsupport 
