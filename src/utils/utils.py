""" Fontional"""

import pandas  as pd
import openai
import random
import os
import csv

from config import (CSV_PATH , TXT_PATH)

class Fonctional():
    def __init__(self) -> None:
        pass

    def load_csv(self , config):
        "This function load the csv file using Pandas library"
        raw = pd.read_csv(filepath_or_buffer=config.CSV_PATH , sep=',')
        return raw

    def csv2text(self , config):
        raw = self.load_csv(config)

        combined_values = ""
        for idx , item in raw.iterrows():
            row_values = "".join(str(val) for val in item.values)
            combined_values = combined_values + row_values + "\n"

        with open(config.TXT_PATH , mode="w", encoding="utf-8") as f:
            f.write(combined_values)

    @staticmethod
    def generate_response(prompt, model , temperature):
        # Define function to generate response
        response = openai.ChatCompletion.create(
            model=model,
            messages=prompt,
            temperature = temperature
        )

        return response

    def ChatGptAPi(self , config , content , temperature = 0):
        # Set OpenAI API key
        openai.api_key = config.API_KEY

        # Set up the OpenAI model
        model_engine = "gpt-3.5-turbo"
        model_prompt = [{"role" : "system" ,"content" : f"{content}"
                        }] # Change the question prompt as needed

        # Generate response using the defined function
        response = self.generate_response(model_prompt, model_engine, temperature)

        # return the response
        return response['choices'][0]['message']['content']

    def text2csv(self , config):

        prompt = ""
        text = self.ChatGptAPi(prompt , temperature= random.random() * 0.9 + 0.1)
        # Ouverture du fichier en mode 'append' pour ajouter de nouvelles lignes
        with open(config.OUTPUT_PATH, mode='a', newline='') as file:
            # Définition des colonnes dans un objet DictWriter
            writer = csv.DictWriter(file, fieldnames=["idx","disease","Symptom","reason","TestsAndProcedures","commonMedications"])

            # Écriture de l'en-tête
            writer.writeheader()

        # Ouverture du fichier en mode 'append' pour ajouter de nouvelles lignes
        with open(config.OUTPUT_PATH, mode='a', newline='') as file1:
            writer1 = csv.writer(file1)
            # Écriture d'une nouvelle ligne dans le fichier CSV
            writer1.writerow(row)