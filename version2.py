import sys
import serial
import time


def connect_phone(device,baurd_rate):
    '''Create a serial connection with the specified parameters'''
    return serial.Serial(sys.argv[1],int(sys.argv[2]),timeout=2)

def call(argv):
    '''call to a spesific number'''
    modem = argv[0]
    number = argv[2]
    modem.write("ATD"+number+";\r\n")

def redial(argv):
    '''Redial a previous call'''
    modem = argv[0]
    modem.write("ATDL;\r\n")

def sendsms(argv):
    '''send an sms to a given number'''
    modem = argv[0]
    number = argv[2]
    modem.write("ATZ\r\n")
    modem.write("AT+CMGF=1\r\n")
    modem.write('''AT+CMGF="''' + number+ '''"\r\n''')
    print '-------------type your message below------------'
    print '>>',
    content = raw_input()
    modem.write(content+"\r\n")
    modem.write(chr(26))

def sms_help(argv):
    '''print the help about how to use the commands'''
    print "commands\n1.call <number>"
    print "2.help"
    print "3.hangup"
    print "4.getinfo"
    print "5.sendsms <number>"

def getinfo(argv):
    '''get the mobile information'''
    modem.write("ATI\r\n")

def hangup(argv):
    '''hang up the call on the line'''
    modem = argv[0]
    modem.write("AT+CHUP\r\n")
    
def answer(argv):
    '''answer the incomming call'''
    modem = argv[0]
    modem.write("ATA+CRING\r\n")
    modem.sendBreak()
    print modem.read(1000)

def search(argv):
    modem = argv[0]
    modem.write('''AT+CPBF="'''+name+'''"\r\n''')
    modem.sendBreak()
    print modem.read(100)

def list_ph_book(argv):
    modem = argv[0]
    modem.write('''AT+CPBP='''+index1+','+index2+''' \r\n''')
    print modme.read(100000)

def modem_close(modem):
    modem = argv[0]
    modem.close()

command_dict = {'call':call,'cut':hangup,'getinfo':getinfo,
                'sendsms':sendsms,'redial':redial,'search':search}

def main():
	modem = connect_phone(sys.argv[1],sys.argv[2])
	while 1:
		print ">"
		command = raw_input()
		argv = command.split()
		command_dict[argv[0]]([modem] + argv)
		
if __name__ == '__main__':
    modem = main()
    modem.close()
