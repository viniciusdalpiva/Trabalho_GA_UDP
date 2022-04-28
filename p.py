import os
import socket
import time
import threading
import sys
import subprocess

inp = input("\n1 > PC e Note: \n2 > DOCKER: ")

if(inp) == "1":
                #PC                  note windows         linux terminal docker vm 
    clients = [('192.168.0.107',9001), ('192.168.0.110',9002), ('172.17.0.2',9003) ]

else:
                #PC                  note windows         linux terminal docker vm 
    clients = [('172.17.0.2',9001), ('172.17.0.3',9002), ('172.17.0.4',9003) ]



def recebe():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((ip_sender, port_sender))

    while True:
        time.sleep(0.4)
        msg, END_cliente = s.recvfrom(2048)
        
        
        comando = msg.decode()
        auxmsgsplit = ''
        if "|" in comando:

            mensagemSplit = comando.split("|")
            print(mensagemSplit[1])
            #envia a str como comando no cmd
            os.system(mensagemSplit[1])
            auxmsgsplit = mensagemSplit[1]
            z = os.popen(auxmsgsplit).read()
            
            x = "\nRetorno de "+ip_sender+"\n"+z #"RETORNO OUTPUT DO COMANDO"
            
            for i in clients:
                if(i[0] == END_cliente[0]):
                    s.sendto(x.encode(), i)   
        else:
            print(comando)

        

def envia():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = ""
    while True:
        if "exit" in text:
            exit()
        else:
            text = input(f'{name}:')
            text = name+"|"+text

            for i in clients:
                #udp.sendto(bytes(MsgEnvio, "utf8"), i)
                if(i[1] != port_sender):
                    s.sendto(text.encode(), i)


            

ip_sender = input("\nDigite seu IP  ")            #"192.168.0.107" #IP PC WINDOWS
port_sender = int(input("\nDigite a sua porta: "))#9001          #PORTA PC WINDOWS
name = ip_sender


send = threading.Thread(target=envia)
receive = threading.Thread(target=recebe)
send.start()
receive.start()
