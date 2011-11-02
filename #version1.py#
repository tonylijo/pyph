import sys
import serial
import time


def connect_phone(device,baurd_rate):
    '''Create a serial connection with the specified parameters'''
    return serial.Serial(sys.argv[1],int(sys.argv[2]),timeout=2)

def redial(modem):
    '''Redial a previous call'''
    modem.write("ATDL;\r\n")

def call(modem,number):
    '''call to a spesific number'''
    modem.write("ATD" +number+";\r\n")

def sendsms(number,modem):
    '''send an sms to a given number'''
    modem.write("ATZ\r\n")
    modem.write("AT+CMGF=1\r\n")
    modem.write('''AT+CMGS="''' + number + '''"\r\n''')
    print '-----------type your message below -------------------'
    print '>>',
    content =  raw_input()
    modem.write(content+"\r\n")
    modem.write(chr(26))
        
def sms_help():
    '''print the help '''
    print "commands\n1.call <number>\n2.help\n3.hangup\n4.getinfo\n5.sendsms <number>\n"

def getinfo(modem):
    '''get the mobile information '''
    modem.write("ATI\r\n")

def hangup(modem):
    '''hang up the call on the line'''
    modem.write("AT+CHUP\r\n")

def answer(modem):
    '''answer the incomming call'''
    modem.write("ATA+CRING\r\n")
    modem.sendBreak()
    print modem.read(1000)

def search(modem,name):
    modem.write('''AT+CPBF="'''+name+'''"\r\n''')
    modem.sendBreak()
    print modem.read(100)
    
def list_ph_book(modem,index1,index2):
    modem.write('''AT+CPBR='''+index1+','+index2+''' \r\n''')
    print modem.read(100000)

def modem_close(modem):
    modem.close()


def main():
    modem = connect_phone(sys.argv[1],sys.argv[2])
    while 1:
        print ">",
        command = raw_input()
        argv = command.split()
        if argv[0] == 'call':
            call(modem,argv[1])
        elif argv[0] == 'hangup' :
            hangup(modem)
        elif argv[0] == 'getinfo':
            getinfo(modem)
        elif argv[0] == 'sendsms':
            sendsms(argv[1],modem)
        elif argv[0] == 'exit':
            return modem
        elif argv[0] == 'answer':
            answer(modem)
        elif argv[0] == 'redial':
            redial(modem)
        elif argv[0] == 'search':
            search(modem,argv[1])
        elif argv[0] == 'list_ph_book':
            list_ph_book(modem,argv[1],argv[2])
        elif argv[0] == 'close_modem':
            close_modem(modem)
        else :
            sms_help()

if __name__ == '__main__':
    modem = main()
    modem.close()
