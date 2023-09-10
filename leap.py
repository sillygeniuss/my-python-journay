def leap_year(year):
    res = False
    if year % 4 == 0:
        res = True
        if year % 100 == 0:
            res = False
            if year % 400 == 0:
                res = True
    return res
    pass
