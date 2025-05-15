import os
def list_of_all_files():
    daily_files_path=os.path.join(os.getcwd(),"daily_files")
    list_of_files=os.listdir(daily_files_path)
    # print(list_of_files)
    list_of_files_path=[]
    for file in list_of_files:
        list_of_files_path.append(os.path.join(daily_files_path,file))
    return list_of_files_path
