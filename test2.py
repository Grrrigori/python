user_input = input('Please insert ID code: ')
condition3 = (int(user_input[0])*1 + int(user_input[1])*2 + int(user_input[2])*3 + int(user_input[3])*4 + int(user_input[4])*5 + int(user_input[5])*6 + int(user_input[6])*7 + int(user_input[7])*8 + int(user_input[8])*9 + int(user_input[9])*1)%11
print(condition3)




condition4 = (int(user_input[0]) * 3 + int(user_input[1]) * 4 + int(user_input[2]) * 5 + int(
                user_input[3]) * 6 + int(user_input[4]) * 7 + int(user_input[5]) * 8 + int(user_input[6]) * 9 + int(
                user_input[7]) * 1 + int(user_input[8]) * 2 + int(user_input[9]) * 3) % 11
print(condition4)
# condition3 = True
# while condition3:
#     try:
#         if condition3 == int(user_input[10]):
#             print('ID code correct')
#     except:
#         print('ID code is not correct')
#     finally:
#         print('Happy Ending')
#         break
