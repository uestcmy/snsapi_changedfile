import snsapi
from snsapi import snstype
from snsapi.utils import console_output, console_input
from snsapi.snspocket import SNSPocket
from snsapi.snslog import SNSLog as logger


sp = SNSPocket() 


sp.list_channel() 
sp.clear_channel() 


nc = sp.new_channel() 


nc["platform"] = "RenrenStatus"
nc["app_secret"] = "ae8216bac5e9468e993678627f4feaba"                   
nc["app_key"] = "03af00adef1440899c62f8a76d05400f"                           
nc["channel_name"] = "test_renren"                      
nc["auth_info"]["callback_url"] = "http://snsapi.sinaapp.com/auth.php" 


sp.add_channel(nc) 


sp.auth()
sp.save_config()


sp.list_channel()


status =  sp.home_timeline()
#print status
nc2 = sp.new_channel();
nc2["platform"] = "RSS2RW"
nc2["channel_name"] = "output"
nc2["url"] = "output.atom"
sp.add_channel(nc2) 
sp.auth()
sp.save_config()
sp.list_channel()

sl = sp.home_timeline(5)
print sl[0]
print sp.home_timeline(channel = "output")
sp.update(text = unicode(sl[0]), channel = "output")
print sp.home_timeline(channel = "output")
sp.update(text = unicode(sl[3]), channel = "output")
print sp.home_timeline(channel = "output")
