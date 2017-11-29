from numpy import zeros, exp, array, pi
def DFT(x):
	if type(x) is tuple:
		for i in range(len(x)):
			if type(x[i]) is str:
				raise ValueError()
	if type(x) is str or type(x) is int or type(x) is dict or type(x) is type(DFT):
		raise ValueError()
	if hasattr(x,'__len__'):
		m =[]
		#x = x.split()
		#x = array(x).astype(float)
		x = array(x)
		N = x.shape[0]
		n = zeros(N)
		for i in range(len(n)):
			n[i] = i
		k = n.reshape((N,1))
		M = exp(-2j * pi * k * n / N)
		#print(M)
		for i in range(N):
			s = 0
			for j in range(N):
				s = s + x[j]* M[i][j]
			m.append(s)
		return array(m)



# def main():
# 	x = (2,3,4,5,"B",3)
# 	print(DFT(x))
# 	#print(fft(x))

# if __name__ == '__main__':
#     main()