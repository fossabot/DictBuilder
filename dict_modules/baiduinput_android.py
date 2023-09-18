def export(dict_list, proj, ver, title):
    write = open('output/' + proj + '_BaiduInputAndroid_' +
                 ver + '.ini', mode='w+', encoding='utf_16_le')
    write.write('\ufeff')
    write.write('[' + title + ']' + '\n')
    for line in dict_list:
        write.write(line[0] + '=0,' + line[1] + '\n')
    write.close()
    