from django.shortcuts import render
from django.db import connection

from django.http import HttpResponse

def xyz(request):
    return render(request,"index.html")

# Create your views here.
def signup(request):
    #get sign up deatails from user
    email = request.GET['email']
    fname = request.GET['fname']
    lname = request.GET['lname']
    phone = request.GET['phone']
    psw = request.GET['psw']

    #connect with data base server
    cursor = connection.cursor()
    query = "select * from signuppage where email= '"+email+"'"
    cursor.execute(query)
    cursor.fetchall()
    count = cursor.rowcount
    if count > 0:
        data = {'email': email}
        return render(request, "second.html", data)

    else:
        #insert data into the database
        query = "insert into signuppage(fname,lname,email,phone,password,date) values (%s, %s,%s,%s,%s,now())"

        value = (fname, lname, email, phone, psw)

        cursor.execute(query, value)

        data = {"fname": fname, 'lname': lname, "email": email, 'phone': phone, "password": psw}
        return render(request, "first.html", data)



def login(request):
    # login details fetch
    email1 = request.GET.get('email1')
    psw1 = request.GET.get('psw1')

    cursor = connection.cursor()

    query = "select password from signuppage where email= '"+email1+"'"
    cursor.execute(query)
    row = cursor.fetchall()

    password = row[0][0]
    if psw1 == password:  #user succesfull login if psw is correct
        data = {"email": email1, "password": psw1}
        return render(request, "first.html", data)

    else:
        data = {"email": email1, "password": psw1}
        return render(request, "second.html", data)



#get otp




