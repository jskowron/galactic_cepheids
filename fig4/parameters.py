
# Sun - Galactic center distance 
GC_dist = 8300.0

# parameters of the Galaxy
pattern_period = 250 # Myr  # Vallee 2017  250, 272
R0, psi = 3560.0, 12.4
arm_names =  ['Perseus', 'Sagittarius-Carina', 'Scutum-Crux-Centaurus', 'Norma-Cygnus / Outer']

# dispersions in the birthplace
vel_dist_r = 8 # km/s 
vel_dist_phi = 8 # km/s 
arm_r_sigma = 100 # pc

def rot_curve(distG):
  return 0.0*distG + 222.6 # km/s P. Mroz et al 2018

