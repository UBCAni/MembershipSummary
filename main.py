""" Parser for condensing CSV information in the google docs """

import csv
import re

__author__ = 'Eddie'

def parse_csv(number_q, membership_q, payment_type):
    """ The 'main' function """

    with open('res/2015.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        proceeds = square = ubc_new = ubc_returning = new = returning = alumni = 0

        for row in reader:
            ans = row.get(membership_q)
            if re.search(r'\d+', ans) is not None:
                if not re.search("Alumni", row.get(number_q)):
                    val = int(re.search(r'\d+', ans).group())

                    # Pertains to 2015 onwards
                    if re.search("Credit Card", row.get(payment_type)):
                        square += val
                    else:
                        proceeds += val
                else:
                    # No payment for alumni!
                    alumni += 1

            # Count the types of returning students
            if re.search("Returning", ans):
                if not re.search("Non-UBC", ans):
                    ubc_returning += 1
                else:
                    returning += 1

            # Count the types of new students
            if re.search("New", ans):
                if not re.search("Non-UBC", ans):
                    ubc_new += 1
                else:
                    new += 1

        print_response(proceeds, square, ubc_new, ubc_returning, new, returning, alumni)

def print_response(proceeds, square, ubc_new, ubc_returning, new, returning, alumni):
    print("Total money: {}".format(proceeds))
    print("Square: {}".format(square))
    print("Cash: {}".format(proceeds - square))
    print("UBC New Members: {}".format(ubc_new))
    print("UBC Returning Members: {}".format(ubc_returning))
    print("non-UBC New Members: {}".format(new))
    print("non-UBC Returning Members: {}".format(returning))
    print("Alumni: {}".format(alumni))
    print("Total Members: {}".format(ubc_new + ubc_returning + new + returning + alumni))

if __name__ == "__main__":
    # Change the values below to account for different years
    parse_csv("Membership Number",
              "Which type of membership did you buy?",
              "How are you paying for membership today?")
