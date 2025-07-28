# #An institution has decided to admit new candidates in different streams on the following criteria:
# Total marks obtained Stream offered
# 300 and above Science
# 200 and above but less than 300 Commerce
# Below 200 but not below 75 Arts
# Otherwise You are in wait list
# Write a program to input total marks obtained in an examination and print the stream allotted

marks = int(input("enter the marks obtained "))
if(marks >=300):
    print("Congratutlations you got science")
elif(marks>=200 and marks<300):
    print("Congratulations you got Commerce")
elif(marks<200 and marks>=75):
    print("Congratulations you got arts")
elif(marks<75):
    print("Unfortunately you are in the waiting list")