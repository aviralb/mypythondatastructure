def binarysearch(A,key,low,high):
    if low>high:
      else:
         mid=(low+high)//2
         if key==A[mid]:
            return True
         elif key<A[mid]:
             return binarysearch(A,key,low,high)
         else:
             return binarysearch(A,key,low,high)
             
             
         
         
         
A=[1,2,3,4,5,6,7,8,9]

found=binarysearch(A,5,0,8)

print("number found in : ", found)         
             
    
