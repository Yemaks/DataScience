from datetime import datetime


def date_difference(first_date, secont_date):
    difference = first_date - secont_date
    return print(abs(difference.days))

date_difference(datetime(2019, 6, 14), datetime(2023, 4, 2))