import xlwt

workbook = xlwt.Workbook()
sheet = workbook.add_sheet('PySheet1', cell_overwrite_ok=True)
sheet.write(0, 0, "Name")
sheet.write(0, 1, "Web")
sheet.write(0, 2, "CASH_BACK_HEIGHT")
sheet.write(0, 3, "TRANCHE_STMT_COUNT")
sheet.write(0, 4, "OFFER_TYPE")
sheet.write(0, 5, "ADVERT_TEXT")

sheet.write(1, 0, "Nike")
sheet.write(1, 1, "https://a3retailgroup.ru/")
sheet.write(1, 2, "4")
sheet.write(1, 3, "")
sheet.write(1, 4, "SPECIAL_CREDIT")
sheet.write(1, 5, "На покупку по кредитной карте не будут начисляться проценты, если погашать рассрочку ежемесячными платежами до даты, указанной в выписке.  Действует при оплате покупки кредитной картой только в магазинах из указанного списка. Nike – это бренд, являющийся лидером в сфере производства спортивной обуви и предметов одежды. Основанная пятьдесят лет назад, компания успела обогнать и оставить далеко позади многие другие спортивные марки.")
workbook.save("meta.xls")