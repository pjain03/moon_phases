#!/bin/python3

#  AUTHOR: Pulkit Jain
# PURPOSE: Contains all the functions we will use in our program

import math


def date_to_jde(y, m, d):
    """
    See Chapter 7 (Astronomical Algorithms, Jean Meeus)
    Converts the Gregorian date passed in to Julian Ephemeris Day (JDE)
    NOTE: it works only for dates past November 23, −4713
    :arg:    y -> year
    :arg:    m -> month
    :arg:    d -> day
    :return: float
    """
    if m == 1 or m == 2:
        y = y - 1
        m = m + 12
    # Gregorian Calendar started on October 15, 1583
    if (y, m, d) >= (1582, 10, 15):
        a = int(y / 100)
        b = 2 - a + int(a / 4)
    else:
        b = 0
    jd = int(365.25 * (y + 4716)) + int(30.6001 * (m + 1)) + d + b - 1524.5
    return jd


def jde_to_T(jd):
    """
    See Chapter 24 (Astronomical Algorithms, Jean Meeus)
    Converts the JDE to Julian centuries
    :arg:    jd -> Julian Ephemeris Day (JDE)
    :return: float
    """
    T = (jd - 2451545) / 36525
    return T


def eccentricity(T):
    """
    See Chapter 45 (Astronomical Algorithms, Jean Meeus)
    Calculates the eccentricity from the Julian centuries
    :arg:    T -> Julian centuries
    :return: float
    """
    E = 1 - 0.002516 * T - 0.0000074 * T * T
    return E


def ecliptic_obliquity(T):
    """
    See Chapter 21 (Astronomical Algorithms, Jean Meeus)
    Calculates the mean obliquity of the ecliptic (epsilon)
    :arg:    T -> Julian centuries
    :return: float
    """
    U = T / 100
    eo = 23.43929 - 1.300258 * U - 1.55 * (U ** 2) + 1999.25 * (U ** 3) - \
         51.38 * (U ** 4) - 249.67 * (U ** 5) - 39.05 * (U ** 6) + \
         7.12 * (U ** 7) + 27.87 * (U ** 8) + 5.79 * (U ** 9) + \
         2.45 * (U ** 10)
    return eo


def mean_longitude_sun(T):
    """
    See Chapter 24 (Astronomical Algorithms, Jean Meeus)
    Calculates the geometric mean longitude of the sun
    :arg:    T -> Julian centuries
    :return: float
    """
    Lo = 280.46645 + 36000.76983 * T + 0.0003032 * T * T
    return Lo


def mean_longitude_moon(T):
    """
    See Chapter 21 (Astronomical Algorithms, Jean Meeus)
    Calculates the geometric mean longitude of the moon
    :arg:    T -> Julian centuries
    :return: float
    """
    Lo = 218.3165 + 481267.8813 * T
    return Lo


def mean_anomaly_sun(T):
    """
    See Chapter 24 (Astronomical Algorithms, Jean Meeus)
    Calculates the mean anomaly of the sun
    :arg:    T -> Julian centuries
    :return: float
    """
    M = 357.52910 + 35999.05030 * T - 0.0001559 * T * T - \
        0.00000048 * T * T * T
    return M % 360


def eccentricity_sun_earth(T):
    """
    See Chapter 24 (Astronomical Algorithms, Jean Meeus)
    Calculates the eccentricity of the earth's orbit around the sun
    :arg:    T -> Julian centuries
    :return: float
    """
    e = 0.016708617 - 0.000042037 * T - 0.0000001236 * T * T
    return e


def center_of_sun(T, M):
    """
    See Champter 24 (Astronomical Algorithms, Jean Meeus)
    Calculates the center of the sun
    :arg:    T -> Julian centuries
    :arg:    M -> Mean anomaly of the sun
    :return: float
    """
    M_rad = math.radians(M)
    C = (1.914600 - 0.004817 * T - 0.000014 * T * T) * math.sin(M_rad) + \
        (0.019993 - 0.000101 * T) * math.sin(2 * M_rad) + \
        0.000290 * math.sin(3 * M_rad)
    return C


def true_longitude_sun(Lo, C):
    """
    See Chapter 24 (Astronomical Algorithms, Jean Meeus)
    Calculates true longitude of the sun
    :arg:    Lo -> Mean longitude of the sun
    :arg:    C -> Center of the sun
    :return: float
    """
    return Lo + C


