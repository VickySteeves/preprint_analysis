import math
import numpy as np
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt

arxives = ["EartharXiv", "EngrXiv", "LawarXiv", "LISSA", "MarXiv", "MindrXiv", "PaleorXiv", "PsyarXiv", "SocarXiv"]

x = np.nan

data = np.array( [
  [x, 0.1, 0.02, 0.1, 0.22, 0.15, 0.03, 0.03,  0.05], # eartharxiv
  [x,  x, 0, 0,  0, 0, 0, 0, 0], #engrxiv
  [x,  x, x, 0.35, 0.15, 0.23, 0, 0.03, 0.27], # lawarxiv
  [x,  x, x, x,  0.33, 0.19, 0, 0.33, 0.65], # LISSA
  [x,  x, x, x,  x, 0.19, 0, 0.38, 0.44], # marxiv
  [x,  x, x, x,  x, x, 0, 0.3, 0.53], # mindarxiv
  [x,  x, x, x,  x, x, x, 0, 0], # paleorxiv
  [x,  x, x, x,  x, x, x, x, 0.22], # psyarxiv
  ])


fig, ax = plt.subplots(figsize=(10, 7))
im = ax.imshow(data, cmap=cm.get_cmap('Reds'))
fig.colorbar(im)

# set up x and y axis
ax.set_xticks(np.arange(len(arxives)))
ax.set_yticks(np.arange(len(arxives)))

# ... and label them 
ax.set_xticklabels(arxives)
ax.set_yticklabels(arxives)

ax.set_title("Keywords in Common")
fig.tight_layout()
#ax.grid()
plt.show()