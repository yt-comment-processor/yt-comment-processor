# 프로그램을 실행하는데 필요한 패키지를 설치한다
# 요구 사항: subprocess 패키지, platfom 패키지와 shell 실행과 인터넷 접근 권한

import subprocess
import platform

requiredpacakges = ['tensorflow']

if platform.system() == 'Linux':
    print('리눅스 환경 감지됨')
    print('/usr/bin/bash 서브프로세스를 실행하는 중')
    for i in requiredpacakges:
        subprocess.run(['/usr/bin/bash', 'pip --install ' + requiredpacakges[i]])
elif platform.system() == 'Windows':
    print('윈도우 환경 감지됨')
    print('powershell.exe 서브프로세스를 실행하는 중')
    for i in requiredpacakges:
        subprocess.run(['powershell.exe', 'py -m pip --install ' + requiredpacakges[i]])