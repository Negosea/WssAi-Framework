from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

# Função para fazer o download dos arquivos
def download_files_from_drive(folder_id, download_path):
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    
    # Autenticação
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Salva as credenciais para o futuro
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    # Construa o serviço do Google Drive
    service = build('drive', 'v3', credentials=creds)

    # Lista os arquivos na pasta específica do Google Drive
    results = service.files().list(q=f"'{folder_id}' in parents", fields="files(id, name)").execute()
    files = results.get('files', [])

    if not files:
        print('Nenhum arquivo encontrado.')
    else:
        for file in files:
            print(f'Downloading file: {file["name"]}')
            request = service.files().get_media(fileId=file['id'])
            file_path = os.path.join(download_path, file['name'])
            with open(file_path, 'wb') as f:
                request.execute()

# Id da pasta do Google Drive que você quer baixar
folder_id = '1r7NTYaXwfQVxSgT77aWbZl9qLvJgpoN3'
download_path = './downloads'  # Caminho onde você deseja salvar os arquivos

# Faz o download
download_files_from_drive(folder_id, download_path)
