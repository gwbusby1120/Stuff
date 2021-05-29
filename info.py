units_calc = 24
name_of_units = "hours"

def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} day(s) have {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} day(s) have {num_of_days * 24*60} hours"

def validate_and_process(days_and_unit_dictionary):
    try:

        user_input_num = int(days_and_unit_dictionary["days"])
        if user_input_num > 0:
            calc_value = days_to_units(user_input_num, days_and_unit_dictionary["units"] )
            print(calc_value)
        elif user_input_num == 0:
            print("Do not enter 0")
        elif user_input_num < 0:
            print("Do Not eneter a negative value")
      
    except ValueError:
        print("input not accepted")

user_input_message = "Enter days and units"