def true_anomaly_sun(M, C):
    """
    See Chapter 24 (Astronomical Algorithms, Jean Meeus)
    Calculates true anomaly of the sun (v)
    :arg:    M -> Mean anomaly of the sun
    :arg:    C -> Center of the sun
    :return: float
    """
    return M + C


def distance_sun_earth(e, v):
    """
    See Chapter 24 (Astronomical Algorithms, Jean Meeus)
    Calculates distance of the earth to the sun in AU
    :arg:    e -> Eccentricity of the earths orbit around the sun
    :arg:    v -> True anomaly of the sun
    :return: float
    """
    R = (1.000001018 * (1 - e * e)) / (1 + e * math.cos(math.radians(v)))
    return R


def omega(T):
    """
    See Chapter 24 (Astronomical Algorithms, Jean Meeus)
    Calculates the value of Omega which is used in a variety of sections below
    :arg:    T -> Julian centuries
    :return: float
    """
    O = 125.04 - 1934.136 * T
    return O


def apparent_longitude_sun(L, T):
    """
    See Chapter 24 (Astronomical Algorithms, Jean Meeus)
    Calculates apparent longitude of the sun (lambda)
    :arg:    L -> True longitude of the sun
    :arg:    T -> Julian centuries
    :return: float
    """
    O = omega(T)
    l = L - 0.00569 - 0.00478 * math.sin(math.radians(O))
    return l


def right_ascension_sun(eo, tl):
    """
    See Chapter 24 (Astronomical Algorithms, Jean Meeus)
    Calculates the right ascension of the sun (alpha)
    :arg:    eo -> ecliptic obliquity
    :arg:    tl -> true longitude of the sun
    :return: float
    """
    a = math.atan2(math.cos(math.radians(eo)) * math.sin(math.radians(tl)),
                   math.cos(math.radians(tl)))
    return math.degrees(a)


def right_declination_sun(eo, tl):
    """
    See Chapter 24 (Astronomical Algorithms, Jean Meeus)
    Calculates the right declination of the sun (delta)
    :arg:    eo -> ecliptic obliquity
    :arg:    tl -> true longitude of the sun
    :return: float
    """
    d = math.asin(math.sin(math.radians(eo)) * math.sin(math.radians(tl)))
    return math.degrees(d)


def apparent_right_ascension_sun(eo, al, T):
    """
    See Chapter 24 (Astronomical Algorithms, Jean Meeus)
    Calculates the apparent position of the sun (p_sun)
    :arg:    eo -> ecliptic obliquity
    :arg:    al -> apparent longitude of the sun
    :arg:    T -> Julian centuries
    :return: float
    """
    O = omega(T)
    eo_corrected = eo + 0.00256 * math.degrees(math.cos(math.radians(O)))
    a = math.atan2(math.cos(math.radians(eo_corrected)) *
                   math.sin(math.radians(al)), math.cos(math.radians(al)))
    return math.degrees(a)


def apparent_right_declination_sun(eo, al, T):
    """
    See Chapter 24 (Astronomical Algorithms, Jean Meeus)
    Calculates the apparent declination of the sun (delta)
    :arg:    eo -> ecliptic obliquity
    :arg:    al -> true longitude of the sun
    :arg:    T -> Julian centuries
    :return: float
    """
    O = omega(T)
    eo_corrected = eo + 0.00256 * math.degrees(math.cos(math.radians(O)))
    d = math.asin(math.sin(math.radians(eo_corrected)) *
                  math.sin(math.radians(al)))
    return math.degrees(d)


def get_portion_illuminated(i):
    """
    See Chapter 46 (Astronomical Algorithms, Jean Meeus)
    Calculates the portion of the moon that's illuminated
    :arg:    i -> Phase angle of the Moon
    :return: float
    """
    k = (1 + math.cos(math.radians(i))) / 2
    return k


def light_time_moon(T):
    """
    See Chapter 45 (Astronomical Algorithms, Jean Meeus)
    Calculating the effect of the light time
    :arg:    T -> Julian centuries
    :return: float
    """
    L_prime = 218.3164591 + 481267.88134236 * T - 0.0013268 * T * T + \
              (T * T * T / 538841) - (T * T * T * T / 65194000)
    return L_prime % 360


