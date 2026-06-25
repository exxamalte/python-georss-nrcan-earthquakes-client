"""Natural Resources Canada Earthquakes constants."""

from typing import Final

from georss_client.consts import CUSTOM_ATTRIBUTE

ATTRIBUTIONS: Final = {
    "en": "Natural Resources Canada",
    "fr": "Ressources naturelles Canada",
}
REGEXP_ATTR_MAGNITUDE: Final = f"<b>magnitude: </b>(?P<{CUSTOM_ATTRIBUTE}>[^<]+)<br/>"
URL_PATTERN: Final = (
    "http://www.earthquakescanada.nrcan.gc.ca/index-{}.php?"
    "tpl_region=canada&tpl_output=rss"
)
URLS: Final = {
    "en": URL_PATTERN.format("en"),
    "fr": URL_PATTERN.format("fr"),
}
