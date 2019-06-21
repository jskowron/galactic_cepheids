#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *
import sys
from os.path import splitext

#  parameter units:    pc  deg
from parameters import R0, psi, arm_names, pattern_period
from functions import projectG

if len(sys.argv) <= 1:
  print('Provide time in Myrs (eg.: 0 - now, 100 - hundred million years earlier than now')
  sys.exit()

try:
  age_before = int(sys.argv[1])
except ValueError:
  print('Provide time in Myrs as integer')
  sys.exit()
  

pattern_rot = age_before * 360.0 / float(pattern_period)


filename, _ = splitext(sys.argv[0]) # 'spiral_arms_now.out'
filename += '_%d.out'%(age_before)

with open(filename, 'w') as outfile:
  # ------------------------------------
  # spiral arms NOW
  outfile.write('#     X         Y        R_GC      phi\n')
  outfile.write('#    kpc       kpc       kpc       deg\n')
  outfile.write('#\n')

  for i, phi0 in enumerate(arange(0, 360, 90) + 70 + pattern_rot):
    p = phi0 + linspace(0, 400.0, 60)
    R = R0 * exp(  (p - phi0) / 180.0 * pi * tan(psi / 180. * pi))
    x1, y1 = projectG(p, R)
    outfile.write('# arm %d  phi0 = %8.3f  %s\n'%(i, phi0, arm_names[i]))
    for row in c_[x1, y1, R * 0.001, p]:
      outfile.write('%9.4f %9.4f  %9.4f %9.4f\n'%tuple(row))

