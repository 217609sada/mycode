#!/usr/bin/env python3

def commandpush(devicecmd):
    for coffeetime in devicecmd.keys():
        print('\nHandshaking. .. ... connecting with ' + coffeetime )
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds)

def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"]}
    print("Welcome to the network device command pusher")
    #print("\nData set found\n")
    #commandpush(work2do)
    print("\n")
    new_list = []
    for ip in work2do.keys():
        new_list.append(ip)
    #print(new_list)
    devicereboot(new_list)

def devicereboot(iplist):
    for ip in iplist:
        print("Connecting to.." + ip)
        print("REBOOTING NOW!\n")

def commandpp(ip_list):
    print("connecting to " + str(ip_list[0]))
    for ii in ip_list:
        if ip_list.index(ii) > 0:
            print(ii)

#main()
with open("file.txt") as ipfile:
    ipfile_list = ipfile.readlines()
    new_list = []
    for item in ipfile_list:
        ff = item.strip()
        new_list.append(ff)
    print(new_list)
    commandpp(new_list)


