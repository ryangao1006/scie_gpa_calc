#!/usr/bin/env python3
"""
Run all subject calculators and generate the report.
"""

import sys
import os

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))) # using ai's help

# Import the calculation functions
import bio # biology calculator
import econ # economics calculator
import geo # geography calculator
import maths # mathematics calculator

print("="*60)
print("Running all subject grade calculators")
print("="*60)

# Run biology calculator
print("\n=== Biology Calculator ===")
bio.calculate_bio_score()

# Run economics calculator
print("\n=== Economics Calculator ===")
econ.calculate_econ_score()

# Run geography calculator
print("\n=== Geography Calculator ===")
geo.calculate_geo_score()

# Run mathematics calculator
print("\n=== Mathematics Calculator ===")
maths.calculate_maths_score()

# Generate the report
print("\n" + "="*60)
print("Generating final report")
print("="*60)

# Import and run the report
import report # report generator, including the final suggestions and advices

print("\nReport generated successfully!")