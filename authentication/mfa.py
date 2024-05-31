from django.utils import timezone
from datetime import timedelta
from .models import MFAToken
import random


def send_mfa_token(user):
    token = str(random.randint(100000, 999999))
    expires_at = timezone.now() + timedelta(minutes=5)
    MFAToken.objects.create(user=user, token=token, token_type="email", expires_at=expires_at)
    # Implement email sending logic here


def verify_mfa_token(user, token):
    try:
        mfa_token = MFAToken.objects.get(user=user, token=token, is_verified=False, expires_at__gt=timezone.now())
        mfa_token.is_verified = True
        mfa_token.save()
        return True
    except MFAToken.DoesNotExist:
        return False
