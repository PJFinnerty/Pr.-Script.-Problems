# IPython log file

get_ipython().run_line_magic('logstart', '')
import pandas as pd
pd.read_csv("http://www.biostat.jhsph.edu/~rpeng/useRbook/faithful.csv")
df["eruptions"]
df["eruptions"]
df = pd.read_csv("http://www.biostat.jhsph.edu/~rpeng/useRbook/faithful.csv")
df["eruptions"]
df["eruptions"]
df
df["waiting"]
import matplotlib.pyplot as plt
plt.plot(df["eruptions"], df["waiting"])
plt.plot(df["eruptions"], df["waiting"], 'b.')
plt.title("Eruptions VS Waiting")
plt.savefig("scatter.png")
plt.clf()
plt.hist(df["Eruptions"])
plt.savefig("Eruptions.png")
plt.clf
()
plt.hist(df["Waiting"])
plt.savefig("Waiting.png")
exit()
