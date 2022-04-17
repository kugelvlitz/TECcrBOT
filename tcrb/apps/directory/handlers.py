from tcrb.apps.directory.buttons import dept_people_paginator
from tcrb.apps.directory.models import Unit
from tcrb.core.handlers import HandlerConfig, CallbackQueryHandler


def dept_people_paginator_handler(reply, context):
    current_page = reply.expect_int(context.match.group(1))
    unit_id = reply.expect_int(context.match.group(2))

    dept = Unit.objects.get(id=unit_id)

    paginator = dept_people_paginator(current_page,
                                      [role.person for role in dept.role_set.all()],
                                      dept.id)

    reply.edit_markup(paginator.markup)


DIRECTORY_HANDLERS = HandlerConfig([
    # TODO: Cambiar por sistema de enlazado general
    CallbackQueryHandler(dept_people_paginator, dept_people_paginator_handler)
])
