#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from os.path import splitext
import generate

simulation_age = 175.0
simulation_data = [( 3, 300, 55, 300), ( 0, 270, 50, 200)]  # (arm_number,  phi_center, phi_span, n_stars)

filename, _ = splitext(argv[0]) # 'generate_175Myr.out'
filename += '.out'

generate.generate(simulation_age, simulation_data, filename)
