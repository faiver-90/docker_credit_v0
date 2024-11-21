# myapp/management/commands/parse_offers.py

from django.core.management.base import BaseCommand
import pandas as pd

from apps.core.models import OffersSovComBank


class Command(BaseCommand):
    help = 'Parse offers file and update the database'

    def handle(self, *args, **kwargs):
        file_path = 'apps/core/banking_services/sovcombank/Кредитные_программы_СКБ_и_их_коды_17_10_2024.xlsx'
        df = pd.read_excel(file_path)
        for _, row in df.iterrows():
            OffersSovComBank.objects.update_or_create(
                id_in_excel_file_sovcom=row['KOD'],
                defaults={
                    'actual_sovcom': row['AKTUALNAJA'],
                    'rating_sovcom': row['rating'],
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully parsed and updated offers'))
