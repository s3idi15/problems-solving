def remove_dupicate_words_(s):
    return ' '.join(set(s.split()))

def remove_dupicate_words__(s):
  words = s.split(' ')
  unique_words = []

  for word in words:
    if word not in unique_words:
      unique_words.append(word)
  return ' '.join(unique_words)

def remove_dupicate_words(s):
  return ' '.join(list(dict.fromkeys(s.split(' '))))
  
print(remove_dupicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))
