import requests
import boto
from prettytable import PrettyTable

STATUS_ENDPOINT = 'devops_status'
AUTH = ('buycheck', 'knightrider2000')
RAILS_APP = 'opsworks:layer:rails-app'

# check on all running rails-apps instances
#
botoEC2 = boto.connect_ec2()
reservations = botoEC2.get_all_instances()

rails_apps = []
pt = PrettyTable(["name", "ip", "id", "state", "answer"])

for reserve in reservations:
    instance = reserve.instances[0]
    if 'Name' in instance.tags and RAILS_APP in instance.tags:
        answer = "N/A"
        if instance.ip_address is not None and instance.state == 'running':
        	r = requests.get('http://%s/%s'%(instance.ip_address, STATUS_ENDPOINT), auth=AUTH )
        	if r.status_code == 200:
        		answer = r.json()
        		answer = answer["git_revision"]

        pt.add_row([instance.tags['Name'], instance.ip_address, instance.id, instance.state, answer])

print pt

# also check on top level domains
#
pt = PrettyTable(["url", "hash"])
urls = ["http://development.carlingo.com/", "http://staging.carlingo.com/", "http://production.carlingo.com/"] 
for url in urls:
   r = requests.get(url + STATUS_ENDPOINT, auth=AUTH )
   if r.status_code == 200:
       answer =  r.json()
       pt.add_row([url, answer['git_revision']])
   else:
   		pt.add_row([url, r.status_code])

print pt


