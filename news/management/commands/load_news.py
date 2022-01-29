import json
import logging

from dateutil import parser
from django.core.management.base import BaseCommand

from news.models import Tag, Article, ArticleTagged
from tcrb.settings import BASE_DIR

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        tags = json.load(open(BASE_DIR / 'webscrap' / 'scrapped_news.json'))

        for key, tag in tags.items():

            print(f'Loading tag: {tag["name"]}')

            tag_db = Tag(
                name=tag['name'].split(' - ')[1],
                description=None if tag['description'] == '' else tag['description'],
                index=key,
                category=True if tag['category'] else False
            )

            tag_db.save()

            total_news = len(tag["news"])

            print(f'Loading {total_news} news')

            for i, article in enumerate(tag['news'], 1):

                print(f'\rLoading article {i}/{total_news}', end='')

                if not Article.objects.filter(guid=article['guid']).exists():
                    article_db = Article(
                        guid=article['guid'],
                        title=article['title'],
                        author=article['authors'][0]['name'],
                        link=article['link'],
                        pub_date=parser.parse(str(article['pub_date']))
                    )

                    article_db.save()

                else:
                    article_db = Article.objects.get(guid=article['guid'])

                ArticleTagged(
                    article=article_db,
                    tag=tag_db
                ).save()

            print('\n')
