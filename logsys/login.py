"""
     * This login system contain: register, sign in, sign out, modify, delete, check, save data to file.
     * This login system is a demo, lot of function and method need promotion.
     * In part 2 --sign in, achieve only one account log still a problem
     * code still need to be optimized

"""
import os

__all__ = ['login']
__version__ = '2.0'


info = []
while True:
    print('===============================')
    print('WEOLCOME TO MY LOGIN SYSTEM v1.0')
    print('1.REGISTER')
    print('2.SIGN IN')
    print('3.SIGN OUT')
    print('===============================')

    command = input('PLEASE ENTER NUMBER：')

    if command == '1':
        account = input('REGISTER ACCOUNT：')
        passwd = input('REGISTER PASSWORD：')
        AKA = input('NICKNAME：')
        age = input('AGE：')

        # This module can set the limitation for registration
        # follow the rule can go deep otherwise back to the host
        if len(account) < 6 or len(account) > 20:
            print('ACCOUNT LENGTH MUST BETWEEN 6-20')

        elif len(passwd) < 8 or len(passwd) > 20:
            print('PASSWORD LENGTH MUST BETWEEN 8-20')

        else:
            # put the register data into a dict
            # set a file to receive the data and save it
            user = {}
            user['account'] = account
            user['passwd'] = passwd
            user['AKA'] = AKA
            user['age'] = age
            info.append(user)
            print('REGISTER SUCCESSFUL')
            # check the current path which avoid the error of file path
            os.getcwd()
            file = open('loginData.txt', 'a')
            file.write(str(info) + ',')
            file.close()

    elif command == '2':
        while True:

            Tips = input('PLEASE SELECT：1.CONTINUE SIGN IN  2.SKIP TO MAIN：')

            if Tips == '1':

                login_account = input('ACCOUNT：')
                login_passwd = input('PASSWORD：')
                # use a dict in loop to save only one account log in
                loginUser = {}
                loginUser['account'] = login_account
                loginUser['passwd'] = login_passwd

                if info == []:
                    print('NO SUCH ACCOUNT')
                    break
                # prevent error shw out when user haven't created account.
                # make sure only one account login
                for tmp in info:
                    if tmp['account'] == loginUser['account']:
                        print('LAODING......HOLD ON')
                    else:
                        print('NO SUCH ACCOUNT')
                        break

                for tmp1 in info:
                    # nest-if can check separately which part is error
                    if login_account == tmp1['account']:
                        if login_passwd == tmp1['passwd']:
                            print('ACCOUNT：%s，WELCOME!!!' % login_account )
                            print('============================')

                            while True:
                                    print('===========================================')
                                    print('WELCOME TO ACCOUNT MANAGEMENT SYSTEM v1.0')
                                    print('1.MODIFY INFORMATION')
                                    print('2.DELETE ACCOUNT')
                                    print('3.CHECK ACCOUNT')
                                    print('4.CHECK ALL ACCOUNT')
                                    print('5.SIGN OUT')
                                    print('===========================================')
                                    number = input('PLEASE ENTER NUMBER：')

                                    if number == '1':
                                        mod_account = input('OLD ACCOUNT:')
                                        for tmp in info:
                                            if mod_account == tmp['account']:
                                                new_account = input('NEW ACCOUNT：')
                                                tmp['account'] = new_account
                                                mentionedword = input('WOULD YOU WANT TO CHANGE OTHER INFORMATION?：Y/N')
                                                if mentionedword == 'Y':
                                                    new_passwd = input('NEW PASSWORD：')
                                                    tmp['passwd'] = new_passwd
                                                    new_AKA = input('NEW_NICKNAME：')
                                                    tmp['AKA'] = new_AKA
                                                    new_age = input('NEW_AGE：')
                                                    tmp['age'] = new_age
                                                    print('ALL UPDATE!')
                                                    break
                                                else:
                                                    print('ACCOUNT UPDATE!')

                                    if number == '2':
                                        del_account = input('DELETE ACCOUNT：')
                                        for tmp in info:
                                            if del_account == tmp['account']:
                                                tmp.clear()
                                            else:
                                                print('NO SUCH ACCOUNT')

                                    if number == '3':
                                        see_account = input('CHECK ACCOUNT：')
                                        for tmp in info:
                                            if see_account == tmp['account']:
                                                print('ACCOUNT：%s      PASSWORD：%s      NICKNAME：%s     AGE:%s' % (tmp['account'],tmp['passwd'],tmp['AKA'],tmp['age']))
                                            else:
                                                print('NO SUCH ACCOUNT')

                                    if number == '4':
                                        for tmp in info:
                                            print('ACCOUNT：%s      PASSWORD：%s       NICKNAME：%s     AGE:%s' % (tmp['account'],tmp['passwd'],tmp['AKA'],tmp['age']))
                                    if number == '5':
                                        # make sure current account sign out the loop
                                        loginUser.clear()
                                        print('SIGN OUT')
                                        break
                        else:
                             print('PASSWORD ERROR')

            elif Tips == '2':
                print('SKIP TO MAIN!!')
                break
            else:
                 print('NO SUCH OPERATION')

    elif command == '3':
        print('EXIT!')
        break

    else:
        print('NO SUCH OPERATION')

