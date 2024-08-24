import qrcode
from django.conf import settings
from django.core.files.base import ContentFile
from io import BytesIO

def is_user_artist(user):
    return user.groups.filter(name='Actor').exists()


def create_artist_profile_and_qr(user):
    if is_user_artist(user):
        artist_url = f"{settings.SITE_URL}/artist/{user.username}/"
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(artist_url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        qr_code_image = ContentFile(buffer.getvalue())

        # Сохранение QR-кода в профиль пользователя или в отдельную модель
        user.profile.qr_code.save(f"{user.username}_qr.png", qr_code_image)
        user.profile.save()
