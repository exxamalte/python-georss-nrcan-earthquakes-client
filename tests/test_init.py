"""Test for the Natural Resources Canada Earthquakes feed."""
import datetime
import unittest
from unittest import mock

from georss_client import UPDATE_OK
from georss_client.exceptions import GeoRssException
from georss_nrcan_earthquakes_client import \
    NaturalResourcesCanadaEarthquakesFeed, \
    NaturalResourcesCanadaEarthquakesFeedManager
from tests import load_fixture

HOME_COORDINATES = (49.25, -123.1)


class TestNaturalResourcesCanadaEarthquakesFeed(unittest.TestCase):
    """Test the Natural Resources Canada Earthquakes feed."""

    @mock.patch("requests.Request")
    @mock.patch("requests.Session")
    def test_update_ok_en(self, mock_session, mock_request):
        """Test updating feed is ok."""
        mock_session.return_value.__enter__.return_value.send\
            .return_value.ok = True
        mock_session.return_value.__enter__.return_value.send\
            .return_value.text = \
            load_fixture('natural_resources_canada_earthquakes_en_feed.xml')

        feed = NaturalResourcesCanadaEarthquakesFeed(HOME_COORDINATES, 'en')
        assert repr(feed) == "<NaturalResourcesCanadaEarthquakesFeed(" \
                             "home=(49.25, -123.1), url=http://www." \
                             "earthquakescanada.nrcan.gc.ca/index-en.php?" \
                             "tpl_region=canada&tpl_output=rss, " \
                             "radius=None, magnitude=None)>"
        status, entries = feed.update()
        assert status == UPDATE_OK
        self.assertIsNotNone(entries)
        assert len(entries) == 2

        feed_entry = entries[0]
        assert feed_entry.title == "Title 1"
        assert feed_entry.external_id == "1234"
        assert feed_entry.coordinates == (44.11, -66.23)
        self.assertAlmostEqual(feed_entry.distance_to_home, 4272.4, 1)
        assert feed_entry.published \
            == datetime.datetime(2018, 9, 29, 8, 30,
                                 tzinfo=datetime.timezone.utc)
        assert feed_entry.category == "Category 1"
        assert feed_entry.magnitude == 4.5
        assert feed_entry.attribution == "Natural Resources Canada"
        assert repr(feed_entry) == "<NaturalResourcesCanadaEarthquakes" \
                                   "FeedEntry(id=1234)>"

        feed_entry = entries[1]
        assert feed_entry.title == "Title 2"
        self.assertIsNone(feed_entry.published)

    @mock.patch("requests.Request")
    @mock.patch("requests.Session")
    def test_update_ok_en_with_magnitude(self, mock_session, mock_request):
        """Test updating feed is ok."""
        mock_session.return_value.__enter__.return_value.send\
            .return_value.ok = True
        mock_session.return_value.__enter__.return_value.send\
            .return_value.text = \
            load_fixture('natural_resources_canada_earthquakes_en_feed.xml')

        feed = NaturalResourcesCanadaEarthquakesFeed(
            HOME_COORDINATES, 'en', filter_minimum_magnitude=4.0)
        assert repr(feed) == "<NaturalResourcesCanadaEarthquakesFeed(" \
                             "home=(49.25, -123.1), url=http://www." \
                             "earthquakescanada.nrcan.gc.ca/index-en.php?" \
                             "tpl_region=canada&tpl_output=rss, " \
                             "radius=None, magnitude=4.0)>"
        status, entries = feed.update()
        assert status == UPDATE_OK
        self.assertIsNotNone(entries)
        assert len(entries) == 1

        feed_entry = entries[0]
        assert feed_entry.title == "Title 1"
        assert feed_entry.external_id == "1234"

    @mock.patch("requests.Request")
    @mock.patch("requests.Session")
    def test_update_ok_fr(self, mock_session, mock_request):
        """Test updating feed is ok."""
        mock_session.return_value.__enter__.return_value.send\
            .return_value.ok = True
        mock_session.return_value.__enter__.return_value.send\
            .return_value.text = \
            load_fixture('natural_resources_canada_earthquakes_fr_feed.xml')

        feed = NaturalResourcesCanadaEarthquakesFeed(HOME_COORDINATES, 'fr')
        assert repr(feed) == "<NaturalResourcesCanadaEarthquakesFeed(" \
                             "home=(49.25, -123.1), url=http://www." \
                             "earthquakescanada.nrcan.gc.ca/index-fr.php?" \
                             "tpl_region=canada&tpl_output=rss, " \
                             "radius=None, magnitude=None)>"
        status, entries = feed.update()
        assert status == UPDATE_OK
        self.assertIsNotNone(entries)
        assert len(entries) == 2

        feed_entry = entries[0]
        assert feed_entry.title == "Title 1"
        assert feed_entry.external_id == "1234"
        assert feed_entry.coordinates == (44.11, -66.23)
        self.assertAlmostEqual(feed_entry.distance_to_home, 4272.4, 1)
        assert feed_entry.published \
            == datetime.datetime(2018, 9, 29, 8, 30,
                                 tzinfo=datetime.timezone.utc)
        assert feed_entry.category == "Category 1"
        assert feed_entry.magnitude == 4.5
        assert feed_entry.attribution == "Ressources naturelles Canada"
        assert repr(feed_entry) == "<NaturalResourcesCanadaEarthquakes" \
                                   "FeedEntry(id=1234)>"

        feed_entry = entries[1]
        assert feed_entry.title == "Title 2"
        self.assertIsNone(feed_entry.published)

    @mock.patch("requests.Request")
    @mock.patch("requests.Session")
    def test_update_ok_fr_with_magnitude(self, mock_session, mock_request):
        """Test updating feed is ok."""
        mock_session.return_value.__enter__.return_value.send\
            .return_value.ok = True
        mock_session.return_value.__enter__.return_value.send\
            .return_value.text = \
            load_fixture('natural_resources_canada_earthquakes_fr_feed.xml')

        feed = NaturalResourcesCanadaEarthquakesFeed(
            HOME_COORDINATES, 'fr', filter_minimum_magnitude=4.0)
        assert repr(feed) == "<NaturalResourcesCanadaEarthquakesFeed(" \
                             "home=(49.25, -123.1), url=http://www." \
                             "earthquakescanada.nrcan.gc.ca/index-fr.php?" \
                             "tpl_region=canada&tpl_output=rss, " \
                             "radius=None, magnitude=4.0)>"
        status, entries = feed.update()
        assert status == UPDATE_OK
        self.assertIsNotNone(entries)
        assert len(entries) == 1

        feed_entry = entries[0]
        assert feed_entry.title == "Title 1"
        assert feed_entry.external_id == "1234"

    def test_update_wrong_language(self):
        """Test invalid feed language."""
        with self.assertRaises(GeoRssException):
            NaturalResourcesCanadaEarthquakesFeed(HOME_COORDINATES,
                                                  'DOES NOT EXIST')

    @mock.patch("requests.Request")
    @mock.patch("requests.Session")
    def test_feed_manager(self, mock_session, mock_request):
        """Test the feed manager."""
        mock_session.return_value.__enter__.return_value.send\
            .return_value.ok = True
        mock_session.return_value.__enter__.return_value.send\
            .return_value.text = load_fixture(
                'natural_resources_canada_earthquakes_en_feed.xml')

        # This will just record calls and keep track of external ids.
        generated_entity_external_ids = []
        updated_entity_external_ids = []
        removed_entity_external_ids = []

        def _generate_entity(external_id):
            """Generate new entity."""
            generated_entity_external_ids.append(external_id)

        def _update_entity(external_id):
            """Update entity."""
            updated_entity_external_ids.append(external_id)

        def _remove_entity(external_id):
            """Remove entity."""
            removed_entity_external_ids.append(external_id)

        feed_manager = NaturalResourcesCanadaEarthquakesFeedManager(
            _generate_entity,
            _update_entity,
            _remove_entity,
            HOME_COORDINATES,
            'en')
        assert repr(feed_manager) == "<NaturalResourcesCanadaEarthquakes" \
                                     "FeedManager(feed=<NaturalResources" \
                                     "CanadaEarthquakesFeed(home=" \
                                     "(49.25, -123.1), " \
                                     "url=http://www.earthquakescanada." \
                                     "nrcan.gc.ca/index-en.php?" \
                                     "tpl_region=canada&tpl_output=rss, " \
                                     "radius=None, magnitude=None)>)>"
        feed_manager.update()
        entries = feed_manager.feed_entries
        self.assertIsNotNone(entries)
        assert len(entries) == 2
        assert feed_manager.last_timestamp \
            == datetime.datetime(2018, 9, 29, 8, 30,
                                 tzinfo=datetime.timezone.utc)
        assert len(generated_entity_external_ids) == 2
        assert len(updated_entity_external_ids) == 0
        assert len(removed_entity_external_ids) == 0
