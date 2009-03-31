"""
Template for module docs. 
"""

def bar(x):
    """Bar() docs are here.

    :param x: x value
    :returns: x**2
    """
    return x**2

class Foo(object):
    """Foo docs are here.

    :param x: x value
    :param y: y value

    .. attribute:: x

       The ``x`` attribute.  In many cases this documentation may not be needed.
    """
    def __init__(self, x, y):
        """
        :param x: x VALUE
        :param y: y VALUE
        """
        self.x = x
        self.y = y

    def _get_r(self):
        """Object radius"""
        return self.x**2 + self.y**2

    def _set_r(self, r):
        """Set object radius."""
        self.x = 0
        self.y = r**0.5

    r = property(_get_r, _set_r)
    """Radius attribute"""

    def method(self, z):
        """My method to print z.

        :param z: the z value
        :returns: None
        """
        print z
