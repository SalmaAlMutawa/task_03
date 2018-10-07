from django.shortcuts import render

def welcome(request):
	return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

	rest_names = [
	{
	   "restaurant_name" : "Kei",
	   "food_type" : "Japenese"
	},
	{
	   "restaurant_name" : "The Bowl",
	   "food_type" : "Healthy"
	},
	{
	   "restaurant_name" : "Burger Boutique",
	   "food_type" : "Burgers"
	},

	]

	context = {
	"my_list" : rest_names,

	}
	return render(request, 'list.html', context)


def restaurant_detail(request):
	rest_obj = {
	  "restaurant_name" : "Joa",
	   "food_type" : "Simply Salmon poke bowl"
	}

	context = {
	  "my_object" : rest_obj
	}
	return render(request, 'detail.html', context)