def mean_elongation_moon(T):
    """
    See Chapter 45 (Astronomical Algorithms, Jean Meeus)
    Calculating the mean elongation of the moon
    :arg:    T -> Julian centuries
    :return: float
    """
    D = 297.8502042 + 445267.1115168 * T - 0.0016300 * T * T + \
        (T * T * T / 545868) - (T * T * T * T / 113065000)
    return D % 360


def mean_anomaly_moon(T):
    """
    See Chapter 45 (Astronomical Algorithms, Jean Meeus)
    Calculating the mean anomly of the moon
    :arg:    T -> Julian centuries
    :return: float
    """
    M = 134.9634114 + 477198.8676313 * T + 0.0089970 * T * T + \
        (T * T * T / 69699) - (T * T * T * T / 14712000)
    return M % 360


def mean_latitude_moon(T):
    """
    See Chapter 45 (Astronomical Algorithms, Jean Meeus)
    Calculating the mean latitude of the moon
    :arg:    T -> Julian centuries
    :return: float
    """
    F = 93.2720993 + 483202.0175273 * T - 0.0034029 * T * T - \
        (T * T * T / 3526000) + (T * T * T * T / 863310000)
    return F % 360


def action_venus(T):
    """
    See Chapter 45 (Astronomical Algorithms, Jean Meeus)
    Calculating the action of Venus on the moon
    :arg:    T -> Julian centuries
    :return: float
    """
    A1 = 119.75 + 131.849 * T
    return A1 % 360


def action_jupiter(T):
    """
    See Chapter 45 (Astronomical Algorithms, Jean Meeus)
    Calculating the action of Jupiter on the moon
    :arg:    T -> Julian centuries
    :return: float
    """
    A2 = 53.09 + 479264.290 * T
    return A2 % 360


def action_earth(T):
    """
    See Chapter 45 (Astronomical Algorithms, Jean Meeus)
    Calculating the action of Earth on the moon
    :arg:    T -> Julian centuries
    :return: float
    """
    A3 = 313.45 + 481266.484 * T
    return A3 % 360


