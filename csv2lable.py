# 依次读入csv文件中每行句子
# 每个字为一行，并在末尾加“ O”
# 每句话结束以空格间隔

import csv
import re
def fun_bios(file,dir):
    new_rows=[]
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        result = []
        for row in reader:
            if not row:
                continue
            for line in row:
                for item in line:
                    # print(item+' O')
                    result.append([item+' O'])
            result.append([''])
    # print(result)
    with open(dir,'a+',encoding='utf-8') as f:
        for res in result:
            print(res)
            f.write(str(res[0])+'\n')
if __name__ == '__main__':
    file = 'data/re_csv/train.csv'
    dir = 'data/re_label/ing_train.txt'
    # fun_csv()
    fun_bios(file,dir)