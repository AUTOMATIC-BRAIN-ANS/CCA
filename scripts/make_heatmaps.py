import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

csv_file_path = "C:\\Users\\48503\Desktop\PSH_patients_for_tests\correlations.csv"
data = pd.read_csv(csv_file_path, sep=';', index_col=0)
sns.set(font_scale=1.3)
plt.figure(figsize=(10, 8))
sns.heatmap(data, annot=True, cmap='viridis')
plt.show()
