import pandas as pd

df = pd.read_excel("conditions (1) (1).xlsx")
df.to_csv("descriptionConditions.csv", index=False, encoding='utf-8-sig')