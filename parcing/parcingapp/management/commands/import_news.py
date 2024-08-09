import json

from django.core.management.base import  BaseCommand
from ...models import News

class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            with open('../data.json', 'r', encoding='utf-8') as file:
                data = json.load(file)

            for item in data:
                News.objects.create(
                    title=item['title'],
                    link=item['link'],
                    visibility=item['visibility'],
                    date=item['date']
                )
                if not data:
                    print('Error')

        except Exception as e:
            print(e)




