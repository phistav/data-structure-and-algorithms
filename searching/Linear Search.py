def linearSearch(arr, x): 
  
    for i in range(len(arr)): 
  
        if arr[i] == x: 
            return i 
  
    return -1

if __name__ == "__main__":
   arr = [0,1,2,3,4,5,6,7,8,9]
   x = 6
   print("Value is present at index number: {}".format(linearSearch(arr,x)))