import weakref
class X:

	def __del__(self):
		print(self,"dead.")
def callback(w):
	print(w,w() is None)

def main():
	a=X()
	w=weakref.ref(a)
	del a

if __name__ == '__main__':
	main()




