from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Create the default superuser (rsb / 12345678) if it does not exist."

    def handle(self, *args, **options):
        User = get_user_model()
        username = "rsb"
        email = "sergej.s001234@ya.ru"
        password = "12345678"
        if not User.objects.filter(username=username).exists():
            u = User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created."))
        else:
            self.stdout.write(self.style.WARNING(f"Superuser '{username}' already exists."))
