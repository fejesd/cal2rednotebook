import struct
import datetime
from os import listdir
from os.path import isfile, join

def convert(fname):
        f = open(fname, 'rb')
        print('Converting... '+fname)
        header = f.read(8)
        refheader = [0xb5, 0xa2, 0xb0, 0xb3, 0xb3, 0xb0, 0xa2, 0xb5]
        if (bytes(header) == bytes(refheader)):
                print("header is ok")
        else:
                print("Not windows 3.1 calendar file")
                return
        (cDateDescriptors,) = struct.unpack("<h", f.read(2))
        print(str(cDateDescriptors)+" entries in the file")
        (MinEarlyRing, fSound, interval, mininterval, f24HourFormat, StartTime) = struct.unpack("<HHHHHH", f.read(12))
        print(MinEarlyRing, fSound, interval, mininterval, f24HourFormat, StartTime)
        f.read(64-22)
        dates = []
        startdate = datetime.datetime.strptime("01/01/80","%m/%d/%y")
        for i in range(0,cDateDescriptors):
                (Datedays, fMarked, cAlarms, FileBlockOffset, resv1, resv2) = struct.unpack("<HHHHHH", f.read(12))
                Date = startdate + datetime.timedelta(days = Datedays)
                dates.append({'Date':Date, 'Offset':FileBlockOffset})
        outs = {}
        for d in dates:
                f.seek(64*d['Offset'])
                (res1, DateDays, res2, cbNotes, cbAppointment) = struct.unpack("<HHHHH", f.read(10))
                Date = startdate + datetime.timedelta(days = Datedays)
                Notes = f.read(cbNotes)
                fn = '-'.join(str(d['Date']).split('-')[0:2])+'.txt'
                if (not (fn in outs)):
                        outs[fn] = ''
                outs[fn] = outs[fn] + str(int(str(d['Date']).split('-')[2].split(' ')[0]))+': {text: \'\n'
                while cbAppointment > 0:
                        (cb, flags, time) = struct.unpack("<BBH", f.read(4))
                        s = f.read(max(cb-5,0))
                        f.read(1)
                        cbAppointment = cbAppointment-cb
                        tt = s.decode('ISO-8859-2','ignore').replace('\'','').replace('\x80','euro')
                        outs[fn] = outs[fn] + '    ' + tt +'\n\n'
                outs[fn] = outs[fn] + '    \'}\n'
        for k in outs.keys():
                print(k)
                f = open(k, 'w',  encoding='utf-8')
                f.write('\ufeff')
                f.write(outs[k])
                f.close()



onlyfiles = [f for f in listdir('.') if isfile(join('.', f))]
for f in onlyfiles:
        if f.find('.CAL') != -1:
                convert(f)
print('No more cal files, exiting...')

