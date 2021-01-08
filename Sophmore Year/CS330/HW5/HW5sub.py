i=[1,2,3]
p=[7,6,5]
t=[5,6,7]
f = [30,10,0]
def photo(f,t):
    ans= (((f[2]-f[0])/t[0])+((f[2]-f[1])/t[1])+((0)/t[2]))
    return ans

print(photo(f,t))
k = input("thats its")