"""Natural Resources Canada Earthquakes feed entry."""

import logging

from georss_client import FeedEntry

from .consts import REGEXP_ATTR_MAGNITUDE

_LOGGER = logging.getLogger(__name__)


class NaturalResourcesCanadaEarthquakesFeedEntry(FeedEntry):
    """Natural Resources Canada Earthquakes feed entry."""

    def __init__(self, home_coordinates: tuple[float, float], attribution, rss_entry):
        """Initialise this service."""
        super().__init__(home_coordinates, rss_entry)
        self._attribution = attribution

    @property
    def attribution(self) -> str:
        """Return the attribution of this entry."""
        return self._attribution

    @property
    def magnitude(self) -> float | None:
        """Return the type of this entry."""
        magnitude = self._search_in_description(REGEXP_ATTR_MAGNITUDE)
        if magnitude:
            # Convert to float. In the 'fr' version of the feed, the
            # magnitude value uses comma as decimal separator, hence replacing
            # comma with dot here. Because magnitude is never above 1000 the
            # value in the feed will never have a comma as thousands-separator
            # in the 'en' version of the feed.
            magnitude = float(magnitude.replace(",", "."))
        return magnitude
