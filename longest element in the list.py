list=["Geek","Geeks","Geeksfor","GeeksforGeeks","GeeksforGeek"]

count=0
# len(list[0]) > count
# count = len(list[0])

for i in range(0,len(list)):
      if len(list[i])>count:
            count=len(list[i])



for i in range(0,len(list)):
      if len(list[i])==count:
            print(list[i])
