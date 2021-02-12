def id_check(id_code, chk_list):
    counter = 0
    result = 0
    for num in chk_list:
        result += int(id_code[counter]) * num
        counter += 1
    return result % 11

id_code = input('Please enter your id code:\n')

chk1 = [1,2,3,4,5,6,7,8,9,1]
chk2 = [3,4,5,6,7,8,9,1,2,3]
id_code_list = list(id_code)



print(id_check(id_code, chk1))


# counter = 0
# result = 0
# for num in chk1:
#     result = chk1[counter] * int(id_code_list[counter])
#     counter += 1
# check_num = result % 11
#
if id_check(id_code, chk1) == 10:
    result = id_check(id_code, chk2)
    if result ==  int(id_code[10]):
    print('ID code is valid')
elif id check(id_code, chk1) == int(id_code[10])
    print
print(id_check(id_code, chk1))
#     for num in chk2:
#         result = chk2[counter] * int(id_code_list[counter])
#         counter += 1
#     check_num = result % 11
#     if check_num == int(id_code[-1]):
#         print('Code is valid')
#     else:
#         print('Code is not valid')
else:
    print('Code is not valid')

# for pozvoljaet primenit funkciju k kazhdomu elementu
#  result v dannom slu4ae kak korzinka s summoj, v kotoruju kazhdij raz novij resultat dobavljaetsja