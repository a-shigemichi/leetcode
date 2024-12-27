class Solution(object):
    def can_type_in_one_row(self,word):
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        word = word.lower()
        word_chars = set(word)

        return (word_chars.issubset(row1) or 
                word_chars.issubset(row2) or 
                word_chars.issubset(row3))
    
    def findWords(self, words):
        return [word for word in words if self.can_type_in_one_row(word)]

def main():
    words = ["Hello","Alaska","Dad","Peace"]
    my_object = Solution()
    res = my_object.findWords(words)
    print(res)

if __name__ == "__main__":
    main()