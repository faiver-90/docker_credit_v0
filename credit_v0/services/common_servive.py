from django.http import JsonResponse


def convert_str_list(li):
    print(f'convert work')
    # return list(map(int, li[0].split(',')))
    return [int(x) for x in li[0].split(',')]


def handle_logger(message, logger_and_lvl, additional_info=None, status=200):
    if additional_info:
        logger_and_lvl(f"{message}: {additional_info[:500]}... (total length: {len(str(additional_info))})")
    else:
        logger_and_lvl(message)

    return JsonResponse(
        {'success': False, 'error': message},
        status=status,
        json_dumps_params={'ensure_ascii': False}
    )
