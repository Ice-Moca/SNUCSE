def leap_year_checker(target_year):
    leap_year = False
    if target_year in [-45, -42, -39, -33, -30, -27, -24, -21, -18, -15, -12, -9, 8, 12]:
        leap_year = True
    #
    elif target_year > 12 and target_year % 4 == 0:
        leap_year = True
        if target_year % 100 == 0:   
              leap_year = False
        if target_year % 400 == 0:    
              leap_year = True
    return leap_year