import os
import json
import zipfile


def out_qqinput_android(line_list, proj):
    write = open('output/' + proj + '_QQInputAndroid_' +
                 ver + '.txt', mode='w+', encoding='utf_16_le')
    write.write('\ufeff')
    for line in line_list:
        write.write(line[0] + '=1,' + line[1] + '\n')
    write.close()


def out_qqinput_pc(line_list, proj):
    write = open('output/' + proj + '_QQInputPC_' + ver +
                 '.ini', mode='w+', encoding='utf_16_le')
    write.write('\ufeff')
    for line in line_list:
        write.write(line[0] + '=1,' + line[1] + '\n')
    write.close()


def out_baiduinput_android(line_list, proj, title):
    write = open('output/' + proj + '_BaiduInputAndroid_' +
                 ver + '.ini', mode='w+', encoding='utf_16_le')
    write.write('\ufeff')
    write.write('[' + title + ']' + '\n')
    for line in line_list:
        write.write(line[0] + '=0,' + line[1] + '\n')
    write.close()


def out_sogou_pc(line_list, proj):
    write = open('output/' + proj + '_SogouPC_' + ver +
                 '.txt', mode='w+', encoding='UTF-8')
    for line in line_list:
        write.write(line[0] + ',1=' + line[1] + '\n')
    write.close()


def out_gboard_android(line_list, proj):
    write = open('dictionary.txt', mode='w+', encoding='UTF-8')
    write.write('# Gboard Dictionary version:1' + '\n')
    for line in line_list:
        write.write(line[0] + '	' + line[1] + '	zh-CN	\n')
    write.close()
    archive = zipfile.ZipFile(
        'output/' + proj + '_GboardAndroid_' + ver + '.zip', 'w')
    archive.write('dictionary.txt', compress_type=zipfile.ZIP_STORED)
    archive.close()
    os.remove('dictionary.txt')


def out_converter(line_list, proj):
    write = open('output/' + proj + '_convert_' + ver +
                 '.txt', mode='w+', encoding='UTF-8')
    for line in line_list:
        write.write(line[0] + ',' + line[1] + '\n')
    write.close()


ver = input('INPUT VERSION NAME:')
conf_file = open('buildconfig.json', encoding='UTF-8')
confs = json.load(conf_file)
conf_file.close()

if not os.path.isdir('output'):
    os.mkdir('output')

completed = 0
for conf in confs:
    src = []
    if isinstance(conf["source"],list):
        for source in conf["source"]:
            src_file = open(source, encoding='UTF-8')
            src.extend(json.load(src_file))
            src_file.close()
    else:
        src_file = open(conf["source"], encoding='UTF-8')
        src.extend(json.load(src_file))
        src_file.close()

    line_list = []
    for phrase in src:
        for input in phrase["input"]:
            line_list.append([phrase["phrase"], input])

    out_qqinput_android(line_list, conf["prefix"])
    out_qqinput_pc(line_list, conf["prefix"])
    out_baiduinput_android(line_list, conf["prefix"], conf["title"])
    out_sogou_pc(line_list, conf["prefix"])
    out_gboard_android(line_list, conf["prefix"])
    out_converter(line_list, conf["prefix"])

    completed += 1
    print(str(completed) + " of " + str(len(confs)) + " task(s) completed")
