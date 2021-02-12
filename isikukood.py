
condition = True
while condition:

    user_choice = input('Please choose:\n1. Check id code\n0. Exit\n-->')
    # \n perenos stroki
    #  IF statement for user to choose option
    if user_choice == '1':
        condition2 = True
        while condition2:
            user_input = input('Please enter ypur national id: ')
            try:
                user_input =str(int(user_input))
                if len(user_input) != 11:
                # print("ID code you entered is too shortor or too long!")
                    if len(user_input) > 11:
                        print("ID code is too long")
                    elif len(user_input) < 11:
                        print(" ID code is too short")
                    raise UserWarning
                else:
                    condition2 = False
            except:
                print('Error')


            condition3 = True
            while condition3:
                condition3 = (int(user_input[0]) * 1 + int(user_input[1]) * 2 + int(user_input[2]) * 3 + int(
                    user_input[3]) * 4 + int(user_input[4]) * 5 + int(user_input[5]) * 6 + int(user_input[6]) * 7 + int(
                    user_input[7]) * 8 + int(user_input[8]) * 9 + int(user_input[9]) * 1) % 11
                if condition3 < 10 and condition3 == int(user_input[10]):
                    print('ID code correct1')
                    user_choice2 = input('Press enter to continue: ')

                elif condition3 >= 10:
                    condition4 = True
                    while condition4:
                        condition4 = (int(user_input[0]) * 3 + int(user_input[1]) * 4 + int(user_input[2]) * 5 + int(
                            user_input[3]) * 6 + int(user_input[4]) * 7 + int(user_input[5]) * 8 + int(
                            user_input[6]) * 9 + int(
                            user_input[7]) * 1 + int(user_input[8]) * 2 + int(user_input[9]) * 3) % 11
                        try:
                            if condition4 <= 10 and int(user_input[10]) == int(condition4):
                                print('ID code correct2')
                            elif condition4 > 10:
                                print('ID code is not correct')
                            else:
                                print('Error')
                        except:
                            print('no chance')

                else:
                    condition3= False
            else:
                # create variables ofr parts of ID
                gender_id = user_input[0]
                birth_year = user_input[1:3]
                birth_month = user_input[3:5]
                birth_day = user_input[5:7]
                birth_region = user_input[7:10]
                check_num = user_input[10]
            #     IF statement to check gender and century of birth
                if gender_id == "1":
                    gender_id = "male"
                    birth_cent = "18"
                elif gender_id == "2":
                    gender = "female"
                    birth_cent = "18"
                elif gender_id == "3":
                    gender = "male"
                    birth_cent = "19"
                elif gender_id == "4":
                    gender = "male"
                    birth_cent = "19"
                elif gender_id == "5":
                    gender = "male"
                    birth_cent = "20"
                elif gender_id == "6":
                    gender = "female"
                    birth_cent = "20"
                else:
                    gender = "unknown"
                    birth_cent = "unknown"
                print(birth_region)
                if int(birth_region) in range(1, 11):
                    region = "Kuresaare haigla"
                elif int(birth_region) in range(11, 20):
                    region = "Tartu Ülikoolki haigla"
                elif int(birth_region) in range(21, 151):
                    region = "Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)"
                elif int(birth_region) in range(151,161):
                    region = 'Keila haigla'
                elif int(birth_region) in range(161,221):
                    region = "Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)"
                elif int(birth_region) in range(221, 271):
                    region = "Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)"
                elif int(birth_region) in range(271, 371):
                    region = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
                elif int(birth_region) in range(371, 421):
                    region = "Narva haigla"
                elif int(birth_region) in range(421, 471):
                    region = 'Pärnu haigla'
                elif int(birth_region) in range(471, 491):
                    region = 'Haapsalu haigla'
                elif int(birth_region) in range(491, 521):
                    region = 'Järvamaa haigla (Paide)'
                elif int(birth_region) in range(521, 571):
                    region = 'Rakvere haigla, Tapa haigla'
                elif int(birth_region) in range(571, 601):
                    region = 'Valga haigla'
                elif int(birth_region) in range(601, 651):
                    region = 'Viljandi haigla'
                elif int(birth_region) in range(651, 701):
                    region = 'Lõuna-Eesti haigla (Võru), Põlva haigla'

                else:
                    region = "unknown"
                print("Your natioanal id is: " + user_input)
                print (" You are " + gender)
                print("Your date of birth is: " + birth_day + "." + birth_month + "." + birth_cent + birth_year)
                print(" You were born in ", region)

    # pass vremennaja konstruckija: propusti bez oshibki
    elif user_choice == "0":
        quit("Program has quit working")
    else:
        print("Choice out of range")

