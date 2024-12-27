import os
from core import google_drive

if __name__ == "__main__":
    file_id = '1mSdPuDeVrwU-tsWN-ckECcileiIc3Bq7'  # Replace with your actual file ID
    destination_folder = '/Users/faridchaanane/Documents/DOWNLOADS_to_CLOUD/'  # Replace with the desired folder path
    credentials_file = 'credentials/google_drive_credentials.json' # Add credentials path
    os.makedirs(destination_folder, exist_ok=True) # Create the folder if it doesn't exist
    try:
        downloaded_file_path = google_drive.download_file(file_id, destination_folder, credentials_file) # Pass credentials

        if downloaded_file_path:
            print(f"File downloaded to: {downloaded_file_path}")
        else:
            print("Download failed. Check file ID and permissions.")

    except Exception as e:
        print(f"An error occurred during download: {e}")