import pandas as pd
import numpy as np
import os as os

def main():
    df = pd.read_csv('../dados/brutos/heart.csv')
    print(df.describe())
main()