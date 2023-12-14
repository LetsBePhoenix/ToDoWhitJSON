# Import all modules that are needed
import json

# Create all variables that are important to run the program
new_open = True
connection_string = "L:\\00_Public\\an_FB\\Projekte mit Flamur\\To_Do_List\\values.json"
list = {
    "ID": 1,
    "DbV": 0.1,
    "value1": False
}


# is used to load values from the json
def load_values():
    print("INFO: Import data from JSON")
    with open(connection_string, "r") as json_file:
        loaded_data = json.load(json_file)
    list["ID"] = loaded_data["ID"]
    list["DbV"] = loaded_data["DbV"]
    for i in range(loaded_data["ID"]):
        list[str("value" + str(i + 1))] = loaded_data[str("value" + str(i + 1))]
    print("INFO: Import completed")


# is used to send values to the JSON
def send_values():
    print("INFO: Export data to JSON")
    with open(connection_string, "w") as json_file:
        json.dump(list, json_file, indent=4)
    print("INFO: Export completed")


# ----------------------------------------------------------------------------------------------------------------------

# is used to create a new save in the json
def create_new_input(value):
    print("INFO: Input incoming")
    list[str("value" + str(list["ID"] + 1))] = str(value)
    list["ID"] = list["ID"] + 1
    print("INFO: Input was written in list")


# is used to mark a task as finished
def finished_task(value):
    list[str("value" + str(value))] = True


# is used to load and save all data
# load all values from the json
def renew_values():
    try:
        send_values()
        load_values()
    except FileNotFoundError:
        print("ERROR: JSON-File not found")
        print("ECC: Create new JSON file")
        with open(connection_string, "w") as json_file:
            json.dump(list, json_file, indent=4)
        print("ECC: Completed")
    except:
        print("FATAL_ERROR: Unknown failre")


def renew_db():
    for i in range(list["ID"]):
        if i:
            list[str("value" + str(i))] = list[str("value" + str(i + 1))]
            list[str("value" + str(i + 1))] = True


# ----------------------------------------------------------------------------------------------------------------------

load_values()
while True:
    eingabe = input("TEST: ")
    if eingabe == "save":
        renew_values()
    if eingabe == "new":
        eingabe = input("Eingabe: ")
        create_new_input(eingabe)
        renew_values()
    if eingabe == "finish":
        eingabe = input("Eingabe: ")
        finished_task(eingabe)
    if eingabe == "exit":
        exit()
    if eingabe == "show":
        print(list)
