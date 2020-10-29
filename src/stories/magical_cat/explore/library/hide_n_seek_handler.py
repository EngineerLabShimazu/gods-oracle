from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name


class HideAndSeekIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        session = handler_input.attributes_manager.session_attributes
        scene = session.get('scene')
        if not scene:
            return False
        return scene == 'explore.library' \
            and is_intent_name("HideAndSeekIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = """
        <audio src="soundbank://soundlibrary/cloth_leather_paper/books/books_04"/>
        『妖精のかくれんぼ』
         <break time="1s"/>
         むかしむかし。あるところに、妖精と遊ぶ盲目の人がいた。妖精は人前に姿を表すことはほとんどない。とってもシャイで用心深い。
         しかし、盲目の人は妖精と遊ぶ事ができた。よくかくれんぼをしていた。たいそう耳がよく、妖精のかすかな羽の音が聞こえていたので、いつもすぐに見つける事ができた。
         くやしがった妖精は、魔法で自分の羽の音を消すことにした。これなら、かくれんぼは僕の勝ちだ！そう思った妖精は、次の日もあっさりと見つかった。
         「どうして僕の居場所がわかったんだい？」。妖精が聞いた。
         「君がかくれている場所だけ、音が聞こえなかったからね。」盲目の人は答えた。
         妖精はこの人とのかくれんぼに「絶対に勝つ」と心に決めた。
         <break time="2s"/>
        勇者「これだ！！！さっそく報告に行こうかな？」
        """
        handler_input.response_builder.speak(
            speech_text).set_should_end_session(False)

        session = handler_input.attributes_manager.session_attributes
        session['scene'] = 'end_flag.library'
        session['oracle_limit'] = session['oracle_limit'] - 1
        session['re_ask'] = '勇者「さっそく報告に行こうかな？」'

        return handler_input.response_builder.response
