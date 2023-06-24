from BA_reviews import reviews_neg, reviews
import matplotlib.pyplot as plt
import numpy as np

x=[len(reviews),len(reviews_neg)]
status=['Verified','Not Verified']
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d})"
wedges, texts, autotexts = ax.pie(x, autopct=lambda pct: func(pct, x),textprops=dict(color="w"))

ax.legend(wedges, status,
          title="Trip Status",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Britis Airways: Trip Status")
plt.show()

