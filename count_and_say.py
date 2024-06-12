def countAndSay(n):
  """
  :type n: int
  :rtype: str
  """
  if n == 1:
      return "1"
  
  def next_sequence(seq):
      result = []
      i = 0
      while i < len(seq):
          count = 1
          while i + 1 < len(seq) and seq[i] == seq[i + 1]:
              i += 1
              count += 1
          result.append(str(count) + seq[i])
          i += 1
      return ''.join(result)
  
  current = "1"
  for _ in range(1, n):
      current = next_sequence(current)
  
  return current
