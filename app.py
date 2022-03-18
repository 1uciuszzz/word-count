import sys
import json
from googletrans import Translator

translator = Translator()

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

waiting_for_translate = list(w_count.keys())

translated = []

for vocabulary in waiting_for_translate:
  translated.append(translator.translate(vocabulary, dest="zh-CN"))

result = open(sys.argv[3], "a", encoding="utf-8")

result_size = len(translated)

for i in range(result_size):
  result.write(
    f"{waiting_for_translate[i]} -> {w_count.get(waiting_for_translate[i])} -> {translated[i].text}"+"\n")

result.close()

print(f"success!")
