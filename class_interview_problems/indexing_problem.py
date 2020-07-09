def build_index(records):
  index = {}

  '''
  for name, state in records:
    value = index.setdefault(state, [])
    value.append(name)
  '''

  # Iterate through list, destructure the tuples
  for name, state in records:
    # For each pair, check if the state is in the dictionary
    if state in index:
      index[state].append(name)
    else:
      index[state] = [name]
  
  return index