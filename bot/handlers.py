from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from whoosh.searching import Results

from bot import apps
from bot.index import search, read_index
from bot.menu import read_main_menu, BotHandler
from bot.pages import read_page_tys

handlers = BotHandler(apps.BotConfig.name)


def main_menu(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Seleccione una opción:",
        reply_markup=ReplyKeyboardMarkup(
            read_main_menu(),
            resize_keyboard=True,
        )
    )


def search_handler(update: Update, context: CallbackContext) -> None:
    msg = update.message.text

    tys = {}

    with read_index() as ix:
        results: Results = search(ix, msg)

        for r in results:
            if not tys.get(r['ty']):
                tys[r['ty']] = [r['id']]
            else:
                tys[r['ty']].append(r['id'])

        if results.is_empty():
            update.message.reply_text(
                f'No se encontraron resultados para <i>{msg}</i>')
            return

        if len(tys.keys()) > 1:
            text = f'Resultados para <i>{msg}</i>'
            buttons = [
                handlers.build_inline_button(f'{read_page_tys()[ty].desc} ({len(ids)})', 'get_type_pages', str(ty))
                for ty, ids in tys.items()
            ]
        else:
            ty = tys.popitem()[0]
            text = f'Resultados de {read_page_tys()[ty].desc} para <i>{msg}</i>'
            buttons = [
                handlers.build_inline_button(f'{r["title"]}', 'get_page', str(ty), str(r["id"]))
                for r in results
            ]

        update.message.reply_text(
            text=text,
            reply_markup=InlineKeyboardMarkup.from_column(buttons)
        )


def type_handler(update: Update, context: CallbackContext) -> None:
    cq = update.callback_query
    cq.answer()
    ent = cq.message.entities[0]
    offset = ent.offset
    lenght = ent.offset + ent.length
    query = cq.message.text[offset:lenght]
    ty = int(context.match.group(1))

    with read_index() as ix:
        results = search(ix, query)

        cq.message.edit_text(
            text=f'Resultados de {read_page_tys()[ty].desc} para <i>{query}</i>',
            reply_markup=InlineKeyboardMarkup.from_column([
                handlers.build_inline_button(r['title'], 'get_page', str(ty), r["id"])
                for r in results if r['ty'] == ty
            ])
        )


def show_page(update: Update, context: CallbackContext) -> None:
    ty = int(context.match.group(1))
    page_id = int(context.match.group(2))
    update.callback_query.answer()

    msg, page_buttons = read_page_tys()[ty].page_builder(page_id)

    update.callback_query.message.edit_text(
        text=msg,
        reply_markup=InlineKeyboardMarkup.from_column(page_buttons)
        if page_buttons else None
    )
