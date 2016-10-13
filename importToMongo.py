
import xlrd
import pymongo

client = pymongo.MongoClient('localhost',27017)
MiddleSchoolProject = client['MiddleSchoolProject']
high2011Score = MiddleSchoolProject['high2011Score']

def ImportData(path):
    workbook = xlrd.open_workbook(path)
    dealSheet = workbook.sheet_by_index(0)
    for i in range(1,dealSheet.nrows):
        flag = True
        for j in range(4,dealSheet.ncols):
            if dealSheet.cell_value(i,j)=='':
                flag = False
        if flag:
            personData={
                '班级':dealSheet.cell_value(i,0),
                '学号':dealSheet.cell_value(i,1),
                '姓名':dealSheet.cell_value(i,2),
                '语文1':dealSheet.cell_value(i,4),
                '语文2':dealSheet.cell_value(i,6),
                '数学1':dealSheet.cell_value(i,8),
                '数学2':dealSheet.cell_value(i,10),
                '英语1':dealSheet.cell_value(i,12),
                '英语2':dealSheet.cell_value(i,14),
                '物理1':dealSheet.cell_value(i,16),
                '化学1':dealSheet.cell_value(i,18),
                '生物1':dealSheet.cell_value(i,20),
                '历史1':dealSheet.cell_value(i,22),
                '地理1':dealSheet.cell_value(i,24),
                '政治1':dealSheet.cell_value(i,26),
            }
            high2011Score.insert_one(personData)
        else:
            continue

if __name__ == '__main__':
    path = str(input('将成绩文件放入本目录后输入文件名/或输入完全路径:'))
    ImportData(path)
    print('finall')