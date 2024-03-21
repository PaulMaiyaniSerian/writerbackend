from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            email = 'admin@gmail.com'
            password = 'admin'
            first_name = 'paul'
            last_name = 'serian'
            admin = User.objects.create_superuser(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
            admin.is_active = True
            # admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')