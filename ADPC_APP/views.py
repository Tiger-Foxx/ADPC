from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from ADPC_APP.forms import CommentForm, DonForm,AdhesionForm,VolontariatForm,Volontariat
from ADPC_APP.models import Commentaire, Informations, Mot_president, Partenaire, Post, Souvenir, Tag
# Create your views here.


def index(request):
    infos=get_object_or_404(Informations,id=1)
    mot=get_object_or_404(Mot_president,id=1)
    posts=Post.objects.all().order_by('-date')
    documents=Post.objects.filter(Tag__contains="document")
    documentsParti=Post.objects.filter(Tag__contains="leparti")
    souvenirs=Souvenir.objects.all()
    partenaires=Partenaire.objects.all()
    
    return render(request,'ADPC_APP/index.html',context={"posts":posts,"documents":documents,"documentsParti":documentsParti,"souvenirs":souvenirs,"partenaires":partenaires,"mot":mot,"infos":infos})

def don(request):
    infos=get_object_or_404(Informations,id=1)
    form = DonForm()
    documents=Post.objects.filter(Tag__contains="document")
    documentsParti=Post.objects.filter(Tag__contains="leparti")
    if request.method == 'POST':
        form = DonForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'ADPC_APP/success.html')
        else :
            return render(request, 'ADPC_APP/fail.html')
    else:
        return render(request,'ADPC_APP/don.html',context={"form":form,"documents":documents,"documentsParti":documentsParti,"infos":infos})

def adhesion(request):
    infos=get_object_or_404(Informations,id=1)
    form = AdhesionForm()
    documents=Post.objects.filter(Tag__contains="document")
    documentsParti=Post.objects.filter(Tag__contains="leparti")
    if request.method == 'POST':
        form = AdhesionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'ADPC_APP/success.html')
        else :
            return render(request, 'ADPC_APP/fail.html')
    else:
       return  render(request,'ADPC_APP/adherer.html',context={"form":form,"documents":documents,"documentsParti":documentsParti,"infos":infos})
        
        

def volontariat(request):
    infos=get_object_or_404(Informations,id=1)
    documents=Post.objects.filter(Tag__contains="document")
    documentsParti=Post.objects.filter(Tag__contains="leparti")
    form = VolontariatForm()
    if request.method == 'POST':
        form = VolontariatForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'ADPC_APP/success.html')
        else :
            return render(request, 'ADPC_APP/fail.html')
    else:
       return  render(request,'ADPC_APP/volontaire.html',context={"form":form,"documents":documents,"documentsParti":documentsParti,"infos":infos})

def comment(request):
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'ADPC_APP/success.html')
        else :
            return render(request, 'ADPC_APP/fail.html')

def blog(request):
    infos=get_object_or_404(Informations,id=1)
    documents=Post.objects.filter(Tag__contains="document")
    documentsParti=Post.objects.filter(Tag__contains="leparti")
    tags=Tag.objects.all()
    posts=Post.objects.all().order_by('-date')
    recentPosts=posts[:3]
    return render(request,'ADPC_APP/blog.html',context={"posts":posts,"recentposts":recentPosts,"tags":tags,"documents":documents,"documentsParti":documentsParti,"infos":infos})


def blogTag(request,tag):
    infos=get_object_or_404(Informations,id=1)
    documents=Post.objects.filter(Tag__contains="document")
    documentsParti=Post.objects.filter(Tag__contains="leparti")
    tags=Tag.objects.all()
    post=Post.objects.filter(Tag__contains=tag).order_by('-date')
    recentPost=Post.objects.order_by('-date')[:3]
    return render(request,'ADPC_APP/blog.html',context={"posts":post,"recentposts":recentPost,"tag":tag,"tags":tags,"documents":documents,"documentsParti":documentsParti,"infos":infos})


def post_detail(request,id):
    infos=get_object_or_404(Informations,id=1)
    documents=Post.objects.filter(Tag__contains="document")
    documentsParti=Post.objects.filter(Tag__contains="leparti")
    post=get_object_or_404(Post,id=id)
    tags=post.Tag.split("#")[1:]
    recentPost=Post.objects.order_by('-date')[:3]
    commentaires=Commentaire.objects.filter(post=post).order_by('-date')
    return render(request,'ADPC_APP/blog-post.html',context={"post":post,"recentposts":recentPost,"tags":tags,"commentaires":commentaires,"documents":documents,"documentsParti":documentsParti,"infos":infos})

def post_Tag(request,tag):
    infos=get_object_or_404(Informations,id=1)
    documents=Post.objects.filter(Tag__contains="document")
    documentsParti=Post.objects.filter(Tag__contains="leparti")
    post=get_object_or_404(Post,Tag=tag)
    tags=post.Tag.split("#")[1:]
    recentPost=Post.objects.order_by('-date')[:3]
    return render(request,'ADPC_APP/blog-post.html',context={"post":post,"recentposts":recentPost,"tags":tags,"documents":documents,"documentsParti":documentsParti,"infos":infos})





