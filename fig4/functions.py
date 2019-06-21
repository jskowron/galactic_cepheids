from numpy import sin, cos, ndarray, linspace, pi, ceil, sign
#  parameter units:      pc        km/s
from parameters import GC_dist, rot_curve


def projectG(phi, distG):
  return distG * sin(phi*pi/180.) * 0.001, -distG * cos(phi*pi/180.) * 0.001


def rotate(t, distG_init, phi_init, vel_r_pecu, vel_phi_pecu):
  '''Evolve position of a star in the Galaxy
     t in Myr, dist in pc, phi in degrees, velocities in km/s
  '''
  step = 2 # Myr
  if isinstance(distG_init, ndarray) and isinstance(phi_init, ndarray):
    distG, phi = distG_init.copy(), phi_init.copy()
  else:
    distG, phi = distG_init, phi_init
  times = linspace(0, abs(t), num=ceil(abs(t)/step), endpoint=True) * sign(t)

  delta_times = (times[1:] - times[:-1])
  for dt in delta_times:
    V_rot_pc_per_myr = (rot_curve(distG) + vel_phi_pecu) / 3.08567758e13 * 31556926.0e6
    phi -= dt * V_rot_pc_per_myr / (distG) * (180.0 / pi)  # degrees
    distG += dt * vel_r_pecu / 3.08567758e13 * 31556926.0e6
  return distG, phi


def gal_centric(l, b, dist):
  global GC_dist
  l_rad, b_rad= l / 180.0 * pi, b / 180.0 * pi
  DGsinPhi = - dist * sin(l_rad) * cos(b_rad)
  GDcosPhi = GC_dist - dist * cos(l_rad) * cos(b_rad)
  distG = sqrt( DGsinPhi**2 + GDcosPhi**2 )
  phi = arctan2(DGsinPhi, GDcosPhi) * 180.0/pi
  return phi, distG


