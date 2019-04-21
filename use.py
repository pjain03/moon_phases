#!/bin/python3

#  AUTHOR: Pulkit Jain
# PURPOSE: Tests all our library functions


from lunar_phases_library import *

print("\n-------------- Lunar Phase Calculator --------------\n")
y = float(input("Enter the year: "))
m = float(input("Enter the month: "))
d = float(input("Enter the day: "))

print("\n--------------   Lunar Phase Output   --------------\n")
out = get_illuminated_fraction_moon(y, m, d)
print("\nPhase Information:")
print("Illuminated Fraction: ", out["illuminated_fraction"])
print("Position Angle: ", out["position_angle"])
# print("\n")
lunar_phase_ascii_art(out)
print("\n----------------------------------------------------\n")


