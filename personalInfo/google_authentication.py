from google.auth.transport.requests import Request
from google.oauth2 import service_account

def get_google_access_token():
    try:
        # Load service account credentials from the file
        credentials = service_account.Credentials.from_service_account_file(
            'path/to/your/cufitnesss.json',  # Your service account credentials file
            scopes=['https://www.googleapis.com/auth/cloud-platform']  # Required scopes
        )

        # Refresh the token if it's expired
        if credentials.expired:
            credentials.refresh(Request())

        return credentials.token  # Return the access token

    except Exception as e:
        print(f"Error obtaining access token: {e}")
        return None
