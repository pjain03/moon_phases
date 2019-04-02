#!/bin/python3

#  AUTHOR: Pulkit Jain
# PURPOSE: Tests all our library functions


from library import *

print("Testing... (All Trues means we passed all the tests)")
print("----------------------------------------------------")

# See p.61, Eg 7a
print(1, date_to_jde(1957, 10, 4.81) == 2436116.31)  # 1957, Oct, 4.81

# See p.62, Test Cases
print(2, date_to_jde(2000, 1, 1.5) == 2451545.0)      # 2000, Jan, 1.5
print(3, date_to_jde(1987, 1, 27.0) == 2446822.5)     # 1987, Jan, 27.0
print(4, date_to_jde(1987, 6, 19.5) == 2446966.0)     # 1987, Jun, 19.5
print(5, date_to_jde(1988, 1, 27.0) == 2447187.5)     # 1988, Jan, 27.0
print(6, date_to_jde(1988, 6, 19.5) == 2447332.0)     # 1988, Jun, 19.5
print(7, date_to_jde(1900, 1, 1.0) == 2415020.5)      # 1900, Jan, 1.0
print(8, date_to_jde(1600, 1, 1.0) == 2305447.5)      # 1600, Jan, 1.0
print(9, date_to_jde(1600, 12, 31.0) == 2305812.5)    # 1600, Dec, 31.0
print(10, date_to_jde(837, 4, 10.3) == 2026871.8)     # 837, Apr, 10.3
print(11, date_to_jde(-1000, 7, 12.5) == 1356001.0)   # -1000, Jul, 12.5 (BC)
print(12, date_to_jde(-1000, 2, 29.0) == 1355866.5)   # -1000, Feb, 29.0 (BC)
print(13, date_to_jde(-1001, 8, 17.9) == 1355671.4)   # -1001, Aug, 17.9 (BC)
print(14, date_to_jde(-4712, 1, 1.5) == 0.0)          # -4712, Jan, 1.5 (BC)
print(get_illuminated_fraction_moon(2019, 11, 17))

print("----------------------------------------------------")
print("Testing Complete.")