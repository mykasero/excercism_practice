# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry:
    def __init__(self, date, description, change):
        self.date = date
        self.description = description
        self.change = change



def create_entry(date, description, change):
    entry = LedgerEntry(datetime.strptime(date, '%Y-%m-%d'), description, change)

    return entry

def money_format(change, locale):
    formatted = ""

    # formatting the change, X is a placeholder to later be replaced by a currency symbol

    if change < -100000:
        if locale == "en_US":
            formatted = "(X" + str(change)[1] + "," + str(change)[2:5] + "." + str(change)[5:len(str(change))] + ")"
        else:
            formatted = "(X " + str(change)[1] + "," + str(change)[2:5] + "." + str(change)[5:len(str(change))] + ")"
    elif -100000 < change < -10000:
        if locale == "en_US":
            formatted = "(X" + str(change)[1:4] + "." + str(change)[4:len(str(change))] + ")"
        else:
            formatted = "X " + str(change)[0:4] + "," + str(change)[4:len(str(change))]
    elif -10000 < change < -1000:
        formatted = "(X" + str(change)[1:3] + "." + str(change)[3:len(str(change))] + ")"
    elif -1000 <= change < -99:
        formatted = "(X" + str(change)[0:len(str(change))-2] + "." + str(change)[len(str(change))-2:len(str(change))] + ")"
        formatted = formatted.replace("-","")
    elif -99 <= change < -9:
        formatted = "(X0." + str(change)[len(str(change)) - 2:len(str(change))] + ")"
        formatted = formatted.replace("-", "")
    elif -9 <= change < 0:
        formatted = "(X0.0" + str(change)[len(str(change)) - 1] + ")"
        formatted = formatted.replace("-", "")
    elif 0 <= change < 10:
        formatted = "X0.0" + str(change)[len(str(change)) - 1]
    elif 10 <= change < 1000:
        formatted = "X0." + str(change)[len(str(change)) - 1]
    elif 1000 <= change < 10000:
        if locale == "en_US":
            formatted = "X" + str(change)[0:2] + "." + str(change)[2:len(str(change))]
        else:
            formatted = "X " + str(change)[0:2] + "," + str(change)[2:len(str(change))]
    elif 10000 < change < 100000:
        if locale == "en_US":
            formatted = "X" + str(change)[0:len(str(change))-2] + "." + str(change)[len(str(change))-2:len(str(change))]
        else:
            formatted = "X " + str(change)[0:len(str(change)) - 2] + "." + str(change)[len(str(change)) - 2:len(str(change))]
    elif 100000 < change < 1000000:
        if locale == "en_US":
            formatted = "X" + str(change)[0] + "." + str(change)[1:len(str(change))-2] + "." + str(change)[len(str(change))-2:len(str(change))]
        else:
            formatted = "X " + str(change)[0] + "." + str(change)[1:len(str(change))-2] + "," + str(change)[len(str(change))-2:len(str(change))]

    return formatted


def format_entries(currency, locale, entries):
    # first | at 11th spot, second at 39th, total len 0-51
    p1 = ""
    p2 = ""
    p3 = ""
    new_line = ""

    currencies_dict = {"USD" : "$", "EUR" : "€"}

    '''
    lens
    p1 = 12 ends with |
    p2 = 28 (space at the start) ends with |
    p3 = 14 (space at the start)
    '''

    lines = []
    final = ""
    if locale == "en_US":
        template = "Date       | Description               | Change       "
    else:
        template = "Datum      | Omschrijving              | Verandering  "
    if not entries:
        return template

    else:
        lines.append(template)

        years = []
        months = []
        days = []
        desc = []
        currencies = []
        total = []
        correct_list = []
        
        for item in entries:
            years.append(item.date.year)
            months.append(item.date.month)
            days.append(item.date.day)
            desc.append(item.description)
            currencies.append(item.change)
            total.append([item.date.year, item.date.month, item.date.day, item.description, item.change])

        if len(list(set(years))) == 1 and len(list(set(months))) == 1 and len(list(set(days))) > 1:
            days.sort()

            for i in range(len(days)):
                for j in range(len(total)):
                    if days[i] == total[j][2]:
                        correct_list.append(total[j])
        else:
            currencies.sort()

            for i in range(len(currencies)):
                for j in range(len(total)):
                    if currencies[i] == total[j][4]:
                        correct_list.append(total[j])

        for item in correct_list:
            #choosing date format based on locale
            if locale == "en_US":
                p1 = datetime.strftime(datetime(item[0],item[1],item[2]),"%m/%d/%Y")
            else:
                p1 = datetime.strftime(datetime(item[0], item[1], item[2]), "%d-%m-%Y")
            p2 = item[3]
            # replacing placeholder with currency symbol
            p3 = money_format(item[4],locale).replace("X",currencies_dict[currency])


            # adding whitespace to align the desired formatting
            if len(p1) < 12:
                p1 += (11-len(p1)) * " " + "|"

            if len(p2) < 26:
                p2 = " " + p2 + (26-len(p2)) * " " + "|"
            elif len(" "+p2) >= 26:
                p2 = " " + p2[:22] + "..." + " " + "|"


            if len(p3) < 14:
                if "(" in p3:
                    p3 = " " + (13-len(p3)) * " " + p3
                else:
                    p3 = " " + (12 - len(p3)) * " " + p3 + " "


            new_line = p1 + p2 + p3
            lines.append(new_line)
            new_line = ""

        # #turn list into a string with new liners
        for i in range(len(lines)):
            if i < len(lines) - 1:
                final += lines[i] + "\n"
            else:
                final += lines[i]


        return final

'''
Instructions
Refactor a ledger printer.

The ledger exercise is a refactoring exercise. There is code that prints a nicely formatted ledger, 
given a locale (American or Dutch) and a currency (US dollar or euro). The code however is rather badly written, 
though (somewhat surprisingly) it consistently passes the test suite.

Rewrite this code. Remember that in refactoring the trick is to make small steps that keep the tests passing. 
That way you can always quickly go back to a working version. Version control tools like git can help here as well.

Please keep a log of what changes you've made and make a comment on the exercise containing that log, this will help reviewers.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/ledger/canonical-data.json
