#check if a string contains certain set of characters
import re
def is_allowed(string):#string goes hereAbcd1234
    chare=re.compile(r'[^a-zA-Z0-9]')#analsize and store in chare,,, the patterns are compiled and stored in chare
    string =chare.search(string) #searches the string and checks if pattern is satisfied
    return not bool(string) #if condtion satisfies return true
print(is_allowed("#$%"))
print(is_allowed("Abcd1234")) #this string will go to the def is_allowed statement

