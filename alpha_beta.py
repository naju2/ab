maximum, minimum = 1000, -1000
def funAlpha(d, node, maxp, v,A,B):
    if d==2:
        return v[node]
    if maxp:
        best = minimum
        for i in range(0,2):
            value=funAlpha(d+1, node*2+i, False, v,A,B)
            best = max(best, value)
            A=max(A, best)
            if B<=A:
                break
        return best
    else:
        best = maximum
        for i in range(2):
            value = funAlpha(d+1, node*2+i, True, v, A,B)
            best = min(best, value)
            A = min(A,best)
            if B<=A:
                break
        return best

src =[]
print()
x= int(input("Enter total number of leaf node:"))
for i in range(x):
    y=int(input("Enter node value : "))
    src.append(y)
d=int(input("Enter depth value :"))
node=int(input("Enter node value :"))
print("The optimal value is:",funAlpha(d,node,True,src,minimum,maximum))
print()