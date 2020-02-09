
def combiner(list):
    a,b = list
    m = min(len(a),len(b))
    s = ""
    for i in range(m):
        s = s + a[i] + b[i]

    if (len(a)>m):
        for i in range(m,len(a)):
            s += a[i]
    if (len(b)>m):
        for i in range(m,len(b)):
            s += b[i]        
    return s

N = int(input("Number of inputs: "))
list = []
answer = []
for i in range(N):
    list = input("Enter the 2 words: ").split(" ")
    answer = answer + [combiner(list)]
for i in answer:
    print(i)    