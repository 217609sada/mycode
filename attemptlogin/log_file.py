#!/usr/bin/env python3

count = 0
with open('/home/student/mycode/attemptlogin/ketstone.common.wsgi') as file_content:
    ip = file_content.readlines()
    for x in ip:
        if "- - - - -] Authorization failed" in x:
            print(x[-11:])
            count = count + 1
#print(count)

