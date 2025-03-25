from django.shortcuts import render
from .models import tweet
from .forms import tweetform,UserRegistration,search_view
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout


# Create your views here.
def index(request):
    return render(request,'index.html')

def list_tweets(request):
    Tweets = tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'Tweets':Tweets})

@login_required
def create_tweet(request):
    if request.method == "POST":
      form = tweetform(request.POST,request.FILES)
      if form.is_valid():
          tweet = form.save(commit=False)
          tweet.user = request.user
          tweet.save()
          return redirect('list_tweets')
    else:
        form = tweetform()

    return render(request,'tweet_form.html',{'form':form})
  
@login_required
def edit_tweet(request,tweet_id):
    Tweet = get_object_or_404(tweet,pk=tweet_id,user = request.user)
    if request.method == "POST":
     form = tweetform(request.POST,request.FILES,instance=Tweet)
     if form.is_valid():
        Tweet = form.save(commit =False)
        Tweet.user = request.user
        Tweet.save()
        return redirect('list_tweets')
    else:
       form = tweetform(instance=Tweet)
    
    return render(request,'tweet_form.html',{'form':form})


@login_required
def delete_tweet(request,tweet_id):
   Tweet = get_object_or_404(tweet,pk=tweet_id,user = request.user)
   if request.method == "POST":
      Tweet.delete()
      return redirect('list_tweets')
   return render(request,"delete_tweet.html",{"tweet":Tweet})

def register(request):
   if request.method == "POST":
      form = UserRegistration(request.POST)
      if form.is_valid():
         user = form.save(commit=False)
         user.set_password(form.cleaned_data['password1'])
         user.save()
         login(request,user)
         return redirect('list_tweets')
   else:
     form = UserRegistration()
   return render(request,"Registration/register.html",{'form':form})

def logout_user(request):
   logout(request)
   return render(request,"Registration/logout.html")


def search_user(request):
   results=[]
   if request.method == 'POST':
      form = search_view(request.POST)
      if form.is_valid():
         qu = form.cleaned_data['search_user']
         results = tweet.objects.filter(user__username__icontains = qu)
      
   return render(request,'Registration/search.html',{'results':results,'form':form})
   

   



