import secrets
import hashlib
import time 

i = 1
string = "04212001"
p = secrets.token_bytes(32)
# only allow while loop to run for 1 min 
timeout = time.time() + 60
start_time = time.time()
while((i < len(string)) and (time.time() < timeout)):
    h=hashlib.sha256(p).digest()
    if(h.hex()[0:i]==string[0:i]):
        print(string[0:i])
        print('SHA256(' + p.hex() + ')=' + h.hex())
        i+=1
    p=h
end_time = time.time()
total_time = (end_time - start_time)
print("total amount of time (seconds) to find", i-1, "amount of nums within hash was:", total_time)
