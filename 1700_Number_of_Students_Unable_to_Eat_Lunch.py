from queue import Queue

class Solution(object):
    def countStudents(self, students, sandwiches):
        student_queue = Queue()
        for s in students:
            student_queue.put(s)
        count=0
        i=0
        while student_queue.qsize() > 0 and count < student_queue.qsize():
          current_student = student_queue.get()
          if sandwiches[i] != current_student:
              student_queue.put(current_student)
              count+=1
          else:
              i+=1
              count=0

        return student_queue.qsize()
        
def main():
    students = [1,1,1,0,0,1]
    sandwiches = [1,0,0,0,1,1]
    my_object = Solution()        
    res = my_object.countStudents(students,sandwiches)
    print(res)

if __name__ == "__main__":
   main()