from twilio.rest import Client
from django.conf import settings


class SmsService:
    def __init__(self, service_id):
        self.client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        self.service_id = service_id
    def send_otp(self, mobile_number):
        verification = self.client.verify.services(self.service_id).verifications.create(
            to=mobile_number, channel='sms')
        if verification.status == 'pending':
            return True
        else:
            return False
    def verify_otp(self, mobile_number, otp):
        verification = self.client.verify.services(self.service_id).verification_checks.create(
            to=mobile_number, code=otp)
        if verification.status == 'approved':
            return True
        else:
            return False
