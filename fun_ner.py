
import csv
import re
def fun_csv():
    new_rows=[]
    with open('recipe_full_result.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            # row = re.sub('\u3002.{1,8}\uff1a', '。$', row[16]).split('：')[1:]# 匹配。：之间
            row=row[16]
            # print(row)

            if not row:
                continue
            # lines = row[0].split('$')
            lines = row.split('。')

            for line in lines:
                if not line:
                    continue
                print(line)
                new_rows.append([line])
    with open('ING_r_origin.csv', 'a+', newline='')as f:
        f_csv = csv.writer(f)
        # f_csv.writerow(['headers'])
        f_csv.writerows(new_rows)

# 依次读入csv文件中每行句子
# 每个字为一行，并在末尾加“ O”
# 每句话“。”结束以空格间隔
def fun_bios():
    new_rows=[]
    with open('ING_r_origin.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        result = []
        for row in reader:
            if not row:
                continue
            for line in row:
                for item in line:
                    # print(item+' O')
                    result.append([item+' O'])
                    if item == '。':
                        result.append([''])
    # print(result)
    with open('ING.txt','a+',encoding='utf-8') as f:
        for res in result:
            print(res)
            f.write(str(res[0])+'\n')
if __name__ == '__main__':
    # fun_csv()
    fun_bios()