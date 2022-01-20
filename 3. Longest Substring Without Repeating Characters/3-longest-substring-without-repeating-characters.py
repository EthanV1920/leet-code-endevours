class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringCount = 0
        largestString = 0
        prevChar = None

        for i in range(len(s)):
            curChar = s[i]

            if curChar != prevChar:
                stringCount +=1
                print(f"INFO: Checked {prevChar} and {curChar} stringCount: {stringCount}")
                prevChar = curChar
            else:
                largestString = stringCount
                stringCount = 0
                prevChar = curChar
                print("INFO: Not equal, restarting count" + str(stringCount))
                return

     
        return(largestString)