def kepler_coeff_longitude(D, M, M_prime, F, E, A1, A2, L_prime):
    """
    See Chapter 45 (Astronomical Algorithms, Jean Meeus)
    Calculates the coefficient of the sine of the longitude (summation l)
    :arg:    D -> Mean elongation of the moon
    :arg:    M -> Mean anomlay of the sun
    :arg:    M_prime -> Mean anomaly of the moon
    :arg:    F -> Mean latitude of the moon
    :arg:    E -> Eccentricity of the Earths orbit
    :arg:    A1 -> Action due to Venus
    :arg:    A2 -> Action due to Jupiter
    :arg:    L_prime -> Effect of light-time
    :return: float (10 ^ -6 degrees)
    """
    l = 6288774 * math.sin(math.radians(M_prime)) \
        + 1274027 * math.sin(math.radians(2 * D - M_prime)) \
        + 658314 * math.sin(math.radians(2 * D)) \
        + 213618 * math.sin(math.radians(2 * M_prime)) \
        - 185116 * math.sin(math.radians(M)) * E \
        - 114332 * math.sin(math.radians(2 * F)) \
        + 58793 * math.sin(math.radians(2 * D - 2 * M_prime)) \
        + 57066 * math.sin(math.radians(2 * D - M - M_prime)) * E \
        + 53322 * math.sin(math.radians(2 * D + M_prime)) \
        + 45758 * math.sin(math.radians(2 * D - M)) * E \
        - 40923 * math.sin(math.radians(M - M_prime)) * E \
        - 34720 * math.sin(math.radians(D)) \
        - 30383 * math.sin(math.radians(M + M_prime)) * E \
        + 15327 * math.sin(math.radians(2 * D - 2 * F)) \
        - 12528 * math.sin(math.radians(M_prime + 2 * F)) \
        + 10980 * math.sin(math.radians(M_prime - 2 * F)) \
        + 10675 * math.sin(math.radians(4 * D - M_prime)) \
        + 10034 * math.sin(math.radians(3 * M_prime)) \
        + 8548 * math.sin(math.radians(4 * D - 2 * M_prime)) \
        - 7888 * math.sin(math.radians(2 * D + M - M_prime)) * E \
        - 6766 * math.sin(math.radians(2 * D + M)) * E \
        - 5163 * math.sin(math.radians(D - M_prime)) \
        + 4987 * math.sin(math.radians(D + M)) * E \
        + 4036 * math.sin(math.radians(2 * D - M + M_prime)) * E \
        + 3994 * math.sin(math.radians(2 * D + 2 * M_prime)) \
        + 3861 * math.sin(math.radians(4 * D)) \
        + 3665 * math.sin(math.radians(2 * D - 3 * M_prime)) \
        - 2689 * math.sin(math.radians(M - 2 * M_prime)) * E \
        - 2602 * math.sin(math.radians(2 * D - M_prime + 2 * F)) \
        + 2390 * math.sin(math.radians(2 * D - M - 2 * M_prime)) * E \
        - 2348 * math.sin(math.radians(D + M_prime)) \
        + 2236 * math.sin(math.radians(2 * D - 2 * M)) * E * E \
        - 2120 * math.sin(math.radians(M + 2 * M_prime)) * E \
        - 2069 * math.sin(math.radians(2 * M)) * E * E \
        + 2048 * math.sin(math.radians(2 * D - 2 * M - M_prime)) * E * E \
        - 1773 * math.sin(math.radians(2 * D + M_prime - 2 * F)) \
        - 1595 * math.sin(math.radians(2 * D + 2 * F)) \
        + 1215 * math.sin(math.radians(4 * D - M - M_prime)) * E \
        - 1110 * math.sin(math.radians(2 * M_prime + 2 * F)) \
        - 892 * math.sin(math.radians(3 * D - M_prime)) \
        - 810 * math.sin(math.radians(2 * D + M + M_prime)) * E \
        + 759 * math.sin(math.radians(4 * D - M - 2 * M_prime)) * E \
        - 713 * math.sin(math.radians(2 * M - M_prime)) * E * E \
        - 700 * math.sin(math.radians(2 * D + 2 * M - M_prime)) * E * E \
        + 691 * math.sin(math.radians(2 * D + M - 2 * M_prime)) * E \
        + 596 * math.sin(math.radians(2 * D - M - 2 * F)) * E \
        + 549 * math.sin(math.radians(4 * D + M_prime)) \
        + 537 * math.sin(math.radians(4 * M_prime)) \
        + 520 * math.sin(math.radians(4 * D - M)) * E \
        - 487 * math.sin(math.radians(D - 2 * M_prime)) \
        - 399 * math.sin(math.radians(2 * D + M - 2 * F)) * E \
        - 381 * math.sin(math.radians(2 * M_prime - 2 * F)) \
        + 351 * math.sin(math.radians(D + M + M_prime)) * E \
        - 340 * math.sin(math.radians(3 * D - 2 * M_prime)) \
        + 330 * math.sin(math.radians(4 * D - 3 * M_prime)) \
        + 327 * math.sin(math.radians(2 * D - M + 2 * M_prime)) * E \
        - 323 * math.sin(math.radians(2 * M + M_prime)) * E * E \
        + 299 * math.sin(math.radians(D + M - M_prime)) * E \
        + 294 * math.sin(math.radians(2 * D + 3 * M_prime))
    l += 3958 * math.sin(math.radians(A1)) + \
         1962 * math.sin(math.radians(L_prime - F)) + \
         318 * math.sin(math.radians(A2))
    return l


