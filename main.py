import csv
import re

# 处理功效数组，去除不相干功效
def handle_effect(new_rows,item,new_row_start):
    if item.find('食谱') != -1 or item.find('年夜饭') != -1 or item.find('菜') != -1 or item.find('膳食') != -1:
        print('含有食谱~~~~~~~~~~~~~~~~')
    else:
        new_rows.append([new_row_start, 'has', item])
    return new_row_start

# 处理主料数组，去除克数
def handle_material(material):
    s = re.sub('[\d{n}克]','', material)
    s = s.replace(',','')
    return s

def read(headers,new_file,row_start,row_end):
    with open('recipe_full_result.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)

        with open(new_file, 'w',newline='')as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)
        for row in reader:
            # 功效
            new_rows = []
            new_row_start = row[row_start]
            if row[row_end] == '':
                continue
            # new_rows.append([new_row_start,'contains',handle_material(row[row_end])])
            items = row[row_end].split(',')
            # print(funs)
            # 进行处理
            for item in items:
                # new_rows.append([new_row_start, 'contains', item])
                handle_effect(new_rows,item,new_row_start)

            print(new_rows)

            with open(new_file,'a+',newline='')as f:
                f_csv = csv.writer(f)
                f_csv.writerows(new_rows)

def find():
    with open('ner.train', 'w', newline='')as f:
        lines =1



if __name__ == '__main__':
    # 功效
    # headers = ['recipe', 'rel', 'effect']
    # new_file = 'effect.csv'
    # row_start = 0
    row_end = 4

    # 主料
    # headers = ['recipe', 'rel', 'nutrient']
    # new_file = 'nutrient.csv'
    # row_start = 0
    # row_end = 9
    # read(headers,new_file,row_start,row_end)

    # f(['营养不良调理', '健脾开胃调理', '青少年食谱', '老人食谱'])


