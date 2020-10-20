# -*- coding: utf-8 -*-
import logging

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name

from util.skill_builder import sb

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        speech_text = """
        どの物語を遊びまちゅか？
        """
        handler_input.response_builder.speak(speech_text).ask(speech_text)

        session = handler_input.attributes_manager.session_attributes
        session['scene'] = 'gods_world'

        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = "「こんにちは」か「ヘルプ」とおっしゃっていただけます。"
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
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        return is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        intent_name = handler_input.request_envelope.request.intent.name
        speech_text = ("You just triggered {}").format(intent_name)
        handler_input.response_builder.speak(
            speech_text).set_should_end_session(True)
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

# sb.lambda_handler()が lambda_handler(event, context)をラップしちゃっているので、静的にadd_request_handlerしなきゃいけない
# しかし各 scene で Handlerをadd_request_handler() したい これによってHandlerの名前がかぶる事を防ぐ
# で、ErrorHandlerとかの前に、各Handlerをimportしたいので以下によってimportの順番を担保している
import stories.magical_cat.intro
import stories.magical_cat.explore.intro.add_handlers
import stories.magical_cat.explore.library.add_handlers
import stories.magical_cat.explore.colosseum.add_handlers
import stories.magical_cat.explore.rooftop.add_handlers
import stories.magical_cat.end_flag.library.add_handlers

sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

sb.add_request_handler(IntentReflectorHandler())
sb.add_exception_handler(ErrorHandler())
handler = sb.lambda_handler()
