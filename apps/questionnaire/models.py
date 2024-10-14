import os

from django.contrib.auth.models import User
from django.db import models
from text_unidecode import unidecode


class PhoneType(models.Model):
    phone_type = models.CharField(max_length=50, unique=True, verbose_name="Тип телефона")

    def __str__(self):
        return self.phone_type

    class Meta:
        verbose_name = "Тип телефона"
        verbose_name_plural = "Типы телефонов"


class ClientPreData(models.Model):
    first_name_to_contact_pre_client = models.CharField(max_length=255, null=True, blank=True, verbose_name="Обращение")
    type_pre_client = models.CharField(max_length=255, null=True, blank=True, default='Физическое лицо',
                                       verbose_name="Тип клиента")
    product_pre_client = models.CharField(max_length=255, null=True, blank=True, default='Кредит на автомобиль',
                                          verbose_name="Продукт")
    phone_number_pre_client = models.CharField(max_length=20, null=True, blank=True, verbose_name="Номер телефона")
    type_phone_pre_client = models.ForeignKey(PhoneType, on_delete=models.CASCADE, null=True, blank=True,
                                              verbose_name="Тип телефона")
    total_loan_amount = models.CharField(max_length=255, blank=True, null=True)
    car_price_display = models.CharField(max_length=255, blank=True, null=True)
    additional_equipment_price_display = models.CharField(max_length=255, blank=True, null=True)
    partner_offers_shown = models.BooleanField(default=False, verbose_name="Показаны партнерские предложения")

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.first_name_to_contact_pre_client or ''} ({self.phone_number_pre_client or ''})"


def upload_to(instance, filename):
    filename = unidecode(filename)
    return os.path.join(f'client_documents/client_{instance.client.id}', filename)


class DocumentType(models.Model):
    document_type = models.CharField(max_length=50, unique=True, verbose_name="Тип документа")

    class Meta:
        verbose_name = "Тип документа"
        verbose_name_plural = "Типы документов"

    def __str__(self):
        return self.document_type


class ClientDocument(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE, null=True, blank=True,
                                      verbose_name="Тип документа")
    document_file = models.FileField(upload_to=upload_to, verbose_name="Выбрать файл")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # def delete(self, *args, **kwargs):
    #     bucket_name = settings.GOOGLE_CLOUD_STORAGE_BUCKET_NAME
    #     blob_name = str(self.document_file)
    #     delete_from_bucket(bucket_name, blob_name)
    #     super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Загруженный документ клиента"
        verbose_name_plural = "Загруженные документы клиентов"

    def __str__(self):
        if self.document_type:
            return f"{self.document_type}"
        else:
            return f"Документ без типа ({self.client})"


class FinancingTerm(models.Model):
    term = models.CharField(max_length=255, unique=True, verbose_name="Срок финансирования")

    def __str__(self):
        return self.term

    class Meta:
        verbose_name = "Срок финансирования"
        verbose_name_plural = "Сроки финансирования"


class ClientFinancingCondition(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='financing_conditions')
    initial_payment = models.CharField(max_length=255, blank=True, null=True, verbose_name="Первоначальный взнос")
    financing_term = models.ForeignKey(FinancingTerm, on_delete=models.SET_NULL, verbose_name="Срок финансирования",
                                       null=True, blank=True)
    monthly_payment = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ежемесячный платеж")
    deferred_payment = models.BooleanField(default=False, verbose_name="Отложенный платеж")

    class Meta:
        verbose_name = "Условия финансирования"
        verbose_name_plural = "Условия финансирования"

    def __str__(self):
        return f"Условия финансирования для {self.client}"


