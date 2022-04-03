Is Likelion?
===============

.. image:: https://coveralls.io/repos/github/shinkeonkim/is_likelion/badge.svg?branch=main


How to use
------------

.. code-block:: shell

  > pip install is_likelion


Usage
-------

.. code-block:: python

  from is_likelion import is_likelion

  is_likelion("likelion")
  # True

  is_likelion("LikeLiOn")
  # True

  is_likelion("lion")
  # False

