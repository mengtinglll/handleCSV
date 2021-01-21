import csv
import re
def read():
    with open('data/re_csv/ING_r_origin(less).csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        row_arr = []
        for row in reader:

            row_strs = row[0].split('：')[1:]
            # print(row_strs)
            if row_strs:
                row_arr.append(row_strs)
            # for row_str in row_strs:
            #     row_arr.append(row_str.split('；'))[]
            #     print(row_arr)
        print(row_arr)
        return row_arr

if __name__ == '__main__':
    # read()
    txt_path = 'data/ner_label/test.txt'
    csv_path = 'data/re_csv/train.csv'
    rows = read()
    with open(csv_path, 'a+', newline='', encoding='utf-8')as f:
        f_csv = csv.writer(f)
        f_csv.writerows(rows)