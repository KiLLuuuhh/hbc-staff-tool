# hbc_staff_tool
This repository is used to generate the timekeeper staff list

## how to run the script
1. clone the repo from this [link](https://github.com/KiLLuuuhh/hbc-staff-tool):
    `git clone git@github.com:KiLLuuuhh/hbc-staff-tool.git`
2. place the excel file in the root folder of the newly created repository.
3. create a `.env` file and extend the staff list with the current staff like:
    `staff='"staff_name_0","staff_name_1", etc'`
4. install pipenv ([info](https://pipenv.pypa.io/en/latest/installation.html)) and run the following command:
`pipenv install`
5. run the script:
    `python staff_generate.py`


