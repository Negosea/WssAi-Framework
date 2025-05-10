import os
import io
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

# Defina o arquivo de credenciais e o ID do arquivo no Google Drive
CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Função para autenticar e retornar o serviço
def authenticate_drive():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    service = build(API_NAME, API_VERSION, credentials=creds)
    return service

# Função para baixar o arquivo
def download_file(service, file_id, download_path):
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(download_path, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")
    print(f"Arquivo {download_path} baixado com sucesso.")

def main():
    # Defina o ID do arquivo que você deseja baixar
    file_id = '1r7NTYaXwfQVxSgT77aWbZl9qLvJgpoN3'  # Substitua pelo ID do seu arquivo no Google Drive
    download_path = 'downloads/planta_forro_drywall.pdf'  # Caminho para salvar o arquivo

    # Crie a pasta de destino caso não exista
    os.makedirs(os.path.dirname(download_path), exist_ok=True)

    # Autenticação e download do arquivo
    service = authenticate_drive()
    download_file(service, file_id, download_path)

if __name__ == '__main__':
    main()


