class Solution(object):
    def even(self,num):
        return num//2
    def odd(self,num):
        return 3*num+1
    def calculate_power_steps(self,num):
        steps=0
        while num!=1:
          if num%2==0:
              num=self.even(num)
          else:
              num=self.odd(num)
          steps+=1
        return steps
    def getKth(self, lo, hi, k):
        numbers = []
        for num in range(lo,hi+1):
            steps=self.calculate_power_steps(num)
            numbers.append((num, steps))
        numbers.sort(key=lambda x: (x[1], x[0]))
        return numbers[k-1][0]


def main():
    lo = 12
    hi = 15
    k = 2
    my_object = Solution()        
    judgement = my_object.getKth(lo,hi,k)
    print(judgement)

if __name__ == "__main__":
   main()