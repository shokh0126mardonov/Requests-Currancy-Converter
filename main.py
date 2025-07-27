from sys import exit
from usd_sum import usd_to_sum
from sum_usd import sum_to_usd
from printers import print_menu

while True:
    print_menu()
    tanlov = int(input("tanlang = ")) 
    if tanlov == 1:
        usd_to_sum()
    elif tanlov == 2:
        sum_to_usd()
    elif tanlov == 3:
        exit()