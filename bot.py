import sys
import socket

def conn(HOST, PORT, NICK, IDENT, REALNAME, BOTMSG, CHAN):
    s=socket.socket( )
    s.connect((HOST, PORT))

    s.send(bytes("NICK {}\n".format(NICK), "UTF-8"))
    s.send(bytes("USER {} {} {} {}\n".format(IDENT, HOST, REALNAME, BOTMSG), "UTF-8"))
    s.send(bytes("JOIN {}\n".format(CHAN), "UTF-8"));
    s.send(bytes("PRIVMSG {} :Oi pessoal! Eu sou o {}, um bot beberrum. Peca sua cerva com {}\n".format(CHAN, NICK, "!CERVA") , "UTF-8"))
    return s

def answer():
    sender = ""
    for char in line[0]:
        if(char == "!"):
            break
        if(char != ":"):
            sender += char 
    size = len(line)
    i = 3
    message = ""
    while(i < size): 
        message += line[i] + " "
        i = i + 1
    message.lstrip(":")
    if "!CERVA" in message:
        s.send(bytes("PRIVMSG {} :Saindo uma gelada para {}!\n".format(CHAN, sender) , "UTF-8"))

###### CONFIG OPTIONS ######
HOST = "irc.freenode.org"
PORT = 6667

NICK = "pogBot"
IDENT = "pogBot"
REALNAME = "pogBot"
BOTMSG = "peça sua cerva"
CHAN = "#pogTest"


s = conn(HOST, PORT, NICK, IDENT, REALNAME, BOTMSG, CHAN)
readbuffer = ""


###### MAIN LOOP ######
while 1:
    readbuffer += s.recv(1024).decode("UTF-8")
    temp = str.split(readbuffer, "\n")
    readbuffer = temp.pop( )

    for line in temp:
        line = str.rstrip(line)
        line = str.split(line)

        if(line[0] == "PING"):
            s.send(bytes("PONG {}\r\n".format(line[1]), "UTF-8"))
        if(line[1] == "PRIVMSG"):
            answer()
        for index, i in enumerate(line):
            print(line[index])
