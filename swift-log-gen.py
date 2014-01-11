#!/usr/bin/python

#The program  create log entries for 'num_of_log_entries' number of lines.
#User-Input : num_of_log_entries -> number of log entries to create,output file

#This program creates a log for number of entries in an output file. The log has 22 fields seperated by space as follows:

#f1 f f3 f4 f5 f6 f7 f8 f9 f10 f11 f12 f13 f14 f15 f16 f17 f18 f19 f20 f21 f22

#f1 = month, f2 = day, f3 = hour/min/sec, f4 = node, f5 = process, f6 = ip address 1, f7 = ip address 2, f8 = day/month/year/hour/mins/secs, f9 = method, f10 = url, f11 = HTTP/1.0, f12 = response code, f13 = referer, f14 = user agent, f15 = auth_token, f16 = bytes received, f17 = bytes sent, f18 = etag, f19 = transaction id, f20 = logged hdrs, f21 = time taken, f22 = source



import os
import random
import os,binascii
import sys



month = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
method = ['GET', 'PUT', 'HEAD', 'DELETE', 'POST']
reseller = ['APPLE','SAMSUNG','TARGET','BESTBUY']
container = ['container0', 'container1', 'container2' , 'container3']
objects = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']
responsecode = ['200','201','202','301','302','400','401','403','404','500','503']


def create_log_entry(num_of_log_entries,filename):
    #tempstr = 'rm' + filename
    #os.system(tempstr)
    with open(filename,'wb') as fd:
        for i in range( num_of_log_entries ):
            f1 = '%s' %month[random.randrange(0,len(month))]
            day = random.randrange(0,28)
            f2 = '%s' %day
            hour = '%02d' % random.randrange(0,23)
            mins = '%02d' %random.randrange(0,59)
            secs = '%02d' %random.randrange(0,59)   
            msecs = random.randrange(0,1000)
            f3 = '%s:%s:%s.%s' %(hour,mins,secs,msecs)
            f4 = 'node1'
            f5 = 'proxy-server'
            f6 = '1.1.1.1'
            f7 = '2.2.2.2'
            year = 2013
            f8 = '%s/%s/%s/%s/%s/%s' %(day,month[random.randrange(0,len(month))],year,hour,mins,secs)
            f9 = method[random.randrange(0,len(method))]
            s1 = reseller[random.randrange(0,len(reseller))]
            s2 = container[random.randrange(0,len(container))]
            s3 = objects[random.randrange(0,len(objects))]
            f10 = '/v1/AUTH_' + s1 + '/' + s2 + '/' + s3
            f11 = 'HTTP/1.0'
            f12 = responsecode[random.randrange(0,len(responsecode))]
            f13 = '-'
            f14 = '-'
            f15 = '-'
            f16 = '%s' %random.randrange(0,1234000)
            f17 = '%s' %random.randrange(0,1234000)
            f18 = '-'
            f19 = binascii.b2a_hex(os.urandom(20))
            f20 = '-'
            timetaken = '%.3f' %random.uniform(0.000,400.000)
            f21 = '%s' %timetaken
            f22 = '-'
            fieldlist = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22]
            str1 = ' '
            str2 = str1.join(fieldlist)
            fd.write(str2)
            fd.write("\n")

if __name__ == "__main__":

    num_of_arguments = len(sys.argv)
    if (num_of_arguments < 5):
        print "Usage: %s -n <num_of_arguments> -o <output filename>" % sys.argv[0]
    else:
        num_of_log_entries =  int(sys.argv[2])
        filename = sys.argv[4]
        create_log_entry(num_of_log_entries,filename)
        
