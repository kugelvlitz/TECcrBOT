from telegram.ext import CallbackContext

from bot.menu import HandlerMaster
from common.util import Reply
from places.apps import PlacesConfig

handlers = HandlerMaster(PlacesConfig.name)


def menu_entry(reply: Reply, context: CallbackContext) -> None:
    response = "Puede buscar lugares escribiendo el nombre " \
               "para obtener detalles como la ubicación geográfica, descripción e imagen.\n" \
               "Algunos ejemplos de consultas que puede realizar son: A1, D3, pretil, restaurantes, entre otros."

    reply.text(response)
