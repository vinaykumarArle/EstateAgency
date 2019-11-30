from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Property, Agent, Contact
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth,sessions
# Create your views here.


def index(request):
    props = Property.objects.all()
    agents = Agent.objects.all()
    return render(request, 'index.html', {"props": props, "agents": agents})

def about(request):
    return render(request, 'about.html')


def addProperty(request):
    return render(request, 'addProperty.html')


def newProperty(request):
    newProp = Property()

    newProp.prop_name = request.POST['prop_name']
    newProp.prop_price = request.POST['prop_price']
    newProp.prop_area = request.POST['prop_area']
    newProp.prop_beds = request.POST['prop_beds']
    newProp.prop_bath = request.POST['prop_bath']
    newProp.prop_garage = request.POST['prop_garage']
    newProp.prop_image = request.FILES['prop_image']

    newProp.save()
    messages.info(request,"Property Added")
    return redirect('/adminPanel')


def viewProperty(request):
    props = Property.objects.all()
    return render(request, 'viewProperty.html', {'props': props})


def agentSingle(request, agentId):
    agent = Agent.objects.get(id=agentId)
    return render(request, 'agentSingle.html', {'agent': agent})
    

def agentsingle(request):
    agents = Agent.objects.all()
    return render(request,'agent-single.html', {'agents': agents})


def adminPanel(request):
    return render(request, 'admin-panel.html')


def addAgent(request):
    return render(request, 'addAgent.html')


def addNewAgent(request):
    agent = Agent()

    agent.agent_name = request.POST['agent_name']
    agent.agent_tagline = request.POST['agent_tagline']
    agent.agent_desc = request.POST['agent_desc']
    agent.agent_phone = request.POST['agent_phone']
    agent.agent_mobile = request.POST['agent_mobile']
    agent.agent_email = request.POST['agent_email']
    agent.agent_skype = request.POST['agent_skype']
    agent.agent_image = request.FILES['agent_image']
    
    get_agent = Agent.objects.filter(agent_email = agent.agent_email).exists()
    if get_agent:
        request.session['level'] = "danger"
        messages.error(request,"Agent Already Exist")
    else:
        request.session['level'] = "success"
        res = agent.save()
        messages.info(request,"Agent Added")
    # return render(request,'admin-panel.html')
    return redirect('/adminPanel')


def agentList(request):
    agents = Agent.objects.all()
    return render(request, 'agent-list.html', {"agents": agents})


def editAgent(request, agentId):
    agent = Agent.objects.get(id=agentId)
    return render(request, 'editAgent.html', {'agent': agent})


def updateAgent(request, agentId):
    agent = Agent.objects.get(id=agentId)

    agent.agent_name = request.POST['agent_name']
    agent.agent_tagline = request.POST['agent_tagline']
    agent.agent_desc = request.POST['agent_desc']
    agent.agent_phone = request.POST['agent_phone']
    agent.agent_mobile = request.POST['agent_mobile']
    agent.agent_email = request.POST['agent_email']
    agent.agent_skype = request.POST['agent_skype']

    if len(request.FILES) != 0:
        agent.agent_image = request.FILES['agent_image']

    res = agent.save()
    return redirect('/adminPanel')


def deleteAgent(request, agentId):
    agent = Agent.objects.get(id=agentId).delete()
    # agent.delete()

    return redirect('/agentList')


def userRegister(request):
    return render(request,'user-register.html')


def addUser(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    username = request.POST['username']
    passd = request.POST['passd']

    if User.objects.filter(email=email).exists():
        messages.error(request,"User Already Exists")
    elif User.objects.filter(username=username).exists():
        messages.error(request,"User Already Exists")
    else:
        user = User.objects.create_user(
            first_name=fname, last_name=lname, email=email, username=username, password=passd)
        user.save()

    return redirect('/user-login')


def userLogin(request):
    return render(request,'user-login.html')


def login(request):
    username = request.POST['username']
    passd = request.POST['passd']
    user = auth.authenticate(username=username, password=passd)

    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        request.session['level'] = "danger"
        messages.error(request,'Invalid username/password')
        return redirect('/user-login')


def logout(request):
    auth.logout(request)
    return redirect('/')

def editProperty(request,propId):
    single = Property.objects.get(id=propId)
    return render(request,'editProperty.html',{'single':single})


def updateProperty(request, propId):
    prop = Property.objects.get(id=propId)

    prop.prop_name = request.POST['prop_name']
    prop.prop_price = request.POST['prop_price']
    prop.prop_area = request.POST['prop_area']
    prop.prop_beds = request.POST['prop_beds']
    prop.prop_bath = request.POST['prop_bath']
    prop.prop_garage = request.POST['prop_garage']
    

    if len(request.FILES) != 0:
        prop.prop_image = request.FILES['prop_image']

    result = prop.save()
    messages.info(request,"Property Updated")
    return redirect('/adminPanel')

def deleteProperty(request,propId):
    delete = Property.objects.get(id=propId).delete()
    messages.info(request,"Property Deleted")
    return redirect('/viewProperty')

def propertyGrid(request):
    props = Property.objects.all()
    return render(request,'property-grid.html',{'props':props})

def blogSingle(request):
    return render(request,'blog-single.html')

def agentsGrid(request):
    agents = Agent.objects.all()
    return render(request,'agents-grid.html',{'agents' : agents})

def propertySingle(request):
    return render(request,'property-single.html')
    
def contact(request):
     return render(request,'contact.html')

def contac(request):
    cont = Contact()

    cont.name = request.POST['name']
    cont.email = request.POST['email']
    cont.sub = request.POST['sub']
    cont.msg = request.POST['msg']

    cont.save()
    return redirect('/contact')

def query(request):
    cont = Contact.objects.all()
    return render(request, 'query.html', {'cont': cont})

def deleteQuery(request, contsId):
    delete = Contact.objects.get(id=contsId).delete()
    messages.info(request,"QueryDeleted")
    return redirect('/query')