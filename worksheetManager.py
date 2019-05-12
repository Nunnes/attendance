
import openpyxl
import os 
from os import listdir
from os.path import isfile, join
import datetime

data_path = "./data" 

def init_attendance_excel_file():
	now = datetime.datetime.now()
	filename = str(now.year) + ".xlsx"

	print("Create attendace excel file with name: " + filename)
	filePath = data_path + "/" + filename

	if os.path.isdir(data_path)==False:
		try:
			os.mkdir(data_path)
		except OSError:
			print ("Error creating directory %s " % data_path)
			return
		else:  
			print ("Successfully created the directory %s " % data_path)

	if os.path.isfile(filePath) == False:
		wb = openpyxl.Workbook()
		months = [datetime.date(2000, m, 1).strftime('%m - %B') for m in range(1, 13)]
		
		for m in months:
			wb.create_sheet(m)
		
		wb.remove_sheet(wb.worksheets[0])
		wb.save(filePath)
	else:
		print ("File already exists: " + filePath)

def print_file_list():
	onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
	print(onlyfiles)

def get_sheet_names(filename):
	wb = openpyxl.load_workbook(data_path + "/" + filename)
	return wb.get_sheet_names()
