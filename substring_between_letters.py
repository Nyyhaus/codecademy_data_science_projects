def substring_between_letters(word, start, end):
  x = word.find(start)
  y = word.find(end)
  print(x, y)
  if x >= 0 and y >= 0:
    return word[x+1:y]
  else:
    return word
# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
