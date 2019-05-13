import rfid_reader
import worksheetManager

import openpyxl
import datetime

def main():

	#Reading RFID code
	rfid_code = rfid_reader.read_rfid()
	print("rfid code: " + str(rfid_code))

	worksheetManager.init_attendance_excel_file()
	
	print("Sheet Names:")
	filename = str(datetime.datetime.now().year) + ".xlsx"
	print(worksheetManager.get_sheet_names(filename))

	while True:
		code = raw_input('Enter your input:')
		worksheetManager.write_attendance(code)
	
if __name__ == "__main__":
	main()