class CarBrand(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Марка автомобиля")

    class Meta:
        verbose_name = "Марка автомобиля"
        verbose_name_plural = "Марки автомобилей"

    def __str__(self):
        return self.name


class CarCondition(models.Model):
    condition = models.CharField(max_length=50, unique=True, verbose_name="Состояние автомобиля")

    class Meta:
        verbose_name = "Состояние автомобиля"
        verbose_name_plural = "Состояния автомобилей"

    def __str__(self):
        return self.condition


class CarConfiguration(models.Model):
    configuration = models.CharField(max_length=50, unique=True, verbose_name="Комплектация автомобиля")

    class Meta:
        verbose_name = "Комплектация автомобиля"
        verbose_name_plural = "Комплектации автомобилей"

    def __str__(self):
        return self.configuration


class EngineType(models.Model):
    engine_type = models.CharField(max_length=50, unique=True, verbose_name="Тип двигателя")

    class Meta:
        verbose_name = "Тип двигателя"
        verbose_name_plural = "Типы двигателей"

    def __str__(self):
        return self.engine_type


class EcoClass(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Экологический класс"
        verbose_name_plural = "Экологические классы"

    def __str__(self):
        return self.name


class ClientCarInfo(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='car_info')

    brand_car_info = models.ForeignKey(CarBrand, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Марка")
    model_car_info = models.CharField(blank=True, null=True, max_length=255, verbose_name="Модель")
    condition_car_info = models.ForeignKey(CarCondition, on_delete=models.CASCADE, null=True, blank=True,
                                           verbose_name="Состояние")
    configuration_car_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="Комплектация")
    year_car_info = models.CharField(max_length=4, blank=True, null=True, verbose_name="Год")
    engine_volume_car_info = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                                 verbose_name="Объем двигателя")
    power_car_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="Мощность (Л.С.)")
    color_car_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="Цвет")
    mileage_car_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="Пробег")
    engine_type_car_info = models.ForeignKey(EngineType, on_delete=models.CASCADE, null=True, blank=True,
                                             verbose_name="Тип двигателя")
    vin_car_info = models.CharField(max_length=17, null=True, blank=True, verbose_name="VIN")
    car_price_car_info = models.CharField(max_length=255, blank=True, null=True, verbose_name="Цена автомобиля")
    dealer_equipment_price_car_info = models.CharField(max_length=255, blank=True, null=True,
                                                       verbose_name="Цена доп. оборудования от дилера")
    price_date_car_info = models.DateTimeField(blank=True, null=True, auto_now_add=True,
                                               verbose_name="Дата формирования цены")

    body_number_car_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="Номер кузова")
    engine_number_car_info = models.CharField(max_length=255, null=True, blank=True, verbose_name="Номер двигателя")
    eco_class_car_info = models.ForeignKey(EcoClass, on_delete=models.CASCADE, null=True, blank=True,
                                           verbose_name="Экологический класс")

    class Meta:
        verbose_name = "Информация о машине"
        verbose_name_plural = "Информация о машинах"

    def __str__(self):
        return f"{self.brand_car_info or ''} {self.model_car_info or ''} ({self.vin_car_info or ''})"


class TypePts(models.Model):
    pts_type = models.CharField(max_length=50, unique=True, verbose_name="Тип ПТС")

    class Meta:
        verbose_name = "Тип ПТС"
        verbose_name_plural = "Типы ПТС"

    def __str__(self):
        return self.pts_type


class AutoSaleDocument(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='documents')
    pts_type_sale_auto = models.ForeignKey(TypePts, on_delete=models.CASCADE, null=True, blank=True,
                                           verbose_name="Тип ПТС")
    pts_number_sale_auto = models.CharField(max_length=255, null=True, blank=True, verbose_name="Номер ПТС")
    pts_issue_sale_auto = models.DateField(null=True, blank=True, verbose_name="Дата выдачи ПТС")
    pts_issued_by_sale_auto = models.CharField(max_length=255, null=True, blank=True, verbose_name="Кем выдан ПТС")
    pts_name_sale_auto = models.CharField(max_length=255, null=True, blank=True, verbose_name="Название ТС по ПТС")
    dcp_number_sale_auto = models.CharField(max_length=255, null=True, blank=True, verbose_name="Номер ДКП")
    dcp_issue_date_sale_auto = models.DateField(null=True, blank=True, verbose_name="Дата выдачи ДКП")

    class Meta:
        verbose_name = "Документ продажи автомобиля"
        verbose_name_plural = "Документы продажи автомобилей"

    def __str__(self):
        return f"Документ продажи для {self.client}"


