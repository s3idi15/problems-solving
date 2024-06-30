def longest_word(words):
  
  longestWord = ""
  word_list = words.split(" ")
  
  for word in word_list:
    if len(word) > len(longestWord):
      longestWord = word
  return longestWord


sentence = "This is a common interview question"
print(longest_word(sentence))
