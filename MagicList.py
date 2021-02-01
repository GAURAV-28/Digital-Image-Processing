class MagicList :
	def __init__(self):
		self.data = [0]
	
	def findMin(self):
		M = self.data
		''' you need to find and return the smallest
			element in MagicList M.
			Write your code after this comment.
		'''
		if len(self.data)==1:
			return None
		else:
			return self.data[1]	
	
	def insert(self, E):
		M = self.data
		''' you need to insert E in MagicList M, so that
			properties of the MagicList are satisfied. 
			Return M after inserting E into M.
			Write your code after this comment.
		'''
		self.data.append(E)
		i=len(self.data)-1
		while not (self.data[i//2] < E or i==1) :
			self.data[i],self.data[i//2]=self.data[i//2],self.data[i]
			
			i=i//2


	def deleteMin(self):
		M = self.data
		''' you need to delete the minimum element in
			MagicList M, so that properties of the MagicList
			are satisfied. Return M after deleting the 
			minimum element.
			Write your code after this comment.
		'''
		E1=self.data[1]
		E2=self.data[len(self.data)-1]
		self.data[1],self.data[len(self.data)-1]=self.data[len(self.data)-1],self.data[1]
		self.data.pop()
		i=1
		
		while 2*i<=len(self.data)-1 and 2*i+1<=len(self.data)-1:
			

			if self.data[i]>self.data[2*i] or self.data[i]>self.data[2*i+1]:
				if self.data[2*i]>self.data[2*i+1]:
					self.data[i],self.data[2*i+1]=self.data[2*i+1],self.data[i]
					i=2*i+1
				else:
					self.data[i],self.data[2*i]=self.data[2*i],self.data[i]
					i=2*i	
			else:
				break		

		while 2*i<=len(self.data)-1 and 2*i+1>=len(self.data)-1:
			

			if self.data[i]>self.data[2*i]:
				
				self.data[i],self.data[2*i]=self.data[2*i],self.data[i]
				i=2*i
			else:
				break		

	
def K_sum(L, K):
	''' you need to find the sum of smallest K elements
		of L using a MagicList. Return the sum.
		Write your code after this comment.
	'''
	M=MagicList()
	for i in L:
		M.insert(i)
	sum=0
	i=0
	while i<K:
		sum+=M.findMin()
		M.deleteMin()
		i=i+1
	return sum	

	
if __name__ == "__main__" :
	'''Here are a few test cases'''
	
	'''insert and findMin'''
	M = MagicList()
	M.insert(4)
	M.insert(3)
	M.insert(5)
	M.insert(2)
	M.insert(8)
	M.insert(7)
	
	x = M.findMin()
	if x == 2:
		print("testcase 1 : Passed")
	else :
		print("testcase 1 : Failed")
		
	'''deleteMin and findMin'''
	M.deleteMin()
	x = M.findMin()
	if x == 3 :
		print("testcase 2 : Passed")
	else :
		print("testcase 2 : Failed")
		
	'''k-sum'''
	L = [2,5,8,3,6,1,0,9,4]
	K = 4
	x = K_sum(L,K)
	if x == 6 :
		print("testcase 3 : Passed")
	else :
		print("testcase 3 : Failed")

	M.deleteMin()
	M.deleteMin()
	a= M.findMin()
	if a==5:
		print('testcase 4 : Passed')
	else:
		print('testcase 4 : Failed')
	M.insert(1)
	M.insert(3)
	y=M.findMin()
	if y==1:
		print('testcase 5 : Passed')
	else:
		print('testcase 5 : Failed')
	M.deleteMin()
	z=M.findMin()
	if z==3:
		print('testcase 6 : Passed')
	else:
		print('testcase 6 : Failed')
	N=[3,5,6,1,2,8,4]
	k=3
	p=K_sum(N,k)	
	if p==6:
		print('testcase 7 : Passed')
	else:
		print('testcase 7 : Failed')						
