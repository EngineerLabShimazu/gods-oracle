from util.skill_builder import sb
from .colosseum_handler import ColosseumIntentHandler
from .library_handler import LibraryIntentHandler
from .rooftop_handler import RooftopIntentHandler

for h in [ColosseumIntentHandler,
          LibraryIntentHandler,
          RooftopIntentHandler]:
    sb.add_request_handler(h())
