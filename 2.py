def write_3pair(fn, conts):
    """
    写(实体-实体-关系)对到文件中
    """
    with open(fn, 'w') as f:
        # 第一行写入数据个数
        f.write('%d\n' % len(conts))
        for cont in conts:
            f.write('%s\t%s\t%s\n' % (cont[0], cont[1], cont[2]))
        # for cont in conts:
        #     print(cont)
        #     f.write('%s\t%d\n' % (cont[0], cont[1]))

if __name__ == '__main__':
    # fn ='D:\\毕业\\开题\\thesis\\原始数据\\KGE\\data1\\test\\valid2id.txt'
    # conts=[[0,1,0],[0,2,1],[1,2,0]]
    # write_3pair(fn,conts)
    art1 = open(r'D:\毕业\开题\thesis\原始数据\KGE\data1\LMT\train2id.txt', 'r',encoding='utf-8')  # 查看新的文件的内容

    print(art1.readlines())
    # print(len(b))
    # for c in b:
    #     print('5')
    art1.close()