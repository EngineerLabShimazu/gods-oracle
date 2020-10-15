from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name


class MagicalCatIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("MagicalCatIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = """
        <audio src="soundbank://soundlibrary/cloth_leather_paper/books/books_04"/>
        魔法の猫、プレシャ。
        プレシャとは、魔法が使える猫型の魔物。使える魔法の属性は、生まれつき、ひたいについている宝石の色によって決まっている。宝石は成長すると取れて、信頼できるパートナーへとプレゼントする。その宝石には絶大な力がひめられている。
        無理やり宝石を取られると魔法が暴走し、プレシャ自身の体が大爆発を起こす。
         <break time="1s"/>
        勇者「うーん、やはりプレシャをこのままほうっておくわけにはいかないようだ、、、他に役に立ちそうな本はどれだろう、、、？」
        """
        handler_input.response_builder.speak(
            speech_text).set_should_end_session(False)

        session = handler_input.attributes_manager.session_attributes
        session['oracle_limit'] = session['oracle_limit'] - 1

        return handler_input.response_builder.response