class ClientExtraInsurance(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='extra_insurance')
    kasko_amount = models.CharField(max_length=255, default=0, blank=True, null=True, verbose_name="КАСКО")
    kasko_amount_include = models.BooleanField(default=False, verbose_name="Добавить в счет кредита КАСКО")

    gap_amount = models.CharField(max_length=255, default=0, blank=True, null=True, verbose_name="GAP")
    gap_amount_include = models.BooleanField(default=False, verbose_name="Добавить в счет кредита GAP")

    szh_amount = models.CharField(max_length=255, default=0, blank=True, null=True, verbose_name="Страхование жизни")
    szh_term = models.CharField(max_length=255, blank=True, null=True, verbose_name="Срок")
    szh_term_include = models.BooleanField(default=False, verbose_name="Добавить в счет кредита СЖ")

    financial_products_amount = models.CharField(max_length=255, blank=True, null=True,
                                                 verbose_name="Финансовые продукты")
    financial_products_amount_include = models.BooleanField(max_length=255, blank=True, null=True,
                                                            verbose_name="Добавить в счет кредита Фин. продукты")

    installment_commission_include = models.BooleanField(blank=True, null=True, default=False,
                                                         verbose_name="Снижение процента")
    sms_notification_include = models.BooleanField(blank=True, null=True, default=False,
                                                   verbose_name="СМС информирование")

    class Meta:
        verbose_name = "Дополнительное страхование"
        verbose_name_plural = "Дополнительные страхования"

    def __str__(self):
        return f"Дополнительное страхование для {self.client}"


class AllApplications(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE)  # Связь с таблицей Client
    financing_conditions = models.ForeignKey(ClientFinancingCondition,
                                             on_delete=models.CASCADE)  # Связь с таблицей FinancingConditions
    car_info = models.ForeignKey(ClientCarInfo, on_delete=models.CASCADE)  # Связь с таблицей CarInfo
    documents = models.ForeignKey(AutoSaleDocument, on_delete=models.CASCADE)  # Связь с таблицей Document

    extra_insurance = models.ForeignKey(ClientExtraInsurance,
                                        on_delete=models.CASCADE)  # Связь с таблицей ExtraInsurance

    status = models.CharField(blank=True, null=True, max_length=255)
    type_all_app = models.CharField(blank=True, null=True, max_length=255)  # Физическое лицо
    financing = models.CharField(blank=True, null=True, max_length=255)  # кредит
    manager = models.CharField(blank=True, null=True, max_length=255)  # имя авторизованного аккаунта
    dealership_all_app = models.CharField(blank=True, null=True, max_length=255)  # Название ДЦ
    organization = models.CharField(blank=True, null=True, max_length=255)  # юридическое лицо
    date_create_all_app = models.DateTimeField(blank=True, null=True, auto_now_add=True)  # Дата создания
    date_changes_all_app = models.DateTimeField(blank=True, null=True, auto_now=True)  # Дата изменения

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"Заявка {self.id} для клиента {self.client}"


class Offers(models.Model):
    title = models.CharField(max_length=255)
    name_bank = models.CharField(max_length=255)
    term = models.IntegerField()
    stavka = models.CharField(max_length=255)
    pay = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Предложение"
        verbose_name_plural = "Предложения"


class ClientOffer(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE)
    offer_id = models.IntegerField()
    title_offer = models.CharField(max_length=255)
    name_bank_offer = models.CharField(max_length=255)
    term_offer = models.IntegerField()
    stavka_offer = models.CharField(max_length=255)
    pay_offer = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Предложение клиента"
        verbose_name_plural = "Предложения клиентов"

    def __str__(self):
        return f"Предложение {self.title_offer} для {self.client}"


class SelectedClientOffer(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE)
    offer_id = models.IntegerField(null=True, blank=True)
    total_loan_amount_select = models.CharField(max_length=255, blank=True, null=True, verbose_name="Сумма кредита")
    car_price_display_select = models.CharField(max_length=255, blank=True, null=True, verbose_name="Цена автомобиля")
    initial_payment_select = models.CharField(max_length=255, blank=True, null=True,
                                              verbose_name="Первоначальный взнос")
    term_select = models.CharField(max_length=255, null=True, blank=True, verbose_name="Срок кредита")
    title_select = models.CharField(max_length=255, null=True, blank=True, verbose_name="Название предложения")
    monthly_payment_select = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ежемесячный платеж")
    stavka_select = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ставка")
    name_bank_select = models.CharField(max_length=255, blank=True, null=True, verbose_name="Название банка")
    status_select_offer = models.CharField(max_length=255, blank=True, null=True)
    info_from_bank = models.CharField(max_length=255, blank=True, null=True)
    id_app_bank = models.CharField(max_length=255, blank=True, null=True)
    id_app_in_system = models.IntegerField(default=0, blank=True, null=True)
    link_to_detail_from_bank = models.CharField(max_length=255, blank=True, null=True)

    # status_selected_card = models.BooleanField(default=False, verbose_name="Выбранное предложение")  # Добавлено

    class Meta:
        verbose_name = "Выбранное предложение клиента"
        verbose_name_plural = "Выбранные предложения клиентов"

    def __str__(self):
        return f"{self.client.id} - Offer ID: {self.offer_id} - Status: {self.status_select_offer}"


