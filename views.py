from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.db.models.query import Q
from firstapp.models import Ngolist
from django.views.generic import TemplateView, ListView
# from operator import attrgetter
# Create your views here.


def functionIndex(request):
    return render(request,'Index.html')

def functionContact(request):
    return render(request,'Contact.html')

def functionLocation(request):
    list = Ngolist.objects.all()
    return render(request,'Location.html',{'list': list})

def search(request):
    query = request.GET['query']
    sortedlist = Ngolist.objects.filter(Q(city__icontains=query) | Q(name__icontains=query) | Q(address__icontains=query))
    params ={'sortedlist': sortedlist , 'list':list}
    return render(request,'Search.html',params)

# class SearchResultsView(ListView):
#     model = Ngolist
#     template_name = 'Location.html'

#     def get_queryset(self): # new
#         query = self.request.GET.get('q')
#         object_list = Ngolist.objects.filter(
#             Q(city__icontains=query) | Q(name__icontains=query)
#         )
#         return object_list


# def get_list_query(query=None):
#          queryset = []
#          queries = query.split("") 
#          for q in queries:
#              posts = Ngolist.objects.filter(
#              Q(title_icontains=q),
#              Q(body_icontains=q)
#          ).distinct()

#          for post in posts:
#              queryset.append(post)
            
#          return list(set(queryset))    

     
    
def functionLogin(request):
    return render(request,'Login.html')

def functionSorting(request):
    return render(request,'Sorting.html')

def functionSchedule(request):
    return render(request,'Schedule.html')

# def get_list_query(query=None):
#     queryset = []
#     queries = query.split("") 
#     for q in queries:
#         posts = Ngolist.objects.filter(
#             Q(title_icontains=q),
#             Q(body_icontains=q)
#         ).distinct()

#         for post in posts:
#             queryset.append(post)
            
#     return list(set(queryset))
    

# def search(request):
#         context = {}
#         query = ""
#         if request.GET:
#         query = request.GET['q']
#         context['query'] = str(query)

#         ngo_lists = sorted(get_list_query(query), key=attrgetter('city'),reverse =True)
#         context['ngo_lists'] = ngo_lists

#         return render(request,'Location.html',context)

