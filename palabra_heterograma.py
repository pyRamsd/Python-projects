# una palabra isograma una palabra que no se repitan letras
def is_isogram(string):
    string = string.lower().replace(" ","").replace("-", "")
    if len(string) == len(set(string)):
        return True
    else:
        return False
print(is_isogram("honda"))
print(is_isogram("palabra"))
