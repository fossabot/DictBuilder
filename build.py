import os
import json
import shutil

from dict_modules.baiduinput_android import export as out_baiduinput_android
from dict_modules.gboard_android import export as out_gboard_android
from dict_modules.newmspinyin_pc import export as out_newmspinyin_pc
from dict_modules.qqinput_android import export as out_qqinput_android
from dict_modules.qqinput_pc import export as out_qqinput_pc
from dict_modules.sogouinput_pc import export as out_sogouinput_pc
from dict_modules.imewlconverter import export as out_imewlconverter

print("=================")
print("   DictBuilder")
print("=================")
print("")
ver = input('Input VERSION NAME:')
conf_file = open('buildconfig.json', encoding='UTF-8')
confs = json.load(conf_file)
conf_file.close()

print("-----------------")

if not os.path.isdir('output'):
    os.mkdir('output')

else:
    print("ATTENTION, folder '/output' exists in current location.")
    print("Proceed to build will overwrite the entire folder,")
    print("EVERYTHING PREVIOUSLY WITHIN WILL BE LOST.")
    chk:str = input('Type "yes" to proceed:')
    chk = chk.lower()
    if chk == 'yes':
        print("-----------------")
        shutil.rmtree('output', True)
        os.mkdir('output')
    else: 
        print("Build aborted.")
        os.system('pause')
        os._exit(0)

completed: int = 0
for conf in confs:
    print("Starting task " + str(completed + 1) +
          " of " + str(len(confs)) + " :")
    src = []
    filecount: int = 0
    if isinstance(conf["source"], list):
        for source in conf["source"]:
            filecount += 1
            src_file = open(source, encoding='UTF-8')
            src.extend(json.load(src_file))
            src_file.close()
    else:
        filecount += 1
        src_file = open(conf["source"], encoding='UTF-8')
        src.extend(json.load(src_file))
        src_file.close()

    print("- Loaded " + str(filecount) + " file(s)")
    dict_list = []
    phrasecount: int = 0
    linecount: int = 0
    for phrase in src:
        phrasecount += 1
        for input in phrase["input"]:
            linecount += 1
            dict_list.append([phrase["phrase"], input])
    print("- Loaded " + str(linecount) + " line(s) from " +
          str(phrasecount) + " phrase(s)")

    out_baiduinput_android(dict_list, conf["prefix"], ver, conf["title"])
    out_gboard_android(dict_list, conf["prefix"], ver)
    out_newmspinyin_pc(dict_list, conf["prefix"], ver)
    out_qqinput_android(dict_list, conf["prefix"], ver)
    out_qqinput_pc(dict_list, conf["prefix"], ver)
    out_sogouinput_pc(dict_list, conf["prefix"], ver)
    out_imewlconverter(dict_list, conf["prefix"], ver)

    completed += 1
    print("Task " + str(completed) + " of " +
          str(len(confs)) + " completed")
    print("-----------------")

os.system('pause')
