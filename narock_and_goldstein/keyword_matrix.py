import math
import numpy as np
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt

arxives = ["EartharXiv", "EngrXiv", "LawarXiv", "LISSA", "MarXiv", "MindrXiv", "PaleorXiv", "PsyarXiv", "SocarXiv"]

x = np.nan

# total papers at each arxiv - used to normalize plot
eartharxiv = 567
lissa = 139
mindrxiv = 121
engrxiv = 362
lawarxiv = 905
marxiv = 324
paleorxiv = 112
psyarxiv = 3540
socarxiv = 3034 

data = np.array( [
  [x, math.log10(17), math.log10(9), math.log10(2), math.log10(14), math.log10(0.1), math.log10(2), math.log10(3),  math.log10(15)],
  [x,  x, math.log10(0.1), math.log10(0.1),  math.log10(0.1), math.log10(0.1), math.log10(0.1), math.log10(0.1),   math.log10(0.1)],
  [x,  x, x, math.log10(7),  math.log10(5), math.log10(0.1), math.log10(0.1), math.log10(6), math.log10(152)],
  [x,  x, x, x,  math.log10(1), math.log10(0.1), math.log10(0.1), math.log10(1),   math.log10(8)],
  [x,  x, x, x,  x, math.log10(0.1), math.log10(0.1), math.log10(2),   math.log10(7)], 
  [x,  x, x, x,  x, x, math.log10(0.1), math.log10(0.1),   math.log10(0.1)], 
  [x,  x, x, x,  x, x, x, math.log10(0.1),   math.log10(0.1)], 
  [x,  x, x, x,  x, x, x, x,  math.log10(23)], 
  ])


fig, ax = plt.subplots(figsize=(10, 7))
im = ax.imshow(data, cmap=cm.get_cmap('Greys'))
fig.colorbar(im)

# set up x and y axis
ax.set_xticks(np.arange(len(arxives)))
ax.set_yticks(np.arange(len(arxives)))

# ... and label them 
ax.set_xticklabels(arxives)
ax.set_yticklabels(arxives)

ax.set_title("Keywords in Common (Log Scale)")
fig.tight_layout()
#ax.grid()
plt.show()