import sys
import json
import deepl


# 修改这里面的参数
deepl_api_key = "<you need apply deepl api auth key>"

translator = deepl.Translator(deepl_api_key)

# 打开“已掌握单词表”
known_words = open(f"{sys.argv[2]}", "r")

# 读取“已掌握单词”
vocabularies = json.loads(known_words.read())

# 关闭文件
known_words.close()

# 打开“待统计文档”
document = open(f"{sys.argv[1]}", "r")

# 读取“待统计文档”的字符流
characters = document.read()

# 关闭文件
document.close()

# 声明所需变量
word = ""
w_count = dict()

# 逐字符统计
for single_char in characters:
  if single_char.isalpha() or single_char == f"'":
    word += single_char
  else:
    if len(word) == 0:
      continue
    if vocabularies.get("data").count(word):
      word = ""
      continue
    if w_count.get(word) is None:
      w_count.update({word: 1})
      word = ""
      continue
    w_count.update({word: w_count.get(word)+1})
    word = ""

waiting_for_translate = w_count.keys()

translated = translator.translate_text(
  waiting_for_translate, target_lang=f"ZH")

result = open(sys.argv[3], "a")

result_size = len(result)

for i in range(result_size):
  result.write(
    f"{waiting_for_translate[i]}::{w_count.get(waiting_for_translate[i])}::{translated[i]}"+"\n")
