from django.db import models

class log(models.Model):
    uname= models.CharField(max_length=30,unique=True)
    password= models.CharField(max_length=30,unique=True)
    role=models.CharField(max_length=30,null=True)
  

    def __str__(self):
        return self.uname
    

#    donar    
class user(models.Model):
    
    uname= models.CharField(max_length=30,null=True)

    email= models.CharField(max_length=30,null=True)
   
    password= models.CharField(max_length=30,null=True)
    cpassword= models.CharField(max_length=30,null=True)
    login=models.ForeignKey(log, on_delete=models.CASCADE)
    def __str__(self):
        return self.email
    

    #  receiver
class user2(models.Model):
    
    uname= models.CharField(max_length=30,null=True)

    email= models.CharField(max_length=30,null=True)
   
    password= models.CharField(max_length=30,null=True)
    cpassword= models.CharField(max_length=30,null=True)
    login=models.ForeignKey(log, on_delete=models.CASCADE)
    def __str__(self):
        return self.email
    


class food(models.Model):
    foodname=models.CharField(max_length=30,null=True)
    foodtype=models.CharField(max_length=30,null=True)
    quantity=models.CharField(max_length=30,null=True)
    cookingtime=models.CharField(max_length=30,null=True)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    address=models.CharField(max_length=30,null=True)
    phone=models.CharField(max_length=30,null=True)
    
    donarid=models.ForeignKey(user, on_delete=models.CASCADE)
    foodstatus=models.CharField(max_length=120,null=True)

    def __str__(self):
        return self.foodname
    

class accepting(models.Model):
    receiverid =models.ForeignKey(user2,on_delete=models.CASCADE)
    foodid=models.ForeignKey(food,on_delete=models.CASCADE)
    donarid=models.ForeignKey(user,on_delete=models.CASCADE) 
    receivername=models.CharField(max_length=30,null=True)
    donarname=models.CharField(max_length=30,null=True)
    foodname=models.CharField(max_length=30,null=True)
    foodtype=models.CharField(max_length=30,null=True)
    cookingtime=models.CharField(max_length=30,null=True)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    address=models.CharField(max_length=30,null=True)
    phone=models.CharField(max_length=30,null=True)
    
   
    acceptingdate=models.CharField(max_length=30,null=True)
    acceptingstatus=models.CharField(max_length=120,null=True)


    def __str__(self):
        return self.foodname