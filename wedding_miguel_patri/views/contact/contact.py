import reflex as rx

from wedding_miguel_patri.components import (
    card,
    icon_section,
    text_section,
    title_section,
)
from wedding_miguel_patri.utils import IconRoutes, utils

from .components import whatsapp_button


def contact() -> rx.Component:
    """
    Create a contact information section component.

    Returns:
    - rx.Component: A Reflex component representing the contact information section.
    """

    return card(
        icon_section(icon=IconRoutes.ICON_PHONE.value, alt=utils.alt_icon_contact),
        title_section(title=utils.contact_title),
        text_section(utils.contact_text_whatsapp),
        whatsapp_button(utils.contact_bride, utils.contact_groom),
        id="contact_section",
    )
