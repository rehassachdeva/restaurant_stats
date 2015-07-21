Restaurant_stats
****************
A simple tool that scrapes data like Restaurants, their respective ratings and cost for two from a zomato.com page that lists them according to the user's requirements and plots a graph between Restaurant name and cost, while displaying the rating so that one glance is all it takes to find the best restaurant in a given price range.

Installation
============
Run
::

    python setup.py install

Dependencies
============
restaurant_stats is based on Python 2.7. Requires ``BeautifulSoup4`` for html parsing, ``urllib`` for downloading page source, ``Matplotlib`` and ``numpy`` for plotting graph.

Usage
=====
Run the simple command
::
    restaurant_stats url
to generate a graph.png file in the current directory containing the required graph, 
    eg. restaurant_stats https://www.zomato.com/amritsar/ranjit-avenue-restaurants?category=1
    or save it under a name of your choice
    
    eg. restaurant_stats https://www.zomato.com/amritsar/ranjit-avenue-restaurants?category=1 -f mygraph.png

For other options and help run
::
    restaurant_stats -h

Why?
====

* I wanted to test out awesome python modules like ``BeautifulSoup4`` and ``Matplotlib``.
* I am a big foodie and thought it'd be nice to optimise restaurant finding in this way.
* Graphs are fun :).

Issues, Bugs?
=============
.. |issues| replace:: https://github.com/rehassachdeva/restaurant_stats/issues

Example
=======

.. image:: https://raw.githubusercontent.com/rehassachdeva/restaurant_stats/master/examples/graph.png









