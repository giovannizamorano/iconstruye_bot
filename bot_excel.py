from pandasai import SmartDataframe
import pandas as pd
from pandasai.llm import OpenAI
import requests

na_values=[""]

df = pd.read_csv('iconstruye-todas-las-solicitudes-view-2024-01-15-1022.csv', delimiter=',', na_values=na_values)

llm = OpenAI(api_token='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')

sdf = SmartDataframe(df, config={'llm':llm})

while True:
    consulta = input("Consulta: ")

    if consulta == "!salir":
        break

    respuesta=sdf.chat(f"español:{consulta}")
    print(respuesta)