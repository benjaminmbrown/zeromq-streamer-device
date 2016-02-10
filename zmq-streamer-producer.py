import time
import zmq

def producer:
	streamer_pull_port = 5559
	context = zmq.Context()
	socket = context.socket(zmq.PUSH)
	#connectC to streamer PULL socket
	socket.connect("tcp://127.0.0.1:%s" % streamer_pull_port)
	publisher_id = random.randrange(0,9999)
	#create some work
	for num in range(20000):
		work_message = {'num': num, 'pId':producer_id}
		print "Sending work message num: ", num
		socket.send_json(work_message)
		time.sleep(0.5)

producer()