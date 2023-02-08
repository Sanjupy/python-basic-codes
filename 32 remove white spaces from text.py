import re
text="python   life"

print("the original text ",text)
print("without white spaces",re.sub(r'\s+','',text))#the blank space is removed by re.sub(r'\s+',"",text

