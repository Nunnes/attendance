import random
import rfid_reader
import openpyxl
import os 
from os import listdir
from os.path import isfile, join

data_path = "./data" 

def main():

	#Reading RFID code
	rfid_code = rfid_reader.read_rfid()
	print("rfid code: " + str(rfid_code))

	init_attendance_excel_file("teste001.xlsx")

	# Load in the workbook
	wb = openpyxl.load_workbook(data_path+"/teste001.xlsx")

	# Get sheet names
	print(wb.get_sheet_names())

	list_file_list();


def init_attendance_excel_file(filename):
	print("Create attendace excel file with name: " + filename)
	filePath = data_path + "/" + filename

	if os.path.isdir(data_path)==False:
		try:
			os.mkdir(data_path)
		except OSError:
			print ("Error creating directory: " + data_path)
			return
		else:  
			print ("Successfully created the directory %s " % data_path)

	if os.path.isfile(filePath) == False:
		wb = openpyxl.Workbook()
		wb.save(filePath)
	else:
		print ("File already exists: " + filePath)

def list_file_list():
	onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
	print(onlyfiles)

if __name__ == "__main__":
	main()
