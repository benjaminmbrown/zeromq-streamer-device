import zmq

# Producer PUSH--> frontend PULL - STREAMER - backend PUSH to Worker -> PULL to worker -> WORKER -> PUSH to results collector
def main():
	try:
		print "Streaming device awaiting work..."
		context = zmq.Context(1)

		fe = context.socket(zmq.PULL)
		fe.bind("tcp://*:5559")

		be = context.socket(zmq.PUSH)
		be.bind("tcp://*:5560")

		#create streamer device with fe & be
		zmq.device(zmq.STREAMER, fe, be)

	except Exception, e:
		print e
		print "Destroying zmq Streamer Now"
	finally:
		pass
		fe.close()
		be.close()
		context.term()

if __name__ =="__main__":
	main()