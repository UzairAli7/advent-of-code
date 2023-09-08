#to read input from file
with open('advent1.txt', 'r') as advent1:
  data=advent1.readlines()
  lst=[]
  for lines in data:
    lst.append(int(lines))

#to find  sum of three elements with sliding windows method and save new data to file
with open('advent1b.txt', 'w') as advent1b:
  def three_sum(list,size):
    if len(list) <= size:
      return list
    for i in range (len(lst)-size +1):
      print(sum(list[i:i+size]) , file=advent1b)
  #lst=[1,2,0,4,5,6,7]
  three_sum(lst,3)

#to read new data from file
with open('advent1b.txt', 'r') as advent1b:
  data=advent1b.readlines()
  list1=[]
  for lines in data:
    list1.append(int(lines))
 

#To compare data and find answer (number of values increased)
previous_depth = 0
with open('advent1bans.txt' , 'w') as advent1bans:
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
  advent1bans.write(str(a)) 

print(a)   
