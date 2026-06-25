"""Natural Resources Canada Earthquakes feed manager."""

import logging

from georss_client.feed_manager import FeedManagerBase

from .feed import NaturalResourcesCanadaEarthquakesFeed

_LOGGER = logging.getLogger(__name__)


class NaturalResourcesCanadaEarthquakesFeedManager(FeedManagerBase):
    """Feed Manager for Natural Resources Canada Earthquakes feed."""

    def __init__(
        self,
        generate_callback,
        update_callback,
        remove_callback,
        coordinates,
        language,
        filter_radius=None,
        filter_minimum_magnitude=None,
    ):
        """Initialize the Natural Resources Canada Earthquakes Feed Manager."""
        feed = NaturalResourcesCanadaEarthquakesFeed(
            coordinates,
            language,
            filter_radius=filter_radius,
            filter_minimum_magnitude=filter_minimum_magnitude,
        )
        super().__init__(feed, generate_callback, update_callback, remove_callback)
