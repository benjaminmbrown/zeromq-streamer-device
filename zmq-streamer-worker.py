import sys
import time
import zmq
import random

def consumer():
	#connect to same port as backend PUSH
	work_port = "5560"
	dest_port = "5561"

	consumer_id = random.randrange(1,10005)

	print "I am consumer #%s" % (consumer_id)

	context = zmq.Context()
	
	work_receiver = context.socket(zmq.PULL)
	work_receiver.connect("tcp://*:%s" % work_port)

  	work_destination = context.socket(zmq.PUSH)
    work_destination.connect("tcp://*:%s" % dest_port)
	
	while True:
		work = work_receiver.recv_json()
		data = work['num']
		pId = work['pId']
		result = {'consumer': consumer_id, 'num':data, 'pId':pId}
		work_destination .send_json(result)


