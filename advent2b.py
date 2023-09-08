import re
def allnumbers(filename):
    with open(filename , 'r') as f:
        number=[]
        for lines in f:
            for numbers in re.findall(r"\d+", lines):
                number.append(int(numbers))
    return number 

num=allnumbers('advent2a.txt')
#print(num)
 
def allnames(filename):
    with open(filename, 'r+') as f:
        names=[]
        for lines in f:
            for name in re.findall(r'[a-zA-Z]+', lines):
                names.append(name)
    return names
names=allnames('advent2a.txt')
#print(names)

with open('advent2bans.txt', 'w')as f:
    def calc_depth_hori(list1 , list2):
        hori=0
        depth=0
        aim=0
        indices=list(range(0,len(list1),1))
        for i in indices:
            a=list2[i]
            if list1[i]=='forward':
                hori+=a
                depth+=aim*a
            elif list1[i]=='up':
                aim-=a
            elif list1[i]=='down':
                aim+=a
        multi=hori*depth
        return hori , depth , aim ,multi
    ans=calc_depth_hori(names, num)
    print(ans, file=f)