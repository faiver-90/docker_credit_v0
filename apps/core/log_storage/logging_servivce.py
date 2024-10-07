# import logging
#
# loggers = {
#     'debug': logging.getLogger('debug').debug,
#     'info': logging.getLogger('info').info,
#     'error': logging.getLogger('error').error,
#     'dev': logging.getLogger('development').debug
# }
#
#
# def custom_logger(message, additional_info=None, logger_name='dev'):
#     formatted_message = format_log_message(message, additional_info)
#
#     logger_func = loggers.get(logger_name.lower())
#
#     if logger_func:
#         logger_func(formatted_message)
#         result_message = f"{logger_name.capitalize()} logger: {formatted_message}"
#     else:
#         result_message = f"Unknown logger: {formatted_message}"
#
#     return result_message
#
#
# def format_log_message(message, additional_info) -> str:
#     return f"\n Message: {message} " \
#            f"\n Add info: {additional_info}"
