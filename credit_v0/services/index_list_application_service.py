from credit_v0.models import SelectedClientOffer, AllApplications, UserProfile


class ApplicationService:
    """Сервис для работы с заявками"""

    @staticmethod
    def get_applications(user, dealership_filter='', status_filter='', ordering='-date_create_all_app'):
        """Получение списка заявок с учетом фильтров"""

        user_profile = UserProfile.objects.get(user=user)
        user_organization = user_profile.organization_manager
        user_dealership = user_profile.get_active_dealership()

        if user.is_superuser:
            object_list = AllApplications.objects.all().order_by(ordering)
        else:
            object_list = AllApplications.objects.filter(
                organization=user_organization,
                dealership_all_app=user_dealership if not dealership_filter else dealership_filter
            ).order_by(ordering)

        if status_filter:
            object_list = object_list.filter(
                client__selectedclientoffer__status_select_offer=status_filter
            ).distinct()

        # Добавление статусов к заявкам
        for application in object_list:
            offers = SelectedClientOffer.objects.filter(client=application.client).exclude(
                status_select_offer__isnull=True).exclude(status_select_offer__exact='')
            application.statuses = [{'status': offer.status_select_offer,
                                     'client_id': offer.client.id,
                                     'button_class': ApplicationService.get_button_class(offer.status_select_offer)} for
                                    offer in offers]

        return object_list

    @staticmethod
    def get_button_class(status):
        """Получение CSS-класса для кнопки по статусу"""
        classes = {
            'Ошибка': 'btn btn-error',
            'Ожидание решения': 'btn btn-pending',
            'Отказ': 'btn btn-reject',
            'Запрос доп информации': 'btn btn-request-info',
            'Одобрение': 'btn btn-approve',
            'Нет статуса': 'btn btn-light'
        }
        return classes.get(status, 'btn btn-light')
