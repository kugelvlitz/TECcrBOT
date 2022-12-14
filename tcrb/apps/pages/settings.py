from tcrb.apps.config.handlers import HandlerConfig, CallbackQueryHandler
from tcrb.apps.pages.handlers import show_page_handler, show_page_button

PAGE_HANDLER_CONFIGS = HandlerConfig([
    CallbackQueryHandler(show_page_button, show_page_handler)
])
