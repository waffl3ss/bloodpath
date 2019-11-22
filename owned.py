#!/usr/bin/python3
# James Pletcher, 2019

import requests, json
import getopt, sys
import base64

dbusername = 'neo4j'
dbpassword = 'BloodHound'

preauth = dbusername + ':' + dbpassword
auth = str(base64.b64encode(preauth.encode('utf-8')), 'utf-8')

url = 'http://localhost:7474/db/data/transaction/commit'
headers = { "Accept": "application/json; charset=UTF-8",
		"Content-Type": "application/json",
		"Authorization": auth }
data = {"statements": [{'statement': statement}]}

def main(argv):
	node_type = ''
	node_label = ''
	request = ''
	domain = ''

	try:
		opts, args = getopt.getopt(argv,"hr:t:l:d:",["request=", "type=","label=","domain="])
	except getopt.GetoptError:
		print ('test.py -r <request type> -t <node type> -l <node label>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('test.py -r <request type> -t <node type> -l <node label>')
			sys.exit()
		elif opt in ("-r", "--request"):
			request = arg
		elif opt in ("-t", "--type"):
			node_type = arg
		elif opt in ("-l", "--label"):
			node_label = arg
		elif opt in ("-d", "--domain"):
			domain = arg
	mux(request, node_type, node_label)

def mux(request, node_type, node_label):
	if request == 'domains':
		get_domains();
	elif request == 'owned':
		mark_owned(node_type, node_label)
	else:
		print("Error: unknown request type")

def mark_owned(nodetype, nodelabel):
	statement = 'MATCH (n) WHERE toLower(n.name) CONTAINS "' + nodelabel.lower() + '" SET n.owned=True RETURN n'
	r = requests.post(url=url,headers=headers,json=data)
	print(r.text)

def get_domains():
	statement = "MATCH (n:Domain) RETURN n"
	r = requests.post(url=url,headers=headers,json=data)
	j = json.loads(r.text)
	output = ''
	for x in range(len(j["results"][0]["data"])):
		output = output + j["results"][0]["data"][x]["row"][0]["name"] + ','
	print(output[0:len(output)-1])

main(sys.argv[1:])
