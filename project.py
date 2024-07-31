#COT5402 Dynamic Programming Project

word=[]
totallines=0
with open("input.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word.append(line.split())
        totallines=totallines+1
#print(word)
#print(totallines)
noofparts=int(word[0][0])
nextsetoflines=int(word[0][1])
sprocter=[]

for x in range(nextsetoflines+1, totallines):
  sprocter.append(int(word[x][0]))
#print(sprocter)


#tracker for base case
tracker=[]
for x in range(0, noofparts):
 tracker.append(x)

for x in range(1, nextsetoflines+1):
 for j in range(0, noofparts):
  if(int(word[x][1])==j):
      if j in tracker:
          tracker.remove(j)
         
#print(tracker)

#Final Answer Holding Array
answer=[]
for i in range(0, noofparts):
 answer.append(int(-3))
#print(answer)

#Filling Base Cases
for x in range(0, len(tracker)):
 answer[tracker[x]]=int(sprocter[tracker[x]])
#print(answer)

xyz=[]
for k in range(0, noofparts):
  xyz.append([])
#print(xyz)

#FiguringOutTheTreeStructure
for j in range(1, nextsetoflines+1):
    for k in range(0, noofparts):
      if(int(word[j][1])==k):
         xyz[k].append(int(word[j][0]))
#print(xyz[5])

#for item in list:
#print("welcome")
#ans=0
#count=0
#FillingTheFinalArray#DynamicProgramming
for l in range(0, noofparts):
 for i in range(0, noofparts):
    ans=0
    count=0
    if(i not in tracker):   #i is not the basecase
      for x in xyz[i]:
         #print(answer[x])
         if (answer[x] == -3):
           count = count+1
         #print(count)
      if(count == 0):
        #print("hurray")
        for y in xyz[i]:
          #print(answer[x])
        #count=1
          #k=answer[x]
          ans=ans+answer[y]
         
        #print(ans)
        ans = ans + sprocter[i]
        answer[i] = ans

#end      

#Writing result back on output file
f_1=open("output.txt","w")
f_1.write(str(answer[noofparts-1]))
f_1.close()

#Printing the result
with open("output.txt", 'r') as f_1:
    print(f_1.read())
