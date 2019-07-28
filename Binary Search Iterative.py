def binarysearch(A,key):
    low=0
    high=len(A)-1
    while low<=high:
         mid=(low+high)//2
         if key==A[mid]:
             return True
         elif key<A[mid]:
              high=mid-1
         else:
             low=mid+1
    return False
    



A=[1.2.3.4.5.6.7.8.9]

found=binarysearch(A,5)

print("number found in : ", found)
         
