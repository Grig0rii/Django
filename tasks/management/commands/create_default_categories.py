from django.core.management.base import BaseCommand
from tasks.models import Category

class Command(BaseCommand):
    help = 'Creates default categories for tasks'

    def handle(self, *args, **kwargs):
        Category.create_default_categories()
        self.stdout.write(self.style.SUCCESS('Successfully created default categories')) 