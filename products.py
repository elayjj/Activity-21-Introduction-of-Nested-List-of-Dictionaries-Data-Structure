
products = [
{
"id": 1,
"name": "IPHONE 13",
"category": "Electronics",
"price" : 2500,
"colors" : ["gray", "black"],
"size": ["small", "medium", "large"],
"stock": [{
"gray-small" : 25,
"gray-medium" : 30,
"gray-large" : 34
},
{
"black-small": 23,
"black-medium": 23,
"black-large": 25
}],
},

{
"id": 2,
"name": "IPHONE 15",
"category":"Electronics",
"price" : 2500,
"colors" : ["gray", "black"],
"size": ["small", "medium", "large"],
"stock": [{
"gray-small" : 25,
"gray-medium" : 30,
"gray-large" : 34
},
{
"black-small": 23,
"black-medium": 23,
"black-large": 25
}],
},

{
"id": 3,
"name": "IPHONE 16",
"category":"Electronics",
"price" : 2500,
"colors" : ["gray", "black"],
"size": ["small", "medium", "large"],
"stock": [{
"gray-small" : 25,
"gray-medium" : 30,
"gray-large" : 34
},
{
"black-small": 23,
"black-medium": 23,
"black-large": 25
}],
}
]
print(products)
products[2]["name"] = "IPHONE 16 PROMAX"


#TODO ACCESS STOCK OF products[2]

print("The stock of the products 2 is",products[2]["stock"])

#TODO ACCESS INDEX 3 STOCK OF products[2]

print("The index 3 of stock of the products 2 is",products[2]["stock"][1])

#TODO CHANGE black small quantity - products[2]

products[2]["stock"][1]["black small"] = 15

print("The new quantity of a stock is",products[2])
