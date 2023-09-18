#
#    Copyright © 2009-2020 studyzy(深蓝,曾毅)
#    Copyright © 2023 MarkussLugia

#    This program "DictBuilder" is free software: you can redistribute it
#    and/or modify it under the terms of the GNU General Public License
#    as published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <https://www.gnu.org/licenses/>.
#


from datetime import datetime

def export(dict_list, proj, ver):
    dict_list = filter(dict_list)

    fs = open('output/' + proj + '_MSPinyinWin10PC_' + ver + '.dat', mode='wb')

    # header 0x00-0x40 64bytes
    fs.write(b"mschxudp")
    fs.write((0x00600002).to_bytes(4, 'little'))
    fs.write((0x01).to_bytes(4, 'little'))  # version
    fs.write((0x40).to_bytes(4, 'little'))  # offsetmap start
    fs.write((0x40 + 4*len(dict_list)).to_bytes(4, 'little'))  # content start
    fs.write((0x00).to_bytes(4, 'little'))  # content end, set later
    fs.write((int(len(dict_list))).to_bytes(4, 'little'))  # phrase count
    fs.write((int(datetime.now().timestamp())).to_bytes(8, 'little'))
    fs.write((0x00).to_bytes(8, 'little'))
    fs.write((0x00).to_bytes(8, 'little'))
    fs.write((0x00).to_bytes(8, 'little'))

    # offsetmap
    offset: int = 0

    for i in range(len(dict_list)):
        fs.write(offset.to_bytes(4, 'little'))
        line = dict_list[i]
        offset += 8 + 8 + len(line[1]) * 2 + 2 + len(line[0]) * 2 + 2

    # phrase content
    for i in range(len(dict_list)):
        fs.write((0x00100010).to_bytes(4, 'little'))  # magic
        line = dict_list[i]
        hanzi_offset: int = 8 + 8 + len(line[0]) * 2 + 2
        fs.write((hanzi_offset).to_bytes(2, 'little'))
        fs.write((0x01).to_bytes(1, 'little'))  # 词条位置
        fs.write((0x06).to_bytes(1, 'little'))  # 不知道
        fs.write((0x00).to_bytes(4, 'little'))  # 不知道
        fs.write((0xE679CD20).to_bytes(4, 'little'))  # 不知道

        fs.write(bytes(line[0], encoding="utf-16-le"))
        fs.write((0x0000).to_bytes(2, 'little'))
        fs.write(bytes(line[1], encoding="utf-16-le"))
        fs.write((0x0000).to_bytes(2, 'little'))

    # set content end
    size = fs.tell()
    fs.seek(0x18)
    fs.write((size).to_bytes(4, 'little'))

    fs.close()


def filter(dict_list):
    result = []
    for line in dict_list:
        if len(line[1]) <= 32 and len(line[0]) <= 64:
            result.append(line)
    return result
