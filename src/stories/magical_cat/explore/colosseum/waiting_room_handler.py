from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name
from ask_sdk_model import ui
from util import assets


class WaitingRoomHandler(AbstractRequestHandler):
    """
    控室
    """

    def can_handle(self, handler_input):
        session = handler_input.attributes_manager.session_attributes
        scene = session.get('scene')
        if not scene:
            return False
        return scene == 'explore.colosseum' \
            and is_intent_name("WaitingRoomIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = """
        勇者「控室ですね！どんな手がかりがあるんだろう...？」
        筋肉質なおじさん「ふんっ！ふんっ！今日も剣術の稽古は気持ちがいいなぁ！」
        勇者「すみません、この辺りで「キャリネズミ」というモンスターを見ませんでしたか？」
        筋肉質なおじさん「すまない、稽古にむちゅうで、何も見ていない。」
        勇者「そうですか、、、」
        筋肉質なおじさん「そんなことより、稽古に付き合ってくれないか？久々に実力者と手合わせ願いたい！」
        勇者「すみません、急いでいて。また今度お願いします！」
        筋肉質なおじさん「そうか、ではまた今度頼む。」
        <audio src="soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_intro_01"/>
        勇者「うーん、他に手がかりがありそうなのはどこだろう、、、？」
        """
        handler_input.response_builder.speak(
            speech_text).set_should_end_session(False)

        session = handler_input.attributes_manager.session_attributes
        session['scene'] = 'explore.colosseum'
        session['oracle_limit'] = session['oracle_limit'] - 1
        session['re_ask'] = '勇者「他に手がかりがありそうなのはどこだろう、、、？」'

        image_url = assets.get_image(
            'humans/hero/hero_stand_512')
        handler_input.response_builder.set_card(
            ui.StandardCard(
                title='勇者「他に手がかりがありそうなのはどこだろう、、、？」',
                text='・客席\r\n'
                     '・倉庫\r\n'
                     '・控室\r\n'
                     '・図書館へ行く\r\n'
                     '・闘技場へ行く\r\n'
                     '・屋上へ行く',
                image=ui.Image(
                    small_image_url=image_url,
                    large_image_url=image_url
                )
            )
        )

        return handler_input.response_builder.response
