#to read input data from file
with open('advent1.txt', 'r') as advent1b:
  data=advent1b.readlines()
  list1=[]
  for lines in data:
    list1.append(int(lines))

#to compare data and find answer(number of avlues increased)
previous_depth = 0
with open('advent1ans.txt' , 'w') as advent1ans:
  a=0
  for i in list1:
    if previous_depth != 0 :
      if i < previous_depth:
        print(i , 'decreased') 
      elif i ==previous_depth:
        print(i , 'No change')
      elif i > previous_depth:
        print(i ,'increased')
        a +=1 

    previous_depth = i  
  advent1ans.write(str(a)) 

print(a)   
