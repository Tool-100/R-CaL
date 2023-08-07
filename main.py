   
def add(a,b):
   print ("~$",a+b)

def sub(a,b):
   print ("~$",a-b)

def mul(a,b):
   print ("~$",a*b)

def divi(a,b):
   print ("~$",a/b)
#=================================================
def Bannr():
    print ("\033[1;33m")
    print ("██████         █████   █████  ██")
    print ("██   ██       ██   ██ ██   ██ ██")
    print ("██████  █████ ██      ███████ ██")
    print ("██   ██       ██   ██ ██   ██ ██")
    print ("██   ██        █████  ██   ██ ███████")
    print ("\033[1;34m_____________________________________")
    print ("               Tool by-#####         ")
    print ("                         red hecker  ")
    print ("\033[1;34m_____________________________________")
    print ("\033[1;31m[1] \033[1;32m ADD      (+)")
    print ("\033[1;31m[2] \033[1;32m SUB      (-)")
    print ("\033[1;31m[3] \033[1;32m MULTIPIY (×)")
    print ("\033[1;31m[4] \033[1;32m DIVIDE   (÷)")
    print ("")
    print ("\033[1;31m[5] \033[1;32m EXIT")
    print ("")
def main():
    x=int(input("\033[1;31m[*]\033[1;33mUser Tool start  Enter your number 》》"))
    a=int(input("\033[1;31m[*]\033[1;33mEnter first number 》》"))
    b=int(input("\033[1;31m[*]\033[1;33mEnter second number 》》"))

    if x==1:
      add(a,b)
    elif x==2:
      sub(a,b)
    elif x==3:
      mul(a,b)
    elif x==4:
      divi(a,b)
    elif x==5:
      Bannr()
    else:
      print ("\033[1;31mUser Tool not fund..! ")


Bannr()
main()
