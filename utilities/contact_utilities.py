import string
import random


def get_option_number_for_month(month):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return months.index(month)


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digits(maxlen):
    return "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])


months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


def generate_random_valid_day():

    month = random.choice(months)
    year = random.randrange(1900, 2001)

    if month == "February":
        if (year % 4 > 0) or ((year % 100 == 0) and (year % 400 > 0)):
            day = random.randrange(1, 29) # 1..28
        else:
            day = random.randrange(1, 30) # 1..29
    elif month in ["April", "June", "September", "November"]:
        day = random.randrange(1, 31) # 1..30
    else:
        day = random.randrange(1, 32) # 1..31

    return [day, month, year]
