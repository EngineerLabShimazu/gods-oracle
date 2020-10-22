from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name


class WarehouseHandler(AbstractRequestHandler):
    """
    倉庫
    """

    def can_handle(self, handler_input):
        session = handler_input.attributes_manager.session_attributes
        scene = session.get('scene')
        if not scene:
            return False
        return scene == 'explore.colosseum' \
            and is_intent_name("WarehouseIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = """
        勇者「倉庫ですね！どんな手がかりがあるんだろう...？
        すごく良い品質の剣がたくさん並んでいる。これなんか特に一級品だ。手入れも行き届いている。良い学校だ。
        ん？倉庫の床に小さな穴が開いている。こんなに手入れも行き届いている学校なのになぜ？
        」
        <audio src="soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_intro_01"/>
        勇者「うーん、他に手がかりがありそうなのはどこだろう、、、？」
        """
        handler_input.response_builder.speak(
            speech_text).set_should_end_session(False)

        session = handler_input.attributes_manager.session_attributes
        session['scene'] = 'explore.colosseum'
        session['oracle_limit'] = session['oracle_limit'] - 1

        return handler_input.response_builder.response
