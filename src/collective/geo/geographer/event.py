from zope.interface import implementer
from zope.interface.interfaces import IObjectEvent

import logging
logger = logging.getLogger('collective.geo.geographer')


class IObjectGeoreferencedEvent(IObjectEvent):
    """An event signaling that an object has been georeferenced
    """


@implementer(IObjectGeoreferencedEvent)
class ObjectGeoreferencedEvent(object):

    def __init__(self, ob):
        self.object = ob


ObjectGeoreferencedEvent.descriptions = {}
logger.info(
    "Patching collective.geo.geographer.events's "
    "ObjectGeoreferencedEvent to have a 'descriptions' "
    "field to handle an issue with p4a.plonevideo."
)
