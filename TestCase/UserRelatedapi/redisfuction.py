"""
@File  ：redisfuction.py
@Author: chenjialuo
@Time  : 2020/7/28
@Desc  : 链接redis，修改验证次数

"""

from rediscluster import StrictRedisCluster

def deviceOR(num,count):
	# nodes传入的redis的ip和port和db
	nodes = [{"host": "192.168.1.201", "port": "8001","db":0}]
	# 链接redis池
	r = StrictRedisCluster(startup_nodes=nodes,decode_responses=True)
	# 根据建get到相关键值
	res = r.get("sms:count:"+str(num)+":"+count)
	if int(res) > 10 :
		# 修改键值
		r.set("sms:count:"+str(num)+":"+count,"1")
def phoneOR(num,area,count):
	# nodes传入的redis的ip和port和db
	nodes = [{"host": "192.168.1.201", "port": "8001","db":0}]
	# 链接redis池
	r = StrictRedisCluster(startup_nodes=nodes,decode_responses=True)
	# 根据建get到相关键值
	res = r.get("sms:count:"+str(num)+":"+area+count)
	if int(res) > 10 :
		# 修改键值
		r.set("sms:count:"+str(num)+":"+area+count,"1")

# deviceORphone("d41b071ca83ece2")
# phoneOR(2,"15816262885")