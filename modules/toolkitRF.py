import math
import cmath


def wavelength(frequency):
    """Calculate the wavelength given the frequency (in Hz)."""
    c = 3e8
    return c / frequency


def frequency(wavelength_):
    """Calculate the frequency given the wavelength (in meters)."""
    c = 3e8
    return c / wavelength_


def path_loss(distance, frequency):
    """Calculate the path loss (in dB) given the distance (in meters) and the frequency (in Hz)."""
    c = 3e8
    return 20 * math.log10(distance) + 20 * math.log10(frequency) + 20 * math.log10(4 * math.pi / c)


def friis_transmission(pt, gt, gr, lambda_, d):
    """Calculate the received power (Pr) using Friis transmission equation."""
    return (pt * gt * gr * (lambda_ ** 2)) / ((4 * math.pi * d) ** 2)


def erp(pt, gt):
    """Calculate the Effective Radiated Power (ERP)."""
    return pt * gt


def eirp(pt, gt):
    """Calculate the Equivalent Isotropically Radiated Power (EIRP)."""
    return pt * gt


def reflection_coefficient(zl, z0):
    """Calculate the reflection coefficient given the load impedance (Zl) and the characteristic impedance (Z0)."""
    return (zl - z0) / (zl + z0)


def vswr(reflection_coeff):
    """Calculate the Voltage Standing Wave Ratio (VSWR) given the reflection coefficient."""
    return (1 + abs(reflection_coeff)) / (1 - abs(reflection_coeff))


def return_loss(reflection_coeff):
    """Calculate the return loss (in dB) given the reflection coefficient."""
    return -20 * math.log10(abs(reflection_coeff))


def smith_chart_impedance(z, z0):
    """Map the impedance (Z) on the Smith chart, given the characteristic impedance (Z0)."""
    return (z - z0) / (z + z0)


def transmission_line_impedance(zl, z0, l, frequency):
    """Calculate the input impedance of a transmission line given the load impedance (Zl), characteristic impedance (Z0), length (l), and frequency."""
    lambda_ = wavelength(frequency)
    beta = 2 * math.pi / lambda_
    return z0 * ((zl + z0 * cmath.tan(beta * l)) / (z0 + zl * cmath.tan(beta * l)))


def antenna_gain(pt, pr, distance, wavelength_):
    """Calculate the gain of an antenna given the transmitted power (Pt), received power (Pr), distance between antennas, and the wavelength."""
    return (4 * math.pi * distance ** 2 * pr) / (pt * wavelength_ ** 2)


def skin_depth(frequency, permeability, conductivity):
    """Calculate the skin depth (in meters) given the frequency (in Hz), permeability (in Henry/meter), and conductivity (in Siemens/meter)."""
    return math.sqrt(1 / (math.pi * frequency * permeability * conductivity))


def link_budget(pt, gt, gr, distance, frequency, system_loss=0):
    """Calculate the total link budget (in dB) given the transmitted power (Pt in dBm), transmitting antenna gain (Gt), receiving antenna gain (Gr), distance (in meters), frequency (in Hz), and system loss (in dB)."""
    lambda_ = wavelength(frequency)
    free_space_loss = (4 * math.pi * distance / lambda_) ** 2
    return pt + gt + gr - 10 * math.log10(free_space_loss) - system_loss
