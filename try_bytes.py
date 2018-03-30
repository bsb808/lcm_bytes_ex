import traceback
from exlcm import array_first_t
from exlcm import byte_first_t
from exlcm import int_array_first_t


# Attempt with byte first
msg_types = [byte_first_t,int_array_first_t,array_first_t]
for m in msg_types:
    txmsg = m()
    data = txmsg.encode()
    try:
        rxmsg = m.decode(data)
        print('Success with message type %s'%m.__name__)
    except:
        print('Failed with message type %s'%m.__name__)
        traceback.print_exc()
