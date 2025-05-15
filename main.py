from utils_file.list_of_all_files import list_of_all_files
from business_logic.read_csv_files import read_csv_files
from business_logic.segregate_data import segregate_data
from utils_file.citywise_directory import create_citywise_directory_and_dump_data
from utils_file.dump_files import dump_into_processedFiles_and_others


def main():

    list_of_files_path=list_of_all_files()

    endswith=".csv"
    data=read_csv_files(list_of_files_path,endswith)

    citywise_data=segregate_data(data)

    del data
    create_citywise_directory_and_dump_data(citywise_data)


    dump_into_processedFiles_and_others(list_of_files_path)

if __name__=="__main__":
    main()


