from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name
from ask_sdk_model import ui
from util import assets


class RooftopIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        session = handler_input.attributes_manager.session_attributes
        scene = session.get('scene')
        if not scene:
            return False
        return scene == 'explore.library' and \
            is_intent_name("RooftopIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = """
        勇者「屋上ですね！かしこまりました！」
        <audio src="soundbank://soundlibrary/human/amzn_sfx_person_running_03"/>
        <audio src="soundbank://soundlibrary/doors/doors_wood/wood_06"/>
        盲目の生徒「すまない。耳をすましているが、何も聞こえない。。。」
        勇者「そうか。何かあったら教えてくれ。
        <break time="1s"/> 
        神よ、次はどうすればよろしいでしょうか？
        """
        handler_input.response_builder.speak(
            speech_text).set_should_end_session(False)

        session = handler_input.attributes_manager.session_attributes
        session['oracle_limit'] = session['oracle_limit'] - 1
        session['scene'] = 'explore.rooftop'
        session['re_ask'] = '勇者「神よ、次はどうすればよろしいでしょうか？」'

        image_url = assets.get_image(
            'humans/blind_hunter/blind_hunter_stand_512')
        handler_input.response_builder.set_card(
            ui.StandardCard(
                title='盲目の生徒',
                text='「すまない。耳をすましているが、何も聞こえない。。。」',
                image=ui.Image(
                    small_image_url=image_url,
                    large_image_url=image_url
                )
            )
        )

        return handler_input.response_builder.response
