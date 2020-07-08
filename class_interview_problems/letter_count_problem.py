# Given a string, return every letter and how many times it occurs
# Sort by frequency of occurrence

def print_letter_count(s):
  letter_cache = {}

  s = s.lower()

  for character in s:
    # if not char.isspace()
    # if char != " "
    if character >= 'a' and character <= 'z':
      if character not in letter_cache:
        letter_cache[character] = 1
      else:
        letter_cache[character] += 1
  
  # sorted(letter_cache.items(), key = lambda x: x[1], reverse = True)
  letter_list = list(letter_cache.items())
  # letter_list.sort(key = lambda x: (-(x[1])))
  letter_list.sort(key = lambda x: x[1], reverse = True)

  for pair in letter_cache:
    print(f'Count: {pair[1]}, Letter: {pair[0]}')