def kepler_coeff_distance(D, M, M_prime, F, E):
    """
    See Chapter 45 (Astronomical Algorithms, Jean Meeus)
    Calculates the coefficient of the cosine of the distance (summation r)
    :arg:    D -> Mean elongation of the moon
    :arg:    M -> Mean anomlay of the sun
    :arg:    M_prime -> Mean anomaly of the moon
    :arg:    F -> Mean latitude of the moon
    :arg:    E -> Eccentricity of the Earths orbit
    :return: float (10 ^ -3 km)
    """
    r = - 20905355 * math.cos(math.radians(M_prime)) \
        - 3699111 * math.cos(math.radians(2 * D - M_prime)) \
        - 2955968 * math.cos(math.radians(2 * D)) \
        - 569925 * math.cos(math.radians(2 * M_prime)) \
        + 48888 * math.cos(math.radians(M)) * E \
        - 3149 * math.cos(math.radians(2 * F)) \
        + 246158 * math.cos(math.radians(2 * D - 2 * M_prime)) \
        - 152138 * math.cos(math.radians(2 * D - M - M_prime)) * E \
        - 170733 * math.cos(math.radians(2 * D + M_prime)) \
        - 204586 * math.cos(math.radians(2 * D - M)) * E \
        - 129620 * math.cos(math.radians(M - M_prime)) * E \
        + 108743 * math.cos(math.radians(D)) \
        + 104755 * math.cos(math.radians(M + M_prime)) * E \
        + 10321 * math.cos(math.radians(2 * D - 2 * F)) \
        + 79661 * math.cos(math.radians(M_prime - 2 * F)) \
        - 34782 * math.cos(math.radians(4 * D - M_prime)) \
        - 23210 * math.cos(math.radians(3 * M_prime)) \
        - 21636 * math.cos(math.radians(4 * D - 2 * M_prime)) \
        + 24208 * math.cos(math.radians(2 * D + M - M_prime)) * E \
        + 30824 * math.cos(math.radians(2 * D + M)) * E \
        - 8379 * math.cos(math.radians(D - M_prime)) \
        - 16675 * math.cos(math.radians(D + M)) * E \
        - 12831 * math.cos(math.radians(2 * D - M + M_prime)) * E \
        - 10445 * math.cos(math.radians(2 * D + 2 * M_prime)) \
        - 11650 * math.cos(math.radians(4 * D)) \
        + 14403 * math.cos(math.radians(2 * D - 3 * M_prime)) \
        - 7003 * math.cos(math.radians(M - 2 * M_prime)) * E \
        + 10056 * math.cos(math.radians(2 * D - M - 2 * M_prime)) * E \
        + 6322 * math.cos(math.radians(D + M_prime)) \
        - 9884 * math.cos(math.radians(2 * D - 2 * M)) * E * E \
        + 5751 * math.cos(math.radians(M + 2 * M_prime)) * E \
        - 4950 * math.cos(math.radians(2 * D - 2 * M - M_prime)) * E * E \
        + 4130 * math.cos(math.radians(2 * D + M_prime - 2 * F)) \
        - 3958 * math.cos(math.radians(4 * D - M - M_prime)) * E \
        + 3258 * math.cos(math.radians(3 * D - M_prime)) \
        + 2616 * math.cos(math.radians(2 * D + M + M_prime)) * E \
        - 1897 * math.cos(math.radians(4 * D - M - 2 * M_prime)) * E \
        - 2117 * math.cos(math.radians(2 * M - M_prime)) * E * E \
        + 2354 * math.cos(math.radians(2 * D + 2 * M - M_prime)) * E * E \
        - 1423 * math.cos(math.radians(4 * D + M_prime)) \
        - 1117 * math.cos(math.radians(4 * M_prime)) \
        - 1571 * math.cos(math.radians(4 * D - M)) * E \
        - 1739 * math.cos(math.radians(D - 2 * M_prime)) \
        - 4421 * math.cos(math.radians(2 * M_prime - 2 * F)) \
        + 1165 * math.cos(math.radians(2 * M + M_prime)) * E * E \
        + 8752 * math.cos(math.radians(2 * D - M_prime - 2 * F))
    return r


