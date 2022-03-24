from django.shortcuts import render
from django.db import connection

from django.http import HttpResponse

def xyz(request):
    return render(request,"index.html")

# Create your views here.
def signup(request):
    #get sign up deatails from user
    email = request.POST['email']
    fname = request.POST['fname']
    lname = request.POST['lname']
    phone = request.POST['phone']
    psw = request.POST['psw']

    #connect with data base server
    cursor = connection.cursor()
    query = "select * from signuppage where email= '"+email+"'"
    cursor.execute(query)
    cursor.fetchall()
    count = cursor.rowcount
    if count > 0:
        data = {'email': "Email Already Exit ! Please Login"}
        return render(request, "second.html", data)

    else:
        #insert data into the database
        query = "insert into signuppage(fname,lname,email,phone,password,date) values (%s, %s,%s,%s,%s,now())"

        value = (fname, lname, email, phone, psw)

        cursor.execute(query, value)

        data = {"fname": fname, 'lname': lname, "email": "You are Successfull login", 'phone': phone, "password": psw}
        return render(request, "first.html", data)



def login(request):
    # login details fetch
    email1 = request.POST['email1']
    psw1 = request.POST['psw1']

    cursor = connection.cursor()

    query = "select password from signuppage where email= '"+email1+"'"
    cursor.execute(query)
    row = cursor.fetchall()
    if len(row)==0:
        data = {"email": 'Email Not Valid', "password": psw1}
        return render(request, "second.html", data)

    password = row[0][0]
    if psw1 == password :  #user succesfull login if psw is correct
        data = {"email": "You Are Successfull Login", "password": psw1}
        return render(request, "first.html", data)

    else:
        data = {"email": "Please Forgot Password", "password": psw1}
        return render(request, "second.html", data)



#get otp




