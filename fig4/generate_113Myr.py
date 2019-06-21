#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
from os.path import splitext
import generate

simulation_age = 113.0
simulation_data = [( 1, 210, 50, 500), ( 0, 260, 5, 70)]  # (arm_number,  phi_center, phi_span, n_stars)

filename, _ = splitext(argv[0]) # 'generate_113Myr.out'
filename += '.out'

generate.generate(simulation_age, simulation_data, filename)
