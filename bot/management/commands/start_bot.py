import logging

from django.core.management.base import BaseCommand

from bot.bot_init import start_polling

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        start_polling()
