import matplotlib.pyplot as plt

blood_sugar_men = [90, 85, 88, 92, 95, 100, 110, 105, 98, 102]
blood_sugar_women = [80, 82, 85, 88, 90, 92, 95, 97, 100, 105]

types = ['blood_sugar_men', 'blood_sugar_women']
colors = ['g', 'r']
lablel = ['Men', 'Women']
bins = [80, 85, 90, 95, 100, 105, 110]
plt.xlabel("Blood Sugar Level")
plt.ylabel("TOTAL Number of People")
# Diabetes Blood Sugar Level Distribution
#
#80 - 100 = normal
#100 - 125 = prediabetes
#126 and above = diabetes

plt.hist([blood_sugar_men, blood_sugar_women], bins=bins, width=0.95, color=colors, label=lablel, orientation='vertical')

plt.title("Diabetes Blood Sugar Level Distribution")
plt.legend()
plt.show()

