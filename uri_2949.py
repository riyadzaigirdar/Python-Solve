N = int(input())
dwarfs = 0
elves = 0
humans = 0
magicians = 0
hobbits = 0

for i in range(N):
    list = input().split(" ")
    string1,string2=list

    if(string1.isalnum() and string2.capitalize()):
        if(string2 == "A"):
            dwarfs += 1
        if(string2 == "E"):
            elves += 1
        if(string2 == "H"):
            humans += 1 
        if(string2 == "M"):
            magicians += 1 
        if(string2 == "X"):
            hobbits += 1                 

print("%i Hobbit(s)" % hobbits)
print("%i Humano(s)" % humans)
print("%i Elfo(s)" % elves)
print("%i Anao(s)" % dwarfs)
print("%i Mago(s)" % magicians)

