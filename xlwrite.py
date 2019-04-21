import xlwt;
from datetime import datetime;
from xlrd import open_workbook;
from xlwt import Workbook;
from xlutils.copy import copy
from pathlib import Path

def output(filename, sheet,num, name, present):
    my_file = Path('firebase/attendance_files/'+filename+str(datetime.now().date())+'.xls');
    if my_file.is_file():
        rb = open_workbook('firebase/attendance_files/'+filename+str(datetime.now().date())+'.xls');
        book = copy(rb);
        sh = book.get_sheet(0)
        
    else:
        book = xlwt.Workbook()
        sh = book.add_sheet(sheet)
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
                         num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

    
    sh.write(0,0,datetime.now().date(),style1);


    col1_name = 'Name'
    col2_name = 'Present'


    sh.write(1,0,col1_name,style0);
    sh.write(1, 1, col2_name,style0);

    sh.write(num+1,0,name);
    sh.write(num+1, 1, present);
    
    fullname=filename+str(datetime.now().date())+'.xls';
    book.save('firebase/attendance_files/'+fullname)
    return fullname;
