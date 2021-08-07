from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.mail import send_mail
from blog.forms import EmailSendForm
from blog.forms import CommentsForm
from taggit.models import Tag
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def post_list_view(request,tag_slug=None):
    post_list=Post.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'post_list.html',{'post_list':post_list,'tag':tag})
@login_required
def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,status='published',publish__year=year,
        publish__month=month,
        publish__day=day)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentsForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else:
        form=CommentsForm()

    return render(request,'post_detail.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})
@login_required
def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='{}({}) recomends you to read"{}"'.format(cd['name'],cd['email'],post.title)
            post_url=request.build_absolute_uri(post.get_absolute_url())
            message='Read Post at:\n{}\n\n{}\'s Comments:\n{}'.format(post_url,cd['name'],cd['comments'])

            send_mail(subject,message,'lohith@blog.com',[cd['to']])
            sent=True
    else:
        form=EmailSendForm()

    return render(request,'sharebymail.html',{'form':form,'post':post,'sent':sent})

def hibernatecheatsheet(request):
    context={
    'welcome':'contact'
    }
    return render(request,'hibernatecheat.html',context)

def djangocheatsheet(request):
    context={
    'welcome':'contact'
    }
    return render(request,'djangocheat.html',context)

def pythoncheatsheet(request):
    context={
    'welcome':'contact'
    }
    return render(request,'pythoncheat.html',context)

def javacheatsheet(request):
    context={
    'welcome':'contact'
    }
    return render(request,'javacheat.html',context)

def springcheatsheet(request):
    context={
    'welcome':'contact'
    }
    return render(request,'springcheat.html',context)
