import pandas as pd
import numpy as np

def leitura(caminho):
    data = pd.read_csv(caminho)
    return data 