class HousingType(models.Model):
    type = models.CharField(max_length=255, unique=True, verbose_name="Тип жилья")

    class Meta:
        verbose_name = "Тип жилья"
        verbose_name_plural = "Типы жилья"

    def __str__(self):
        return self.type


class Gender(models.Model):
    gender = models.CharField(max_length=255, unique=True, verbose_name="Пол")

    class Meta:
        verbose_name = "Пол"
        verbose_name_plural = "Пола"

    def __str__(self):
        return self.gender


class SocialStatus(models.Model):
    status = models.CharField(max_length=255, unique=True, verbose_name="Социальный статус")

    class Meta:
        verbose_name = "Социальный статус"
        verbose_name_plural = "Социальные статусы"

    def __str__(self):
        return self.status


class ClientPersonalInfo(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='client_person_data')
    first_name_to_contact_client = models.CharField(max_length=255, verbose_name="Обращение", blank=True, null=True)
    first_name_client = models.CharField(max_length=255, verbose_name="Имя", blank=True, null=True)
    last_name_client = models.CharField(max_length=255, verbose_name="Фамилия", blank=True, null=True)
    middle_name_client = models.CharField(max_length=255, verbose_name="Отчество", blank=True, null=True)
    type_client = models.CharField(max_length=255, default='Физическое лицо', verbose_name="Тип", blank=True, null=True)
    product_client = models.CharField(max_length=255, default='Кредит на автомобиль', verbose_name="Продукт",
                                      blank=True, null=True)
    birth_date_client = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    birth_place_citizenship = models.CharField(max_length=255, verbose_name="Место рождения", blank=True, null=True)
    registration_address_client = models.CharField(max_length=255, verbose_name="Адрес регистрации", blank=True,
                                                   null=True)

    housing_type_client = models.ForeignKey(HousingType, on_delete=models.SET_NULL, verbose_name="Тип жилья",
                                            blank=True, null=True)
    registration_date_client = models.DateField(verbose_name="Дата регистрации", blank=True, null=True)
    gender_choice_client = models.ForeignKey(Gender, on_delete=models.SET_NULL, verbose_name="Пол", blank=True,
                                             null=True)
    social_status_client = models.ForeignKey(SocialStatus, on_delete=models.SET_NULL, verbose_name="Социальный статус",
                                             blank=True, null=True)
    country_name_pre_client = models.CharField(max_length=255, blank=True, null=True, verbose_name="Страна регистрации")
    post_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Почтовый индекс")
    fact_address_same_registration = models.BooleanField(verbose_name="Место проживания совпадает с местом регистрации",
                                                         default=False)

    class Meta:
        verbose_name = "Личная информация клиента"
        verbose_name_plural = "Личная информация клиентов"

    def __str__(self):
        return f"Личная информация для {self.client}"


class ClientContact(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='contact_data')
    living_address_contact = models.CharField(max_length=255, verbose_name="Адрес проживания", blank=True, null=True)
    housing_type_contact = models.ForeignKey(HousingType, on_delete=models.CASCADE, null=True, blank=True,
                                             verbose_name="Тип жилья")
    living_start_date_contact = models.DateField(verbose_name="Дата начала проживания", blank=True, null=True)
    phone_number_contact = models.CharField(max_length=20, verbose_name="Номер телефона", blank=True, null=True)
    phone_type_contact = models.ForeignKey(PhoneType, on_delete=models.CASCADE, null=True, blank=True,
                                           verbose_name="Тип телефона")
    email_contact = models.EmailField(verbose_name="Email", blank=True, null=True)
    notes_contact = models.TextField(verbose_name="Примечание", blank=True, null=True)

    class Meta:
        verbose_name = "Контактные данные клиента"
        verbose_name_plural = "Контактные данные клиентов"

    def __str__(self):
        return f"{self.client} - {self.phone_number_contact or ''}"


