def export(dict_list, proj, ver):
    fs = open('output/' + proj + '_convert_' + ver +
                 '.txt', mode='w+', encoding='UTF-8')
    for line in dict_list:
        fs.write(line[0] + ',' + line[1] + '\n')
    fs.close()
