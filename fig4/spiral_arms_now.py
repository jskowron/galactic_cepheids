#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *
import sys
from os.path import splitext

#  parameter units:    pc  deg
from parameters import R0, psi, arm_names
from functions import projectG

filename, _ = splitext(sys.argv[0]) # 'spiral_arms_now.out'
filename += '.out'

with open(filename, 'w') as outfile:
  # ------------------------------------
  # spiral arms NOW
  outfile.write('#     X         Y        R_GC      phi\n')
  outfile.write('#    kpc       kpc       kpc       deg\n')
  outfile.write('#\n')

  for i, phi0 in enumerate(arange(0, 360, 90) + 70):
    p = phi0 + linspace(0, 400.0, 60)
    R = R0 * exp(  (p - phi0) / 180.0 * pi * tan(psi / 180. * pi))
    x1, y1 = projectG(p, R)
    outfile.write('# arm %d  phi0 = %8.3f  %s\n'%(i, phi0, arm_names[i]))
    for row in c_[x1, y1, R * 0.001, p]:
      outfile.write('%9.4f %9.4f  %9.4f %9.4f\n'%tuple(row))

