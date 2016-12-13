import json
from utils import *

MainContainer = []

# Some Wonderful Creators!
illustid = '********'

MainContainer.append({
		'author' : illustid,
		'containers' : getSingleUser(illustid)
	})

print(json.dumps(MainContainer))