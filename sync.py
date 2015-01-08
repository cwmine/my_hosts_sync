#!/usr/bin/env python2
# encoding: utf-8
import os, shutil, filecmp, time

google_hosts = '../hosts'
my_hosts = 'myhosts'
output_hosts = 'output_hosts'
sync_path = output_hosts


def combine_host():
    """ combine the google host and my own host file segments """
    lines = []
    for path in [google_hosts, my_hosts]:
        with open(path, 'r') as f:
            lines += f.readlines()
    with open(output_hosts, 'w') as f:
        f.writelines(line for line in lines)



def sync_host_file():
    if os.name == 'nt':
        host_path = r'C:\Windows\System32\drivers\etc\hosts'
    elif os.name == 'posix':
        host_path = r'/etc/hosts'

    try:
        shutil.copy(sync_path, host_path)
    except IOError as e:
        print 'Copy error, need system previlege to do the synchronization!'
        print e.message
    else:
        if filecmp.cmp(sync_path, host_path):
            print 'Hosts file sync successfully!'
        else:
            print 'Sync failed !'
    finally:
        wait_time = 3.
        point_num = 5
        print 'Close in %.1f second' % wait_time,
        for i in range(point_num):
            time.sleep(wait_time/point_num)
            print '.',

if __name__ == '__main__':
    combine_host()
    sync_host_file()

