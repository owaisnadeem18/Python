# # Day : 19
# # 100 Days of Code
# # Topic : Break and continue Statement in Python

# # X---------------------------------------------------------------------------------X

# # i = 1

# for i in range(2, 11):
#     print(i)
#     i = i + 1
#     if (i == 10):
#         break  # It Will not print the next statement after the condition is being true and this process in programming is called as loop out

# # Continue Statement In Python
# print("*****Continue Statement*****")
# # i = 1

# # while(i<10):
# #     if(i==3):
# #         # print("Skip this 03rd Number")
# #         continue #The puropse of continue is to basically skip the next iteration , means it dont allow it to run and execute the next statement iteration of the program .
# #     print(i)
# #     # i = i + 1

# for i in range(1, 11):
#     if (i == 8):
#         continue  # It Will continue the loop again without executing the iteration condition print the next statement after the condition is being true and this process in programming is called as continue statement or skipping of an iteration
#     print(i)
#     i = i + 1

# # It is the most simplest concept of break and continue , whenever you use it , then it means that you are working on it to break a statement from a loop after some specific iterations

# for i in range(1, 11):
#   if i == 5:
#     continue
#   print(f"5 * {i} = {i*5}")

# for i in range(1, 11):
#   if i == 5:
#     break # The whole program will get terminated from here , because of this break function

#   print(f"5 * {i} = {i*5}")

# !!! Note: !!!
# Break statement: get out from loop
# Continue Statement: ignore the specific iteration
