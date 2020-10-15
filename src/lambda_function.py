# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK.
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

from scenes.library.silent_step_handler import SilentStepIntentHandler
from scenes.library.hide_n_seek_handler import HideAndSeekIntentHandler
from scenes.library.magical_cat_handler import MagicalCatIntentHandler
from scenes.library.rooftop_handler import LibraryRooftopIntentHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # speech_text = "ようこそ, 「こんにちは」か「ヘルプ」とおっしゃっていただけます。どうしますか？"
        speech_text = """
        「猫とネズミと盲目の狩人」。始まります。
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
        handler_input.response_builder.speak(speech_text).ask(speech_text)

        session = handler_input.attributes_manager.session_attributes
        session['oracle_limit'] = 5

        return handler_input.response_builder.response


class LibraryIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("LibraryIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = """
        勇者「図書館ですね！かしこまりました！」
        <audio src="soundbank://soundlibrary/human/amzn_sfx_person_running_03"/>
        <audio src="soundbank://soundlibrary/doors/doors_wood/wood_06"/>
        勇者「ここが図書館かぁ。うーん、役に立ちそうな本はどれだろう、、、？」
        """
        handler_input.response_builder.speak(
            speech_text).set_should_end_session(False)

        session = handler_input.attributes_manager.session_attributes
        session['oracle_limit'] = session['oracle_limit'] - 1

        return handler_input.response_builder.response


class RooftopIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("RooftopIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = """
        勇者「屋上ですね！かしこまりました！」
        <audio src="soundbank://soundlibrary/human/amzn_sfx_person_running_03"/>
        盲目の生徒「すまない。耳をすましているが、何も聞こえない。。。」
        勇者「そうか。何かあったら教えてくれ。
        <break time="1s"/> 
        神よ、次はどうすればよろしいでしょうか？」
        """
        handler_input.response_builder.speak(
            speech_text).set_should_end_session(False)

        session = handler_input.attributes_manager.session_attributes
        session['oracle_limit'] = session['oracle_limit'] - 1

        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "「こんにちは」か「ヘルプ」とおっしゃっていただけます。"
        handler_input.response_builder.speak(speech_text).ask(speech_text)
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Goodbye!"
        handler_input.response_builder.speak(speech_text)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        return handler_input.response_builder.response


# The intent reflector is used for interaction model testing and debugging.
# It will simply repeat the intent the user said. You can create custom handlers
# for your intents by defining them above, then also adding them to the request
# handler chain below.
class IntentReflectorHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = handler_input.request_envelope.request.intent.name
        speech_text = ("You just triggered {}").format(intent_name)
        handler_input.response_builder.speak(
            speech_text).set_should_end_session(True)
        return handler_input.response_builder.response


# Generic error handling to capture any syntax or routing errors. If you receive an error
# stating the request handler chain is not found, you have not implemented a handler for
# the intent being invoked or included it in the skill builder below.
class ErrorHandler(AbstractExceptionHandler):
    """Catch-all exception handler, log exception and
    respond with custom message.
    """

    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)
        speech_text = "Sorry, I couldn't understand what you said. Please try again."
        handler_input.response_builder.speak(speech_text).ask(speech_text)
        return handler_input.response_builder.response


# This handler acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.
sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(LibraryIntentHandler())
# sb.add_request_handler(RooftopIntentHandler())
sb.add_request_handler(SilentStepIntentHandler())
sb.add_request_handler(HideAndSeekIntentHandler())
sb.add_request_handler(MagicalCatIntentHandler())
sb.add_request_handler(LibraryRooftopIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(
    IntentReflectorHandler())  # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(ErrorHandler())

handler = sb.lambda_handler()
