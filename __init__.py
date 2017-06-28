from modules import app, cbpi
from thread import start_new_thread
import logging
import time
import requests

ifttt_key = None
ifttt_event = None
ifttt = None

def iftttKEY():
	global ifttt_key
	ifttt_key = cbpi.get_config_parameter("ifttt_key", None)
	if ifttt_key is None:
		print "INIT IFTTT KEY"
		try:
			cbpi.add_config_parameter("ifttt_key", "", "text", "IFTTT Maker Key")
		except:
			cbpi.notify("IFTTT Error", "Unable to update database. Update CraftBeerPi and reboot.", type="danger", timeout=None)

def iftttEvent():
	global ifttt_event
	ifttt_event = cbpi.get_config_parameter("ifttt_event_name", None)
	if ifttt_event is None:
		print "INIT IFTTT EVENT NAME"
		try:
			cbpi.add_config_parameter("ifttt_event_name", "", "text", "IFTTT Maker Event Name")
		except:
			cbpi.notify("IFTTT Error", "Unable to update database. Update CraftBeerPi and reboot.", type="danger", timeout=None)

@cbpi.initalizer(order=9000)
def init(cbpi):
	global ifttt
	cbpi.app.logger.info("INITIALIZE IFTTTMessages PLUGIN")
	iftttKEY()
	iftttEvent()
	if ifttt_key is None or not ifttt_key:
		cbpi.notify("IFTTT Error", "Check ifttt_key parameter", type="danger", timeout=None)
	elif ifttt_event is None or not ifttt_event:
		cbpi.notify("IFTTT Error", "Check ifttt_event_name parameter", type="danger", timeout=None)
	else:
		ifttt = "OK"

@cbpi.event("MESSAGE", async=True)
def messageEvent(message):
	report = {}
	report["value1"] = message["headline"]
	report["value2"] = message["message"]
	requests.post("https://maker.ifttt.com/trigger/{}/with/key/{}".format(ifttt_event, ifttt_key), data=report)
