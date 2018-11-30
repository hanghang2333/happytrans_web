file1 = 'xhj.conv'
file2 = 'xhj.happy'
import codecs
lines = codecs.open(file1,'r','utf8').readlines()
lines = [i.replace('\n','').replace('M','').replace('E','').strip() for i in lines]

ooo = []
end = len(lines)
start = 0
while start<end:
    tmp1 = start+1;tmp2 = start+2
    ooo.append(lines[tmp1]+' '+lines[tmp2])
    start+=3
file2 = codecs.open(file2,'w','utf8')
file2.write('\n'.join(ooo))
file2.close()