# 2023 | staff_generate

# import pandas
import pandas as pd
import glob
import os
import random
from random import randrange, shuffle
import math
from typing import List
import ast


# variables
file_name = glob.glob("*.xlsx")[0]
sheet = 0
last_date = ""

excel_file = pd.read_excel(io=file_name, sheet_name=sheet)

def get_random_staff() -> List[str]:

    staff_string = os.getenv("staff")

    if not staff_string:
        raise ValueError("Environment variable 'staff' is not set or is empty.")

    # Parse the string into a list, handling quotes and commas
    try:
        staff_list = ast.literal_eval(f"[{staff_string}]")
    except (ValueError, SyntaxError) as e:
        raise ValueError("Failed to parse the 'staff' environment variable. Ensure it uses proper formatting.") from e

    # Shuffle the staff list
    random.shuffle(staff_list)

    return staff_list

def isnan(value) -> bool:
    try:
        math.isnan(float(value))

        return False
    except:
        return True


staff = get_random_staff()

for row in excel_file.iloc:

    # check if M3 is reponsible
    if isnan(row[0]) and "M3-Team 1" in row[10]:

        if len(staff) == 0:
            staff = get_random_staff()

        date = str(row[0])

        if last_date != date:

            staff_1 = staff.pop(randrange(len(staff)))
            staff_2 = staff.pop(randrange(len(staff)))


        time = str(row[1])
        category = str(row[2])
        home = str(row[3]).strip()
        away = str(row[4]).strip()

        last_date = date

        # get two random staff
        print(f"{staff_1} {staff_2} {date} {time} {category} {home} vs. {away} ")
