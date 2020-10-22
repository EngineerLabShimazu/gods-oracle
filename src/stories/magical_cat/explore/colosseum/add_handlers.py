from util.skill_builder import sb
from .rooftop_handler import RooftopIntentHandler
from .colosseum_handler import ColosseumIntentHandler
from .library_handler import LibraryIntentHandler

for h in [
    RooftopIntentHandler,
    ColosseumIntentHandler,
    LibraryIntentHandler
          ]:
    sb.add_request_handler(h())
