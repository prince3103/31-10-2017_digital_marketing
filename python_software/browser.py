import webbrowser, sys

sys.argv

if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
	
print(sys.argv)
webbrowser.open("https://www.google.com/maps/place/"+address)	