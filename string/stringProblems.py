
import re
from collections import Counter
paragraph = "a b.b"
banned=[]
banned_set=set(banned)
word=re.findall(r'[A-Za-z]+',paragraph)
counts=Counter(w.lower() for w in word if w.lower() not in banned_set)
print(counts.most_common(1)[0][0])
