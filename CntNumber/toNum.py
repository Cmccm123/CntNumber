def toNum(inp):
    num_d = {
    '〇': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '零': 0,
    '壹': 1, '貳': 2, '叁': 3, '肆': 4, '伍': 5, '陸': 6, '柒': 7, '捌': 8, '玖': 9, '貮': 2, '兩': 2}
    unit_d = {'零':'0','十':'s0','百':'s00','千':'s000','萬':'s0000','億':'s00000000','万':'s0000', '亿':'s00000000'}
    unit_zh = {'十':'十','百':'百','千':'千','萬':'萬','億':'億','万':'萬', '亿':'億'}
    unit = ['十', '百', '千', '萬', '億'] 
    result_list = []
    unit_list = unit[0:3]
    for i in unit[3:]:
        unit_list.append(i)
        for j in unit_list[:-1]:
            unit_list.append(j+i)
    if(all([i not in inp for i in unit])):
        rs = ""
        for i in inp:
            rs += str(num_d[i])
        return int(rs)
    index = 0
    while(index < len(inp)):
        i = inp[index]
        if i in list(unit_zh.keys()):
            i = unit_zh[inp[index]]
            inp = inp[0:index] + i +inp[index+1:]
            if(inp[index-1] in unit[1:] and index != len(inp) - 1 and all([inp[index-len(u)+1:index+1] != u for u in unit_list if index >= len(u)-1 and len(u) > 1])):
                inp = inp[0:index]+'一'+inp[index:]
            elif(index == 0):
                inp = '一' + inp
        else:
            if(inp[index-1] in unit[1:] and index == len(inp) - 1):
                inp += unit[unit.index(inp[index-1])-1]
            elif(inp[index-1] in unit[1:] and (inp[index+1] in unit[3:] or inp[index+1] == '零')):
                inp = inp[0:index+1]+unit[unit.index(inp[index-1])-1]+inp[index+1:]
        index += 1
    for index,i in enumerate(inp):
            if(i in unit or i == '零'):
                result_list.append(unit_d[i])
            else:
                result_list.append(num_d[i])
    i = 0
    def sumNum(lis,inlis = ['s0000','s00000000']):
        s = [str(lis[0])]
        s_n = 0
        i = 1
        while(i < len(lis)):
            if('s' not in str(lis[i])):
                s[s_n] += str(lis[i])
            elif(lis[i] not in inlis):
                s[s_n] += str(lis[i].replace('s',''))
                if(i < len(lis)-1 and 's' not in str(lis[i+1])):
                    s_n += 1
                    i+=1
                    s.append('n' + str(lis[i]))
            else:
                s[s_n] = "n"+ s[s_n]
                s.append(lis[i])
                if(i < len(lis)-1 and 's' not in str(lis[i+1])):
                    i+=1
                    s.append('n'+str(lis[i]))
                    s_n += 2
            i+=1
        n = [int(s[0].replace('n',''))]
        n_n = 0
        i = 1
        while(i < len(s)):
            if('n' in s[i]):
                n[n_n] += int(s[i].replace('n',''))
            else:
                n.append(s[i])
                n_n += 1
                if(i < len(s)-1):
                    if('s' not in s[i+1]):
                        i+=1
                        n.append(int(s[i].replace('n','')))
                        n_n += 1
            i+=1
        return n
    return sumNum(sumNum(sumNum(result_list),['s00000000']),[])[0]

if __name__ == "__main__":
    print(toNum('十萬億零四'))