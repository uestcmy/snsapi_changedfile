import snsapi
from snsapi import snstype
from snsapi.utils import console_output, console_input
from snsapi.snspocket import SNSPocket
from snsapi.snslog import SNSLog as logger


sp = SNSPocket() 


sp.list_channel() 
sp.clear_channel() 


nc = sp.new_channel() 


nc["platform"] = "SinaWeiboStatus"
nc["app_secret"] = "c08d929687f1c78cf42784c25ef439f8"                   
nc["app_key"] = "2914339525"                           
nc["channel_name"] = "test_weibo"                      
nc["auth_info"]["callback_url"] = "http://snsapi.sinaapp.com/auth.php" 



sp.add_channel(nc) 


sp.auth()


sp.save_config()


sp.list_channel()


status =  sp.home_timeline()
print status
