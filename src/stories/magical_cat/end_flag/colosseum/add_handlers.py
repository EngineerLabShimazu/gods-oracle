from util.skill_builder import sb
from .rooftop_handler import RooftopIntentHandler
from .colosseum_handler import ColosseumIntentHandler
from .library_handler import LibraryIntentHandler
from .audience_seat_handler import AudienceSeatHandler
from .waiting_room_handler import WaitingRoomHandler
from .warehouse_handler import WarehouseHandler
from .yes_handler import YesIntentHandler

for h in [
    RooftopIntentHandler,
    ColosseumIntentHandler,
    LibraryIntentHandler,
    AudienceSeatHandler,
    WaitingRoomHandler,
    WarehouseHandler,
    YesIntentHandler,
          ]:
    sb.add_request_handler(h())
