#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from os.path import splitext
import generate

simulation_age = 64.0
simulation_data = [( 3, 210-2*70, 62, 100), ( 2, 210-70, 44, 100), ( 1, 210, 44, 100)]  # (arm_number,  phi_center, phi_span, n_stars)

filename, _ = splitext(sys.argv[0]) # 'generate_64Myr.out'
filename += '.out'

generate.generate(simulation_age, simulation_data, filename)
