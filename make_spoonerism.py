def make_spoonerism(word1, word2):
  # switch the first letters of each word.
  string1 = word1.replace(word1[0], word2[0])
  string2 = word2.replace(word2[0], word1[0])
  # Return the two new words as a single string separated by a space.
  return string1 + " " + string2

# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a
