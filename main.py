import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Yu Gothic'

df = pd.read_excel("data.xlsx")

summary = df.describe()
summary.to_excel("summary.xlsx")

plt.figure(figsize=(8,5))
df["売上"].plot(kind="line")
plt.title("売上推移")
plt.savefig("graph.png")
