class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a=int(a,2)
        int_b=int(b,2)
        
        sum= int_a+int_b
        
        binary_sum=bin(sum)[2:]
        
        return binary_sum
        