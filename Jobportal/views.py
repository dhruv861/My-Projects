from django.shortcuts import render,redirect
from django.urls import reverse
from Jobportal.models import JobPost,Location
from Jobportal.forms import SubscribeForm,AddJobPost,LocationForm,AuthorForm

# Create your views here.
def home(request):
    job_title=JobPost.objects.all()
    context={'joblist':job_title}
    return render(request,'jobportal/home.html',context)

def job_detail(request, slug_url,id):
    detail=JobPost.objects.get(id=id)
    context={'Job':detail}
    return render(request,'jobportal/Details.html',context)

def subscribe(request):
    subscribe_form = SubscribeForm()
    
    email_error_empty=""
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            return redirect(reverse('home'))

    context={"form": subscribe_form,"email_error_empty":email_error_empty}
    return render(request, 'jobportal/subscribe.html', context)

def addjobpost(request):
    job_form = AddJobPost()
    location_form= LocationForm()
    if request.POST:
        print(request.POST)

        job_form = AddJobPost(request.POST)
        location_form = LocationForm(request.POST)
        if job_form.is_valid() and location_form.is_valid():
            job_form.save()
            #location_form.save()

        job=JobPost.objects.all()
        job=job[len(job)-1]
        city=Location.objects.all().filter(city__iexact=request.POST['city'])
        if city:
            job.location=city[0]
        else:
            location_form.save()
            city=Location.objects.all().filter(city__iexact=request.POST['city'])
            job.location=city[0]
        
        job.save()
        #loc.save()

        return redirect(reverse('home'))

    context={"form": job_form , "location":location_form}
    return render(request, 'jobportal/add_jobpost.html', context)

def author(request):
    authorform=AuthorForm()
    if request.POST:
        authorform=AuthorForm(request.POST)
        if authorform.is_valid():
            authorform.save()
            return redirect(reverse('home'))
    context={"form":authorform}
    return render(request, 'jobportal/author.html', context)

def thankyou(request):
    return render(request,'jobportal/thankyou.html')
