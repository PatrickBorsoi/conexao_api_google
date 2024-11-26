import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os

load_dotenv()

ARQ_JSON  = os.getenv('JSON')
TITLE  = os.getenv('NOME_DO_ARQUIVO')
FOLDER_ID  = os.getenv('ID_PASTA')

filename = f'{ARQ_JSON}'
scopes = [
    
    "https://spreadsheets.google.com/feeds", # google sheets
    "https://www.googleapis.com/auth/drive", # google drive
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    filename=filename,
    scopes=scopes
    ) # Credenciais

client = gspread.authorize(creds)
# print(client)

planilha_homolog = client.open(
    title=TITLE, 
    folder_id=FOLDER_ID
    ) # abrir o arquivo 'titulo = o nome do arquivo' 'folder_id = depois de folder/ copiar o id, na pasta onde esta o arquivo'

planilha = planilha_homolog.get_worksheet(0) # selecionando a aba da planilha

dados = planilha.get_all_records() # pegando os dados
pd.DataFrame(dados)