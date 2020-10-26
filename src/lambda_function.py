# -*- coding: utf-8 -*-
import logging
from datetime import datetime

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model import ui

from util import assets
from util.skill_builder import sb

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def is_first_launch_skill(handler_input):
    attr = handler_input.attributes_manager.persistent_attributes
    if not attr:
        return True
    return 'first_launch_skill_datetime' not in attr


def save_first_launch_skill_datetime(handler_input):
    attr = handler_input.attributes_manager.persistent_attributes
    attr['first_launch_skill_datetime'] = datetime.today().isoformat()
    handler_input.attributes_manager.save_persistent_attributes()


class LaunchRequestHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        if is_first_launch_skill(handler_input):
            save_first_launch_skill_datetime(handler_input)
            speech_text = """
            オルぺ「はじめまちて。ぼくはオルぺ。
            これから見習い神の君には、神ランクを上げてもらうために、僕が出す課題に挑戦してもらうよ。
            課題というのは、簡単にいうと人助けのことでちゅ。
            じゃあさっそく、、、
            <break time="1s"/>
            どの課題に挑戦しまちゅか？
            」
            """
            ask_text = 'オルぺ「どの課題に挑戦しまちゅか？」'
        else:
            speech_text = ask_text = 'オルぺ「どの課題に挑戦しまちゅか？」'
        handler_input.response_builder.speak(speech_text).ask(ask_text)

        session = handler_input.attributes_manager.session_attributes
        session['scene'] = 'gods_world'
        session['re_ask'] = ask_text

        image_url = assets.get_image('gods/orphe/orphe-stand')
        handler_input.response_builder.set_card(
            ui.StandardCard(
                title='どの課題に挑戦しまちゅか？',
                text='・盲目の狩人\r\n'
                     '・？？？\r\n'
                     '・？？？',
                image=ui.Image(
                    small_image_url=image_url,
                    large_image_url=image_url
                )
            )
        )

        return handler_input.response_builder.response


class GameOverHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        session = handler_input.attributes_manager.session_attributes
        oracle_limit = session.get('oracle_limit')
        if oracle_limit is None:
            return False
        return oracle_limit <= 0

    def handle(self, handler_input):
        speech_text = """
        <audio src="soundbank://soundlibrary/scifi/amzn_sfx_scifi_explosion_2x_01"/>
        勇者「ぐわあーーー！」
        <break time="3s"/>
        オルぺ「おいおい、なにやってるんでちゅか。はぁ。ゲームオーバーでちゅ。
        <break time="1s"/>
        <audio src="soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_intro_01"/>
        どの課題に挑戦しまちゅか？」
        """
        handler_input.response_builder.speak(speech_text).ask(speech_text)

        session = handler_input.attributes_manager.session_attributes
        session['scene'] = 'gods_world'
        session['oracle_limit'] = 5
        session['re_ask'] = 'どの課題に挑戦しまちゅか？'

        return handler_input.response_builder.response


class ReAskHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        session = handler_input.attributes_manager.session_attributes
        re_ask = session.get('re_ask', False)
        return re_ask

    def handle(self, handler_input):
        session = handler_input.attributes_manager.session_attributes
        speak_output = session['re_ask']
        handler_input.response_builder.set_should_end_session(False)
        return handler_input.response_builder.speak(speak_output).response


class HelpIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = """
        このスキルでは、あなたが神となってあなたの事を信仰している「勇者」を導いて頂きます。勇者に「お告げ」を与え、困っている人を救いましょう。
        """
        session = handler_input.attributes_manager.session_attributes
        re_ask = session['re_ask']
        if re_ask:
            speech_text += '<break time="2s"/>' + re_ask
        handler_input.response_builder.speak(speech_text).ask(speech_text)
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        speech_text = "Goodbye!"
        handler_input.response_builder.speak(speech_text)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""

    def can_handle(self, handler_input):
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        return handler_input.response_builder.response


# The intent reflector is used for interaction model testing and debugging.
# It will simply repeat the intent the user said. You can create custom handlers
# for your intents by defining them above, then also adding them to the request
# handler chain below.
class IntentReflectorHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        return is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        intent_name = handler_input.request_envelope.request.intent.name
        speech_text = f"{intent_name}は現在の文脈において答えられる内容ではありません。"
        session = handler_input.attributes_manager.session_attributes

        re_ask = session.get('re_ask')
        if re_ask:
            speech_text += re_ask

        handler_input.response_builder.speak(
            speech_text).set_should_end_session(False)
        return handler_input.response_builder.response


class ErrorHandler(AbstractExceptionHandler):
    """Catch-all exception handler, log exception and
    respond with custom message.
    """

    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        logger.error(exception, exc_info=True)
        speech_text = "Sorry, I couldn't understand what you said. Please try again."
        handler_input.response_builder.speak(speech_text).ask(speech_text)
        return handler_input.response_builder.response


sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(GameOverHandler())

# sb.lambda_handler()が lambda_handler(event, context)をラップしちゃっているので、静的にadd_request_handlerしなきゃいけない
# しかし各 scene で Handlerをadd_request_handler() したい これによってHandlerの名前がかぶる事を防ぐ
# で、ErrorHandlerとかの前に、各Handlerをimportしたいので以下によってimportの順番を担保している
import stories.magical_cat.intro
import stories.magical_cat.explore.intro.add_handlers
import stories.magical_cat.explore.library.add_handlers
import stories.magical_cat.explore.colosseum.add_handlers
import stories.magical_cat.explore.rooftop.add_handlers
import stories.magical_cat.end_flag.library.add_handlers
import stories.magical_cat.end_flag.colosseum.add_handlers

sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

sb.add_request_handler(ReAskHandler())
sb.add_request_handler(IntentReflectorHandler())
sb.add_exception_handler(ErrorHandler())
handler = sb.lambda_handler()
