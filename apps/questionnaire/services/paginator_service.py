from django.core.paginator import Paginator


class PaginationService:
    """Сервис для пагинации"""
    @staticmethod
    def paginate(object_list, page_number=1, per_page=5):
        """Пагинация списка объектов"""

        paginator = Paginator(object_list, per_page)
        page_obj = paginator.get_page(page_number)
        return page_obj
