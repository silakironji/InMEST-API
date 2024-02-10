from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View

# def users(request):
#     return HttpResponse('This is ')

def say_hello(request):
    return HttpResponse("<h1>Hello Fleur<h1>")

def user_profile(request):
    
    user_data = {
        "your name": "Sila", 
        "email": "sila.muremwa@meltwater.org", 
        "phone_number":"+254745051091"}

    return JsonResponse(user_data)

# Define the query data before the view function
query_data = [
    {
        'id': 1,
        'title': "Sila",
        'description': "Senior",
        'status': "infite loop",
        'submitted_by': "SKM"
    },
    {
        'id': 2,
        'title': "Oyinlade",
        'description': "Senior",
        'status': "Infinite loop",
        'submitted_by': "Oyinlade"
    },
        {
        'id': 3,
        'title': "Misheck",
        'description': "Senior",
        'status': "Infinite loop",
        'submitted_by': "ML"
    },
]

def filter_queries(request, query_id):
    for query in query_data:
        if query['id'] == query_id:
            return JsonResponse(query)
    
    # Return a 404 error if no query with the given ID is found
    return JsonResponse({'error': 'Query not found'}, status=404)

class QueryViews(View):
    queries  =[
        {"id":1, "title":"Slide to fly"},
        {"id":2, "title":"Tap to land"}  
    ]
    def get(self,request):
        return JsonResponse({"result":self.queries})
    def post(self,request):
        return JsonResponse({"status":"ok"})

