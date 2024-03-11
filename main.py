content_list = ["北京", "天津"]  # 列表中的单词
text = "北京是中国的首都，而天津是一个重要的港口城市。"  # 要检查的文本

# 检查文本中是否包含列表中的任何单词
if any(word in text for word in content_list):
    print("文本中包含列表中的单词")
else:
    print("文本中不包含列表中的单词")
