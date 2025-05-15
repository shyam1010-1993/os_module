import shutil
import os
def dump_into_processedFiles_and_others(list_of_files_path):
    csv_dest_path = os.path.join(os.getcwd(), 'processed files')
    other_dest_path=os.path.join(os.getcwd(),'other files')
    for file_path in list_of_files_path:
        if file_path.endswith('.csv'):
            shutil.move(file_path,csv_dest_path)
        else:
            shutil.move(file_path,other_dest_path)



