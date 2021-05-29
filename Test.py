import info

user_input = ""
while user_input != "exit":
    user_input = input("_message")
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days":days_and_unit[0], "units":days_and_unit[1]}
    info.validate_and_process()
    