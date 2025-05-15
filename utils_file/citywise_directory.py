import os
import csv
import datetime

def get_file_name(city_name):
    today = str(datetime.datetime.now())[:11:]
    csv_filename = city_name + '_' + today + '_.csv'
    return csv_filename

def make_dir(city_name):
    city_dir_path = os.path.join(os.getcwd(), 'Cities', city_name)
    os.makedirs(city_dir_path, exist_ok=True)
    return city_dir_path

def create_citywise_directory_and_dump_data(citywise_data):

    for city in citywise_data.items():

        city_name = city[0]
        city_dir_path = make_dir(city_name)
        csv_filename = get_file_name(city_name)

        final_csv_file_path=os.path.join(city_dir_path,csv_filename)

        with open(final_csv_file_path,"w",newline='') as fp:

            obj=csv.DictWriter(fp,fieldnames= city[1][0].keys())
            obj.writeheader()
            obj.writerows(city[1])



