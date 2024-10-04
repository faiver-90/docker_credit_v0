def format_log_message(message, additional_info) -> str:
    return f"\n Message: {message} \n Add info: {additional_info}"


def handle_logger(message, logger_and_lvl, additional_info=' ') -> str:
    formatted_message = format_log_message(message, additional_info)

    result_type = "Error" if 'error' in str(logger_and_lvl).lower() else "Success"
    result_message = f"{result_type}: {formatted_message}"
    logger_and_lvl(result_message)

    return result_message
