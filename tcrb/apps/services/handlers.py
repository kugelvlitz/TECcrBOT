from telegram.ext import CallbackContext


def main_menu_handler(reply, context: CallbackContext) -> None:
    response = "Para buscar servicios escriba el nombre, " \
               "actualmente puede encontrar servicios de becas, " \
               "bibliotecarios, matrícula, servicios médicos o del DOP, entre otros.\n\n" \
               "Ejemplos de las consultas que puede realizar son: becas, libro beca, emergencias, pscologia"

    reply.text(response)