class ClientPassport(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='passport_data')
    series_number_passport = models.CharField(max_length=20, verbose_name="Серия и номер", blank=True, null=True)
    issue_date_passport = models.DateField(verbose_name="Дата выдачи", blank=True, null=True)
    division_code_passport = models.CharField(max_length=10, verbose_name="Код подразделения", blank=True, null=True)
    issued_by_passport = models.CharField(max_length=200, verbose_name="Кем выдан", blank=True, null=True)

    class Meta:
        verbose_name = "Паспортные данные клиента"
        verbose_name_plural = "Паспортные данные клиентов"

    def __str__(self):
        return f"Паспортные данные для {self.client}"


class ClientDriverLicense(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='driver_license_data')
    series_number_driver_license = models.CharField(max_length=20, verbose_name="Серия и номер", blank=True, null=True)
    issue_date_driver_license = models.DateField(verbose_name="Дата выдачи", blank=True, null=True)
    issued_by_driver_license = models.CharField(max_length=200, verbose_name="Кем выдан", blank=True, null=True)
    experience_start_date_driver_license = models.DateField(verbose_name="Стаж (дата выдачи первого ВУ)", blank=True,
                                                            null=True)

    class Meta:
        verbose_name = "Водительское удостоверение клиента"
        verbose_name_plural = "Водительские удостоверения клиентов"

    def __str__(self):
        return f"Паспортные данные для {self.client}"


class ClientTaxDocument(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='tax_document')
    series_number_tax_document = models.CharField(max_length=20, verbose_name="Серия и номер", blank=True, null=True)
    number_tax_document = models.CharField(max_length=20, verbose_name="ИНН", blank=True, null=True)

    class Meta:
        verbose_name = "Налоговый документ клиента"
        verbose_name_plural = "Налоговые документы клиентов"

    def __str__(self):
        return f"Налоговый документ для {self.client}"


class ClientPensionCertificate(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='pension_certificate')
    number_pension_sert = models.CharField(max_length=20, verbose_name="Номер", blank=True, null=True)

    class Meta:
        verbose_name = "Пенсионное свидетельство клиента"
        verbose_name_plural = "Пенсионные свидетельства клиентов"

    def __str__(self):
        return f"Пенсионное свидетельство для {self.client}"


class ClientInternationalPassport(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='international_passport')
    series_number_international_passport = models.CharField(max_length=20, verbose_name="Серия и номер", blank=True,
                                                            null=True)
    issue_date_international_passport = models.DateField(verbose_name="Дата выдачи", blank=True, null=True)
    issued_by_international_passport = models.CharField(max_length=200, verbose_name="Кем выдан", blank=True, null=True)

    class Meta:
        verbose_name = "Загранпаспорт клиента"
        verbose_name_plural = "Загранпаспорта клиентов"

    def __str__(self):
        return f"Загранпаспорт для {self.client}"


class EducationLevel(models.Model):
    level = models.CharField(max_length=255, unique=True, verbose_name="Уровень образования")

    class Meta:
        verbose_name = "Уровень образования"
        verbose_name_plural = "Уровни образования"

    def __str__(self):
        return self.level


class ClientEducation(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='education')
    education_level_client = models.ForeignKey(EducationLevel, on_delete=models.SET_NULL,
                                               verbose_name="Уровень образования", blank=True, null=True)

    class Meta:
        verbose_name = "Образование клиента"
        verbose_name_plural = "Образование клиентов"

    def __str__(self):
        return str(self.education_level_client) if self.education_level_client else ''


class OrganizationType(models.Model):
    type = models.CharField(max_length=255, unique=True, verbose_name="Тип организации")

    class Meta:
        verbose_name = "Тип организации"
        verbose_name_plural = "Типы организаций"

    def __str__(self):
        return self.type


class ActivityCode(models.Model):
    code = models.CharField(max_length=255, unique=True, verbose_name="Код вида деятельности")

    class Meta:
        verbose_name = "Код вида деятельности"
        verbose_name_plural = "Коды видов деятельности"

    def __str__(self):
        return self.code


