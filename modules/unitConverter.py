class UnitConverter:
    """A class for converting units of measurement."""

    def meters_to_feet(self, meters):
        """Convert length from meters to feet."""
        return meters * 3.28084

    def feet_to_meters(self, feet):
        """Convert length from feet to meters."""
        return feet / 3.28084

    def celsius_to_fahrenheit(self, celsius):
        """Convert temperature from Celsius to Fahrenheit."""
        return (celsius * 9 / 5) + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        """Convert temperature from Fahrenheit to Celsius."""
        return (fahrenheit - 32) * 5 / 9

    def liters_to_gallons(self, liters):
        """Convert volume from liters to gallons."""
        return liters * 0.264172

    def gallons_to_liters(self, gallons):
        """Convert volume from gallons to liters."""
        return gallons / 0.264172

    def kilograms_to_pounds(self, kilograms):
        """Convert mass from kilograms to pounds."""
        return kilograms * 2.20462

    def pounds_to_kilograms(self, pounds):
        """Convert mass from pounds to kilograms."""
        return pounds / 2.20462

    def pascals_to_psi(self, pascals):
        """Convert pressure from pascals to psi."""
        return pascals * 0.000145038

    def psi_to_pascals(self, psi):
        """Convert pressure from psi to pascals."""
        return psi / 0.000145038

    def kmh_to_mph(self, kmh):
        """Convert speed from kilometers per hour to miles per hour."""
        return kmh * 0.621371

    def mph_to_kmh(self, mph):
        """Convert speed from miles per hour to kilometers per hour."""
        return mph / 0.621371

"""
# Usage examples
if __name__ == "__main__":
    converter = UnitConverter()
    print("10 meters to feet:", converter.meters_to_feet(10))
    print("50 feet to meters:", converter.feet_to_meters(50))
    print("20°C to Fahrenheit:", converter.celsius_to_fahrenheit(20))
    print("68°F to Celsius:", converter.fahrenheit_to_celsius(68))
    print("5 liters to gallons:", converter.liters_to_gallons(5))
    print("2 gallons to liters:", converter.gallons_to_liters(2))
    print("10 kilograms to pounds:", converter.kilograms_to_pounds(10))
    print("22 pounds to kilograms:", converter.pounds_to_kilograms(22))
    print("101325 pascals to psi:", converter.pascals_to_psi(101325))
    print("14.7 psi to pascals:", converter.psi_to_pascals(14.7))
    print("100 km/h to mph:", converter.kmh_to_mph(100))
    print("60 mph to km/h:", converter.mph_to_kmh(60))
"""
