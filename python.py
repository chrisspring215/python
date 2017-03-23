f = open('cats.js', 'r')
file_contents = f.read()

c = file_contents.rpartition('var myCat = [')[2]
d = c.rpartition(']')[0]
import re
print re.sub('[\s+]', '', d)

f.close()
