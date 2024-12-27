import io
import os

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account

def download_file(file_id, destination_folder, credentials_file):  # Added credentials_file
    """Downloads a file from Google Drive."""
    SCOPES = ['https://www.googleapis.com/auth/drive.file'] # Or ['https://www.googleapis.com/auth/drive'] for full drive access

    creds = service_account.Credentials.from_service_account_file(
        credentials_file, scopes=SCOPES)  # Use credentials_file here

    try:
        service = build('drive', 'v3', credentials=creds)

        request = service.files().get_media(fileId=file_id)
        file_metadata = service.files().get(fileId=file_id).execute()
        file_name = file_metadata.get('name')

        file_path = os.path.join(destination_folder, file_name)

        fh = io.FileIO(file_path, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))
        print(f"File saved to {file_path}")
        return file_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None