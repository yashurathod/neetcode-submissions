class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for i in range(len(strs)):
            s=s+str(len(strs[i]))+'#'+ strs[i]
        return s
    def decode(self, s: str) -> List[str]:
        i=0
        result=[]
        while i < len(s):
            # 1. Find the delimiter '#' starting from current position i
            j = s.find("#", i)
            
            # 2. Extract the length (handles single or multi-digit numbers like '12#')
            length = int(s[i:j])
            
            # 3. Slice out the exact word right after '#'
            start = j + 1
            end = start + length
            word = s[start:end]
            result.append(word)
            
            # 4. Jump the pointer to the start of the next length prefix
            i = end
        return result
        
            

