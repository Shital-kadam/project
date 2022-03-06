from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
def login(request):
    return render(request, "index.html")

# Create your views here.
def signup(request):
    email = request.GET['email']
    fname = request.GET['fname']
    lname = request.GET['lname']
    phone = request.GET['phone']
    psw = request.GET['psw']

    cursor = connection.cursor()
    query = "select * from signuppage where email= '"+email+"'"
    cursor.execute(query)
    cursor.fetchall()
    count = cursor.rowcount

    if count > 0:
        data = {'email': email}
        return render(request, "second.html", data)

    else:
        query = "insert into signuppage(fname,lname,email,phone,password,date) values (%s, %s,%s,%s,%s,now())"

        value = (fname, lname, email, phone, psw)

        cursor.execute(query, value)

        data = {"fname": fname, 'lname': lname, "email": email, 'phone': phone, "password": psw}
        return render(request, "first.html", data)






