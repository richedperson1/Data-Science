def ArrayChallenge(arr):

  # code goes here
  size = len(arr)
  
  index1 = arr.index(1)

  count = 1

  leftIndex = index1
  
  while leftIndex>=0:
    
    if arr[leftIndex]!=2:
      count+=1
    else:
      break

    leftIndex-=1
  
  RightIndex = index1
  count2 = 1

  while RightIndex<size:

    if arr[RightIndex]!=2:
      count2+=1
    else:
      break

    RightIndex+=1
  
  return min(count2,count)


arr =  [1, 0, 0, 0, 2, 2, 2]

print(ArrayChallenge(arr))