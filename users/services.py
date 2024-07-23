from django.contrib.auth import get_user_model

User = get_user_model()


def create_look_user(user_data):
    user = User.objects.create_user(
        username=user_data.get('email'),
        email=user_data.get('email'),
        phone=user_data.get('phone'),
        password=user_data.get('password1'),
    )

    return user
