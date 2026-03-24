import numpy as np
import matplotlib.pyplot as plt

N = 5
scores = (20, 35, 30, 35, 27)

ind = np.arange(N)  # the x locations for the groups
width = 0.35        # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, scores, width, yerr=Std)
plt.ylabel('Scores')
plt.title('Scores by group')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))

plt.show()