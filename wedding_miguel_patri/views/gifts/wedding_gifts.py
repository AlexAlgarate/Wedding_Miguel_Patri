import reflex as rx

from wedding_miguel_patri.components import (
    card,
    icon_section,
    text_section,
    title_section,
)
from wedding_miguel_patri.styles.fonts import FontWeight
from wedding_miguel_patri.utils import IconRoutes, utils


def wedding_gifts() -> rx.Component:
    """
    Create a component for displaying wedding gift information.

    Returns:
    - rx.Component: A Reflex component representing the wedding gifts section.

    This component includes an icon, title, and paragraphs with information about wedding gifts.
    """

    return card(
        icon_section(icon=IconRoutes.ICON_GIFT.value, alt=""),
        title_section(title=utils.gift_title),
        text_section(utils.gift_text),
        text_section(utils.account_number_text, font_weight=FontWeight.HIGH.value),
        id="gift_section",
    )
