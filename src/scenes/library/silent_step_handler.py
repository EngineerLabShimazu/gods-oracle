from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name


class SilentStepIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("SilentStepIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = """
        <audio src="soundbank://soundlibrary/cloth_leather_paper/books/books_04"/>
        スキル『シノビアシ』とは、かつて伝説の勇者パーティで諜報部員として活躍した召喚獣『キャリネズミ』が使用し、高度な情報戦を優位に戦った。
         <break time="1s"/>
        勇者「うーん、やっぱりシノビアシは無敵なのだろうか、、、他に役に立ちそうな本はどれだろう、、、？」
        """
        handler_input.response_builder.speak(
            speech_text).set_should_end_session(False)

        session = handler_input.attributes_manager.session_attributes
        session['oracle_limit'] = session['oracle_limit'] - 1

        return handler_input.response_builder.response
