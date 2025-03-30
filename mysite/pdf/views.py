from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

# Create your views here.
def accept(request):
    

    if request.method == 'POST':
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        address = request.POST.get('address',"") 
        summary = request.POST.get('summary',"")
        degree = request.POST.get('degree',"")
        school = request.POST.get('school',"")
        university = request.POST.get('university',"")
        previous_work = request.POST.get('previous_work',"")
        skills = request.POST.get('skills',"")

        profile = Profile(
            name=name,
            email=email,
            phone=phone,
            address=address,
            summmary=summary,
            school=school,
            university=university,
            previous_work=previous_work,
            skills=skills
        )
        profile.save()


    return render(request, 'pdf/accept.html')

def resume(request, id):
    user_profile = Profile.objects.get(pk=id)

    template  = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile': user_profile})
    options={
        'page-size': 'letter', 
        'encoding': "UTF-8"
        }

    pdf = pdfkit.from_string(html, False, options=options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment' 
    filename ='pdf/resume.pdf'    

    
    return response
    