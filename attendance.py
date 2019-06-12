import worksheetManager
import databaseManager
import os 
from os import listdir
from os.path import isfile, join
import black_rfid_reader

import datetime

global_dataPath = "./data"

def main():

	#create data path
	print("create data path")
	create_data_path(global_dataPath)

	#init database
	print("Init database") 
	conn = databaseManager.init(global_dataPath)

	#init attendance excel file
	print("Init excel")
	filepath = worksheetManager.init_attendance_excel_file(global_dataPath)
	
	while True:
		print("Read barcode")
		rfid_code = black_rfid_reader.read_rfid()
		print(rfid_code)
		worksheetManager.write_attendance(str(rfid_code), conn)

def create_data_path(data_path):
	if os.path.isdir(data_path)==False:
		try:
			os.mkdir(data_path)
		except OSError:
			print ("Error creating directory %s " % data_path)
			return
	else:  
		print ("Successfully created the directory %s " % data_path)

if __name__ == "__main__":
	main()
