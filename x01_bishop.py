#!python3

def bishop(square):
  """
  input:
  str square: the coordinate of the square that the bishop is currently located in
  examples: 'f3' or 'g6'
  
  return:
  list of possible squares that the bishop can move to:
  """
  print(square)
  available = []

  crow = square[0]
  ccollumn = square[1]
  
  row = ['a','b','c','d','e','f','g','h']
  collumn = ['1','2','3','4','5','6','7','8']
  
  rownum = row.index(crow)
  collumnum = collumn.index(ccollumn)
  
  for i in range(0,8):
    x = row[i]
    differ = abs(rownum - row.index(x))

    if collumnum-differ+1 > 0 and collumnum-differ+1 <= 8:
      available.append(f"{x}{collumnum-differ+1}")
      
    if collumnum+differ+1 <= 8 and collumnum+differ+1 <= 8:
      available.append(f"{x}{collumnum+differ+1}")

    if str(square) in available:
      available.remove(str(square))
  
  print(available)

    
  return available


def main():
  myList = bishop('f3')
  myList.sort()
  assert myList == ['a8', 'b7', 'c6', 'd1', 'd5', 'e2', 'e4', 'g2', 'g4', 'h1', 'h5']
  myList = bishop('g7')
  myList.sort()
  assert myList == ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'f8', 'h6', 'h8']

if __name__ == "__main__":
  main()
