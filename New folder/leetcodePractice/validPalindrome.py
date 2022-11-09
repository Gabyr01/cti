
import re

def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        # for i and j
        # s[i-1,i]
        # s
        
        #get string
            #removing all non-alphanumeric characters
            #allAlphChar 
            #new string 
            #loop until it gets to the middle  of the new string length
            #checks if the front = with the back 
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        
        s = s.lower()
        # print(s+"\n")
        front = 0
        back = len(s)-1
        while True:
            if(s[front] !=s[back]):
                return False
            front = front + 1 
            back = back - 1
            # print(front, back)
            if front >=back:
                break
                
        return True
    
print(isPalindrome("A man, a plan, a canal: Panama"))