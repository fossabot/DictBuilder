def export(dict_list, proj, ver):
    write = open('output/' + proj + '_SogouPC_' + ver +
                 '.txt', mode='w+', encoding='UTF-8')
    for line in dict_list:
        write.write(line[0] + ',1=' + line[1] + '\n')
    write.close()
