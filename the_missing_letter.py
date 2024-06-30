import string


def find_missing_letter(givenLetters):
  lowerLetters = string.ascii_lowercase
  start = lowerLetters.index(givenLetters[0])

  for letter in lowerLetters[start:]:
    if letter not in givenLetters:
      return letter
  return f"No missing letter in {givenLetters}"
