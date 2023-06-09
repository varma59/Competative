class Solution:
    def partitionString(self, s: str) -> int:
        dic={}
        c=0
        for i in s:
            if(i in dic):
                c+=1
                dic={}
                dic[i]=1
            else:
                dic[i]=1
        if len(dic)!=0:
            c+=1
        return c
