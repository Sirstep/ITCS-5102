import operator

#l = []
#d = {}
#d_ascending = []
#d_input = []
#d_usage = []

t = {}
t_input = []
t_ascending = []
t_usage = []
# make new output from input
# maybe replace d with d_timeline

file = input('Enter text file name (include \'.txt\' extension): ')
text = open(file, 'r')

#for x in range(0, 10):
 #   l.append(input("Enter item {}: ".format(x + 1)))

for line in text:
    for char in line:
        t[char] = t.get(char, 0) + 1

for key, value in t.items():
    temp = (key,value)
    t_input.append(temp)

t_ascending = sorted(t.items(), key=operator.itemgetter(0))

t_usage = sorted(t.items(), key=operator.itemgetter(1), reverse=True)

#for i in l:
 #   for c in iter(i):
  #      d[c] = d.get(c, 0) + 1

#for key, value in d.items():
 #   temp = (key,value)
  #  d_input.append(temp)

#d_ascending = sorted(d.items(), key=operator.itemgetter(0))

#d_usage = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

#print("\nInput (first-to-last):", d_input, "\n\nASCII (ascending):", d_ascending, "\n\nUsage (descending):", d_usage)

print("\nInput (first-to-last):", t_input, "\n\nASCII (ascending):", t_ascending, "\n\nUsage (descending):", t_usage)