inp="abbaca"

class Solution:
    def removeDuplicates(self, S):
        i=0
        # Cannot use for loop here as we have to go back after one removal (bb)
        # Classix example of while loop usage
        while True:
            if i+1==len(S):   #or i>len(S)-2 or i+1>len(S)-1 or i+1==len(S)
                break
            if S[i]==S[i+1]:
                S=S[:i]+S[i+2:]
                i=max(i-1,0)
            else:
                i+=1
        return S

print(Solution().removeDuplicates(inp))