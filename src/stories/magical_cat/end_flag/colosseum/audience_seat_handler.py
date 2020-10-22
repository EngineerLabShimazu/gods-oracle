from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name


class AudienceSeatHandler(AbstractRequestHandler):
    """
    客席
    """

    def can_handle(self, handler_input):
        session = handler_input.attributes_manager.session_attributes
        scene = session.get('scene')
        if not scene:
            return False
        return scene == 'end_flag.colosseum' \
            and is_intent_name("AudienceSeatIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = """
        勇者「客席ですね！どんな手がかりがあるんだろう...？」
        読書している人「やぁ。どうかした？」
        勇者「実は訳あって、キャリネズミというモンスターをさがしているんだ。君はみていない？」
        読書している人「ごめん、読書に夢中で。あ！でもキャリネズミって、確かものすごく隠れるのが得意なモンスターだよね？」
        勇者「そうなんだよ！そのせいでさがし辛くて困っているんだ」
        読書している人「確か図書館でそんな感じの本を読んだ事がある気がするなぁ。うちの図書館はいろんな本があって、情報ならたいてい揃うよ」
        勇者「そっか！ありがとう！」
        読書している人「うん、がんばってねー！」
        <audio src="soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_intro_01"/>
        勇者「そろそろ屋上へ報告に行こうかな？」
        """
        handler_input.response_builder.speak(
            speech_text).set_should_end_session(False)

        session = handler_input.attributes_manager.session_attributes
        session['scene'] = 'end_flag.colosseum'
        session['oracle_limit'] = session['oracle_limit'] - 1

        return handler_input.response_builder.response
