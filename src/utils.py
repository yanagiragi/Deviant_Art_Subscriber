import requests
from bs4 import BeautifulSoup

class utils:

	def __init__(self):
		self.debug = None

	def __init__(self, debug):
		self.debug = debug

	def getSingleUser(self, illustid):
		return self.getPage('http://' + illustid + '.deviantart.com/gallery/?catpath=%2F&offset=',container=[])

	# start of getPage -----------------------------------------------------------
	def getPage(self, url, offset=0, container=[]):
		
		if self.debug:
			print('// Fetching Page: ' + url + str(offset))
		
		r = requests.get(url + str(offset));
		
		if r.status_code == 200:
			soup = BeautifulSoup(r.text, "html.parser")

			isend = soup.find('div', attrs={'class' : 'message'})
			if isend and isend.text == 'This section has no deviations yet!':
				if self.debug:
					print('// Done Fetching All Pages for [ ' + url + ' ]');
				return container

			span = soup.findAll('div', attrs={'id' : 'gmi-ResourceStream'})
			span = soup.findAll('span', attrs={ 'class' : 'shadow' })
			
			for i in range(0, len(span)):
				try:
					href = span[i].find('a').attrs['href']
				except AttributeError:
					continue
				
				try:
					title = span[i].find('a').find('img').attrs['alt']
				except KeyError:
					continue # skip since it may be novels

				try:
					thumbnail = span[i].find('a').attrs['data-super-img']
				except KeyError:
					try:
						thumbnail = span[i].find('img').attrs['src']
					except KeyError:
						thumbnail = '';

				try:
					pretitle = title.lower()
					if pretitle.index('dl') or pretitle.index('download'):
						flag = 1
					else:
						flag = 0
				except ValueError:
					flag = 0

				tmp = {
					'href' : href,
					'thumb' : thumbnail,
					'title' : title,
					'DL' : flag
				}

				if tmp not in container:
					container.append(tmp)

			return self.getPage(url, offset + 24, container) # continue fetching next page

		else:
			if self.debug:
				print('// Unable to Fetch Pages: [ ' + url + str(offset) + ' ]. Code = ' + str(r.status_code))
			return container

	# end of getPage -----------------------------------------------------------
