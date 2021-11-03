#install the package openpyxl for read/write document excel
#pip install openpyxl

import openpyxl 

document_excel = openpyxl.load_workbook("inventory.xlsx") #load the file of excel
elements_sheet =  document_excel["part_1"] #put the name of the sheet of excel

#show the element of the document as a dictionary
element_excel = {}

#use looping for go through each and every row in the sheet and execute same logic 
#on each item and repeat the loop the number of row of the table of elements

#max_row show the number maximum of row for element of the sheet
#range - create a sequence of integer numbers (value valid for loop)
for element_row in range(2, elements_sheet.max_row): #is two because the list of element start in the row two
