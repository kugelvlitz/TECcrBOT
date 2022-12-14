import itertools

from telegram import InlineKeyboardMarkup

from tcrb.apps.search import index
from . import settings
from .buttons import dept_people_paginator
from .models import Person, Unit, Role, RoleTy, Location
from ..pages.handlers import build_show_page_button


def index_people(person: Person):
    return {
        'kw': person_kws(person),
        'name': person.name,
        'surname': person.surname,
        'tel': person.phone,
        'email': person.email,
    }


def person_kws(person):
    return [kw.text
            for role in Role.objects.filter(person=person)
            for source in ((role.unit,), (role_ty.ty for role_ty in RoleTy.objects.filter(role=role)))
            for term in source
            for kw in index.HINT_ANALYZER(term.name)]


def loc_builder(location: Location, reply):
    reply.text(href(location))


def dept_builder(dept: Unit, reply):
    reply.text(href(dept),
               reply_markup=dept_people_paginator(1,
                                                  [role.person for role in dept.role_set.all()],
                                                  dept.id).markup)


def people_builder(person: Person, reply) -> None:
    def role_msg(role):
        functions, types = '', ''
        groups = itertools.groupby(role.rolety_set.all(), lambda role_ty: role_ty.is_function)
        for is_function, group in groups:
            group = ', '.join(role_ty.ty.name for role_ty in group)
            if is_function:
                functions = group
            else:
                types = f' ({group})'

        yield f'<u>{role.unit.name}</u>{types}'
        if functions:
            yield functions

    def msg():
        yield f'Correo electrónico: {or_unavailable(person.email)}'
        yield f'Teléfono: {or_unavailable(person.phone)}'

        for role in person.role_set.all():
            yield ''
            yield from role_msg(role)

        yield ''
        yield href(person)
    # TODO: Cambiar por sistema de enlazado general
    reply.text('\n'.join(msg()),
               reply_markup=InlineKeyboardMarkup.from_column(list(
                   build_show_page_button(f"Ver {role.unit.name}", settings.DEPT_PAGES.ty, role.unit.id)
                   for role in person.role_set.all()
               ))
               )


def or_unavailable(text, *, key=lambda x: x):
    return key(text) if text else 'No disponible'


def href(obj):
    return f'<a href="https://www.tec.ac.cr{obj.href}">Ver más información</a>'
