#Python script to delete columns with specific names from a csv file, this script requires the Pandas' module which can be install through pip by running the command below:
#pip install pandas

# Import necessary modules
import pandas as pd
import os
import sys
import platform

# Define global variables:
user_args = sys.argv[0:]
columns_to_delete = []
os_system = platform.system()
pwd_win = os.getcwd()+"\export_file_with_columns_deleted.csv"
pwd_lin = os.getcwd()+"/export_file_with_columns_deleted.csv"

############################# Functions ##############################
def check_input_file():
    """Function to determine if the user passed an argument to the 1st parameter"""
    if ( user_args[1:2] == [] ):
        print("\nINPUT ERROR: No file was provided as the first argument..stopping execution\n")
        print("Program usage:")
        print("              Drop_Columns_From_CSV target_csv_file.csv 'column to delete 01' 'column to delete 03' 'column to delete 02'\n")
        print('Example:')
        print("        Drop_Columns_From_CSV my_csv_file.csv 'Agent ID' 'Agent Address' 'Agent Version'\n")
        return True

def check_csv_file(file):
    """This function check wether the 1st argument is a file."""
    if os.path.isfile(file):
        print(f"SUCCESS: {file} file found\n")
        return True
    else:
        print(f"INPUT ERROR: {file} is not a file or it doesn't exist.\n")
        return False

def delete_columns(file):
    """This function is in charge of deleting the target columns"""
    print(f"INFO: Loading {file}. If the file size is more than 100MB this could take some time.")
    buffer_file = pd.read_csv(file, low_memory=False)
    try:
        print(f"INFO: Attempting to delete the {columns_to_delete} column(s)...\n")
        drop_columns= buffer_file.drop(columns_to_delete, axis = 1)
        if ( os_system == 'Windows' ):
            print("INFO: Exporting file...")
            export_csv = drop_columns.to_csv(pwd_win, index = False)
            print(f"SUCCESS: The columns were sucessfully deleted, a new file was generated:\n {pwd_win}")
        else:
            print("INFO: Exporting file")
            export_csv = drop_columns.to_csv(pwd_lin, index = False)
            print(f"SUCCESS: The columns were sucessfully deleted, a new file was generated:\n {pwd_lin}")
        return True
    except:
        print(f"INPUT ERROR: One or more of the provided column names don't exist, make sure the target columns exist, remember to use quotes for column names that contain spaces.\n")
        return False
            
def column_names(name):
    """This function reads all the column names provided by the user"""
    if name == []:
        print("INPUT ERROR: No column names were provided..exiting.\n")
        return False
    else:
        for object in name:
            new_list = [object]
            columns_to_delete.extend(new_list)
        return True
######################################################################


############################ Main Program ############################
try:
    if check_input_file() is not True:
        if check_csv_file(user_args[1]) is True:
            if column_names(user_args[2:]) is True:
                delete_columns(user_args[1])
except:
    print("Last exception triggered\n")
######################################################################