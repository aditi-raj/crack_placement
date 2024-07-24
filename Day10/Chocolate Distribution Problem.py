
def calculate(s: str) -> int:
    # pri={'/':3,'*':2,'+':1,'-':1}
    stack=[]
    i=0
    while i<len(s):
        print(s[i])
        if s[i]!=' ':
            stack.append(s[i])
        i+=1

    i=0
    while i+1<len(stack):
        if stack[i+1]=='/':
            stack.pop(i+1)
            num,den=stack.pop(i),stack.pop(i)
            stack.insert(i,int(num)//int(den))
        else:
            i+=1
    i=0
    while i+1<len(stack):
        if stack[i+1]=='*':
            stack.pop(i+1)
            num,den=stack.pop(i),stack.pop(i)
            stack.insert(i,int(num)*int(den))
        else:
            i+=1
    i=0
    while i+1<len(stack):
        if stack[i+1]=='-':
            stack.pop(i+1)
            num,den=stack.pop(i),stack.pop(i)
            stack.insert(i,int(num)-int(den))
        else:
            i+=1
    i=0
    while i+1<len(stack):
        if stack[i+1]=='+':
            stack.pop(i+1)
            num,den=stack.pop(i),stack.pop(i)
            stack.insert(i,int(num)+int(den))
        else:
            i+=1
    return stack[0]

s = "1+2*5/3+6/4*2"
print(calculate(s))