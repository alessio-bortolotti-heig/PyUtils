
# PyUtils

PyUtils is a versatile collection of tools and utilities in Python, designed to simplify tasks. This repository hosts a series of mini-modules and scripts, each focused on a specific area of utility.

## Installation

To install the modules and scripts in PyUtils, follow these steps:

1. Clone the repository locally using Git:
   ```
   git clone https://github.com/alessio-bortolotti-heig/PyUtils.git
   ```
2. Navigate to the project folder:
   ```
   cd PyUtils
   ```
3. (Optional) It is recommended to create a virtual environment to manage dependencies:  
   Linux & macOS
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
   Windows
   ```
   python3 -m venv venv
   venv\Scripts\activate
   ```
4. Install the necessary dependencies:
   ```
   pip3 install -r requirements.txt
   ```

Once the installation is complete, you are ready to use the tools available in PyUtils.

## Modules

Below is a list of the mini-modules and scripts included in PyUtils, with a brief description for each:

### MolecularMassCalculator.py
This Python program calculates the molecular mass of chemical compounds. It maps elements to atomic masses, splits molecular formulas into individual elements with multipliers, and sums the atomic masses to find the total molecular mass. Users can input a formula (e.g., Penicillin G) to get its molar mass.

### EpidemicsMetrics.py
This Python script calculates epidemiological metrics: the Basic Reproduction Number (R0) and the Herd Immunity Threshold (HIT). R0 represents the average number of cases one infected person generates, while HIT indicates the fraction of the population that needs immunity to halt the epidemic's spread.

### Radioactivity.py
This Python code defines a model for radioactive isotopes and a converter to calculate radiation-related measurements. It includes functions for converting decay energy to joules, calculating absorbed dose in gray, and determining dose equivalent in sievert, based on activity level, distance, and other factors for a specific isotope.

### UnitConverter.py
This Python program defines a `UnitConverter` class to perform unit conversions across different measurement categories, including length, temperature, volume, mass, pressure, and speed. It offers methods for converting between commonly used units, such as meters to feet, Celsius to Fahrenheit, and liters to gallons.
