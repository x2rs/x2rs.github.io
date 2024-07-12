text = """
Got this panda plush toy for my daughter's birthday,
who loves it and takes it everywhere. It's soft and
super cute, and its face has a friendly look. It's
a bit small for what I paid though. I think there
might be other options that are bigger for the
same price. It arrived a day earlier than expected,
so I got to play with it myself before I gave it
to her.
"""

import re
from collections import Counter

def wordcount(text: str):
    # 去除标点符号
    text = re.sub(f"[!.,?]", "", text)

    # 转换为小写并分割单词
    words = text.lower().split()

    # 统计单词
    return dict(Counter(words))

print(wordcount(text))