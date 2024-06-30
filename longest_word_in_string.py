def longest_word(words):
  
  longestLen = 0
  longestWord = ""
  splArray = words.split(" ")
  
  for i in range(len(splArray)):
    if len(splArray[i]) > longestLen:
      longestWord = splArray[i]
      longestLen = len(longestWord)
  return longestWord


sentence = "This is a common interview question"
#longest_word(sentence)
print(longest_word(sentence))
