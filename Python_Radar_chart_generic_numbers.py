# -*- coding: utf-8 -*-
"""
Created on 13 May 2023

@author: dcrem
"""
import numpy as np
import matplotlib.pyplot as plt

# matplotlib 1.5.3
class Radar(object):
    def __init__(self, fig, titles, labels, rotation=0, rect=None):
        if rect is None:
            rect = [0.05, 0.05, 0.95, 0.95]

        self.n      = len(titles)                                                # Number of lines in the graph
        self.a0     = 90-360/len(titles)                                         # Starting angle of the graph
        self.angles = np.arange(self.a0, 360+self.a0, 360.0/self.n)              # Angles between each line in the graph
        self.axes = [fig.add_axes(rect, projection="polar", label="axes%d" % i)  # Create axes with right angular distance
                         for i in range(self.n)]

        self.ax = self.axes[0]
        self.ax.set_thetagrids(self.angles, labels=titles, fontsize=14)          # Titles of the variables

        for ax in self.axes[1:]:
            ax.patch.set_visible(False)
            ax.grid("off")
            ax.xaxis.set_visible(False)

        for ax, angle, label in zip(self.axes, self.angles, labels):
            ax.set_rgrids(range(1,n_ring+1), angle=angle, labels=label)
            ax.spines["polar"].set_visible(False)                                # Make external circle of the radar chart invisible
            ax.set_ylim(0, n_ring+1)
            ax.set_theta_offset(np.deg2rad(rotation))

    def plot(self, values, *args, **kw):
        angle = np.deg2rad(np.r_[self.angles, self.angles[0]])
        values = np.r_[values, values[0]]
        self.ax.plot(angle, values, *args, **kw)
        
fig  = plt.figure(figsize=(6, 6))
fig2 = plt.figure(figsize=(6, 6))

# Change the titles to have the radar plots variables:
titles = ["OCV", "$i_d$", "RTE", "$c_{m}$", "$c_a$"]
#
# Values of the variables in y-axes:
n_ring = 5                                                                       # Number of concentric rings in the graph
#
xmin   = [ 0,  10, 1.5, 3.5, -1]
xmax   = [10, 100, 1.1, 9.5, -5]
#
V_OCV  = np.linspace(xmin[0], xmax[0], n_ring)
V_id   = np.linspace(xmin[1], xmax[1], n_ring)
V_RTE  = np.linspace(xmin[2], xmax[2], n_ring)
V_cm   = np.linspace(xmin[3], xmax[3], n_ring)
V_ca   = np.linspace(xmin[4], xmax[4], n_ring)
#
V_OCV = ["{:.0f}".format(x) for x in V_OCV]                                      # Define number of positions after decimal point
V_id  = ["{:.0f}".format(x) for x in V_id]
V_RTE = ["{:.1f}".format(x) for x in V_RTE]
V_cm  = ["{:.2f}".format(x) for x in V_cm]
V_ca  = ["{:.0f}".format(x) for x in V_ca]
#
labels = [
    V_OCV,
    V_id,
    V_RTE,
    V_cm,
    V_ca
]
#
x_I    = [5,  77, 1.2, 6.53, -2.7]  # I
x_II   = [0,  90, 1.1, 9.05, -1.0]  # II
x_III  = [9,  30, 1.4, 5-00, -4.0]  # III
#
Y = np.zeros(len(titles))
Z = np.zeros(len(titles))
P = np.zeros(len(titles))
#
for i in range(len(titles)):
    Y[i]   = (x_I[i]-xmin[i])/(xmax[i]-xmin[i])*(n_ring-1)+1
    Z[i]   = (x_II[i]-xmin[i])/(xmax[i]-xmin[i])*(n_ring-1)+1
    P[i]   = (x_III[i]-xmin[i])/(xmax[i]-xmin[i])*(n_ring-1)+1
#
radar = Radar(fig, titles, labels)
radar.plot(Y,"-", lw=2, color="b", alpha=0.4, label="I")
radar.plot(Z,"-", lw=2, color="r", alpha=0.4, label="II")
radar.plot(P,"-", lw=2, color="g", alpha=0.4, label="III")
radar.ax.legend()
#
# fig.savefig("my_radar_plot.png", dpi=600, bbox_inches='tight',transparent=True) # Saving the figure
#