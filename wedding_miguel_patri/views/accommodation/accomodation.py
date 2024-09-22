import reflex as rx

from wedding_miguel_patri.components import (  # icon_section,  #TODO pendiente icono
    card,
    text_section,
    title_section,
)
from wedding_miguel_patri.styles.colors import Color


def accomodation() -> rx.Component:
    return card(
        # icon_section  # TODO añadir icono
        rx.icon(
            "bed",
            size=60,
            stroke_width=0.8,
            color=Color.TITLES.value,
            max_height="auto",
        ),
        title_section(title="Alojamiento"),
        text_section(
            text="Si te vas a querer quedar alojado en Guadalajara,existe una tarifa especial en el hotel Pax."
        ),
        text_section("Si necesitas información, dínoslo."),
    )
