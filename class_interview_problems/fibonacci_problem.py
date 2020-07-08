cache = {}

def fibonacci(n):
  if n <= 1:
    return n
  
  if n in cache:
    return cache[n]
  else:
    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
  
  return cache[n]