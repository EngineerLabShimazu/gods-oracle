from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name
from ask_sdk_model import ui
from util import assets


class RooftopIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        session = handler_input.attributes_manager.session_attributes
        scene = session.get('scene')
        if not scene:
            return False
        return scene == 'explore.rooftop' and \
            is_intent_name("RooftopIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = """
        盲目の生徒「ん？すまない。手がかりは何も掴めていない。。。」
        勇者「そうか。たびたびすまない。何かあったら教えてくれ。
        <break time="1s"/> 
        神よ、次はどうすればよろしいでしょうか？」
        """
        handler_input.response_builder.speak(
            speech_text).set_should_end_session(False)

        session = handler_input.attributes_manager.session_attributes
        session['oracle_limit'] = session['oracle_limit'] - 1
        session['re_ask'] = '勇者「神よ、次はどうすればよろしいでしょうか？」'

        image_url = assets.get_image(
            'humans/hero/hero_stand_512')
        handler_input.response_builder.set_card(
            ui.StandardCard(
                title='勇者「神よ、次はどうすればよろしいでしょうか？」',
                text='・図書館へ行く\r\n'
                     '・闘技場へ行く\r\n'
                     '・屋上へ行く',
                image=ui.Image(
                    small_image_url=image_url,
                    large_image_url=image_url
                )
            )
        )

        return handler_input.response_builder.response
