# DictBuilder
用于构建词库的自动化Python脚本。

*** 
这是什么？
---

这个Python脚本可以从**特定格式的JSON源文件**构建供输入法导入的词库文件。   
标准的词库源文件格式可以参考此项目中的demo文件。
### 目前支持的输入法有：
**Windows:**
* 微软拼音输入法（Win10/11）
* 搜狗拼音输入法
* QQ拼音输入法

**Android:**
* 百度输入法
* Gboard
* QQ输入法

此外，还会额外构建一个用于在 **[深蓝词库转换](https://github.com/studyzy/imewlconverter)** 中进行转换的自定义格式txt文件。

*** 
我可以用它做什么？
---
如果你想搞一个类似于 **[Pboard](https://github.com/MarkussLugia/Pboard)** 的自定义词库，不妨试试这个脚本。   
配置完毕后，它可以从结构复杂的词库源文件中按需求分类构建出词库文件，并输出到/output文件夹中。
