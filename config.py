from python-dotenv import load_dotenv
import os
load_dotenv("./env/.env")

CSV_PATH = "./data/raw/format_dataset.csv"
TXT_PATH = "./data/processed/format_dataset.txt"
OUTPUT_PATH = "./data/final/"
API_KEY = os.getenv("API_KEY")

