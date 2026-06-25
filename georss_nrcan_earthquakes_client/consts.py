"""Natural Resources Canada Earthquakes constants."""

from georss_client.consts import CUSTOM_ATTRIBUTE

ATTRIBUTIONS = {"en": "Natural Resources Canada", "fr": "Ressources naturelles Canada"}
REGEXP_ATTR_MAGNITUDE = f"<b>magnitude: </b>(?P<{CUSTOM_ATTRIBUTE}>[^<]+)<br/>"
URL_PATTERN = (
    "http://www.earthquakescanada.nrcan.gc.ca/index-{}.php?"
    "tpl_region=canada&tpl_output=rss"
)
URLS = {
    "en": URL_PATTERN.format("en"),
    "fr": URL_PATTERN.format("fr"),
}
