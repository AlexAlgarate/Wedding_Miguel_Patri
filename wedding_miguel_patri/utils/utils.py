import os
from typing import Dict, List

from dotenv import load_dotenv

load_dotenv()

menu_data: Dict[str, str] = {
    "Confirmación": "/#confirmation_section",
    "Dirección": "/#celebration_section",
    "Autobús": "/#bus_service_section",
    "Contacto": "/#contact_section",
    "Fotos": "/#photos_section",
}


# Web descriptions
title_main = "Invitación de boda de Patri y Miguel 30/05/2025"
description_main = """
    ¡Quedas invitada a nuestra boda! ¡Acompáñanos en este día mágico e inolvidable!
"""


# Header texts
title_header = "¡Nos casamos!"
wedding_date: List[str] = [
    "30",
    "mayo",
    "2025",
]
wedding_hour = "19:30"


# Image descriptions
alt_image_celebration = "Foto de Montealvar."
alt_image_partners = "Foto principal de los novios."
alt_image_leafs = "Foto de unas hojas amarillas."
alt_image_lavender = "Foto de unas ramas de lavanda con sus hojas"

# Icons desriptions
alt_icon_confirmation = "Icono de un sobre morado"
alt_icon_celebration = "Icono de un pórtico con velo morado"
alt_icon_bus = "Icono de un bus morado"
alt_icon_ubication = "Icono de ubicación morado"
alt_icon_whatsapp = "Icono de Whatsapp morado"
alt_icon_camera = "Icono de una cámara de fotos morada"


# SECTION TEXTS
# Countdown texts
countdown_text = "¡Ven a acompañarnos en el día más feliz de nuestras vidas!"
countdown_button = "Guardar fecha"

# Confirmation
confirmation_title = "Confirmación"
confirmation_button = "Confirmar asistencia"
confirmation_text = """Seguro que tienes muchas ganas de compartir este día con nosotros.\n
    ¿Confirmas tu asistencia?"""


# Celebration
celebration_title = "¿Dónde nos casamos"
celebration_button = "Abrir en Google Maps"
celebration_text = "Hemos elegido un sitio muy especial para celebrar este gran día."
wedding_place = "Finca Montealvar"
wedding_address_street = "Yebes"
wedding_address_province = "Guadalajara"


# Bus
bus_title = "Servicio de autobús"
bus_text = """
Para garantizar que todo el mundo se lo pueda pasar genial y disfrutar con nosotros
sin preocuparse de conducir habrá servicio de autobús de vuelta a Guadalajara cuando terminemos. 
Los coches se pueden quedar en la finca y recoger al día siguiente sin problema."""
bus_destination_title = "Regreso a casa"

# TODO Review this variables, if origin() don't be used in the future, drop them
hotel_address = "Plaza de Santo Domingo"
origin_bus_schedule = "12:00"


# Photo Album
title_photo = "Álbum de Fotos"
google_photo_text_two = """
    Queremos que no se nos escape ningún detalle de este día por eso,
    sube todas tus fotos y vídeos al álbum compartido que hemos hecho.
"""
google_photo_button = "Abrir álbum"


# Gift
gift_title = "Lista de regalos"
gift_text = """
    Vuestra presencia es nuestro mayor regalo,
    pero si nos queréis hacer una aportacion para ayudarnos a celebrar,
    este es nuestro número de cuenta
"""
account_number_text = os.environ["ACCOUNT_NUMBER"]


# Contact & Accomodation
contact_bride = dict(
    name="Patri",
    phone_number=os.environ["PATRI_PHONE"],
)
contact_groom = dict(
    name="Miguel",
    phone_number=os.environ["MIGUEL_PHONE"],
)
accomodation_title = "Alojamiento"
accomodation_main_text = """
    Si te quieres alojar en Guadalajara,
    existe una tarifa especial en el hotel Pax.
"""
accomodation_ask_info = "Si necesitas información, ¡pregúntanos!"

# Bottom web message
bottom_text = "Te esperamos"
