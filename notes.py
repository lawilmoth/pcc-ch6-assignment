# Chapter 6 Dictioanries

# Dictionaries are key value pairs
# You use a key to find a value

#Example
languages = {"mrw": "Python", "Halim": "JS", "Hayden": "Minecraft"}

#print(languages["mrw"]) # The key is mrw and the value is Python

alien = {"color": "green", "points": 5, "location" : "center"}
#print(alien["color"])

#looping over all keys
for key in alien.keys():
    print(key)

#Check if a key is in the dictionary
if "vehicle" in alien.keys():
    print(alien["vehicle"])
else:
    # Adding a key
    alien["vehicle"] = "ufo"
    print(f'{alien["vehicle"]} added')

#Changing a value
alien["color"] = "red"
print(alien["color"])

#loop over values
for value in alien.values():
    print(value)

# Loop over keys and values
for key, value in alien.items():
    print(f"{key} : {value}")

#accessing Values in a dictionary of dictionaries
my_dict = {
    "string" : "hello",
    "integer" : 4,
    "float" : 6.9,
    "dict" : {"a": 1, "b": 2},
    "list" : [1,2,3]
}
print(my_dict["dict"]["a"])