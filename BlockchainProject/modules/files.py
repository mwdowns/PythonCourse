f = open('chain.txt', mode='w')
f.write('hello from python')
f.close()

f = open('chain.txt', mode='r')
fc = f.read()
print(fc)
f.close()