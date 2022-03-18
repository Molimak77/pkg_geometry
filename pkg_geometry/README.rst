pkg_geometry
============

the python package destined to trait the geometry computers

Purpose of the pacakge
----------------------

-  The purpose of the package is to computed the essential metrics

Features
--------

-  class facequadi

   -  perimetre
   -  surface
   -  volume

Getting Started
---------------

The package can be found on pypi

installation
------------

.. code:: terminal

   pip install pkg_geometry

Usage
-----

Compute the perimetre

.. code:: {python}

   >>> from pkg_geometry.geometry import facequadri as fc
   >>> fac_fig = fc(2,3,4)
   >>> fac_fig.perimetre()

compute the surce

.. code:: python

   >>> from pkg_geometry.geometry import facequadri as fc
   >>> fac_fig = fc(2,3,4)
   >>> fac_fig.surface()

Compute the volume

.. code:: python

   >>> from pkg_geometry.geometry import facequadri as fc
   >>> fac_fig = fc(2,3,4)
   >>> fac_fig.perimetre

Contribution
------------

Contribution are welcom. Notice a lbug let us know. Thans

Author
------

-  MAin MAintainer: Molière Nguile-Makao
-  `molier.nguile@gmail.com <#molier.nguile@gmail.com>`__
