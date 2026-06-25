"""Natural Resources Canada Earthquakes feed."""

import logging

from georss_client import GeoRssFeed
from georss_client.exceptions import GeoRssException

from .consts import ATTRIBUTIONS, URLS
from .feed_entry import NaturalResourcesCanadaEarthquakesFeedEntry

_LOGGER = logging.getLogger(__name__)


class NaturalResourcesCanadaEarthquakesFeed(GeoRssFeed):
    """Natural Resources Canada Earthquakes feed."""

    def __init__(
        self,
        home_coordinates,
        language,
        filter_radius=None,
        filter_minimum_magnitude=None,
    ):
        """Initialise this service."""
        if language in URLS:
            super().__init__(
                home_coordinates, URLS[language], filter_radius=filter_radius
            )
            self._language = language
            self._filter_minimum_magnitude = filter_minimum_magnitude
        else:
            _LOGGER.error("Unknown feed language %s", language)
            raise GeoRssException("Feed language must be one of %s")

    def __repr__(self):
        """Return string representation of this feed."""
        return f"<{self.__class__.__name__}(home={self._home_coordinates}, url={self._url}, radius={self._filter_radius}, magnitude={self._filter_minimum_magnitude})>"

    def _new_entry(self, home_coordinates, rss_entry, global_data):
        """Generate a new entry."""
        return NaturalResourcesCanadaEarthquakesFeedEntry(
            home_coordinates, ATTRIBUTIONS[self._language], rss_entry
        )

    def _filter_entries(self, entries):
        """Filter the provided entries."""
        entries = super()._filter_entries(entries)
        if self._filter_minimum_magnitude:
            # Return only entries that have an actual magnitude value, and
            # the value is equal or above the defined threshold.
            return list(
                filter(
                    lambda entry: (
                        entry.magnitude
                        and entry.magnitude >= self._filter_minimum_magnitude
                    ),
                    entries,
                )
            )
        return entries
