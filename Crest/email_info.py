import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from django.conf import settings

def send_brevo_email(subject, html_content, to_emails, text_content=""):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )

    sender = {"email": "fintexgroundtrade@gmail.com", "name": "Fintex Ground Trade"}
    to_list = [{"email": email} for email in to_emails]

    email = sib_api_v3_sdk.SendSmtpEmail(
        to=to_list,
        sender=sender,
        subject=subject,
        html_content=html_content,
        text_content=text_content or html_content,
    )

    try:
        response = api_instance.send_transac_email(email)
        return response
    except ApiException as e:
        print(f"❌ Brevo API exception: {e}")
        return None