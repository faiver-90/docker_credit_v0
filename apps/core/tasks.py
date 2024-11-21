import os

import pandas as pd

from celery import shared_task
from dotenv import load_dotenv

from apps.core.models import OffersSovComBank

load_dotenv()


@shared_task
def parse_offers_file():
    file_path = os.getenv("SOVCOMBANK_FILE_NAME_PRODUCT")
    df = pd.read_excel(file_path)
    for _, row in df.iterrows():
        OffersSovComBank.objects.update_or_create(
            id_in_excel_file_sovcom=row['KOD'],
            defaults={
                'actual_sovcom': row['AKTUALNAJA'],
                'rating_sovcom': row['rating'],
            }
        )
