#!/usr/bin/env python3
"""Original illustration of the explicit counterexample to Ghys Fact 1's disk claim."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
import numpy as np

out = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(8.4, 3.3))
h = np.sqrt(3) / 2
ax.plot([0, 1], [0, 0], color='#165a8c', lw=5)
ax.add_patch(Polygon([[1, 0], [2, 0], [1.5, h]], facecolor='#e9c87c',
                     edgecolor='#8b5b05', alpha=.75, lw=2))
ax.plot([2, 3], [0, 0], color='#487b43', lw=5)
ax.add_patch(Circle((1.5, 0), .5, fill=False, ls='--', lw=1.7, edgecolor='#a12b3a'))
ax.text(1.5, h+.11, r'$K_2$: equilateral triangle, diameter $1$', ha='center', fontsize=11)
ax.text(.5, -.34, r'$K_1=[0,1]$', ha='center', color='#165a8c', fontsize=11)
ax.text(2.5, -.34, r'$K_3=[2,3]$', ha='center', color='#487b43', fontsize=11)
ax.text(1.5, -.67, 'Forced middle disk: center 1.5, radius 0.5', ha='center',
        color='#a12b3a', fontsize=11)
for x in [0, 1, 2, 3]:
    ax.plot(x, 0, 'o', ms=4, color='black')
    ax.text(x, -.13, str(x), ha='center', va='top', fontsize=11)
ax.annotate('', xy=(3, -.94), xytext=(0, -.94), arrowprops={'arrowstyle':'<->','color':'#444'})
ax.text(1.5, -1.08, r'$\operatorname{diam}(K_1\cup K_2\cup K_3)=3=1+1+1$',
        ha='center', fontsize=11)
ax.set(xlim=(-.22, 3.22), ylim=(-1.2, 1.25), aspect='equal')
ax.axis('off')
fig.tight_layout()
fig.savefig(out/'ghys-fact1-counterexample.png', dpi=180, bbox_inches='tight')
fig.savefig(out/'ghys-fact1-counterexample.svg', bbox_inches='tight')
plt.close(fig)
