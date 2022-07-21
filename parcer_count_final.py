import re
from collections import Counter

def reader(filename):
    
    with open(filename) as f:
        log = f.read()
        log = re.sub(':\d{2}]', ']', log)
        while 0 < log.count("  "):
            log = log.replace('  ', ' ')
        ips_list = re.findall('\[.*NOK', log)

    return ips_list

def count(ips_list):
    
    count = Counter(ips_list)
    print(count)
  
if __name__ == '__main__':
    count(reader('events.log'))