import os 
import pandas as pd 
from dotenv import load_dotenv

load_dotenv()

pasta = os.getenv('pasta_fatura')

for arquivo in os.listdir(pasta):
    if arquivo.endswith('.csv'):
        caminho_arquivo = os.path.join(pasta, arquivo)
        print(f"Lendo o arquivo: {caminho_arquivo}")

        df = pd.read_csv(caminho_arquivo)

        