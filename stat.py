# -*- coding:utf-8 -*-

# 目前仍然是单进程单线程版本，5000+记录跑了大概十几分钟

import getcetgrade
import xlrd
import xlwt
import time

x1_workbook = xlrd.open_workbook('cet6.xls')
x1_sheet = x1_workbook.sheet_by_index(0)
TotalRows = x1_sheet.nrows
# print x1_sheet.cell(1,2).value
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

sta = time.time()

#原表中4428行某人叫李兆X，X无法编码……，不过反正他也没考

for rownum in range(4428,TotalRows):
	pid = x1_sheet.cell(rownum,1).value
	pname = x1_sheet.cell(rownum,2).value
	pgradedict = getcetgrade.GetCetGra(pid, pname.encode('gbk'))
	pgender = x1_sheet.cell(rownum,3).value
	pcode = x1_sheet.cell(rownum,4).value
	pdep = x1_sheet.cell(rownum,5).value
	ws.write(rownum,1,pid)
	ws.write(rownum,2,pname)
	ws.write(rownum,3,pgender)
	ws.write(rownum,4,pcode)
	ws.write(rownum,5,pdep)
	ws.write(rownum,6,pgradedict['listening'])
	ws.write(rownum,7,pgradedict['reading'])
	ws.write(rownum,8,pgradedict['writing'])
	ws.write(rownum,9,pgradedict['total'])

end = time.time()
wb.save('analysis2.xls')
print end-sta