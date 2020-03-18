choose = int(input('Enter your choice 1 for Encryption, 0 for Decrption'))

if choose == 1:
    msg = input('Enter your message here:- ')
    k1 = int(input('Enter your enc. key here:- '))
    a=0
    peek = str()

    while a < len(msg):
        seek = msg[a]
        a += 1
        enmsg = chr(ord(seek) + k1)
            #print (enmsg)
        for i in range(0,1):
            peek += enmsg[-1]
    print (peek)

elif choose == 0:
    msg = input('Enter your message here:- ')
    nick = str()
    a=0
    k2 = int(input('Enter your decrypt key here:- '))
    while a < len(msg):
        tip = msg[a]
        a += 1
        demsg = chr(ord(tip) - k2)
        for i in range(0,1):
            nick += demsg[-1]
    print (nick)

else:
    print ('Enter the given choice.')
