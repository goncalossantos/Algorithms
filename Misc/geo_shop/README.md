Products Near You
=================

The purpose of this exercise is to build an API that returns the most popular products
from shops near you.

Provided goodies
----------------

1. A server boilerplate using `Flask`. To run the server:

  ```
  $ python runserver.py
  ```

2. A rudimentary client so you can visualize the results more easily. The client does not
have any way to communicate with the API so you will need to implement that. To run the
client:

  ```
  $ cd client
  $ python -m SimpleHTTPServer
  ```

3. Four datasets in CSV format:
    * `shops.csv`: shops with their coordinates
    * `products.csv`: products per shop along available quantity and global popularity
    * `tags.csv`: a bunch of tags
    * `taggings.csv`: what tags each shop has
Resources
---------

1. `Flask`: http://flask.pocoo.org/
2. `pytest`: http://pytest.org/latest/
3. `virtualenvwrapper`: https://virtualenvwrapper.readthedocs.io/en/latest/
