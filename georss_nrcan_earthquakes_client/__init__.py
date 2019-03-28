"""
Natural Resources Canada Earthquakes Feed.

Fetches GeoRSS feed from Natural Resources Canada Earthquakes.
"""
import logging

from typing import Optional

from georss_client import GeoRssFeed, FeedEntry
from georss_client.consts import CUSTOM_ATTRIBUTE
from georss_client.exceptions import GeoRssException
from georss_client.feed_manager import FeedManagerBase

_LOGGER = logging.getLogger(__name__)

ATTRIBUTIONS = {
    'en': "Natural Resources Canada",
    'fr': "Ressources naturelles Canada"
}

REGEXP_ATTR_MAGNITUDE = '<b>magnitude: </b>(?P<{}>[^<]+)<br/>'\
    .format(CUSTOM_ATTRIBUTE)

URL_PATTERN = 'http://www.earthquakescanada.nrcan.gc.ca/index-{}.php?' \
              'tpl_region=canada&tpl_output=rss'
URLS = {
    'en': URL_PATTERN.format('en'),
    'fr': URL_PATTERN.format('fr'),
}


class NaturalResourcesCanadaEarthquakesFeedManager(FeedManagerBase):
    """Feed Manager for Natural Resources Canada Earthquakes feed."""

    def __init__(self, generate_callback, update_callback, remove_callback,
                 coordinates, language, filter_radius=None,
                 filter_minimum_magnitude=None):
        """Initialize the Natural Resources Canada Earthquakes Feed Manager."""
        feed = NaturalResourcesCanadaEarthquakesFeed(
            coordinates,
            language,
            filter_radius=filter_radius,
            filter_minimum_magnitude=filter_minimum_magnitude)
        super().__init__(feed, generate_callback, update_callback,
                         remove_callback)


class NaturalResourcesCanadaEarthquakesFeed(GeoRssFeed):
    """Natural Resources Canada Earthquakes feed."""

    def __init__(self, home_coordinates, language, filter_radius=None,
                 filter_minimum_magnitude=None):
        """Initialise this service."""
        if language in URLS:
            super().__init__(home_coordinates, URLS[language],
                             filter_radius=filter_radius)
            self._language = language
            self._filter_minimum_magnitude = filter_minimum_magnitude
        else:
            _LOGGER.error("Unknown feed language %s", language)
            raise GeoRssException("Feed language must be one of %s".format(
                URLS.keys()))

    def __repr__(self):
        """Return string representation of this feed."""
        return '<{}(home={}, url={}, radius={}, magnitude={})>'.format(
            self.__class__.__name__, self._home_coordinates, self._url,
            self._filter_radius, self._filter_minimum_magnitude)

    def _new_entry(self, home_coordinates, rss_entry, global_data):
        """Generate a new entry."""
        return NaturalResourcesCanadaEarthquakesFeedEntry(
            home_coordinates, ATTRIBUTIONS[self._language], rss_entry)

    def _filter_entries(self, entries):
        """Filter the provided entries."""
        entries = super()._filter_entries(entries)
        if self._filter_minimum_magnitude:
            # Return only entries that have an actual magnitude value, and
            # the value is equal or above the defined threshold.
            return list(filter(lambda entry:
                               entry.magnitude and entry.magnitude >= self.
                               _filter_minimum_magnitude, entries))
        return entries


class NaturalResourcesCanadaEarthquakesFeedEntry(FeedEntry):
    """Natural Resources Canada Earthquakes feed entry."""

    def __init__(self, home_coordinates, attribution, rss_entry):
        """Initialise this service."""
        super().__init__(home_coordinates, rss_entry)
        self._attribution = attribution

    @property
    def attribution(self) -> str:
        """Return the attribution of this entry."""
        return self._attribution

    @property
    def magnitude(self) -> Optional[float]:
        """Return the type of this entry."""
        magnitude = self._search_in_description(REGEXP_ATTR_MAGNITUDE)
        if magnitude:
            # Convert to float. In the 'fr' version of the feed, the
            # magnitude value uses comma as decimal separator, hence replacing
            # comma with dot here. Because magnitude is never above 1000 the
            # value in the feed will never have a comma as thousands-separator
            # in the 'en' version of the feed.
            magnitude = float(magnitude.replace(',', '.'))
        return magnitude
