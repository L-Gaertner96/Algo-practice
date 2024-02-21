class Solution:
    def find_missing_number(arr, N):
        temp_list = [0]*(N+1)
        
        for i in range (0,N):
            temp_list[arr[i]-1] = 1
            
        for i in range (0,N+1):
            if temp_list[i] == 0:
                return i+1
            
arr = [1,2,3,4,6,7,8]
N = len(arr)
print(Solution.find_missing_number(arr,N))