def kepler_coeff_latitude(D, M, M_prime, F, E, L_prime, A3, A1):
    """
    See Chapter 45 (Astronomical Algorithms, Jean Meeus)
    Calculates the coefficient of the sine of the latitude (summation b)
    :arg:    D -> Mean elongation of the moon
    :arg:    M -> Mean anomlay of the sun
    :arg:    M_prime -> Mean anomaly of the moon
    :arg:    F -> Mean latitude of the moon
    :arg:    E -> Eccentricity of the Earths orbit
    :arg:    L_prime -> Effect of light-time
    :arg:    A3 -> Another action argument tbh I couldn't find any reference
                   explaining what this was. Not in the book, not in the
                   interwebz, nowhere rip dios mio
    :arg:    A1 -> Action due to Venus
    :return: float (10 ^ -6 degrees)
    """
    b = 5128122 * math.sin(math.radians(F)) \
        + 280602 * math.sin(math.radians(M_prime + F)) \
        + 277693 * math.sin(math.radians(M_prime - F)) \
        + 173237 * math.sin(math.radians(2 * D - F)) \
        + 55413 * math.sin(math.radians(2 * D - M_prime + F)) \
        + 46271 * math.sin(math.radians(2 * D - M_prime - F)) \
        + 32573 * math.sin(math.radians(2 * D + F)) \
        + 17198 * math.sin(math.radians(2 * M_prime + F)) \
        + 9266 * math.sin(math.radians(2 * D + M_prime - F)) \
        + 8822 * math.sin(math.radians(2 * M_prime - F)) \
        + 8216 * math.sin(math.radians(2 * D - M - F)) * E \
        + 4324 * math.sin(math.radians(2 * D - 2 * M_prime - F)) \
        + 4200 * math.sin(math.radians(2 * D + M_prime + F)) \
        - 3359 * math.sin(math.radians(2 * D + M - F)) * E \
        + 2463 * math.sin(math.radians(2 * D - M - M_prime + F)) * E \
        + 2211 * math.sin(math.radians(2 * D - M + F)) * E \
        + 2065 * math.sin(math.radians(2 * D - M - M_prime - F)) * E \
        - 1870 * math.sin(math.radians(M - M_prime - F)) * E \
        + 1828 * math.sin(math.radians(4 * D - M_prime - F)) \
        - 1794 * math.sin(math.radians(M + F)) * E \
        - 1749 * math.sin(math.radians(3 * F)) \
        - 1565 * math.sin(math.radians(M - M_prime + F)) * E \
        - 1491 * math.sin(math.radians(D + F)) \
        - 1475 * math.sin(math.radians(M + M_prime + F)) * E \
        - 1410 * math.sin(math.radians(M + M_prime - F)) * E \
        - 1344 * math.sin(math.radians(M - F)) * E \
        - 1335 * math.sin(math.radians(D - F)) \
        + 1107 * math.sin(math.radians(3 * M_prime + F)) \
        + 1021 * math.sin(math.radians(4 * D - F)) \
        + 833 * math.sin(math.radians(4 * D - M_prime + F)) \
        + 777 * math.sin(math.radians(M_prime - 3 * F)) \
        + 671 * math.sin(math.radians(4 * D - 2 * M_prime + F)) \
        + 607 * math.sin(math.radians(2 * D - 3 * F)) \
        + 596 * math.sin(math.radians(2 * D + 2 * M_prime - F)) \
        + 491 * math.sin(math.radians(2 * D - M + M_prime - F)) * E \
        - 451 * math.sin(math.radians(2 * D - 2 * M_prime + F)) \
        + 439 * math.sin(math.radians(3 * M_prime - F)) \
        + 422 * math.sin(math.radians(2 * D + 2 * M_prime + F)) \
        + 421 * math.sin(math.radians(2 * D - 3 * M_prime - F)) \
        - 366 * math.sin(math.radians(2 * D + M - M_prime + F)) * E \
        - 351 * math.sin(math.radians(2 * D + M + F)) * E \
        + 331 * math.sin(math.radians(4 * D + F)) \
        + 315 * math.sin(math.radians(2 * D - M + M_prime + F)) * E \
        + 302 * math.sin(math.radians(2 * D - 2 * M - F)) * E * E \
        - 283 * math.sin(math.radians(M_prime + 3 * F)) \
        - 229 * math.sin(math.radians(2 * D + M + M_prime - F)) * E \
        + 223 * math.sin(math.radians(D + M - F)) * E \
        + 223 * math.sin(math.radians(D + M + F)) * E \
        - 220 * math.sin(math.radians(M - 2 * M_prime - F)) * E \
        - 220 * math.sin(math.radians(2 * D + M - M_prime - F)) * E \
        - 185 * math.sin(math.radians(D + M_prime + F)) \
        + 181 * math.sin(math.radians(2 * D - M - 2 * M_prime - F)) * E \
        - 177 * math.sin(math.radians(M + 2 * M_prime + F)) * E \
        + 176 * math.sin(math.radians(4 * D - 2 * M_prime - F)) \
        + 166 * math.sin(math.radians(4 * D - M - M_prime - F)) * E \
        - 164 * math.sin(math.radians(D + M_prime - F)) \
        + 132 * math.sin(math.radians(4 * D + M_prime - F)) \
        - 119 * math.sin(math.radians(D - M_prime - F)) \
        + 115 * math.sin(math.radians(4 * D - M - F)) * E \
        + 107 * math.sin(math.radians(2 * D - 2 * M + F)) * E * E
    b += - 2235 * math.sin(math.radians(L_prime)) \
         + 382 * math.sin(math.radians(A3)) \
         + 175 * math.sin(math.radians(A1 - F)) \
         + 175 * math.sin(math.radians(A1 + F)) \
         + 127 * math.sin(math.radians(L_prime - M_prime)) \
         - 115 * math.sin(math.radians(L_prime + M_prime))
    return b


