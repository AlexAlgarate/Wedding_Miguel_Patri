import reflex as rx

from wedding_miguel_patri.pages.index import index
from wedding_miguel_patri.styles import style as style

app = rx.App(
    style=style.BASE_STYLE,
    stylesheets=style.STYLESHEETS,
)
app.add_page(index)
