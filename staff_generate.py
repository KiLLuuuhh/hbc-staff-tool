# 2023 | staff_generate

# import pandas
import pandas as pd
import glob
from random import randrange, shuffle
import math

# variables
file_name = glob.glob("*.xlsx")[0]
sheet = 0
last_date = ""

excel_file = pd.read_excel(io=file_name, sheet_name=sheet)

def get_random_staff():

    staff = [
        "Cyrill Dubach",
        "Cyrill Soltermann",
        "Dominic Hänni",
        "Fabian Kaufmann",
        "Kvido Schmer",
        "Mani Streit",
        "Nicola Rauch",
        "Nils Kipfer",
        "Petz Balogh",
        "Sebastian Kipfer",
        "Tim Gerber",
        "Toni Aschwanden",
        ]

    shuffle(staff)

    return staff

def isnan(value):
    try:
        math.isnan(float(value))

        return False
    except:
        return True


staff = get_random_staff()

for row in excel_file.iloc:

    # check if M2 is reponsible
    if isnan(row[0]) and "M2" in row[10]:

        if len(staff) == 0:
            staff = get_random_staff()
        
        date = str(row[0])

        if last_date != date:
                    
            staff_1 = staff.pop(randrange(len(staff)))
            staff_2 = staff.pop(randrange(len(staff)))
        
        
        time = str(row[1])
        category = str(row[3])
        home = str(row[4])
        away = str(row[5])

        last_date = date

        # get two random stuff
        print(f" {staff_1} {staff_2} {date} {time} {category} {home} {away} ")
