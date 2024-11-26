# 3
# name = input("Enter your name: ")
# phonenumber = input("Enter your phone number: ")
# email = input("Enter your email: ")
# student ={}
# student['Name'] = name
# student['Phone'] = phonenumber
# student['Email'] = email
# print(student)

# 2
# details = {
#     'name' : 'jayaseelan',
#     'class1' : [1,2,3,4,5],
#     'section' : ['tamil','english','maths']
# }

# value=details['class1'][4]
# value1=details['section'][1]

# print(value)
# print(value1)


# my_dict = {
#     'goat': 'vijay',
#     'arabam': 'ajith',
#     'erumugam': 'vikram'
# }

# print(my_dict.keys())
# print(my_dict.values())
  


# member1 ={
#     "name":"plant",
#     "instrument":"guitar"
# }
# member2 = {
#     "name":"page",
#     "instrument":"guitar"
# }
# band ={
#     "member1": member1,
#     "member2": member2
# }
# print(band)
# print(band["member1"]["name"])


# family ={
#     "father": {
#     "son":"dasy",
#     "wife":"shaerin",
#     "status":"death"
# },
# "grandfather": {
#     "mother":"meena",
#     "status":"death"
# }
# }
# print(family["father"]["son"])
  




# a=24
# b=24
# if a==b:
#     a+=23
# if a!=b:
#     a+=24
#     print(a)
# else:
#     b+=27
#     print(b)
# if b%2==0:
#     print("divisible by 2")
# else:
#     print("not divisible by 2")


# a=int(input("enter the number:"))
# if a>0:
#     if a%2==0:
#         print("divisible by 2")
#     elif a%3==0:
#         print("divisible by 3")
#     elif a%5==0:
#         print("divisibe by 5")
#     else:
#         print("not divisible by any number")
# else:
#     print("invalid input")




# list1=[89,65,30,100]
# maximum=(list1[0])
# for i in  list1:
#   if  i>maximum:
#     maximum=i
# print(maximum)

# a = 24
# a = 2
# a=45
# print(a)


# fruits = ["apple","banana","cherry"]
# for x in range(2):
#   if x == "banana":
#     break
#   print(x)


# for x in range (6):
#     print(x)
# else:
#     print("finally finished!")


# for x in range (6):
#     if x == 3: break
#     print(x)
# else:
#     print("finally finished!")

# adj = ["red","big","tasty"]
# fruits = ["apple","banana","cherry"]
# for x in adj :
#     for y in fruits :
#         print(x,y)


# fruits = ["apple","banana","cheery"]
# for x in fruits:
#     print(x)


# value1 = "a3b5c4"
# num = []
# alpha = []
# for i in value1 :
#     if i.isdigit():
#         num.append(int(i))
#     else:
#         alpha.append(i)
# print(num)
# print(alpha)


# n = int(input("Enter the number:"))
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()


# a="iam good not"
# b="you are super"
# a_words = a.split()
# b_words = b.split()
# output_words = []
# for word in a_words[:2]:
#     output_words.append(word)
# for word in b_words:
#     output_words.append(word)
# for word in a_words[2:]:
#     output_words.append(word)
# output = " ".join(output_words)
# print(output)




# a = [56,56,23,44,44,29]




# result = [] 

# for i in a: 

#     if i not in result: 

#         result.append(i) 


# print (str(result))




# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break
# print(x)  


# i = 1
# while i<6 :
#     print(i)
#     if i == 3:
#         break
#     i +=1

# i =1
# while i <6:
#     print(i)
#     i +=1
# else:
#     print("i no longer less than 6")


# list1 = [64, 25, 12, 22, 11]

# def average(list1):
#     total_sum = 0
    
#     for number in list1:
#         total_sum += number
    
#     avg = total_sum / len(list1)
    
#     return avg

# print("Average:", average(list1))



# list1 = [64, 25, 12, 22, 11]
# max_value = list1[0]
# for number in list1:
#     if number > max_value:
#         max_value = number
# print("The maximum value in the list is:", max_value)



# list1 = [64, 25, 12, 22, 11]
# min_value = list1[0]
# for number in list1:
#     if number < min_value:
#         min_value = number
# print("The minimum value in the list is:", min_value)


# students = [
#     {'Name': 'Priya' ,'Age': 99, 'Rank' : 5},
#     {'Name': 'Amma' ,'Age': 45, 'Rank' : 100},
#     {'Name': 'Arun' ,'Age': 29, 'Rank' : 2},
#     {'Name': 'Ranju' ,'Age': 50, 'Rank' : 4},
#     {'Name': 'Appa' ,'Age': 52, 'Rank' : 99}
# ]

# def min_rank(data):
#     rank = data[0]['Rank']
#     count=0
#     for i in range(len(students)):
#         if rank >data[i]['Rank']:
#             rank =data[i]['Rank'] 
#             count= i4[43]
#     return data[count]
# print(min_rank(students))


# age_below_50 = []

# for student in students:
#     if student['Age'] < 50:
#         age_below_50.append(student)

# print(age_below_50)


class Test:
 
    def __init__(self, limit):
        self.limit = limit
 
    def __iter__(self):
        self.x = 10
        return self
 
    def __next__(self):
 
        x = self.x
 
        if x > self.limit:
            raise StopIteration
 
        self.x = x + 1;
        return x
 
for i in Test(15):
    print(i)
 
for i in Test(5):
    print(i)






