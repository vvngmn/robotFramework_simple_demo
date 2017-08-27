

class Test(object):
	def __init__(self,url):
		print url
		

	def test_login(self,**kargs):
		#self.logger.debug('login*******************************')
		print 'Login: '+kargs['username']
		return "Login successful"
		
		
	def test_logout(self,**kargs):
		print 'Logout: '+kargs['username']
		return "Logout successful"

if __name__=='__main__':
	print "start"

