a='Sodium 123.1 mmol'
word='Sodium'
count=len(word)
b=a.find(word)+count
#[0:count]
print (b)
print (a[b:].strip())