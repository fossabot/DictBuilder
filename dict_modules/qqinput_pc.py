def export(dict_list, proj, ver):
    fs = open('output/' + proj + '_QQInputPC_' + ver +
                 '.ini', mode='w+', encoding='utf_16_le')
    fs.write('\ufeff')
    for line in dict_list:
        fs.write(line[0] + '=1,' + line[1] + '\n')
    fs.close()
    