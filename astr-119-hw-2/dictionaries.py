#define a dicitionary data structure

#dictionaries have key : value for the elements
example_dict = {
	"class" : "Astr 119",
	"prof" 	: "Brant", 
	"awesomeness"	: 10
}
print(type(example_dict)) 	#will say dict

#get a value via a key
course = example_dict["class"]
print(course)

#change a value via key
example_dict["awesomeness"] += 1 #increase awesomness by 1

#print the dictionary
print(example_dict)

#print dictionary element by element
for x in example_dict.keys():
	print(x, example_dict[x])