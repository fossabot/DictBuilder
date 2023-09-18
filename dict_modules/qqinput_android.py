def export(dict_list, proj, ver):
    write = open('output/' + proj + '_QQInputAndroid_' +
                 ver + '.txt', mode='w+', encoding='utf_16_le')
    write.write('\ufeff')
    for line in dict_list:
        write.write(line[0] + '=1,' + line[1] + '\n')
    write.close()
    