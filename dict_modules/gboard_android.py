import os
import zipfile

def export(dict_list, proj, ver):
    fs = open('dictionary.txt', mode='w+', encoding='UTF-8')
    fs.write('# Gboard Dictionary version:1' + '\n')
    for line in dict_list:
        fs.write(line[0] + '	' + line[1] + '	zh-CN	\n')
    fs.close()
    archive = zipfile.ZipFile(
        'output/' + proj + '_GboardAndroid_' + ver + '.zip', 'w')
    archive.write('dictionary.txt', compress_type=zipfile.ZIP_STORED)
    archive.close()
    os.remove('dictionary.txt')
