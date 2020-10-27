from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name
from util.skill_builder import sb
from ask_sdk_model import ui
from util import assets


class BlindHunterHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        session = handler_input.attributes_manager.session_attributes
        scene = session.get('scene')
        if not scene:
            return False
        return scene == 'gods_world' and \
            is_intent_name("BlindHunterIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = """
        オルぺ「盲目の狩人。この課題は、お告げ7回以内にクリアしてくだちゃい。それでは、いってらっちゃい。」
        <audio src="soundbank://soundlibrary/magic_spells/magic_spells_09"/>
        勇者「ここがソルジャースクールか。」
        受付「ようこそソルジャースクールへ。見学ですか？」
        勇者「はい。」
        受付「どうぞ。」
        <break time="2s"/>
        いじめっこA「やーい、このノロマ！」
        盲目の生徒「<break time="1s"/>」
        いじめっこA「おい、無視すんのかよ。頭きたぜ！」
        いじめっこB「おもしろくねーな。いくぞ。」
        いじめっこA「くそっ。」
        勇者「なんだろう？」
        <break time="2s"/>
        勇者「君、大丈夫？」
        盲目の生徒「ああ、いつものことだから。」
        勇者「おだやかじゃないね。」
        盲目の生徒「もうなれっこさ。」
        勇者「どうしてあんな風に言われているんだい？」
        盲目の生徒「僕は目が不自由で、あいつらはそんな僕を見下して充実感を得たいんじゃないかな」
        勇者「つまんねぇ連中だな」
        盲目の生徒「まったくだ」
        <break time="2s"/>
        <audio src="soundbank://soundlibrary/human/amzn_sfx_person_running_03"/>
        先生「あなたたち！私の召喚獣、プレシャの宝石が盗まれたの！何か知らない！？」
        盲目の生徒「、、、？特にこちらは、、、」
        勇者「申し訳ない。存じ上げないです。」
        先生「そう、、、。」
        勇者「緊急の事態でしょうか？」
        先生「そうなの！このままだと、、、」
        先生「この建物が吹っ飛ぶ！」
        <audio src="soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_intro_01"/>
        先生「なにか手がかりはないかしら、、、」
        勇者「もしかしたら、さっきの悪戯っ子たち、、、」
        先生「え？」
        盲目の生徒「実は、、、」
        <break time="2s"/>
        いたずらっこA「お前たちなんかに、見つけられるもんかぁ！」
        先生「あなたたち！早く返しなさい！」
        いたずらっこB「やなこったぁ♪」
        いたずらっこA「オレの召喚獣、キャリネズミに運ばせている！オレのキャリネズミは一味違うんだぜぇ。なんといっても、足音を完全に聞こえなくするスキル、『シノビアシ』を使う！このオレにだって、帰ってくるまで見つけ出すことは不可能なのさ！」
        勇者「なんてことを！」
        先生「あなたたち、それがどんな災いに発展するかわかっているの？」
        いたずらっこB「災い？ただの憂さ晴らしだろ？」
        先生「私のプレシャから宝石が一定距離離れると、大規模な爆発が起きてしまうのよ！授業でもやったでしょ！」
        いたずらっこA「え！！！」
        いたずらっこB「嘘だろ！」
        いたずらっこA「もうオレでもさがせねぇぞ！」
        いたずらっこB「にげろぉぉぉ」
        <audio src="soundbank://soundlibrary/human/amzn_sfx_person_running_03"/>
        先生「盲目の生徒君。あなたのズバ抜けた耳の良さなら、なんとか探せないかしら？」
        盲目の生徒「足音を一切消してしまうスキル『シノビアシ』を使われていては、僕も探しようがありません。しかし念のため、校舎全体の音が聞こえるように屋上にいきます！」
        <audio src="soundbank://soundlibrary/human/amzn_sfx_person_running_03"/>
        <break time="1s"/> 
        勇者「いったいどうすれば？神よ！私はどうすればよいでしょうか？」
        """
        handler_input.response_builder.speak(
            speech_text).set_should_end_session(False)

        session = handler_input.attributes_manager.session_attributes
        session['oracle_limit'] = 7
        session['scene'] = 'explore.intro'
        session['re_ask'] = ' 勇者「神よ！私はどうすればよいでしょうか？」'

        image_url = assets.get_image('humans/here/hero_stand_512')
        handler_input.response_builder.set_card(
            ui.StandardCard(
                title='勇者',
                text='「神よ！私はどうすればよいでしょうか？」',
                image=ui.Image(
                    small_image_url=image_url,
                    large_image_url=image_url
                )
            )
        )

        return handler_input.response_builder.response


sb.add_request_handler(BlindHunterHandler())
