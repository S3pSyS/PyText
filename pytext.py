import os
import subprocess
import platform


print('''
------------------------------------------------------------------
:::::::::  :::   ::: ::::::::::: :::::::::: :::    ::: ::::::::::: 
:+:    :+: :+:   :+:     :+:     :+:        :+:    :+:     :+:     
+:+    +:+  +:+ +:+      +:+     +:+         +:+  +:+      +:+     
+#++:++#+    +#++:       +#+     +#++:++#     +#++:+       +#+     
+#+           +#+        +#+     +#+         +#+  +#+      +#+     
#+#           #+#        #+#     #+#        #+#    #+#     #+#     
###           ###        ###     ########## ###    ###     ###
------------------------------------------------------------------
** Terminal Based Text Editor Written in Python By NecroSyS **
------------------------------------------------------------------
''')


print('[1] Create New File')
print('[2] Use Existing file')
print('[3] Exit')
choice = input('\n$:PyText~>: ')
if choice == '1':
    file_name = input('File Name: ')
    with open(file_name, 'w') as f:
        f.close()
        print('[*] File created!')
        print('------------------------------------------------------------------')
        while True:
            with open(file_name, 'a') as new_file:
                user_input = input('')
                if user_input == '/close' or user_input == '/exit':
                    new_file.close()
                    print('\n[*] Goodbye :)\n')
                    exit()
                    break

                elif user_input == '/cmd' or user_input == '/run':
                    user_input_cmd = input('')
                    subprocess.Popen(user_input_cmd, shell=True)
                    continue

                elif user_input == '/cls' or user_input == '/clear':
                    os.system('cls')
                    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)
                    continue

                else:
                    new_file.writelines(user_input + '\n')
                    continue


elif choice == '2':
    print('[*] using existing file')
    file_name = input('File Path: ')
    print('\n------------------------------------------------------------------\n')
    with open(file_name, 'r') as f:
        pre_written_text = f.read()
        print(pre_written_text)
        f.close()

    while True:
        with open(file_name, 'a') as f:
            user_input = input('')
            if user_input == '/close' or user_input == '/exit':
                f.close()
                print('\n[*] Goodbye :)\n')
                exit()
                break

            elif user_input == '/cmd' or user_input == '/run':
                user_input_cmd = input('')
                os.system(user_input_cmd)
                continue

            elif user_input == '/help' or user_input == '/h':
                print('''---------------------------------------------
                Usage:
                - /help or /h to display this message.
                - /cls or /clear to clear the terminal.
                - /cmd or /run to execute OS commands.
                - /close or /exit to save your file and exit.
                ---------------------------------------------
                ''')
                continue

            elif user_input == '/cls' or user_input == '/clear':
                os.system('cls')
                subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)
                continue

            else:
                f.writelines(user_input + '\n')
                continue

elif choice == '3':
    print('\n[*] Goodbye :)\n')
    exit()

else:
    print('invalid command')
    exit()
