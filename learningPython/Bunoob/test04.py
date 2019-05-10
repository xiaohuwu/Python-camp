thisdict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}

# get item
key = thisdict.get("model")
key1 = thisdict["model"]
print(key)

# print value
for x in thisdict.values():
	print(x, end="\t")

print()
for y in thisdict:
	print(thisdict[y], end="\t")

print()

for x, y in thisdict.items():
	print(y, end="\t")