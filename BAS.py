import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Generate age data for 100 adults
age_group1 = np.random.randint(low=18, high=37, size=100)
age_group2 = np.random.randint(low=27, high=55, size=100)

# Calculate the mean of the groups
ag1_mean = np.mean(age_group1)
ag2_mean = np.mean(age_group2)

# Calculate the median of the groups
ag1_med = np.median(age_group1)
ag2_med = np.median(age_group2)

# Calculate the standard deviation of the groups
ag1_sd = np.std(age_group1)
ag2_sd = np.std(age_group2)

# Create a dataframe from the age data
df = pd.DataFrame({
    "G 1": age_group1,
    "G 2": age_group2
})

# Create a box plot using seaborn
plt.figure(figsize=(12, 5))
sns.boxplot(data=df, orient="v", palette="Set2", saturation=0.75)

# Add a title for the plot
plt.title("Side-by-Side Box Plot and Histogram", fontsize = 20)

# Increase plot size
plt.gcf().set_size_inches(9,6)

# Histogram
plt.hist(age_group1, bins=20, color='blue', alpha=0.5, label='Age Group 1')
plt.hist(age_group2, bins=20, color='red', alpha=0.5, label='Age Group 2')

# Histogram labels
plt.xlabel('Age', fontsize=15)
plt.ylabel('Counts', fontsize=15)
plt.legend(fontsize=15)

# T-Test and P Value tests
t_stat, p_value = ttest_ind(age_group1, age_group2)

# Round the t-statistic and p-value to 4 digits after the period
t_statistic_rounded = round(t_stat, 4)
p_value_rounded = round(p_value, 4)

print('The first group:', age_group1)
print('The mean of the group is:', ag1_mean)
print('The median of the group is:', ag1_med)
print('The standard deviation of the group is:', ag1_sd)
print()
print('The second group:', age_group2)
print('The mean of the group is:', ag2_mean)
print('The median of the group is:', ag2_med)
print('The standard deviation of the group is:', ag2_sd)
print()

print("T-statistic: {:.4f}".format(t_statistic_rounded))
print("P-value: {:.4f}".format(p_value_rounded))
# Show the plot
plt.show()
