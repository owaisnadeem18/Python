# Question # 03
# here in this Question , we've to answer about a question that if we're creating two things . One is class attribute and the next is instance attribute . Now, we've to answer that will the class attribute get changed ? if we're creating another instance attribute after declaring our object of any name ?

class A:
    class_attribute = "Owais"
    # print(class_attribute)

obj = A()

obj.class_attribute = "Hamza"
print(A.class_attribute)
print(obj.class_attribute)
# print(obj.class_attribute)
# class_attribute = "hamza"

# Here , we got our answer that obj attribute is another thing , while class attribute is a different thing . Our class attribute will not get change even if we call our class attribute with object of the same class 