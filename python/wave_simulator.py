import numpy as np
from scipy import constants
permittivity_water = 80


def atten_coeff(f=902.75*10**6, permittivity=80, loss_tan=0.05, permeability=1):
    return 2 * np.pi * f * np.sqrt(permeability*permittivity*(np.sqrt(1+loss_tan**2)-1)/2) / constants.speed_of_light


def phase_coeff(f=902.75*10**6, permittivity=80, loss_tan=0.05, permeability=1):
    return 2 * np.pi * f * np.sqrt(permeability*permittivity*(np.sqrt(1+loss_tan**2)+1)/2) / constants.speed_of_light


def wavelength(f=902.75*10**6, permittivity=75.64, loss_tan=0.19, permeability=1):
    return 2 * np.pi / phase_coeff(f=f, permittivity=permittivity, loss_tan=loss_tan, permeability=permeability)


def attenuate(d, f=902.75*10**6, permittivity=80, loss_tan=0.05, permeability=1):
    return np.e**(d*-atten_coeff(f, permittivity, loss_tan, permeability))


def trans_coeff(z_from, z_to):
    return 2*z_to / (z_from+z_to)


def refl_coeff(z_from, z_to):
    return (z_to-z_from) / (z_from+z_to)


def z(permittivity=80):
    return 377/np.sqrt(permittivity)


def n(permittivity=80, loss_tan=0.05, permeability=1):
    return np.sqrt(permeability * permittivity * (np.sqrt(1 + loss_tan ** 2) + 1) / 2)



