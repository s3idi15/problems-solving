#1
def remove_char_from_(word, char):
  return word.replace(char, "")

#2
def remove_char_from(word, char):
  return "".join(filter(lambda x: x != char.lower() and x != char.upper(), word))
  
print(remove_char_from("mouhssine", "s"))
