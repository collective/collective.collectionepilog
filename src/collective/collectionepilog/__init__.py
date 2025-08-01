"""Init and utils."""

import logging
from zope.i18nmessageid import MessageFactory

__version__ = "0.1.0a7.dev0"

PACKAGE_NAME = "collective.collectionepilog"

_ = MessageFactory(PACKAGE_NAME)

logger = logging.getLogger(PACKAGE_NAME)
