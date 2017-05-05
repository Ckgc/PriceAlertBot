import sys
import requests
from time import sleep
import fileinput

URL = 'https://ca.pcpartpicker.com/product/3KL7YJ/acer-xr342ck-340-3440x1440-75hz-monitor-xr342ck-bmijpphz'
filename = 'E:\Test\source.txt'
search = 'class='
response = str(requests.get(URL).content)

def WriteSourceToFile(filename, source):
    f = open(filename, "w")
    f.write(source)
    f.close()

if __name__ == '__main__':
    while search in response:
        print('Nothing yet...')
        WriteSourceToFile(filename, response)
        sleep(60)
        response = str(requests.get(URL).content)

    WriteSourceToFile(filename, response)
    
    while True:
        sys.stdout.write('\aSOMETHING CHANGED!\n')
        sleep(0.5)
