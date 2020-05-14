from django.shortcuts import render,redirect , HttpResponse
from django.http import FileResponse
from .models import course , content
from .forms import content_form
from django.conf import settings
# Create your views here.
def courselist(request):
    print(request.path)
    sem = request.path[-2]
    print(sem)
    k = request.path.split('/')
    k = k[2]
    courses = course.objects
    courses = courses.filter(Branch = k , semester = sem)
    return render(request , 's.html' , {'Courses': courses} )


def create_content(request):
    form = content_form()
    if( request.method == 'POST'):
        li  = request.GET.get('li')
        print(li)
        k = request.POST.copy()
        li = li[1:-1].split(',')
        k['semester'] = li[-1]
        k['course_name'] = li[0]
        k['course_code'] = li[1]
        form = content_form(k , request.FILES)
        print(request.FILES['content'])
        if( form.is_valid()):
            user = form.save(commit = False)
            user.content = request.FILES['content']
            ftype = user.content.url.split('.')[-1]
            if( ftype in ['pdf' , 'docx']):
                user.save()
                return render(request , 'successful.html' , {'messages' : ['successful'] , 'color' : 'green'} )
            return render( request , 'successful.html' , { 'messages' : ['Your attachment can only be a pdf or docx'] , 'color' : 'red' } )
    cont = {"form" : form ,}
    return render(request , 'addcontent.html' , cont )

def show_content(request):
    var = request.path
    li = request.GET.get('li')
    li= li [1:-1]
    li = li.split(',')
    sem = li[-1]

    coursename = li[0]
    coursecode = li[1]
    var = var.split('/')
    var = var[-1]
    path = settings.MEDIA_ROOT+"/"
    print(path)
    resource = content.objects
     
    if( var == "NT"):
        resource = resource.filter(Notes = "True" , semester = sem , course_name = coursename , course_code = coursecode )
        h = "Notes"
    elif( var == "QP"):
        h = "Question Paper"
        resource = resource.filter(QP = "True" , semester = sem , course_name = coursename , course_code = coursecode )
    elif ( var == "TB"):
        h = "Text-Book"
        resource = resource.filter(Textbook = "True" , semester = sem , course_name = coursename , course_code = coursecode )
    else :
        resource = None

    return render( request , 'showcontent.html' , {'resource':resource , 'path' :path , 'h' :h })


def generate_pdf(request):
    k = request.path
    print(k)
    pdf = open(k , 'rb')
    return FileResponse(pdf,  content_type = 'application/pdf')


