class Solution(object):
    def plus(self,code,k):
      n=len(code)
      new_code=[]
      for ind in range(n):
          new_element=0
          for i in range(1,k+1):
            new_element+= code[(ind+i)%n]
          new_code.append(new_element)
      return new_code
        
    def minus(self,code,k):
        n=len(code)
        new_code=[]
        for ind in range(n):
            new_element=0
            for i in range(1,k+1):
              new_element+= code[(ind-i)%n]
            new_code.append(new_element)
        return new_code
    
    def equal(self,code):
        code = [0] * len(code)
        return code
    def decrypt(self, code, k):
        if k>0:
            return self.plus(code,k)
        elif k<0:
            return self.minus(code,-k)
        else:
            return self.equal(code)
        
    


def main():
    code = [5,7,1,4]
    k = 3
    my_object = Solution()        
    judgement = my_object.decrypt(code, k)
    print(judgement)

if __name__ == "__main__":
   main()