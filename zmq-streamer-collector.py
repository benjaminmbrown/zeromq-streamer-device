import time
import zmq
import pprint

def collector():
	port = "5561"
	print "Running results collector"
	context = zmq.Context()
	results_receiver = context.socket(zmq.PULL)
	results_receiver.bind("tcp://*:%s" % port)

	collector_data = {}

	for x in xrange(1000):
		result = results_receiver.recv_json()
		print "Got a result", result
		if(collector_data.has_key(result['consumer'])):
			collector_data[result['consumer']] = collector_data[result['consumer']] +1
		else:
			collector_data[results['consumer']] = 1
		if x ==999:
			pprint.pprint(collector_data)
		pprint.pprint(result)

collector()