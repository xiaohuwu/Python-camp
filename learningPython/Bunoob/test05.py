#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
import webbrowser, sys

if len(sys.argv) > 1:
	print(sys.argv)
	webbrowser.open("https://cn.bing.com/search?q=" + sys.argv[1])
else:
	print("error")
