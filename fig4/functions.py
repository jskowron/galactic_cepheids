from numpy import sin, cos, ndarray, linspace, pi, ceil, sign
#  parameter units:      pc        km/s
from parameters import GC_dist, rot_curve


def projectG(phi, distG):
  '''
    Takes azimuth (in degrees) and the distance from the Galactic center (in pc)
    Returns simple cartesian coordinates (in pc)
  '''
  return distG * sin(phi * pi / 180.), -distG * cos(phi * pi / 180.)

def project(phi, distG):
  '''
    Takes azimuth (in degrees) and the distance from the Galactic center (in pc)
    Returns (in pc):
      X - axis X is towards the Galactic Center, with X=0 at the Sun and X = 8300 at the GC.
      Y - axis Y is in the Galactic disk plane, towards the direction of Galactic rotation. Sun has Y = 0.
  '''
  x, y = projectG(phi, distG)
  return y + GC_dist, -x

def rotate(t, distG_init, phi_init, vel_r_pecu, vel_phi_pecu):
  '''
    Evolve position of a star in the Galaxy
      t - time of the forward evolution (in Myr)
      distG_init - initial Galactocentric distance (in pc)
      phi_init - initial azimuth (in degrees), counted from the Sun in oposite direction than Galactic rotation
      vel_r_pecu, vel_phi_pecu - peculiar velocities in radial and azimuthal directions (in km/s)
    Returns:
      distG, phi - new, evolved galactocentric distance and azimuth
  '''
  step = 2.0 # Myr
  if isinstance(distG_init, ndarray) and isinstance(phi_init, ndarray):
    distG, phi = distG_init.copy(), phi_init.copy()
  else:
    distG, phi = distG_init, phi_init
  times = linspace(0, abs(t), num=max(2, int(ceil(abs(t)/step))), endpoint=True) * sign(t)

  delta_times = (times[1:] - times[:-1])
  for dt in delta_times:
    V_rot_pc_per_myr = (rot_curve(distG) + vel_phi_pecu) / 3.08567758e13 * 31556926.0e6
    phi -= dt * V_rot_pc_per_myr / (distG) * (180.0 / pi)  # degrees
    distG += dt * vel_r_pecu / 3.08567758e13 * 31556926.0e6
  return distG, phi


def gal_centric(l, b, dist):
  '''
    l - galactic longitude (degrees)
    b - galactic latitude (degrees)
    dist - distance from the Sun in pc

    Returns:
      phi, distG - azimuth (in deg) and the Galactocentric distance (in pc)
  '''
  l_rad, b_rad= l / 180.0 * pi, b / 180.0 * pi
  DGsinPhi = - dist * sin(l_rad) * cos(b_rad)
  GDcosPhi = GC_dist - dist * cos(l_rad) * cos(b_rad)
  distG = sqrt( DGsinPhi**2 + GDcosPhi**2 )
  phi = arctan2(DGsinPhi, GDcosPhi) * 180.0/pi
  return phi, distG


