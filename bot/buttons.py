from enum import Enum

from bot.apps import BotConfig
from tcrb.core import BotAppConfig


class States(Enum):
    GET_PAGE = "get_page"
    ONE_TYPE_RESULTS = "one_type_results"
    MULTIPLE_TYPE_RESULTS = "multi_type_results"


config = BotAppConfig(BotConfig.name, BotConfig.verbose_name)
page_button = config.create_inline_button(States.GET_PAGE, r"(\d+)", r"(\d+)")

one_type_paginator = config.create_paginator(States.ONE_TYPE_RESULTS, rf"(\d+)")

multiple_types_paginator = config.create_paginator(States.MULTIPLE_TYPE_RESULTS)

type_selection_button = config.create_inline_button(States.MULTIPLE_TYPE_RESULTS, rf"(\d+)")
