from django.shortcuts import render
from django.db.models import Count
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.loader import get_template
from django.template import Context
import datetime, xlrd
from django.template import loader
from .models import Visitor, Person, Staff, Event, Comment, Data
#from datetime import date, datetime, timedelta
from datetime import datetime,timedelta
import MySQLdb
from django.template import loader
#import xlsxwriter
from django.shortcuts import render_to_response
from xlrd import open_workbook
from django.views.generic.base import TemplateView
import json as simplejson
from django.shortcuts import render
from .forms import uploadExcel
#from chartit import DataPool, Chart

def sample_view(request):
	a = "shubham"
	return str(a)
def male(request):
	return render_to_response('male.html',
				 {'male' : Person.objects.filter(sex='m')})

def dashboard(request) :
	return render_to_response('dashboard.html',
				  {'person' : Person.objects.all().order_by('person_id')[:15:1]})
def count(request) :
	a = Visitor.objects.values('to_whom').annotate(c=Count('to_whom')).order_by('-c')
	male = Person.objects.filter(sex="m").count()
	print "no of males"
	print male
	female = Person.objects.filter(sex="f").count()
	print female
	tym = Visitor.objects.filter(date = "42420.0").count()

	print "time = "
	print tym
	#a = simplejson.dumps(a);
	#return HttpResponse("works")
	#print a[0].c
	a  = str(male) +"," + str(female)
		
	return render_to_response('count.html', {"count" : a})

def countdate(request) :
	
	tym1 = Visitor.objects.filter(date = "42420.0").count()
	tym2 = Visitor.objects.filter(date = "42423.0").count()	
	tym3 = Visitor.objects.filter(date = "42424.0").count()	
	tym4 = Visitor.objects.filter(date = "42425.0").count()
	tym5 = Visitor.objects.filter(date = "42426.0").count()
	tym6 = Visitor.objects.filter(date = "42421.0").count()
	tym7 = Visitor.objects.filter(date = "42422.0").count()
	a  = str(tym1) +"," + str(tym2)+"," + str(tym3)+"," + str(tym4)+"," + str(tym5)+"," + str(tym6)+"," + str(tym7)
		
	return render_to_response('countdate.html', {"countdate" : a})

				

def table(request):
	return render_to_response('table.html')

def table1(request):
	date1 = request.GET['terid']
	date2 = request.GET['date2']
	staffId = request.GET['staffId']

	print staffId
	if date2 == "":
		print "date2 is blank"
	else:
		print "blank"
	date1 = date1.encode("utf-8")
	date2 = date2.encode("utf-8")
	date1 = datetime.strptime(date1, '%m/%d/%Y')
	date2 = datetime.strptime(date2, '%m/%d/%Y')
	if staffId == "null":
		print "staff id is blank"
		ids = Visitor.objects.filter(date__range = [date1,date2])
	else:
		print "staff visitor"
		ids = Visitor.objects.filter(date__range = [date1,date2], to_whom = staffId)
		print ids
	persons = Person.objects.filter(person_id__in = ids.values('person_id'))
	
	# visitor1 = Visitor.objects.filter(person = persons).select_related()
	print persons
	# return render_to_response('actual_table.html',
	# 			  {'tables' : Visitor.objects.filter(date__range = [date1,date2])}
	# )
	return render_to_response('actual_table.html',
				  {'tables' : persons })
	 
#def gender(request):
 #   a = person.objects.get(sex='m')
 #   return HttpResponse(a.name)
    
def insert(request):
	# if request.method == 'GET':
	# 	form = UploadFileForm(request.GET, request.FILES)
	#  	if form.is_valid():
	#  		handle_uploaded_file(request.FILES['file'])
	#  		return HttpResponseRedirect('http://www.google.com')
	#  	else:
	#  		form = UploadFileForm()
	# return render_to_response('sidebar.html', {'form' : form} ) 

    wb = open_workbook("/home/shubham/proj/sample.xls")
    for s in wb.sheets():
        for row in range(1, s.nrows):
			col_value = []
			for col in range(s.ncols):
				value = (s.cell(row, col).value)
				col_value.append(value)
			a = Person(person_id = str(col_value[0]), id_type = col_value[1], name = col_value[2], sex = col_value[3])
			a.save()
		   # b = Staff(person_id = str(col_value[0]), department = col_value[4], location = col_value[5], staff_type = col_value[6])
			#b.save()
			# print "staff_type"
			# staff_type = Staff.objects.filter(staff_type = col_value[10]).values('person_id')
			# print staff_type

			col_value[4] = datetime(*xlrd.xldate_as_tuple(col_value[4],0))

			#print(col_value[7])
			#col_value[7] = TEXT(col_value,"yyyy-mm-dd")
			# c = Comment(person_id = str(col_value[0]), date = col_value[1], comment = col_value[2])
			# c.save()
			c = Visitor(person_id = str(col_value[0]),date = col_value[4],  to_whom = col_value[7], purpose = col_value[8])
			c.save()
    #q = Person.objects.get(sex='m')
   # return HttpResponse(q.name)
    return HttpResponse("Values r inserted in db")
    
