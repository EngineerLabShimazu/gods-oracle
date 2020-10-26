from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name


class LibraryIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        session = handler_input.attributes_manager.session_attributes
        scene = session.get('scene')
        if not scene:
            return False
        return scene == 'explore.library' \
            and is_intent_name("LibraryIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = """
        勇者「ここはもう図書館でございます、、、役に立ちそうな本はどれだろう、、、？」
        """
        handler_input.response_builder.speak(
            speech_text).set_should_end_session(False)

        session = handler_input.attributes_manager.session_attributes
        session['oracle_limit'] = session['oracle_limit'] - 1
        session['re_ask'] = '勇者「役に立ちそうな本はどれだろう、、、？」'

        return handler_input.response_builder.response
