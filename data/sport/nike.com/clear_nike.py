import re
import xlrd
import xlwt
import os


rb = xlrd.open_workbook("v_data copy.xls", formatting_info=True)
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('PySheet1', cell_overwrite_ok=True)
sheet.write(0, 0, "Название")
sheet.write(0, 1, "Описание")
sheet.write(0, 2, "Цена")
sheet.write(0, 3, "старая цена")
sheet.write(0, 4, "путь")

sheet_r = rb.sheet_by_index(0)
rownum = 1
for t in range(1, sheet_r.nrows):
    row = sheet_r.row_values(t)
    name = row[0]
    name = re.sub(r"nike+", "", name)
    name = re.sub(r"Nike+", "", name)
    name = "Nike " + name.strip()
    if(name == "Nike"): continue
    print(name)
    sheet.write(rownum, 0, name)

    discr = row[1]
    sheet.write(rownum, 1, discr)

    price = row[2]
    sheet.write(rownum, 2, price)

    path = row[4]
    path = re.sub(r"nike+", "", path)
    path = re.sub(r"Nike+", "", path)
    sheet.write(rownum, 4, path)
    rownum += 1
workbook.save("v_data.xls")