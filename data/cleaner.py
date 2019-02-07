import re
import xlrd
import xlwt
import os

pa = ['/Users/kalugin/git_proj/mipt_tinkoff_hackathon_2019/data/food/',
         '/Users/kalugin/git_proj/mipt_tinkoff_hackathon_2019/data/sport/']

files = []
for p in pa:
    files += [f.path for f in os.scandir(p) if f.is_dir()]
# print(files)

def get_value(s):
    s = str(s)
    s = re.sub(r"\.+$", "", s)
    s = re.sub(r",", ".", s)
    s = re.sub(r"[^\d+\.]", "", s)
    return s


for fl in files:
    try:
        rb = xlrd.open_workbook(fl + "/data_cleaned.xls", formatting_info=True)
    except FileNotFoundError:
        continue
    print(fl)

    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('PySheet1', cell_overwrite_ok=True)
    sheet.write(0, 0, "Название")
    sheet.write(0, 1, "Описание")
    sheet.write(0, 2, "Цена")
    sheet.write(0, 3, "старая цена")
    sheet.write(0, 4, "путь")

    sheet_r = rb.sheet_by_index(0)
    for rownum in range(1, sheet_r.nrows):
        row = sheet_r.row_values(rownum)
        name = row[0].split('~')[-1]
        sheet.write(rownum, 0, name)

        discr = row[1]
        sheet.write(rownum, 1, discr)

        price = get_value(row[2])
        sheet.write(rownum, 2, price)

        path = "~".join(row[0].split('~')[:-1])
        sheet.write(rownum, 4, path)
        workbook.save(fl + "/v_data.xls")