def profile(request):
	person_id = request.GET['profileId']
	print person_id
	
	profile = Person.objects.filter(person_id = person_id)
	# ids = Visitor.objects.filter(date__range = [date1,date2])
	# persons = Person.objects.filter(person_id__in = ids.values('person_id'))
	visitor = Visitor.objects.filter(person_id = person_id)
	comment = Comment.objects.filter(person_id = person_id)
	print comment
	return render_to_response('profile.html',
				{'profile' : profile ,'visitor' : visitor, 'comments': comment}
	)

def staff(request):
	# ids = Visitor.objects.filter(date__range = [date1,date2])
	# persons = Person.objects.filter(person_id__in = ids.values('person_id'))
	staff_member = Staff.objects.all()
	staff = Person.objects.filter(person_id__in = staff_member.values('person_id'))
	# staff_member = zip(staff, staff_member)
	# print staff_member.value

	# i = 0;
	# for i in len(staff):
	# 	staff_member[i].append(staff[i].name)
	# print staff_member
	return render_to_response('staff.html',
				  {'staff_member' : staff_member,'staff': staff}
	)

def event(request):
	# ids = Visitor.objects.filter(date__range = [date1,date2])
	# persons = Person.objects.filter(person_id__in = ids.values('person_id'))
	events= Event.objects.all()
	# staff_member = zip(staff, staff_member)
	# print staff_member.value

	# i = 0;
	# for i in len(staff):
	# 	staff_member[i].append(staff[i].name)
	# print staff_member
	return render_to_response('events.html',
							  {'events': events}
							  )
def eventProfile(request):
	event_id = request.GET['eventId']
	print event_id

	events= Event.objects.filter(event_id = event_id)
	# ids = Visitor.objects.filter(date__range = [date1,date2])
	# persons = Person.objects.filter(person_id__in = ids.values('person_id'))
	visitor = Visitor.objects.filter(to_whom = event_id)
	comment = Comment.objects.filter(person_id = event_id)
	print comment
	return render_to_response('eventProfile.html',
				{'events' : events,'visitor' : visitor, 'comments': comment}
	)

def staffProfile(request, person_id):
	# person_id = request.GET['profileId']
	print "person_id"
	staff = Staff.objects.filter(person_id = person_id)
	print staff
	profile = Person.objects.filter(person_id = person_id)
	# profile = Person.objects.filter()
	#	 ids = Visitor.objects.filter(date__range = [date1,date2])
	# persons = Person.objects.filter(person_id__in = ids.values('person_id'))
	# visitor = Visitor.objects.filter(person_id = person_id)
	# print visitor
	return render_to_response('staffProfile.html',
				  {'profile' : profile, 'staff' : staff }
	)




def comment(request):
	person_id = request.GET['person_id']
	comment = request.GET['comment']
	a = Comment(person_id = person_id, comment = comment, date = datetime.now())
    	a.save()
	return HttpResponse("success")


def uploadFile(request):

    form = uploadExcel(request.POST or None, request.FILES or None)
    print form
    if form.is_valid():
    	
    	print "here never"
        album = form.save(commit=False)
        # album.user = request.user
        album.file_name = request.FILES['file_name']
        filename = "file/" + str(album.file_name)
        # file_type = album.album_logo.url.split('.')[-1]
        # file_type = file_type.lower()
        # if file_type not in IMAGE_FILE_TYPES:
        context = {
            'album': album,
            'form': form,
            'error_message': 'Image file must be PNG, JPG, or JPEG',
        }
        # return render(request, 'music/create_album.html', context)
        album.uploader = "shubham"
        print "works"
        
        album.save()

        # filename = "/file" +  str(album.file_name)
        # print filename
        wb = open_workbook(filename)
        for s in wb.sheets():
			for row in range(1, s.nrows):
				col_value = []
				for col in range(s.ncols):
					value = (s.cell(row, col).value)
					col_value.append(value)
				a = Person(person_id = str(col_value[0]), id_type = col_value[1], name = col_value[2], sex = col_value[3])
				a.save()
			   # b = Staff(person_id = str(col_value[0]), department = col_value[4], location = col_value[5], staff_type = col_value[6])
				#b.save()
				# print "staff_type"
				# staff_type = Staff.objects.filter(staff_type = col_value[10]).values('person_id')
				# print staff_type

				col_value[4] = datetime(*xlrd.xldate_as_tuple(col_value[4],0))

				#print(col_value[7])
				#col_value[7] = TEXT(col_value,"yyyy-mm-dd")
				# c = Comment(person_id = str(col_value[0]), date = col_value[1], comment = col_value[2])
				# c.save()
				c = Visitor(person_id = str(col_value[0]),date = col_value[4],  to_whom = col_value[7], purpose = col_value[8])
				c.save()
	    #q = Person.objects.get(sex='m')
	   # return HttpResponse(q.name)
        return HttpResponse("Values r inserted in db")
    context = {
        "form": form,
    }
    return render(request, 'uploadFile.html', context)
