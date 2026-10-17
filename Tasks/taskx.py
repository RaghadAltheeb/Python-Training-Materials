N,M=map(int,input().split)
test="WELCOME"
x=test.center(M,"-")

for i in range(1,N,2):
    pattern=".|."*i
    print(pattern.center(M,"-"))
print(x)
for i in range(N-2,0,-2):
    pattern=".|."*i
     print(pattern.center(M,"-"))

    
