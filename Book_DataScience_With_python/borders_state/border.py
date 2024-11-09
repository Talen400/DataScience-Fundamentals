import json
import matplotlib.pyplot as plt
import pandas as pd

arquivo = r'borders_state\gadm41_BRA_1.json'

with open(arquivo, 'r') as file:
    serial = json.load(file)

df = pd.json_normalize(serial)
df.head()