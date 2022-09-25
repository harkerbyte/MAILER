import sys
from http.client import responses
from ast import Break, Try, excepthandler
import mechanize


if sys.version_info[0] !=3:
    print("please run tool with python3 : python3 MAIL.py!!")
    sys.exit()

print('----------------------------------------------------------------')
print('\033[1;31m ___  ___  ___   _____  _      _____ ______ \033[1;31m')
print(' |  \/  | / _ \ |_   _|| |    |  ___|| ___ \\')
print('\033[1;31m | .  . |/ /_\ \  | |  | |    | |__  | |_/ /\033[1;31')
print('\033[1;31m | |\/| ||  _  |  | |  | |    |  __| |    / \033[1;31')
print('\033[1;31m | |  | || | | | _| |_ | |____| |___ | |\ \ \033[1;32')
print('\033[1;31m \_|  |_/\_| |_/ \___/ \_____/\____/ \_| \_|\033[1;0')
print('----------------------------------------------------------------')
print("\033[1;33mEXPLORE MORE IN HACKING - https://facebook.com/cyberhacks6\033[1;0m")
print('\033[1;33mGITHUB PROFILE - https://github.com/shade234sherif\033[1;32m')
                                           
                                           
print("\033[1;32mANONY MAILER BY CYBERNETICS ~ MADE BY AN HACKER FOR HACKERS\033[1;32m")

br = mechanize.Browser()

to = input("Enter receivers mail address: ")
subject = input("Enter your message subject: ")
print ("Message: ")
message = input("Enter your message content: ")

url = "https://anonymouse.org/anonemail.html"
headers = "Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)"
br.addheaders = [('User-agent',headers)]
br.open(url)
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handler_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_debug_http(False)
br.set_debug_redirects(False)

br.select_form(nr=0)

br.form['To'] = to
br.form['Subject'] = subject
br.form['Message'] = message

responses = br.submit()

responses_data = responses.r()

if "Please note:	In order to increase your privacy, the anonymouse-mail will be randomly delayed up to 12 hours." in responses_data:
    print("\n The message has been successfully sent \n The recipient will get the message within 6hours!!! ")
else: 
    print('\033[1;31mFailed to send message\033[1;32m')
    print('\nPreparing an alternative module to fix issues.......\n')

excepthandler
 
ConnectionError
ConnectionRefusedError

Try
print('\n please check your wifi ~ cellular data connection\n then RESTART SOFTWARE!!')

sys.exit
