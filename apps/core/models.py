import uuid

from django.contrib.auth.models import User
from django.db import models

from apps.questionnaire.models import ClientPreData


class Event(models.Model):
    event_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    aggregate_id = models.CharField(max_length=64)
    event_type = models.CharField(max_length=255)
    payload = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)
    id_user_changing = models.IntegerField(default=None)

    def __str__(self):
        return f"{self.event_type} - {self.aggregate_id}"

    class Meta:
        verbose_name = "Ивент"
        verbose_name_plural = "Ивенты"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.user.username}'


# Спарсенные продукты СовКомБанка из файла
class OffersSovComBank(models.Model):
    id_in_excel_file_sovcom = models.IntegerField(null=True, blank=True, verbose_name="ID в ексель файле")
    actual_sovcom = models.IntegerField(null=True, blank=True, verbose_name="actual столбец")
    rating_sovcom = models.IntegerField(null=True, blank=True, verbose_name="Рейтинг выдачи")


# Модели для калькулятора СовКомБанк
class ResponseCalculationSovComBank(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    request_id = models.UUIDField(default=uuid.uuid4)
    dealer_id = models.CharField(max_length=255)


class CalculationSovComBank(models.Model):
    calculation_id = models.CharField(max_length=255)
    request = models.ForeignKey(ResponseCalculationSovComBank, related_name="calculations", on_delete=models.CASCADE)
    is_calculation_positive = models.BooleanField()
    comment = models.TextField(null=True, blank=True)


class CreditInfoSovComBank(models.Model):
    calculation = models.OneToOneField(CalculationSovComBank, related_name="credit_info", on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    period = models.IntegerField()
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    payment_no_subsidy = models.DecimalField(max_digits=10, decimal_places=2)
    credit_amount = models.DecimalField(max_digits=15, decimal_places=2)
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2)
    credit_rate = models.DecimalField(max_digits=5, decimal_places=2)


class DealCostSovComBank(models.Model):
    calculation = models.OneToOneField(CalculationSovComBank, related_name="deal_cost", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=10)


class InsuranceSovComBank(models.Model):
    calculation = models.ForeignKey(CalculationSovComBank, related_name="insurance_list", on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    period = models.IntegerField()
    agreement_percent = models.DecimalField(max_digits=5, decimal_places=3)
    cost_amount = models.DecimalField(max_digits=15, decimal_places=2)
    cost_currency = models.CharField(max_length=10)
    payment_type = models.CharField(max_length=255)
    company_type = models.CharField(max_length=255)
    insurer_id = models.CharField(max_length=255)
