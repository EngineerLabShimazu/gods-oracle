from util.skill_builder import sb
from .library_handler import LibraryIntentHandler
from .rooftop_handler import RooftopIntentHandler


for h in [LibraryIntentHandler,
          RooftopIntentHandler,
          ]:
    sb.add_request_handler(h())
