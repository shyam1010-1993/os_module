import csv
def read_csv_files(list_of_files_path,endswith):
    data=[]
    for file in list_of_files_path:
        if file.endswith(endswith):
            with open(file) as fp:
                data.extend(list(csv.DictReader(fp)))
    return data