def apparent_longitude_moon(L_prime, sl):
    """
    See Chapter 45 (Astronomical Algorithms, Jean Meeus)
    Calculates the geocentric longitude for the moon (lambda)
    :arg:    L_prime -> Effect of light-time
    :arg:    sl -> the summation longitude (Kepler coefficient)
    :return: float
    """
    l = L_prime + sl / (10 ** 6)
    return l


def apparent_latitude_moon(sb):
    """
    See Chapter 45 (Astronomical Algorithms, Jean Meeus)
    Calculates the geocentric latitude for the moon (beta)
    :arg:    sb -> the summation latitude (Kepler coefficient)
    :return: float
    """
    b = sb / (10 ** 6)
    return b


def distance_moon_earth(sr):
    """
    See Chapter 45 (Astronomical Algorithms, Jean Meeus)
    Calculates the distance between the moon and the Earth (delta)
    :arg:    sr -> the summation distance for the moon (Kepler coefficient)
    :return: float
    """
    d = 385000.56 + sr / (10 ** 3)
    return d


def apparent_right_ascension_moon(l_moon, b_moon, e_moon):
    """
    See Chapter 12 (Astronomical Algorithms, Jean Meeus)
    Calculates the apparent latitude
    :arg:    l_moon -> geocentric longitude
    :arg:    b_moon -> geocentric latitude
    :arg:    e_moon -> obliquity of the ecliptic
    :return: float
    """
    a = math.atan2(math.sin(math.radians(l_moon)) *
                   math.cos(math.radians(e_moon)) -
                   math.tan(math.radians(b_moon)) *
                   math.sin(math.radians(e_moon)),
                   math.cos(math.radians(l_moon)))
    return math.degrees(a)


def apparent_right_declination_moon(l_moon, b_moon, e_moon):
    """
    See Chapter 12 (Astronomical Algorithms, Jean Meeus)
    Calculates the apparent longitude
    :arg:    l_moon -> geocentric longitude
    :arg:    b_moon -> geocentric latitude
    :arg:    e_moon -> obliquity of the ecliptic
    :return: float
    """
    d = math.asin(math.sin(math.radians(b_moon)) *
                  math.cos(math.radians(e_moon)) +
                  math.cos(math.radians(b_moon)) *
                  math.sin(math.radians(e_moon)) *
                  math.sin(math.radians(l_moon)))
    return math.degrees(d)


def delta_epsilon(T):
    """
    See Chapter 21 (Astronomical Algorithms, Jean Meeus)
    Calculations the nutation in the obliquity of the ecliptic
    :arg:    T -> Julian centuries
    :return: float
    """
    O = omega(T)
    L = mean_longitude_sun(T)
    L_prime = mean_longitude_moon(T)
    de = 0.002555556 * math.cos(math.radians(O)) + \
         0.0001583333 * math.cos(math.radians(2 * L)) + \
         0.00002777778 * math.cos(math.radians(2 * L_prime)) + \
         0.000025 * math.cos(math.radians(2 * O))
    return de


def delta_shi(T):
    """
    See Chapter 21 (Astronomical Algorithms, Jean Meeus)
    Calculations the nutation in the longitude
    :arg:    T -> Julian centuries
    :return: float
    """
    O = omega(T)
    L = mean_longitude_sun(T)
    L_prime = mean_longitude_moon(T)
    ds = 0.004777778 * math.sin(math.radians(O)) - \
         0.0003666667 * math.sin(math.radians(2 * L)) + \
         0.00006388889 * math.sin(math.radians(2 * L_prime)) + \
         0.00005833333 * math.sin(math.radians(2 * O))
    return ds


