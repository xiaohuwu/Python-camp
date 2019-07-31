def print_models(unprint_designs, completed_models):
	while unprint_designs:
		item = unprint_designs.pop(0)
		print("print " + item)
		completed_models.append(item)


def show_models(completed_models):
	print("the following models have been printed")
	for completed_model in completed_models:
		print(completed_model)


unprint_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprint_designs[:], completed_models) # 此处只是传递了一个副本
print("unprint_designs:", unprint_designs)
show_models(completed_models)

