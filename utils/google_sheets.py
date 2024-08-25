import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def authenticate_google_sheets():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = {
        "type": os.getenv("KEY_TYPE"),
        "project_id": os.getenv("KEY_PROJECT_ID"),
        "private_key_id": os.getenv("KEY_PRIVATE_KEY_ID"),
        "private_key": os.getenv("KEY_PRIVATE_KEY").replace("\\n", "\n"),
        "client_email": os.getenv("KEY_CLIENT_EMAIL"),
        "client_id": os.getenv("KEY_CLIENT_ID"),
        "auth_uri": os.getenv("KEY_AUTH_URI"),
        "token_uri": os.getenv("KEY_TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("KEY_AUTH_PROVIDER_CERT_URL"),
        "client_x509_cert_url": os.getenv("KEY_CLIENT_CERT_URL")
    }

    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds, scope)
    client = gspread.authorize(creds)
    return client
