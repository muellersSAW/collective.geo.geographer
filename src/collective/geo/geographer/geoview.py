import pkg_resources
from zope.interface import implementer

from Products.Five.browser import BrowserView

from .interfaces import IGeoreferenceable
from .interfaces import IGeoreferenced
from .interfaces import IGeoView


@implementer(IGeoView)
class GeoView(BrowserView):
    """A simple view to know if an object is geo referenceable.

    See: :class:`collective.geo.geographer.interfaces.IGeoView`
    """

    def __init__(self, context, request):
        super(GeoView, self).__init__(context, request)

    def isGeoreferenceable(self):
        return IGeoreferenceable.providedBy(self.context)

    def getCoordinates(self):
        if self.isGeoreferenceable():
            geo = IGeoreferenced(self.context)
            return geo.type, geo.coordinates

    def hasCoordinates(self):
        """Return whether context has been georeferenced or not
        """
        if self.isGeoreferenceable():
            geo = IGeoreferenced(self.context)
            return geo.hasCoordinates()
        return False
