import json
from utils import *
from pprint import pprint

if __name__ == "__main__":

	util = utils(debug=None)

	MainContainer = []

	# Store wonderful creators in json/users.json!
	with open('../json/users.json') as json_data:
		illustids = json.load(json_data)
		json_data.close()

	for illustid in illustids:
		MainContainer.append({
				'author' : illustid,
				'containers' : util.getSingleUser(illustid)
			})
		
	print(json.dumps(MainContainer,indent = 4 ))