#!/usr/bin/env python3

vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "zach", "stuart"]
approved_vendors = ["cisco", "juniper", "big_ip"]
for x in vendors:
    print("The vendor is:" + x)
    if x not in approved_vendors:
        print(" - NOT AN APPROVED VENDOR!", end="\n")
print("\nOur loop has ended")
