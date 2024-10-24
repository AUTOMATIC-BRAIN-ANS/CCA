import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

csv_file_path = "C:\\Users\\48503\Desktop\PSH_patients_for_tests\correlations.csv"
data = pd.read_csv(csv_file_path, sep=';', index_col=0)
sns.set(font_scale=1.46)
plt.figure(figsize=(10, 8))
ax = sns.heatmap(data, annot=True, cmap='viridis')
ax.xaxis.set_label_position('top')
ax.xaxis.tick_top()
ax.xaxis.set_tick_params(length=0)
plt.tight_layout()
plt.savefig("likely_corr_vals.pdf", dpi=900)
plt.show()
plt.close()

unlik_csv_file_path = "C:\\Users\\48503\Desktop\PSH_patients_for_tests\\unlikely.csv"
unlik_data = pd.read_csv(unlik_csv_file_path, sep=';', index_col=0)
max_val = max(data.max().max(), unlik_data.max().max())



sns.set(font_scale=1.46)
plt.figure(figsize=(10, 8))
ax = sns.heatmap(unlik_data, annot=True, cmap='viridis', vmax=max_val)
ax.xaxis.set_label_position('top')
ax.xaxis.tick_top()
ax.xaxis.set_tick_params(length=0)
plt.tight_layout()
plt.savefig("unlikely_corr_vals.pdf", dpi=900)
plt.show()
plt.close()