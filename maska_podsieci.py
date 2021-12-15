def host_count(maska):
    mlist = maska.split('.')
    zeros = 0
    for octet in mlist:
        octint = int(octet)
        if octint == 0:
            zeros += 8
        elif (octint > 0) and (octint < 255):
            octbin = str(bin(octint))
            zeros += octbin.count('0')-1 # Minus jedno zero, bo funkcja bin() zwraca liczbe z prefixem 0b np. 0b11110000
    return 2**zeros - 2
  

maskvals = ['0','128','192','224','240','248','252','254']

for maskval in maskvals:
    maska = maskval+'.0.0.0'
    hosty = host_count(maska)
    print(' '*(15-len(maska)),maska,'=',hosty)
for maskval in maskvals:
    maska = '255.'+maskval+'.0.0'
    hosty = host_count(maska)
    print(' '*(15-len(maska)),maska,'=',hosty)
for maskval in maskvals:
    maska = '255.255.'+maskval+'.0'
    hosty = host_count(maska)
    print(' '*(15-len(maska)),maska,'=',hosty)
for maskval in maskvals:
    maska = '255.255.255.'+maskval
    hosty = host_count(maska)
    print(' '*(15-len(maska)),maska,'=',hosty)
