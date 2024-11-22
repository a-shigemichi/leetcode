class Solution(object):
    def sum_next_k_element(self,code,k):
        n=len(code)
        new_code=[]
        for i in range(n):
            sum_val=0
            for j in range(1,k+1):
              sum_val+= code[(i+j)%n]
            new_code.append(sum_val)
        return new_code
        
    def sum_prev_k_elements(self,code,k):
        n=len(code)
        new_code=[]
        for i in range(n):
            sum_val=0
            for j in range(1,abs(k)+1):
              sum_val+= code[(i-j)%n]
            new_code.append(sum_val)
        return new_code
    
    def clear_array(self,code):
        code = [0] * len(code)
        return code
    def decrypt(self, code, k):
        if k>0:
            return self.sum_next_k_element(code,k)
        elif k<0:
            return self.sum_prev_k_elements(code,k)
        else:
            return self.clear_array(code)
        
    


def main():
    code = [5,7,1,4]
    k = 3
    my_object = Solution()        
    res = my_object.decrypt(code, k)
    print(res)

if __name__ == "__main__":
   main()