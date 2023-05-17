i=0
while True:
    with open ('test1.txt','a') as f:
        f.write(str(i))

    with open ('test2.txt','a') as g:
        g.write(str(i))
    
    i=i+1