# 依次读入打标txt文件中每行
# 拼接每行的第一个字符（汉字），舍弃后面的打标
# 匹配空格，每句话结束以空格间隔

import csv
import re

def label2csv(path):
    with open(path,"r", encoding='utf-8') as f:
        lines = f.readlines()
        row = ''
        rows = []
        for line in lines:
            # 匹配空行（表示一句话结束）
            if re.match('^\s+$', line):
                print(row)
                rows.append([row])
                row = ''
            else:
                # row = row.join(str(line.split()[0]))
                # 每行第一个字符，后面的标签不要
                row = row + line.split()[0]
        return rows



if __name__ == '__main__':
    txt_path = 'data/ner_label/test.txt'
    csv_path = 'data/ner_csv/test.csv'
    rows = label2csv(txt_path)
    with open(csv_path, 'a+', newline='', encoding='utf-8')as f:
        f_csv = csv.writer(f)
        f_csv.writerows(rows)