def get_coordinates_sun(y, m, d):
    """
    Calculates and returns the equatorial coordinates of the Sun
    :arg:    y -> year
    :arg:    m -> month
    :arg:    d -> day
    :return: {"alpha": float, "delta": float, "lambda": float,
              "ecliptic_obliquity: "float, "distance_to_earth": float}
    """
    T = jde_to_T(date_to_jde(y, m, d))
    Lo = mean_longitude_sun(T) % 360
    M = mean_anomaly_sun(T)
    C = center_of_sun(T, M)
    L = true_longitude_sun(Lo, C)
    al = apparent_longitude_sun(L, T)
    e = ecliptic_obliquity(T) + delta_epsilon(T)
    a = apparent_right_ascension_sun(e, al, T)
    d = apparent_right_declination_sun(e, al, T)
    ec = eccentricity_sun_earth(T)
    v = true_anomaly_sun(M, C)
    R = distance_sun_earth(ec, v) * 149597870.7  # AU to km
    output = {
                "alpha": a,
                "delta": d,
                "lambda": al,
                "ecliptic_obliquity": e,
                "distance_to_earth": R
    }
    return output


def get_coordinates_moon(y, m, d):
    """
    Calculates and returns the equatorial coordinates of the Sun
    :arg:    y -> year
    :arg:    m -> month
    :arg:    d -> day
    :return: {"alpha": float, "delta": float, "lambda": float, "beta": float,
              "ecliptic_obliquity: "float, "distance_to_earth": float}
    """
    T = jde_to_T(date_to_jde(y, m, d))
    L_prime = light_time_moon(T)
    D = mean_elongation_moon(T)
    M = mean_anomaly_sun(T)
    M_prime = mean_anomaly_moon(T)
    F = mean_latitude_moon(T)
    A1 = action_venus(T)
    A2 = action_jupiter(T)
    A3 = action_earth(T)
    E = eccentricity(T)
    sl = kepler_coeff_longitude(D, M, M_prime, F, E, A1, A2, L_prime)
    sr = kepler_coeff_distance(D, M, M_prime, F, E)
    sb = kepler_coeff_latitude(D, M, M_prime, F, E, L_prime, A3, A1)
    l_moon = apparent_longitude_moon(L_prime, sl)
    b_moon = apparent_latitude_moon(sb)
    d_moon = distance_moon_earth(sr)
    e_moon = ecliptic_obliquity(T)
    a_moon = apparent_right_ascension_moon(l_moon, b_moon, e_moon) 
    d_moon = apparent_right_declination_moon(l_moon, b_moon, e_moon)
    d = distance_moon_earth(sr)
    output = {
                "alpha": a_moon,
                "delta": d_moon,
                "lambda": l_moon,
                "beta": b_moon,
                "ecliptic_obliquity": e_moon,
                "distance_to_earth": d
    }
    return output


def get_illuminated_fraction_moon(y, m, d):
    """
    See Chapter 46 (Astronomical Algorithms, Jean Meeus)
    Calculates and returns the fraction of the moon that is illuminated
    :arg:    y -> year
    :arg:    m -> month
    :arg:    d -> day
    :return: {"illuminated_fraction": float, "position_angle": float}
    """
    sun = get_coordinates_sun(y, m, d)
    moon = get_coordinates_moon(y, m, d)

    # geocentric elongation of the moon
    shi = math.acos(math.cos(math.radians(moon['beta'])) * \
                    math.cos(math.radians(moon['lambda'] - sun['lambda'])))
    
    # phase angle of the moon
    i = math.atan2(sun['distance_to_earth'] * math.sin(shi),
                   moon['distance_to_earth'] - sun['distance_to_earth'] *
                   math.cos(shi))

    k = (1 + math.cos(i)) / 2   # Ratio of the illuminated area of the moon to
                                # its total area.
                                # See p.315 for more information on what this
                                # ratio means.

    # position angle of the moon
    # Starting at the north of the disk of the moon, this is the angle swept
    # out by the area covered by light. The cusps of this area are given by
    # x + 90 and x - 90. This sweeping angle is calculated clockwise.
    # This means that when we go from new moon to the waxing period, we have
    # a x value around 270 degrees (the western part of the moon is illuminated)
    # When we wane from full moon towards first quarter however, the position
    # angle is around 90 degrees or so.
    x = math.atan2(math.cos(math.radians(sun['delta'])) *
                   math.sin(math.radians(sun['alpha'] - moon['alpha'])),
                   math.sin(math.radians(sun['delta'])) *
                   math.cos(math.radians(moon['delta'])) -
                   math.cos(math.radians(sun['delta'])) *
                   math.sin(math.radians(moon['delta'])) *
                   math.cos(math.radians(sun['alpha'] - moon['alpha'])))
    output = {
        "illuminated_fraction": k,
        "position_angle": math.degrees(x) % 360
    }
    return output


