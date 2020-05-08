from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from .models import Article
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def articles(request):

    article  = Article.objects.all()
    if(article.count()>0):
        new = article[0]

    return render(request,"articles.html",{"articles":article,"new":new})
def index(request):
    return redirect("article:articles")

def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)

        article.save()

        messages.success(request,"Ок")
        return redirect("article:articles")
    return render(request,"addarticle.html",{"form":form})
# def detail(request,id):
#     #article = Article.objects.filter(id = id).first()
#     article = get_object_or_404(Article,id = id)
#
#     comments = article.comments.all()
#     return render(request,"detail.html",{"article":article,"comments":comments})
# @login_required(login_url = "user:login")
# def updateArticle(request,id):
#
#     article = get_object_or_404(Article,id = id)
#     form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
#     if form.is_valid():
#         article = form.save(commit=False)
#
#         article.author = request.user
#         article.save()
#
#         messages.success(request,"Makale başarıyla güncellendi")
#         return redirect("article:dashboard")
#
#
#     return render(request,"update.html",{"form":form})
# @login_required(login_url = "user:login")
# def deleteArticle(request,id):
#     article = get_object_or_404(Article,id = id)
#
#     article.delete()
#
#     messages.success(request,"Makale Başarıyla Silindi")
#
#     return redirect("article:dashboard")
# def addComment(request,id):
#     article = get_object_or_404(Article,id = id)
#
#     if request.method == "POST":
#         comment_author = request.POST.get("comment_author")
#         comment_content = request.POST.get("comment_content")
#
#         newComment = Comment(comment_author  = comment_author, comment_content = comment_content)
#
#         newComment.article = article
#
#         newComment.save()
#     return redirect(reverse("article:detail",kwargs={"id":id}))
#