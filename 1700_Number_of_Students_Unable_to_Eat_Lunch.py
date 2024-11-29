from collections import deque

class Solution(object):
    def countStudents(self, students, sandwiches):
        queue = deque(students)
        count = 0
        i = 0
        
        while queue and count < len(queue):
            if queue[0] == sandwiches[i]:
                queue.popleft()
                i += 1
                count = 0
            else:
                queue.append(queue.popleft())
                count += 1
                
        return len(queue)
        
def main():
    students = [1,1,1,0,0,1]
    sandwiches = [1,0,0,0,1,1]
    my_object = Solution()        
    res = my_object.countStudents(students,sandwiches)
    print(res)

if __name__ == "__main__":
   main()