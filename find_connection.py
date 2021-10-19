import sys
import time
import psutil
def get_dcur(dpid):
    return [i.raddr.ip for i in psutil.net_connections() if i.pid == dpid and i.status == 'ESTABLISHED' and i.laddr.ip != '127.0.0.1' and i.raddr.port != 1119]

def add_seen(seen, dcur):
    new = set(set(dcur) - seen)
    return seen.union(new), new

def alarm():
    print('\aGAME FOUND')

def main(dtgt):
    dpid = [i for i in psutil.process_iter() if i.name()=="D2R.exe"][0].pid
    seen = set()
    while True:
        seen, new = add_seen(seen, get_dcur(dpid))
        print(f'New IP: {new}')
        if dtgt in new:
            alarm()
            break
        time.sleep(2)


if __name__ == '__main__':
    if (len(sys.argv) <= 1 or re.match(r'\d+\.\d+\.\d+\.\d+', sys.argv[1]) is None):
        search_ip = '127.0.0.1'
        print(f'passed argument is not an IP Address. Using default: {search_ip}')
    else:
        search_ip = sys.argv[1]
    main(search_ip)
