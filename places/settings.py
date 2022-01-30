from telegram.ext import MessageHandler, Filters, CallbackQueryHandler

from . import apps
from .handlers import menu_entry, select_place, get_place, name_edit

MAIN_MENU_COMMAND = 'Ubicaciones 📍'

HANDLERS = [
    MessageHandler(Filters.text(MAIN_MENU_COMMAND), menu_entry),
    CallbackQueryHandler(select_place, pattern=rf'{apps.PlacesConfig.name}:tag_id:\d*'),
    CallbackQueryHandler(get_place, pattern=rf'{apps.PlacesConfig.name}:place_id:.*'),
    CallbackQueryHandler(name_edit, pattern=rf'{apps.PlacesConfig.name}:name_edit:\d+'),
]
