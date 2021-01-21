import csv
import re

def writefile(arr):
    with open(csv_path, 'a+', newline='', encoding='utf-8')as f:
        f_csv = csv.writer(f)
        f_csv.writerows(arr)
def h_sub_row(row,entities):
    # print(row,entities)
    new_row = []
    ING = []
    NUT = []
    DIS = []
    FUN = []
    for entity in entities:
        if 'ING' in entity.keys():
            ING.append(list(entity.values())[0])
        if 'NUT' in entity.keys():
            NUT.append(list(entity.values())[0])
        if 'DIS' in entity.keys():
            DIS.append(list(entity.values())[0])
        if 'FUN' in entity.keys():
            FUN.append(list(entity.values())[0])
    for ing in ING:
        for sub_ing in ING:
            if ing[0] == sub_ing[0]:
                # print('同名删除', ing, sub_ing)
                continue
            elif ing[1] >= sub_ing[1]:
                continue
                # print('同类删除', ing, sub_ing)
            else:
                new_row.append([row,'忌搭配',ing[0],ing[1],sub_ing[0],sub_ing[1]])
                # print('搭配',ing,sub_ing)
        for sub_fun in FUN:
            new_row.append([row, '具有功效',ing[0],ing[1], sub_fun[0],sub_fun[1]])
            # print('食材功效',ing,sub_fun)
        for sub_nut in NUT:
            new_row.append([row, '含有营养素', ing[0],ing[1], sub_nut[0], sub_nut[1]])
            # print('食材营养素', ing, sub_nut)
        for sub_dis in DIS:
            new_row.append([row, '利于疾病', ing[0],ing[1], sub_dis[0], sub_dis[1]])
            # print('食材疾病', ing, sub_dis)

    for nut in NUT:
        # for sub_fun in FUN:
            # print('营养素功效', nut, sub_fun)
            # new_row.append([row, '营养素功效',nut[0],nut[1], sub_fun[0], sub_fun[1]])
        for sub_dis in DIS:
            # print('营养素疾病', nut, sub_dis)
            new_row.append([row, '营养素疾病', nut[0],nut[1], sub_dis[0],sub_dis[1]])
    return new_row

def label2csv(path):
    with open(path,"r", encoding='utf-8') as f:
        lines = f.readlines()
        row = ''
        rows = []
        entity = ''
        entities = []
        num = 0
        for line in lines:
            # 为空，表示一句话结束
            if re.match('^\s+$', line):
                # print(row)
                # print(entities)
                sub_row=h_sub_row(row, entities)
                if sub_row:
                    writefile(sub_row)
                # rows.append(sub_row)
                row = ''
                entity=''
                entities = []
                num = 0
            else:
                # 遇到新的实体
                if re.search('B-', line):
                    # 记录开头实体下标
                    if not entity:
                        N = num
                    # 连续实体，遇到下一个实体时，存储上一个实体
                    if entity:
                        entities.append({e_type1:[entity,N]})
                        N = num
                    entity = ''
                    e_type1 = line.split('B-')[-1].replace("\n", "")
                    entity = entity+line.split()[0]
                    # print('type',e_type1)
                elif re.search('O', line):
                    # 完成存储
                    if entity:
                        entities.append({e_type1:[entity,N]})
                    entity = ''
                else:
                    entity = entity + line.split()[0]
                num = num + 1
                row = row + line.split()[0]

        return rows



if __name__ == '__main__':
    csv_path = 'data/re_csv/re_train2.csv'
    with open(csv_path, 'a+', newline='', encoding='utf-8')as f:
        f_csv = csv.writer(f)
        f_csv.writerow(['sentence','relation','head','head_offset','tail','tail_offset'])

    txt_path = 'data/ner_label/ner.train'
    rows = label2csv(txt_path)

