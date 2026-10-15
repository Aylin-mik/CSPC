import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("heart.csv")
print("shape: ", df.shape)
print("head: ", df.head())
continuous = df[["age", "chol", "trestbps", "thalach"]]
print("statistics: ", df.describe())

fig, axes = plt.subplots(2,2,figsize=(12,8))
axes[0, 0].hist(df["age"], bins = 15, edgecolor ="black")
axes[0, 0].set_title("Distribution of age")
axes[0, 0].set_xlabel("age")
axes[0, 0].set_ylabel("frequency")

axes[0, 1].hist(df["chol"], bins = 15, edgecolor ="black")
axes[0, 1].set_title("Distribution of chol")
axes[0, 1].set_xlabel("chol")
axes[0, 1].set_ylabel("frequency")

axes[1, 0].hist(df["trestbps"], bins = 15, edgecolor ="black")
axes[1, 0].set_title("Distribution of trestbps")
axes[1, 0].set_xlabel("trestbps")
axes[1, 0].set_ylabel("frequency")

axes[1, 1].hist(df["thalach"], bins = 15, edgecolor ="black")
axes[1, 1].set_title("Distribution of thalach")
axes[1, 1].set_xlabel("thalach")
axes[1, 1].set_ylabel("frequency")

plt.tight_layout()
plt.savefig("plots/distribution.png", dpi=150)

fig2, axes2 = plt.subplots(2,2, figsize=(12, 8))
stats.probplot(df["age"], dist = "norm", plot=axes2[0, 0])
axes2[0, 0].set_title("Q-Q plot of age")

stats.probplot(df["chol"], dist = "norm", plot=axes2[0, 1])
axes2[0, 1].set_title("Q-Q plot of chol")

stats.probplot(df["trestbps"], dist = "norm", plot = axes2[1, 0])
axes2[1, 0].set_title("Q-Q plot of trestbps")

stats.probplot(df["thalach"], dist = "norm", plot = axes2[1, 1])
axes2[1, 1].set_title("Q-Q plot of thalach")

plt.tight_layout()
plt.savefig("plots/Q-Q.png", dpi=150)

disease = df[df["target"] == 1]["thalach"]
healthy = df[df["target"] == 0]["thalach"]
stat_disease, p_disease = stats.shapiro(disease)
stat_healthy, p_healthy = stats.shapiro(healthy)
print("")
print("Shapiro-Wilk normality test:")
print(f"Disease group: stat_disease = {stat_disease:.4f}, p = {p_disease:.6g}")
print(f"Healthy group: stat_healthy = {stat_healthy:.4f}, p = {p_healthy:.6g}")

#Mann-Whitney U test
u_stat, p_value = stats.mannwhitneyu(disease, healthy, alternative="two-sided")
print("")
print("Mann-Whitney U test:")
print(f"U statistic = {u_stat:.3f}")
print(f"p value = {p_value:.6g}")
if p_value < 0.05:
    print("Reject H0: there is a statistically significant difference.")
else:
    print("Fail to reject H0: insufficient evidence of difference.")

def mean_ci(data):
    n = len(data)
    mean = data.mean()
    se = stats.sem(data)
    margin = stats.t.ppf(0.975,df=n-1) * se
    return mean, mean - margin, mean + margin

for name, group in [("Disease", disease), ("Healthy", healthy)]:
    mean, low, high = mean_ci(group)
    print(f"{name}: mean = {mean:.2f}, "f"95% CI = [{low:.2f}, {high:.2f}]")

groups = [disease, healthy]
labels = ["Disease", "Healthy"]
means = [disease.mean(), healthy.mean()]
errors = [stats.t.ppf(0.975, len(g)-1) * stats.sem(g) for g in groups]
plt.figure(figsize = (7, 5))
plt.errorbar(labels, means, yerr=errors, fmt ="o", capsize= 6)
plt.ylabel("maximum heart rate (thalach)")
plt.title(f"Mean maximum heart rate with 95% CI")
plt.tight_layout()
plt.savefig("plots/thalach_comparison.png", dpi = 150)

age = df["age"]
thalach = df["thalach"]
r, p_value= stats.pearsonr(age, thalach)
print("")
print("Correlation between age and maximum heart rate")
print(f"Pearson correlation coefficient = {r:.4f}")
print(f"p_value = {p_value:.6g}")

plt.figure(figsize=(7, 5))
plt.scatter(age, thalach, alpha= 0.7)
plt.xlabel("Age (years)")
plt. ylabel("Maximum heart rate (thalach)")
plt.title("Age vs maximum heart rate")
plt.tight_layout()
plt.savefig("plots/age_thalach_correlation.png", dpi=150)

chemical_data= pd.read_csv("chemicals_cancer.csv")
print("")
print("Chemical dataset shape:")
print(chemical_data.shape)
print("")
print("First five rows")
print(chemical_data.head())
print("")
print("Column name:")
print(chemical_data.columns.tolist())

benzene_r, benzene_p = stats.pearsonr(chemical_data["benzene"], chemical_data["malignancy"])
cadmium_r, cadmium_p = stats.pearsonr(chemical_data["cadmium"], chemical_data["malignancy"])
print("")
print("Naive chemical associations:")
print(f"Benzene_r = {benzene_r:.4f}, benzene_p = {benzene_p:.6g}")
print(f"cadmium_r = {cadmium_r:.4f}, cadmium_p = {cadmium_p:.6g}")

pollution = chemical_data[(chemical_data["pollution_index"]>=40)&(chemical_data["pollution_index"]<=60)]
print("")
print("Patirnts with pollution index 40-60:")
print(len(pollution))
benz_r_retsr, benz_p_restr = stats.pearsonr(pollution["benzene"], pollution["malignancy"])
cadm_r_restr, cadm_p_restr = stats.pearsonr(pollution["cadmium"], pollution["malignancy"])
print("")
print("associations within the restricted groups:")
print(f"benzene_r(restricted) = {benz_r_retsr:.4f}, benzene_p(restricted) = {benz_p_restr:.6g}")
print(f"Cadmium_r(restricted) = {cadm_r_restr:.4f}, cadmium_p(restricted) = {cadm_p_restr:.6g}")
print(chemical_data["pollution_index"].describe())

#BONUS
proportions = df["target"].value_counts(normalize=True)
entropy = -(proportions * np.log2(proportions)).sum()
print("Proportions")
print(proportions)
print(f"entropy :{entropy:.4f} bits")