class PositionType(models.Model):
    type = models.CharField(max_length=255, unique=True, verbose_name="Тип должности")

    class Meta:
        verbose_name = "Тип должности"
        verbose_name_plural = "Типы должностей"

    def __str__(self):
        return self.type


class ClientEmployment(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='employment')
    organization_inn = models.CharField(max_length=20, verbose_name="ИНН организации", blank=True, null=True)
    organization_form = models.CharField(max_length=255, verbose_name="Форма организации (чем занимается)", blank=True,
                                         null=True)
    organization_name = models.CharField(max_length=255, verbose_name="Юр. название", blank=True, null=True)
    organization_type = models.ForeignKey(OrganizationType, on_delete=models.SET_NULL, verbose_name="Тип организации",
                                          blank=True, null=True)
    activity_code = models.ForeignKey(ActivityCode, on_delete=models.SET_NULL, verbose_name="Код вида деятельности",
                                      blank=True, null=True)
    position = models.CharField(max_length=255, verbose_name="Наименование должности", blank=True, null=True)
    position_type = models.ForeignKey(PositionType, on_delete=models.SET_NULL, verbose_name="Тип должности", blank=True,
                                      null=True)
    registration_address_employment = models.CharField(max_length=255, verbose_name="Адрес регистрации", blank=True,
                                                       null=True)
    phone_number_organization = models.CharField(max_length=20, verbose_name="Номер телефона", blank=True, null=True)
    current_experience = models.CharField(max_length=255, verbose_name="Стаж на текущем месте", blank=True, null=True)
    total_experience = models.CharField(max_length=255, verbose_name="Стаж общий", blank=True, null=True)
    shift_method = models.BooleanField(verbose_name="Работа вахтовым методом", default=False, blank=True, null=True)
    official_position = models.BooleanField(verbose_name="Должностное лицо", default=False, blank=True, null=True)

    class Meta:
        verbose_name = "Трудоустройство клиента"
        verbose_name_plural = "Трудоустройство клиентов"

    def __str__(self):
        return f"Трудоустройство для {self.client}"


class Country(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название страны")

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def __str__(self):
        return self.name


class ClientCitizenship(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='citizenship')
    birth_country_client = models.ForeignKey(Country, on_delete=models.SET_NULL, verbose_name="Страна рождения",
                                             blank=True, null=True)
    russian_citizenship = models.BooleanField(verbose_name="Гражданство Россия, единственно", default=False, blank=True,
                                              null=True)
    residence_permit = models.BooleanField(verbose_name="Вид на жительство в другой стране", default=False, blank=True,
                                           null=True)
    us_citizenship = models.BooleanField(verbose_name="Гражданство США", default=False, blank=True, null=True)
    tax_resident_foreign = models.BooleanField(verbose_name="Налоговый резидент иностранного государства",
                                               default=False, blank=True, null=True)
    tax_residence_countries = models.CharField(max_length=255, verbose_name="Страны налогового резиденства", blank=True,
                                               null=True)
    foreign_inn = models.CharField(max_length=20, verbose_name="ИНН иностранного государства", blank=True, null=True)

    class Meta:
        verbose_name = "Гражданство клиента"
        verbose_name_plural = "Гражданства клиентов"

    def __str__(self):
        return f"Гражданство для {self.client}"


class MaritalStatus(models.Model):
    status = models.CharField(max_length=255, unique=True, verbose_name="Семейное положение")

    class Meta:
        verbose_name = "Семейное положение"
        verbose_name_plural = "Семейные положения"

    def __str__(self):
        return self.status


class PurchaseMethod(models.Model):
    method = models.CharField(max_length=255, unique=True, verbose_name="Способ приобретения")

    class Meta:
        verbose_name = "Способ приобретения"
        verbose_name_plural = "Способы приобретения"

    def __str__(self):
        return self.method


class RealEstateType(models.Model):
    type = models.CharField(max_length=255, unique=True, verbose_name="Тип недвижимости")

    class Meta:
        verbose_name = "Тип недвижимости"
        verbose_name_plural = "Типы недвижимости"

    def __str__(self):
        return self.type


class ClientFamilyInfo(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='family_info')
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.SET_NULL, verbose_name="Семейное положение",
                                       blank=True, null=True)
    children_under_18 = models.IntegerField(verbose_name="Дети до 18 лет", blank=True, null=True)
    dependents = models.IntegerField(verbose_name="Иждивенцы", blank=True, null=True)
    years_married = models.IntegerField(verbose_name="Количество лет в браке", blank=True, null=True)
    official_position_relative = models.BooleanField(verbose_name="Должностное лицо (родственник)", default=False)
    degree_of_kinship = models.CharField(max_length=255, verbose_name="Степень родства", blank=True, null=True)
    relative_position = models.CharField(max_length=255, verbose_name="Должность и место работы", blank=True, null=True)

    class Meta:
        verbose_name = "Семейная информация клиента"
        verbose_name_plural = "Семейная информация клиентов"

    def __str__(self):
        return f"Семейная информация для {self.client}"


