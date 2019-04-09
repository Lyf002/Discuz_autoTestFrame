import xlrd
from framework.logger import Logger

logger=Logger(logger="Util").getlog()
class Util(object):
    @classmethod
    def read_excel(self,excel_path,sheetName):
        """
        思路：先读行，再读列，然后存储到声明的字典中
        :return:
        """
        workbook=xlrd.open_workbook(excel_path)
        sheet=workbook.sheet_by_name(sheetName)

        #获取第一行（表头）
        keys=sheet.row_values(0)
        #总行数
        rowNum=sheet.nrows
        #总列数
        ncloNum=sheet.ncols
        if rowNum<=1:
            logger.info("该表格中数据为空")
        else:
            r=[]
            for i in range(1,rowNum):
                dict1={ }
                values=sheet.row_values(i)
                for j in range(0,ncloNum):
                    dict1[keys[j]]=values[j]
                r.append(dict1)
            return r

if __name__=="__main__":
    print(Util.read_excel("D:/自动化测试/py_workspace/Discuz_autoTestFrame/book1.xlsx","Sheet1"))

