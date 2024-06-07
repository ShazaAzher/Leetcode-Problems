def convert(s, numRows) -> str:
  if numRows == 1 or numRows >= len(s):
      return s
  
  result = [''] * numRows
  row = 0
  direction = 1
  
  for char in s:
      result[row] += char
      if row == 0:
          direction = 1
      elif row == numRows - 1:
          direction = -1
      row += direction
  
  return ''.join(result)
