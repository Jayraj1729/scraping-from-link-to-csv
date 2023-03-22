#import openpyxl

#from openpyxl import load_workbook
#from openpyxl import Workbook
 
# import xlsxwriter module
import xlsxwriter
r=40
        # Workbook() takes one, non-optional, argument
        # which is the filename that we want to create.
#workbook = xlsxwriter.Workbook(('sample{}.xlsx'.format(i))for i in range(1, 6))
#xlsxwriter.Workbook('sample{}.xlsx'.format(i)).close() for i in range(1, 6))
    
#[xlsxwriter.Workbook('sample{}.xlsx'.format(i))for i in range(1, 6)]



        # The workbook object is then used to add new
        # worksheet via the add_worksheet() method.
#worksheet = workbook.add_worksheet()

        # Use the worksheet object to write
        # data via the write() method.
for i in range(1, r):
    data = ['1', '2', 'a', 'not good', 'excellent'+str(i)+'']
    print(data)
    workbook = xlsxwriter.Workbook(('sample{}.xlsx'.format(i))for i in range(1, r))
    worksheet = workbook.add_worksheet()

    worksheet.write_row(1+i, 0, data)
    workbook.close()
    #i +=1
    # Finally, close the Excel file
    # via the close() method.
#workbook.close()
