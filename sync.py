#!/usr/bin/env python2
# encoding: utf-8

import os, shutil, filecmp, time

if __name__ == '__main__':
    sync_path = os.path.join(os.path.dirname(__file__), 'hosts')
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
