import os

#Function to convert the file size from bytes to mega kilo and giga
def file_size_process(file_size):
    # Define conversion constants
    KB, MB, GB = 1024, 1024**2, 1024**3

    # Determine the most appropriate unit for the file size
    if file_size < MB:
        size, unit = file_size / KB, 'Kilobytes'
    elif file_size < GB:
        size, unit = file_size / MB, 'Megabytes'
    else:
        size, unit = file_size / GB, 'Gigabytes'
    
    return_str = str(size)+" "+unit
    
    return return_str

  
#Function to get the file sixe and the extension of the file

def Get_file_Extension_and_Size(fullpath_str):
    Path_Parts = fullpath_str.split("/")
    File_Name = Path_Parts[-1]
    #os.path.splitext() method in Python is used to split the path name into a pair root and ext. Here, ext stands for extension and has the extension portion of the specified path while root is everything except ext part.
    #ext is empty if specified path does not have any extension. If the specified path has leading period (‘.’), it will be ignored.
    Split_Tuple = os.path.splitext(File_Name)
    name = Split_Tuple[0]
    extension = Split_Tuple[1]
    #The method os.path.getsize method returns a integer value which represents the size of specified path in bytes.
    file_size = os.path.getsize(fullpath_str)
    full_file_size = file_size_process(file_size)
    return_tuple = (name,extension,full_file_size)
    return return_tuple

    


def directory_scanner(directory_to_scan):
    result = []
    # for each file name in the list created by 
    for filename in os.listdir(directory_to_scan):
        fullpath_str = directory_to_scan + "/" + filename
        #os.apth.isdir checks if the file path is a directory if it is a new scan is done in the new path trought iteration
        if os.path.isdir(fullpath_str):
            loc_res = directory_scanner(fullpath_str)
            result += loc_res
        #os.path.isfile checks if the path is really a file if it is a function is called to the path to get its datas
        elif os.path.isfile(fullpath_str):
            File_Datas = Get_file_Extension_and_Size(fullpath_str)
            result.append(File_Datas)
       
    #  The resulting tuple list is sorted based on the second element the size so the tuple list will be sorted uscing the second element of each tuple
    return sorted(result, key=lambda x: x[1] )

directory_to_scan = os.getcwd()
out_list = directory_scanner(directory_to_scan)

for item in out_list:
    print(item)
