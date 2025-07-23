from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)                                                 # Create Flask Object
import serial

Url_Address = "192.168.90.48"                                        # Change your IP Address here
s = serial.Serial('COM2',9600)                                        # Define Serial  Communication Baud rate

flag = False

@app.route('/loginservelate',methods = ['POST', 'GET'])
def loginservelate():
   global flag
   try:  
      u_name = request.form['username']                               # collect ID from webpage 
      u_password = request.form['userpassword']                       # collect Password from webpage 
      if((str(u_name) == "ras") and (str(u_password) == "pi")):   # compare ID and Password
         flag=1                                                       # if ID and Password is correct then only open bulb control web page
      else:
         flag=0                                                       # if ID and Password is not correct then open not succesfull webpage
      if(flag==1):                                                    # if ID and Password is correct then only open bulb control web page
         return render_template("Bulb_Control.html",HTML_address=Url_Address) #Opne bulb control webpage
      else:
         return render_template("unsuccessfull.html",name=u_name)     # Open uncessfull webpage
   except:
      print ("Error: unable to fecth data")                           # If servet not open then send error 

@app.route('/LEVEL1',methods = ['POST', 'GET'])                      # If light ON button press then open this servelet 
def LEVEL1():                                                        
   global flag 
   try:
       
      if(flag==1):                                                     # check valid user
         s.write(b'a')                                                 # Send 'a' value to proteus software when bulb on detected 
         return render_template("Bulb_Control.html",HTML_address=Url_Address)  #Refresh the control panel webpage after button press
      else:
         return render_template("login.html",HTML_address=Url_Address)  # If user name and password is not correct then after button press then jump to login page 
   except:
      print ("Error: unable to fecth data")

@app.route('/LEVEL2',methods = ['POST', 'GET'])                   # If light OFF button press then open this servelet 
def LEVEL2():
   global flag 
   try:
      if(flag==1):                                                   # check valid user
         s.write(b'b')                                               # Send 'b' value to proteus software when bulb off detected 
         return render_template("Bulb_Control.html",HTML_address=Url_Address) #Refresh the control panel webpage after button press
      else:
         return render_template("login.html",HTML_address=Url_Address)  # If user name and password is not correct then after button press then jump to login page 
   except:
      print ("Error: unable to fecth data")


@app.route('/LEVEL3',methods = ['POST', 'GET'])                   # If light OFF button press then open this servelet 
def LEVEL3():
   global flag 
   try:
      if(flag==1):                                                   # check valid user
         s.write(b'c')                                               # Send 'b' value to proteus software when bulb off detected 
         return render_template("Bulb_Control.html",HTML_address=Url_Address) #Refresh the control panel webpage after button press
      else:
         return render_template("login.html",HTML_address=Url_Address)  # If user name and password is not correct then after button press then jump to login page 
   except:
      print ("Error: unable to fecth data")

@app.route('/LEVEL4',methods = ['POST', 'GET'])                   # If light OFF button press then open this servelet 
def LEVEL4():
   global flag 
   try:
      if(flag==1):                                                   # check valid user
         s.write(b'd')                                               # Send 'b' value to proteus software when bulb off detected 
         return render_template("Bulb_Control.html",HTML_address=Url_Address) #Refresh the control panel webpage after button press
      else:
         return render_template("login.html",HTML_address=Url_Address)  # If user name and password is not correct then after button press then jump to login page 
   except:
      print ("Error: unable to fecth data")

@app.route('/login')                                                   # Entry point for web servelet
def login():
   return render_template("login.html",HTML_address=Url_Address)  # Jump to login page

      
if __name__ == '__main__':
   app.run(Url_Address,8080,debug = False)



