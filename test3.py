condition3 = True
while condition3:
    user_input = input("Enter ID code: ")
    condition3 = (int(user_input[0])*1 + int(user_input[1])*2 + int(user_input[2])*3 + int(user_input[3])*4 + int(user_input[4])*5 +int(user_input[5])*6 + int(user_input[6])*7 + int(user_input[7])*8 + int(user_input[8])*9 + int(user_input[9])*1)%11
    if condition3 < 10 and condition3 == int(user_input[10]):
        print('ID code correct1')
    elif condition3 >= 10:
        condition4 = True
        while condition4:
            condition4 = (int(user_input[0]) * 3 + int(user_input[1]) * 4 + int(user_input[2]) * 5 + int(
                user_input[3]) * 6 + int(user_input[4]) * 7 + int(user_input[5]) * 8 + int(user_input[6]) * 9 + int(
                user_input[7]) * 1 + int(user_input[8]) * 2 + int(user_input[9]) * 3) % 11
            try:
                if condition4 <= 10 and int(user_input[10]) == int(condition4):
                    print('ID code correct2')
                elif condition4 > 10:
                    print('ID code is not correct')
                else: print('Error')
            except:
                print('no chance')

    else:
        print('wrong')

    # elif condition3 >= 10:
    # condition4 = (int(user_input[0])*3 + int(user_input[1])*4 + int(user_input[2])*5 + int(user_input[3])*6 + int(user_input[4])*7 +int(user_input[5])*8 + int(user_input[6])*9 + int(user_input[7])*1 + int(user_input[8])*2 + int(user_input[9])*3)%11
    # if condition4 >= 10:
    #     print('ID code correct')
    # elif condition4 <=10:
    #     print('ID code correct')
    # elif int(user_input[11]) == int(0):
    #     print('ID code correct')
    # else: print('Error')





# some_number = 100
#
# if some_number > 10 and some_number > 200:
#     print(" Some string is greater than 10 characters")
# else:
#     print("error")