class IncomeType(models.Model):
    type = models.CharField(max_length=255, unique=True, verbose_name="Тип дохода")

    class Meta:
        verbose_name = "Тип дохода"
        verbose_name_plural = "Типы доходов"

    def __str__(self):
        return self.type


class ClientFinancialInfo(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='financial_info')
    income_amount = models.CharField(max_length=255, verbose_name="Сумма дохода", blank=True, null=True)
    confirmed_income_amount = models.CharField(max_length=255, verbose_name="Подтвержденная сумма", blank=True,
                                               null=True)
    income_proof_document = models.CharField(max_length=255, verbose_name="Документ подтверждающий доход", blank=True,
                                             null=True)
    income_source = models.CharField(max_length=255, verbose_name="Источник доходов", blank=True, null=True)
    disposable_income = models.CharField(max_length=255, verbose_name="Сумма которую вы можете выделять", blank=True,
                                         null=True)
    spouse_income = models.CharField(max_length=255, verbose_name="Сумма доходов супруга", blank=True, null=True)
    income_type = models.ForeignKey(IncomeType, on_delete=models.SET_NULL, verbose_name="Тип дохода", blank=True,
                                    null=True)

    class Meta:
        verbose_name = "Финансовая информация клиента"
        verbose_name_plural = "Финансовая информация клиентов"

    def __str__(self):
        return f"Семейная информация для {self.client}"


class ClientExpenses(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='expenses')
    mandatory_payments = models.CharField(max_length=255, verbose_name="Обязательные платежи в месяц", blank=True,
                                          null=True)
    loan_payments = models.CharField(max_length=255, verbose_name="Платежи по кредитам", blank=True, null=True)
    mortgage_payments = models.CharField(max_length=255, verbose_name="Платежи по ипотеке", blank=True, null=True)

    class Meta:
        verbose_name = "Расходы клиента"
        verbose_name_plural = "Расходы клиентов"

    def __str__(self):
        return f"Расходы для {self.client}"


class ClientVehicle(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='vehicle')
    brand_vehicle = models.CharField(max_length=255, verbose_name="Марка", blank=True, null=True)
    year_vehicle = models.IntegerField(verbose_name="Год", blank=True, null=True)
    model_vehicle = models.CharField(max_length=255, verbose_name="Модель", blank=True, null=True)
    purchase_year = models.IntegerField(verbose_name="Год приобретения", blank=True, null=True)
    purchase_method_vehicle = models.ForeignKey(PurchaseMethod, on_delete=models.SET_NULL,
                                                verbose_name="Способ приобретения", blank=True, null=True)

    class Meta:
        verbose_name = "Транспортное средство клиента"
        verbose_name_plural = "Транспортные средства клиентов"

    def __str__(self):
        return f"Транспортное средство {self.brand_vehicle or ''} для {self.client}"


class ClientRealEstate(models.Model):
    client = models.ForeignKey(ClientPreData, on_delete=models.CASCADE, related_name='real_estate')
    real_estate_type = models.ForeignKey(RealEstateType, on_delete=models.SET_NULL, verbose_name="Тип недвижимости",
                                         blank=True, null=True)
    purchase_method_real_estate = models.ForeignKey(PurchaseMethod, on_delete=models.SET_NULL,
                                                    verbose_name="Способ приобретения", blank=True, null=True)
    address_real_estate = models.CharField(max_length=255, verbose_name="Адрес", blank=True, null=True)


    class Meta:
        verbose_name = "Недвижимость клиента"
        verbose_name_plural = "Недвижимость клиентов"

    def __str__(self):
        return f"Недвижимость {self.address_real_estate or ''} для {self.client}"
