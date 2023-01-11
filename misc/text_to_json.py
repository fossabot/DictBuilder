import json

filename = "source_allRole.txt"
spliter = "<MID>"

src = open(filename, encoding='UTF-8')
srclines = src.readlines()
src.close()

obj_list = {}
key_list = []

line_count = 0

for line in srclines:
    line_count += 1
    parts = line.split(spliter)
    match = False
    matched = None
    if parts[1].strip('\n') in obj_list:
        if parts[0] not in obj_list[parts[1].strip('\n')]:
            obj_list[parts[1].strip('\n')].append(parts[0])
    else:
        obj_list[parts[1].strip('\n')] = [parts[0]]
        key_list.append(parts[1].strip('\n'))
    # for obj in obj_list:
    #     if obj["phrase"] == parts[1].strip('\n'):
    #         match = True
    #         matched = obj
    #         break
    # if match:
    #     matched["input"].append(parts[0])
    # else:
    #     add = {
    #         "phrase": parts[1].strip('\n'),
    #         "input": [parts[0]]
    #     }
    #     obj_list.append(add)
    print("processed " + str(line_count) + " line(s)")

final_array = []

for key in key_list:
    final_array.append({
        "phrase": key,
        "input": obj_list[key]
    })

file = open(filename + ".json", mode='w+', encoding='UTF-8')
json.dump(final_array, file, indent=4, ensure_ascii=False)
file.close()

log = open(filename + ".log.txt", mode='w+', encoding='UTF-8')
log.write("processed " + str(line_count) + " line(s)\n")
log.write(str(len(key_list)) + " entries")
log.close()
