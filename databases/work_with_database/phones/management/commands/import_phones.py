import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for row in phone_reader:
                # TODO: Добавьте сохранение модели
                slugn = row[1]
                slugn = slugn.lower().split()
                slugn = "-".join(slugn)
                p = Phone(id=row[0], model=row[1], image=row[2], price=row[3],
                          release_date=row[4], lte_exists=row[5], slug=slugn)
                p.save()

