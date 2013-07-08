===========================
Testing utilities for Oscar
===========================

Warning
-------

As of Oscar 0.6, this package has been merged back into Oscar, within the
``oscar/test`` package.  There will be no 0.5 release of this package.

Description
-----------

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
