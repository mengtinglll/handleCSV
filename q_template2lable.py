import csv

class Q_template:
    ING_list = [['牛 B-ING', '奶 I-ING'], ['西 B-ING', '瓜 I-ING']]
    DIS_list = []
    FUN_list = []
    NUT_list = []
    REC_list = []
    ING_index = 0
    DIS_index = 0
    FUN_index = 0
    NUT_index = 0
    REC_index = 0
    def ING_LIST(self,start = 0,end = 80):
        with open('data/question/ING.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            ING_lables = []
            for i, row in enumerate(reader):
                if i>= start and i < end:
                    for n, word in enumerate(row):
                        ING_lable = []
                        for j, letter in enumerate(word):
                            if j == 0:
                                ING_lable.append(letter + ' B-ING')
                            else:
                                ING_lable.append(letter + ' I-ING')
                    ING_lables.append(ING_lable)
                else:
                    continue
            self.ING_list = ING_lables
            print(self.ING_list)
            return 0
    def DIS_LIST(self,start = 0,end = 80):
        with open('data/question/DIS.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            ING_lables = []
            for i, row in enumerate(reader):
                if i>= start and i < end:
                    for n, word in enumerate(row):
                        ING_lable = []
                        for j, letter in enumerate(word):
                            if j == 0:
                                ING_lable.append(letter + ' B-DIS')
                            else:
                                ING_lable.append(letter + ' I-DIS')
                    ING_lables.append(ING_lable)
                else:
                    continue
            self.DIS_list = ING_lables
            return 0
    def NUT_LIST(self,start = 0,end = 80):
        with open('data/question/NUT.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            ING_lables = []
            for i, row in enumerate(reader):
                if i>= start and i < end:
                    for n, word in enumerate(row):
                        ING_lable = []
                        for j, letter in enumerate(word):
                            if j == 0:
                                ING_lable.append(letter + ' B-NUT')
                            else:
                                ING_lable.append(letter + ' I-NUT')
                    ING_lables.append(ING_lable)
                else:
                    continue
            self.NUT_list = ING_lables
            return 0
    def FUN_LIST(self,start = 0,end = 80):
        with open('data/question/FUN.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            ING_lables = []
            for i, row in enumerate(reader):
                if i>= start and i < end:
                    for n, word in enumerate(row):
                        ING_lable = []
                        for j, letter in enumerate(word):
                            if j == 0:
                                ING_lable.append(letter + ' B-FUN')
                            else:
                                ING_lable.append(letter + ' I-FUN')
                    ING_lables.append(ING_lable)
                else:
                    continue
            self.FUN_list = ING_lables
            return 0
    def REC_LIST(self,start = 0,end = 80):
        with open('data/question/REC.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            ING_lables = []
            for i, row in enumerate(reader):
                if i>= start and i < end:
                    for n, word in enumerate(row):
                        ING_lable = []
                        for j, letter in enumerate(word):
                            if j == 0:
                                ING_lable.append(letter + ' B-REC')
                            else:
                                ING_lable.append(letter + ' I-REC')
                    ING_lables.append(ING_lable)
                else:
                    continue
            self.REC_list = ING_lables
            return 0

    def lable(self,sentence):
        lable = []
        sentence = sentence.replace('【食材】','@').replace('【疾病】',"#").replace('【功效】',"&").replace('【营养素】',"*").replace('【食谱】',"+")
        for word in sentence:
            # 食材
            if word == '@':
                for item in self.ING_list[self.ING_index]:
                    lable.append(item)
                self.ING_index = self.ING_index + 1
                if self.ING_index == 80:
                    self.ING_index = 0
            # 疾病
            elif word == '#':
                for item in self.DIS_list[self.DIS_index]:
                    lable.append(item)
                    self.DIS_index = self.DIS_index + 1
                    if self.DIS_index == 50:
                        self.DIS_index = 0
            # 功效
            elif word == '&':
                for item in self.FUN_list[self.FUN_index]:
                    lable.append(item)
                    self.FUN_index = self.FUN_index + 1
                    if self.FUN_index == 150:
                        self.FUN_index = 0
            # 营养素
            elif word == '*':
                for item in self.NUT_list[self.NUT_index]:
                    lable.append(item)
                    self.NUT_index = self.NUT_index + 1
                    if self.NUT_index == 60:
                        self.NUT_index = 0
            # 食谱
            elif word == '+':
                for item in self.REC_list[self.REC_index]:
                    lable.append(item)
                    self.REC_index = self.REC_index + 1
                    if self.REC_index == 400:
                        self.REC_index = 0
            else:
                lable.append(word+' O')
        return lable
    def write_txt(self,dir,result):
        with open(dir, 'a+', encoding='utf-8') as f:
            for res in result:
                print(res)
                f.write(res+'\n')
            f.write('\n')
    def read_excel(self,file):
        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, rows in enumerate(reader):
                for j, row in enumerate(rows):
                    # 选用1到5，这5个句式
                    if j>0 and j<10:
                        # 一个句式重复用5次
                        for n in range(5):
                            result = self.lable(row)
                            # print('两个食材',result)
                            self.write_txt('data/question/r.txt',result)



if __name__ == '__main__':

    filepath = "data/question/question_template.csv"
    q = Q_template()
    q.ING_LIST(0, 80)
    q.DIS_LIST(0, 50)
    q.FUN_LIST(0, 150)
    q.NUT_LIST(0, 60)
    q.REC_LIST(0, 400)
    result = q.read_excel(filepath)
    # print(result)