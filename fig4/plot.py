#!/usr/bin/env python3

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from numpy import *
from collections import defaultdict
from parameters import arm_names
import plot_parameters # arm_names_abr, arm_colors, arm_symbol, arm_symbol_size, axis_view


# Uses:
#   spiral_arms_now.out
#   spiral_arms_earlier_64.out
#   spiral_arms_earlier_113.out
#   spiral_arms_earlier_175.out
#   generate_64Myr.out
#   generate_113Myr.out
#   generate_175Myr.out
#   generate_64Myr_evolved.out
#   generate_113Myr_evolved.out
#   generate_175Myr_evolved.out
# to generate run: ./do 

def loadarms(filename):
  try:
    f = open(filename, 'r')
  except IOError:
    print('Error opening file: %s'%filename)
    sys.exit()

  arms = defaultdict(list)
  arm_id = 0
  for line in f:
    if len(line) <= 0: continue
    l = line.strip()
    if len(l) <= 0: continue
    row = l.split()
    if l[0] == '#':
      if len(row) > 2 and row[1] == 'arm':
        try:
          arm_id = int(row[2])
          arm_id = arm_id % 4
        except ValueError:
          print('Arm ID should be an integer, e.g: "# arm 1".\nIn line: %s'%line)
          sys.exit()
      continue # other comment
    if len(row) >= 2:
      X, Y = float(row[0]), float(row[1])
      #print(X, Y, row)
      arms[arm_id].append([X, Y])

  f.close()
  return arms

fig, ax = plt.subplots(len(plot_parameters.simulation_ages), 2, figsize=plot_parameters.figsize)
arms_now = loadarms('spiral_arms_now.out')
for row, age in enumerate(plot_parameters.simulation_ages):
  arms = loadarms('spiral_arms_earlier_%d.out'%(age))

  for i in arms: # Galaxy "age" Myrs ago
    arm_name = arm_names[i]
    X, Y = array(arms[i]).T
    ax[row, 0].plot(Y, X, '-', color=plot_parameters.arm_colors[i], alpha=plot_parameters.arm_alpha)
    Xend, Yend = X[-1], Y[-1]
    marker, color, size = plot_parameters.arm_symbol[i], plot_parameters.arm_colors[i], plot_parameters.arm_symbol_size[i] * 0.6
    try:
      ax[row, 0].plot([Yend], [Xend], ms=size, color=color, marker=marker, mec=color)
    except ValueError:
      ax[row, 0].plot([Yend], [Xend], ms=size, color=color, marker='x', mec=color, mew=2.5)
      

  for i in arms_now: # Galaxy NOW
    arm_name = arm_names[i]
    X, Y = array(arms_now[i]).T
    ax[row, 1].plot(Y, X, '-', color=plot_parameters.arm_colors[i], alpha=plot_parameters.arm_alpha)
    Xend, Yend = X[-1], Y[-1]
    marker, color, size = plot_parameters.arm_symbol[i], plot_parameters.arm_colors[i], plot_parameters.arm_symbol_size[i] * 0.6
    try:
      ax[row, 1].plot([Yend], [Xend], ms=size, color=color, marker=marker, mec=color)
    except ValueError:
      ax[row, 1].plot([Yend], [Xend], ms=size, color=color, marker='x', mec=color, mew=2.5)

  pos_at_birth = loadtxt('generate_%dMyr.out'%(age), usecols=(0,1))
  pos_now = loadtxt('generate_%dMyr_evolved.out'%(age), usecols=(0,1))

  ax[row, 0].scatter(pos_at_birth.T[1], pos_at_birth.T[0], c=plot_parameters.simulation_colors[row], **plot_parameters.star_marker_params)
  ax[row, 1].scatter(pos_now.T[1],      pos_now.T[0],      c=plot_parameters.simulation_colors[row], **plot_parameters.star_marker_params)

  for col in [0, 1]:
    ax[row, col].set_xlim(*plot_parameters.axis_view[:2])
    ax[row, col].set_ylim(*plot_parameters.axis_view[2:])
    if row == len(plot_parameters.simulation_ages) - 1: 
      ax[row, col].set_xlabel('Y [kpc]')
  ax[row, 0].set_ylabel('X [kpc]')

plt.savefig('plot.png')

