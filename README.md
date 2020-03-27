# Drop_Columns_From_CSV
Python script to delete columns with specific names from csv files of big size. Do consider that the bigger the csv file is the more RAM, CPU and time will take.

This script requires the Pandas' module which can be install through pip by running the command below:
```sh
pip install pandas
```
# Usage
```sh
./Drop_Columns_From_CSV target_csv_file.csv 'column to delete 01' 'column to delete 03' 'column to delete 02'
  
Example:
        Drop_Columns_From_CSV my_csv_file.csv 'Agent ID' 'Agent Address' 'Agent Version'
```
