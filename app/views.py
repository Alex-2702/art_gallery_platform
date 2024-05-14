from django.shortcuts import render
from .models import artist,customer,product,comment,purchased
# Create your views here.
def start(request):
	return render(request,"start.html")
	
def start1(request):
	return render(request,"start.html")
	
def regform(request):
	return render(request,"register.html")
	
def register(request):
	responseDic={}
	try:
		N=request.POST['name']
		P=request.POST['password']
		R=request.POST['id']
		if R=="op1":
			art=artist(name=N,password=P)
			art.save()
			responseDic['msg1']="Artist added"
			return render(request,"register.html",responseDic)
		elif R=="op2":
			cus=customer(name=N,password=P)
			cus.save()
			responseDic['msg1']="Customer added"
			return render(request,"register.html",responseDic)
		else:
			responseDic['msg1']="Invalid selection"
			return render(request,"register.html",responseDic)
	except Exception as e:
		print(e)
		responseDic['msg1']="Error..!! Try again..!!"
		return render(request,"register.html",responseDic)
		
def login(request):
	responseDic={}
	try:
		N=request.POST['name']
		request.session['user_name']=N
		P=request.POST['password']
		id=request.POST['id']
		if id=="op1":
			artist_present=artist.objects.all()
			for i in artist_present:
				if N in i.name and P in i.password:
					return render(request,"artisthome.html")
			responseDic['msg2']="No artist found"
			return render(request,"login.html",responseDic)
		elif id=="op2":
			customer_present=customer.objects.all()
			for i in customer_present:
				if N in i.name and P in i.password:
					return render(request,"customerhome.html")
			responseDic['msg2']="No Customer found"
			return render(request,"login.html",responseDic)
		else:
			return render(request,"login.html")
	except Exception as e:
		print(e)
		return render(request,"login.html")

def perform(request):
	try:
		if request.method=="POST":
			sub_val=request.POST.get("sub")
			if sub_val=="View Image":
				responseDic={}
				prod=product.objects.all()
				responseDic['pro']=prod
				return render(request,"customerview.html",responseDic)
			elif sub_val=="Buy Image":
				return render(request,"customerbuy.html")
			elif sub_val=="Your Purchases":
				responseDic={}
				usname=request.session.get('user_name')
				purc=purchased.objects.all()
				for i in purc:
					if usname==i.uname:
						pu=purchased.objects.filter(uname=usname)
						responseDic['pur']=pu
						return render(request,"customerpurchasedview.html",responseDic)
					responseDic['msg6']="No purchased images"
					return render(request,"customerpurchasedview.html",responseDic)
			elif sub_val=="Comment":
				return render(request,"customercomment.html")
		return render(request,"customerhome.html")
	except Exception as e:
		print(e)
		return render(request,"customerhome.html")
		
def perform1(request):
	try:
		if request.method=="POST":
			sub_val=request.POST.get("sub")
			if sub_val=="View Image":
				responseDic={}
				prod=product.objects.all()
				responseDic['pro']=prod
				return render(request,"artistview.html",responseDic)
			elif sub_val=="Add Image":
				return render(request,"artistadd.html")
			elif sub_val=="Purchased Image":
				responseDic={}
				purc=purchased.objects.all()
				responseDic['pur']=purc
				return render(request,"artistpurchasedview.html",responseDic)
			elif sub_val=="Read Comment":
				responseDic={}
				comm=comment.objects.all()
				responseDic['com']=comm
				return render(request,"artistcomment.html",responseDic)
		return render(request,"artisthome.html")
	except Exception as e:
		print(e)
		return render(request,"artisthome.html")
		
def addimg(request):
	responseDic={}
	try:
		if request.method=="POST":
			img=request.FILES.get('image')
			nm=request.POST.get('name')
			pri=request.POST.get('price')
			pro=product(image=img,name=nm,price=pri)
			pro.save()
			responseDic['msg3']="Image added successfully"
			return render(request,"artistadd.html",responseDic)
		return render(request,"artistadd.html",responseDic)
	except Exception as e:
		print(e)
		responseDic['msg3']="Image cannot be added"
		return render(request,"artistadd.html",responseDic)
		
def comment1(request):
	responseDic={}
	try:
		if request.method=="POST":
			unm=request.POST.get('uname')
			anm=request.POST.get('aname')
			cm=request.POST.get('comment')
			com=comment(urname=unm,arname=anm,comments=cm)
			com.save()
			responseDic['msg4']="Comment added successfully"
			return render(request,"customercomment.html",responseDic)
		return render(request,"customercomment.html",responseDic)
	except Exception as e:
		print(e)
		responseDic['msg4']="Comment cannot be added"
		return render(request,"customercomment.html",responseDic)
		
def continue1(request):
	try:
		if request.method=="POST":
			name=request.POST.get('name')
			item=product.objects.get(name=name)
			return render(request,"customerconfirm.html",{'item':item})
		return render(request,"customerbuy.html")
	except Exception as e:
		print(e)
		return render(request,"customerbuy.html")
		
def confirm(request):
	try:
		responseDic={}
		if request.method=="POST":
			img=request.POST.get('image_name')
			nm=request.POST.get('name')
			itmdel=product.objects.get(name=img)
			pur=purchased(uname=nm,iname=img,image=itmdel.image,price=itmdel.price)
			pur.save()
			itmdel.delete()
			responseDic['msg5']="Image purchase successful"
			return render(request,"customerconfirm.html",responseDic)
		return render(request,"customerconfirm.html") 
	except Exception as e:
		print(e)
		responseDic['msg5']="Image purchase unsuccessful"
		return render(request,"customerconfirm.html",responseDic)