import os
import time
source=[r'C:\Python27\example\cat.py',r'C:\Python27\example\for.py']

target_dir=r'C:\Python27\example\d'

target=target_dir+os.sep+time.strftime('%Y%m%d%H%M%S')+'.rar'
print source
print target
 
rar_command= '"C:\Python27\example\WinRAR.exe" a %s %s' %(target,' '.join(source))
print(rar_command)
print(os.system(rar_command))
if os.system(rar_command)==0:
    print 'Successful ',target
else:
    print 'fail'
