import math

class Isotope:
    def __init__(self, name, half_life, energy_per_decay):
        self.name = name
        self.half_life = half_life  # in seconds
        self.energy_per_decay = energy_per_decay  # in MeV

class RadioactivityConverter:
    def __init__(self, activity, unit, isotope):
        self.activity = activity
        self.unit = unit
        self.isotope = isotope

    def decay_energy_joules(self):
        # Convert energy per decay from MeV to Joules
        return self.isotope.energy_per_decay * 1.60218e-13

    def calculate_absorbed_dose_gray(self, distance, mass, fraction_absorbed=1, geometry_factor=1, shielding_factor=1, energy_distribution_factor=1):
        energy_per_decay_joules = self.decay_energy_joules()
        # Incorporate geometry, shielding, and energy distribution into the dose calculation
        absorbed_dose_gray = ((activity * energy_per_decay_joules * fraction_absorbed * geometry_factor * shielding_factor * energy_distribution_factor) /
                              (4 * math.pi * distance ** 2 * mass))
        return absorbed_dose_gray

    def calculate_dose_equivalent_sievert(self, absorbed_dose_gray, quality_factor=1):
        # Convert absorbed dose in Gray to dose equivalent in Sievert
        dose_equivalent_sievert = absorbed_dose_gray * quality_factor
        return dose_equivalent_sievert

if __name__ == "__main__":
    cesium_137 = Isotope("Cesium-137", 30 * 365 * 24 * 3600, 5.662)  # Example isotope
    activity = 1000  # Example activity in Bq
    unit = "Bq"  # SI unit
    cesium_converter = RadioactivityConverter(activity, unit, cesium_137)
    
    # Example parameters for an advanced dose calculation
    distance = 1/1000  # meters
    mass = 1.0  # kg
    fraction_absorbed = 1  # Simplified assumption
    geometry_factor = 1  # Placeholder for geometry of exposure
    shielding_factor = 1  # Placeholder for shielding effects
    energy_distribution_factor = 1  # Placeholder for energy distribution of radiation

    absorbed_dose_gray = cesium_converter.calculate_absorbed_dose_gray(distance, mass, fraction_absorbed, geometry_factor, shielding_factor, energy_distribution_factor)
    dose_equivalent_sievert = cesium_converter.calculate_dose_equivalent_sievert(absorbed_dose_gray)
    energy_per_decay_joules = cesium_converter.decay_energy_joules()
    
    print(f"Energia per decadimento di {cesium_converter.isotope.name} in joule: {energy_per_decay_joules:.6e} J")
    print(f"Absorbed dose at {distance} m for {activity} Bq of {cesium_converter.isotope.name} is {absorbed_dose_gray} Gy")
    print(f"Dose equivalent is {dose_equivalent_sievert} Sv")
