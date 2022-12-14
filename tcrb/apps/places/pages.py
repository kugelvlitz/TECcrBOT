from django.conf import settings

from .models import Place


def show_place(place: Place, reply):
    message = reply.text(place.description or '')

    if place.latitude and place.longitude:
        message.reply_location(latitude=place.latitude,
                               longitude=place.longitude,
                               reply_to_message_id=message.message_id)
    else:
        message.reply_text("Ubicación no disponible",
                           reply_to_message_id=message.message_id)

    if place.photo:
        message.reply_photo(open(settings.BASE_DIR / place.photo, mode='rb'),
                            reply_to_message_id=message.message_id)
    else:
        message.reply_text("Imagen no disponible",
                           reply_to_message_id=message.message_id)
