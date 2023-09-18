import os
import json

from dict_modules.baiduinput_android import export as out_baiduinput_android
from dict_modules.gboard_android import export as out_gboard_android
from dict_modules.newmspinyin_pc import export as out_newmspinyin_pc
from dict_modules.qqinput_android import export as out_qqinput_android
from dict_modules.qqinput_pc import export as out_qqinput_pc
from dict_modules.sogouinput_pc import export as out_sogouinput_pc
from dict_modules.imewlconverter import export as out_imewlconverter

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

    dict_list = []
    for phrase in src:
        for input in phrase["input"]:
            dict_list.append([phrase["phrase"], input])

    out_baiduinput_android(dict_list, conf["prefix"], ver, conf["title"])
    out_gboard_android(dict_list, conf["prefix"], ver)
    out_newmspinyin_pc(dict_list, conf["prefix"], ver)
    out_qqinput_android(dict_list, conf["prefix"], ver)
    out_qqinput_pc(dict_list, conf["prefix"], ver)
    out_sogouinput_pc(dict_list, conf["prefix"], ver)
    out_imewlconverter(dict_list, conf["prefix"], ver)

    completed += 1
    print(str(completed) + " of " + str(len(confs)) + " task(s) completed")
