from util.skill_builder import sb
from .hide_n_seek_handler import HideAndSeekIntentHandler
from .library_handler import LibraryIntentHandler
from .magical_cat_handler import MagicalCatIntentHandler
from .rooftop_handler import RooftopIntentHandler
from .silent_step_handler import SilentStepIntentHandler


for h in [HideAndSeekIntentHandler,
          LibraryIntentHandler,
          MagicalCatIntentHandler,
          RooftopIntentHandler,
          SilentStepIntentHandler,
          ]:
    sb.add_request_handler(h())
