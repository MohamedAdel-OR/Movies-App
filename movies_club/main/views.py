from django.shortcuts import render

# Create your views here.
def main(request):
    context=None
    return render(request,'home.html',context)
