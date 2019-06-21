#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *

#  parameter units:         Myr        pc  deg   pc        km/s         km/s           pc          km/s
from parameters import pattern_period, R0, psi, GC_dist, vel_dist_r, vel_dist_phi, arm_r_sigma, rot_curve, arm_names
from functions import projectG, rotate, gal_centric

# ---------------------------------
simulation_seed = 423432
random.seed( simulation_seed )

def generate(simulation_age, simulation_data, filename):
  pattern_rot = simulation_age * 360.0 / float(pattern_period)

  # ------------------------------
  # model
  with open(filename, 'w') as outfile:
    outfile.write('# %.2f Myrs before\n'%(simulation_age))
    outfile.write('#  X_start   Y_start   R_start phi_start        X_now     Y_now      R_now   phi_now     pecu_vel_r peru_vel_phi\n')
    outfile.write('#   kpc        kpc       kpc     deg             kpc        kpc       kpc     deg            km/s      km/s\n')
    outfile.write('#\n')
    for arm, phi_offset, dphi, ni in simulation_data:
      # spiral arm position at earlier time (i.e., simulation_age before) 
      phi0 = 90 * arm + 70 + pattern_rot   
      outfile.write('# arm %d  phi0 = %8.3f  nstars = %4d  angle_offset = %8.3f  angle_span = %8.3f  %s\n'%(arm, phi0, ni, phi_offset, dphi, arm_names[arm]))
      # here we randomly choose ni stars along the spiral arm, with spread: dphi
      phi_init = phi0 + phi_offset  + (random.rand(ni)) * dphi
      # we randomly widen the spiral arm a little (with sigma: arm_r_sigma)
      distG_init = R0 * exp( (phi_init - phi0) /180.0 * pi * tan(psi/180.*pi)) + random.normal(0.0, arm_r_sigma, ni)
      # we assign each star a pecular velocity in concordance with 
      # the velocity distribution of spiral arms (with sigmas: vel_dist_r and vel_dist_phi, 
      # in r and phi directions, respectively)
      vel_r_pecu = random.normal(0.0, vel_dist_r, ni)
      vel_phi_pecu = random.normal(0.0, vel_dist_phi, ni)
 
      # xy positions at birth are: 
      xG_1, yG_1 = projectG(phi_init, distG_init)
 
      # we simulate position of stars in the future by advancing their positions
      # using rotation curve and pecular velocities of individual stars
      distG, phi = rotate(simulation_age, distG_init, phi_init, vel_r_pecu, vel_phi_pecu)
 
      # xy positions evolved to the current time are:
      xG, yG = projectG(phi, distG)
 
      for row in c_[xG_1, yG_1, distG_init * 0.001, phi_init, xG, yG, distG * 0.001, phi, vel_r_pecu, vel_phi_pecu]:
        outfile.write('%9.4f %9.4f  %9.4f %9.4f    %9.4f %9.4f  %9.4f %9.4f    %9.2f %9.2f\n'%tuple(row))

if __name__ == '__main__':
  pass

