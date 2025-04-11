import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

def create_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='Grigorii',
            email='shunin.grigorii@mail.ru',
            password='20094908'
        )
        print('Суперпользователь создан успешно')
    else:
        print('Суперпользователь уже существует')

if __name__ == '__main__':
    create_superuser() 