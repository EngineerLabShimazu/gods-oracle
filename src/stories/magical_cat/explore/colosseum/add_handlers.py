from util.skill_builder import sb
from .rooftop_handler import RooftopIntentHandler
from .colosseum_handler import ColosseumIntentHandler

for h in [RooftopIntentHandler,
          ColosseumIntentHandler,
          ]:
    sb.add_request_handler(h())
