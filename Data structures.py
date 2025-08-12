'''


'''
class solution:
    def freq(self,word):
        hashmap={}
        for char in s:
            hashmap[char]=hashmap.get(char,0)+1
        max_char=0
        for num in hashmap.values():
            if num>max_char:
                max_char=num
        max_list=[]
        for i,num in hashmap.items():
            if num==max_char:
                max_list.append(i)
        return hashmap,max_list
obj=solution()
s="programming"
hashmap,max_list=obj.freq(s)
print(hashmap,max_list)
    
