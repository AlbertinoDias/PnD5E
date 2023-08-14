import json
import csv
import os

# List of parameters to extract from JSON
parameters = ["Name","Type","Move Power","Move Time","PP","Duration", "Range","Description","Scaling", "Save"]
# List of parameter keys for header row in CSV
csv_header = parameters

# List to store data from JSON files
data_list = []



def replace_commas_with_underscores(input_string):
    modified_string = input_string.replace(",", "_")
    return modified_string


# Loop through JSON files in the folder
for filename in os.listdir("moves_data"):
    if filename.endswith(".json"):
        with open("moves_data/"+filename, "r") as json_file:
            intermidiary = ""
            json_data = json.load(json_file)
            if "Description" in json_data:
                Description = replace_commas_with_underscores(json_data["Description"])
            else: Description = "Missing"
            if "Duration" in json_data:
                Duration = replace_commas_with_underscores(json_data["Duration"])
            else: Duration = "Missing"
            if "Move Power" in json_data:
                MovePower = json_data["Move Power"]
                for i in MovePower:
                    intermidiary = intermidiary + i + " "
            else: intermidiary = "Missing"
            if "Move Time" in json_data:
                MoveTime = replace_commas_with_underscores(json_data["Move Time"])
            else: MoveTime = "Missing"
            if "PP" in json_data:
                PP = json_data["PP"]
            else: PP = "Missing"
            if "Range" in json_data:
                Range = replace_commas_with_underscores(json_data["Range"])
            else: Range = "Missing"
            if "Save" in json_data:
                Save = replace_commas_with_underscores(json_data["Save"])
            else: Save = "Missing"
            if "Type" in json_data:
                Type = replace_commas_with_underscores(json_data["Type"])
            else: Type = "Missing"
            if "Scaling" in json_data:
                Scaling = replace_commas_with_underscores(json_data["Scaling"])
            else: Scaling = "Missing"
            name = filename[:-5]
            
            data_row = [name,Type,intermidiary,MoveTime,PP,Duration,Range,Description,Scaling,Save]
            data_list.append(data_row)

# Write data to CSV
with open("moves.csv", "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write CSV header
    csv_writer.writerow(csv_header)
    
    # Write data rows
    csv_writer.writerows(data_list)

print("CSV file 'moves.csv' created.")
