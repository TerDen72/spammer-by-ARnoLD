import os
os.system("pkg install dos2unix")
os.system("pip install colorama")
os.system("pip install requests")
os.system("cp ~/spammer-by-ARnoLD/spammer.py /data/data/com.termux/files/usr/bin/spammer-by-ARnoLD")
os.system("dos2unix /data/data/com.termux/files/usr/bin/spammer-by-ARnoLD")
os.system("chmod -R 777 ~/spammer-by-ARnoLD")
os.system("chmod 777 /data/data/com.termux/files/usr/bin/spammer-by-ARnoLD")
os.system("spammer")