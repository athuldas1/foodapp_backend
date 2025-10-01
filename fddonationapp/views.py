from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .models import log,user,user2,food,accepting
from fddonationapp.serializers import userserializer,userserializers,logserializer,foodserializer,acceptingserializer
from .PythonMail import sentmail
from datetime import date
# Create your views here.


    #    ....................donar.................
class userregister(GenericAPIView):
    serializer_class=userserializer
    serializer_class_login=logserializer
    # sSerializer
    def post(self,request):
        login_id=''
        uname=request.data.get("uname")
        email=request.data.get("email")
        password=request.data.get("password")
        cpassword=request.data.get("cpassword")
        role="user"

        userstatus="1"
        
        if(log.objects.filter(uname=uname)):
            return Response({'message':'Duplicate username found'},status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login=self.serializer_class_login(data={'uname':uname,'password':password,'role':role})    
        if serializer_login.is_valid():
            Log=serializer_login.save()
            login_id=Log.id
            print(login_id)    
        serializer=self.serializer_class(
            data={
               
                'uname':uname,
                
                'email':email,
                
                'password':password,
                'cpassword':cpassword,
                'login':login_id,


            }
        )
        print(serializer)
        if serializer.is_valid():
            print('hi')
            sentmail(email,"Doner")
            serializer.save()
            return Response({'data':serializer.data,'message':"Registration succesful","sucess":True},status=status.HTTP_201_CREATED)
        return Response({'data': serializer.errors, 'message': 'registarion failed', 'success': False}, status= status.HTTP_400_BAD_REQUEST)



        # ..............receiver...............
class userregister2(GenericAPIView):
    serializer_class=userserializers
    serializer_class_login=logserializer
    # sSerializer
    def post(self,request):
        login_id=''
        uname=request.data.get("uname")
        email=request.data.get("email")
        password=request.data.get("password")
        cpassword=request.data.get("cpassword")
        role='user2'

        userstatus="1"
        
        if(log.objects.filter(uname=uname)):
            return Response({'message':'Duplicate username found'},status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login=self.serializer_class_login(data={'uname':uname,'password':password,'role':role})    
        if serializer_login.is_valid():
            Log=serializer_login.save()
            login_id=Log.id
            print(login_id)    
        serializer=self.serializer_class(
            data={
               
                'uname':uname,
                
                'email':email,
                
                'password':password,
                'cpassword':cpassword,
                'login':login_id,


            }
        )
        print(serializer)
        if serializer.is_valid():
            print('hi')
            serializer.save()
            return Response({'data':serializer.data,'message':"Registration succesful","sucess":True},status=status.HTTP_201_CREATED)
        return Response({'data': serializer.errors, 'message': 'registarion failed', 'success': False}, status= status.HTTP_400_BAD_REQUEST)




class LoginAPIView1(GenericAPIView):
    serializer_class = logserializer
    def post (self,request):
        u_id= ''
        uname = request.data.get('uname')
        password = request.data.get('password')
        print(uname)
        print(password)
        logreg=log.objects.filter(uname=uname,password=password)
        
        if(logreg.count()>0):
            read_serializer = logserializer(logreg, many=True)
            for i in read_serializer.data:
                id=i['id']
                print(id)
                role = i['role']

                # ......donar....
                regdata = user.objects.all().filter(login= id).values()
                print(regdata)
 
                for i in regdata:
                    u_id = i['id']
                    uname = i['uname']
                
                    print(u_id)

                        #  ......receiver.... 
                regdatas = user2.objects.all().filter(login= id).values()
                print(regdatas)

                for i in regdatas:
                    u_id = i['id']
                    uname = i['uname']
                
                    print(u_id)




            return Response({
                'data':{
                    'login_id':id,
                    'uname':uname,
                    'password':password,
                    'userid':u_id,
                    'role':role
                }
            })

        else:
            return Response({
                'message':'username is invalid',
                'success':'false'
            },status=status.HTTP_400_BAD_REQUEST)
        



class UserView(GenericAPIView):
    serializer_class = userserializer
    def get(self,request):
        queryset = user.objects.all()
        if(queryset.count()>0):
            serializers = userserializer(queryset,many= True)

            return Response({'data': serializers.data, 'message': 'all Product data set', 'success': True}, status= status.HTTP_200_OK)
        else:
            return Response({'data':'non data available','success': False}, status= status.HTTP_201_CREATED)
        

class receiverView(GenericAPIView):
    serializer_class = userserializers
    def get(self,request):
        queryset = user2.objects.all()
        if(queryset.count()>0):
            serializers = userserializers(queryset,many= True)

            return Response({'data': serializers.data, 'message': 'all receiver data set', 'success': True}, status= status.HTTP_200_OK)
        else:
            return Response({'data':'non data available','success': False}, status= status.HTTP_201_CREATED)







class addfood(GenericAPIView):
    serializer_class=foodserializer


    def post(self,request):
        foodname=request.data.get("foodname")
        foodtype=request.data.get("foodtype")
        quantity=request.data.get("quantity")
        cookingtime=request.data.get("cookingtime")
        image=request.data.get("image")
        address=request.data.get("address")
        phone=request.data.get("phone")
        donarid=request.data.get("donarid")
        
        foodstatus="0"



        serializer=self.serializer_class(data={'foodname':foodname, 'foodtype':foodtype,'quantity':quantity,'cookingtime':cookingtime,'image':image,'address':address,'phone':phone,'donarid':donarid})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'food was added susccesfully','success':'1'},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'adding food was failed','success':'0'},status=status.HTTP_400_BAD_REQUEST)            









class allfoodview(GenericAPIView):
    serializer_class=foodserializer
    def get(self,request):
        queryset=food.objects.all()
        if(queryset.count()>0):
            serializer=foodserializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'all food data  set' ,'success':1},status=status.HTTP_200_OK)
        else:
            return Response({'data':'no datas avaialable ','success':0},status=status.HTTP_201_CREATED) 
        



class singlefoodview(GenericAPIView):
    def get(self,request,id):
        queryset=food.objects.get(pk=id)
        serializer=foodserializer(queryset)
        return Response({'data':serializer.data,'messgae':'single food view','success':True},status=status.HTTP_200_OK)  




class deletesinglefoodview(GenericAPIView):

    def delete(self,request,id):
        deletefood=food.objects.get(pk=id)
        deletefood.delete()
        return Response({'message':'Deleted suscesfully','sucess':True},status=status.HTTP_200_OK)




class updatefood(GenericAPIView):
    serializer_class=foodserializer
    def post(self,request,id):
        queryset=food.objects.get(pk=id)
        print(queryset)
        serializer=foodserializer(instance=queryset,data=request.data,partial=True)
        print(serializer)
        if serializer.is_valid():



            serializer.save()
            return Response({'data':serializer.data,'message':'updated succesfulluyy','success':True},status=status.HTTP_200_OK)
        else:
            return Response({'data':'something went wrong','sucess':False},status=status.HTTP_400_BAD_REQUEST)  




class searchfood(GenericAPIView):
    def post(self, request):
        query = request.data.get('query')
        print(query)

        i = food.objects.filter(foodname__icontains=query)
        for dta in i:
            print(dta)

        data = [{'foodname': info.foodname, 'foodtype': info.foodtype,' cookingtime': info. cookingtime} for info in i]
        return Response({'data': data, 'message': 'Successfully fetched', 'success': True}, status=status.HTTP_200_OK)





class donarfoodview(GenericAPIView):
    serializer_class=foodserializer
    def get(self,request,id):
        queryset=food.objects.filter(donarid=id)
        if(queryset.count()>0):
            serializer=foodserializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'all food data  set' ,'success':1},status=status.HTTP_200_OK)
        else:
            return Response({'data':'no datas avaialable ','success':0},status=status.HTTP_201_CREATED)   



class receiverfoodview(GenericAPIView):
    serializer_class=foodserializer
    def get(self,request):
        queryset=food.objects.all().filter(foodstatus=0)
        if(queryset.count()>0):
            serializer=foodserializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'all food data  set' ,'success':1},status=status.HTTP_200_OK)
        else:
            return Response({'data':'no datas avaialable ','success':0},status=status.HTTP_201_CREATED)    
        



# class acceptingAPIView(GenericAPIView):
#     serializer_class = acceptingserializer

#     def post(self, request):
        

        
#         receiver=request.data.get('receiverid')
#         donar=request.data.get("donarid")
#         foodss=request.data.get('foodid')
#         acceptingdate=str(date.today())
#         print(foodss)
#         acceptingstatus="0"
        
#         accept =  accepting.objects.filter(receiverid=receiver, foodid=foodss)
#         if  accept.exists():
#             return Response({'message':'food is already in accepted','success':False}, status=status.HTTP_400_BAD_REQUEST)

#         else:
#             data=food.objects.all().filter(id=foodss).values()
#             for i in data:

#                 print(i)
#                 foodname=i['foodname']
#                 foodtype=i['foodtype']
#                 cookingtime=i['cookingtime']
#                 address=i['address']
#                 phone=i['phone']
#             i.foodstatus = "1"
#             i.save() 


#             # fooddata=food.objects.get(id=food)
#             # quant=fooddata.quantity
#             # foodcount=int(quant)


#             # fooddata.quantity=foodcount-bkquantity
#             # fooddata.save()


#             data2=user2.objects.all().filter(id=receiver).values()
#             for i in data2:
#                 print(i)
#                 receivername=i['uname']
#             data3= user.objects.all().filter(id= donar).values()
#             for i in data3:
#                 print(i)
#                 donarname=i['uname']




#             foodz = food.objects.get(id=foodss)
#             food_image = foodz.image
#             print( food_image)
                

    
#             serializer = self.serializer_class(data= {'receiverid':receiver,'donarname':donarname,'donarid':donar,'foodid':foodss,'foodname':foodname,'receivername': receivername,'image':food_image,'foodtype': foodtype,'cookingtime': cookingtime,'address': address,'phone':phone,'acceptingdate': acceptingdate,'acceptingstatus': acceptingstatus})
#             print(serializer)
#             if serializer.is_valid():
#                 print("hi")
#                 serializer.save()   
#                 return Response({'data':serializer.data,'message':'food added successfully', 'success':True}, status = status.HTTP_201_CREATED)
#             return Response({'data':serializer.errors,'message':'Invalid','success':False}, status=status.HTTP_400_BAD_REQUEST)

class AcceptingAPIView(GenericAPIView):
    serializer_class = acceptingserializer  # Assuming AcceptingSerializer is a valid serializer class

    def post(self, request):
        receiver = request.data.get('receiverid')
        donar = request.data.get("donarid")
        foodss = request.data.get('foodid')
        acceptingdate = str(date.today())
        print(foodss)
        acceptingstatus = "0"

        accept = accepting.objects.filter(receiverid=receiver, foodid=foodss)
        if accept.exists():
            return Response({'message': 'Food is already accepted', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

        else:
            food_data = food.objects.get(id=foodss)
            foodname = food_data.foodname
            foodtype = food_data.foodtype
            cookingtime = food_data.cookingtime
            address = food_data.address
            phone = food_data.phone
            food_data.foodstatus = "1"
            food_data.save()

            receiver_data = user2.objects.get(id=receiver)
            receivername = receiver_data.uname

            donar_data = user.objects.get(id=donar)
            donarname = donar_data.uname

            foodz = food.objects.get(id=foodss)
            food_image = foodz.image
            print(food_image)

            serializer = self.serializer_class(data={
                'receiverid': receiver,
                'donarname': donarname,
                'donarid': donar,
                'foodid': foodss,
                'foodname': foodname,
                'receivername': receivername,
                'image': food_image,
                'foodtype': foodtype,
                'cookingtime': cookingtime,
                'address': address,
                'phone': phone,
                'acceptingdate': acceptingdate,
                'acceptingstatus': acceptingstatus
            })

            if serializer.is_valid():
                print("hi")
                serializer.save()
                return Response({'data': serializer.data, 'message': 'Food added successfully', 'success': True},
                                status=status.HTTP_201_CREATED)
            return Response({'data': serializer.errors, 'message': 'Invalid', 'success': False},
                            status=status.HTTP_400_BAD_REQUEST)




class receiveracceptingview(GenericAPIView):
    serializer_class=acceptingserializer
    def get(self,request):
        queryset=accepting.objects.all()
        if(queryset.count()>0):
            serializer=acceptingserializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'all accepting data  set' ,'success':1},status=status.HTTP_200_OK)
        else:
            return Response({'data':'no datas avaialable ','success':0},status=status.HTTP_201_CREATED) 
        


class deletereceiveracceptingview(GenericAPIView):

    def delete(self,request,id):
        deletefood=accepting.objects.get(pk=id)
        deletefood.delete()
        return Response({'message':'Deleted suscesfully','sucess':True},status=status.HTTP_200_OK)




class donaracceptingview(GenericAPIView):
    serializer_class=acceptingserializer
    def get(self,request,id):
        queryset=accepting.objects.filter(donarid=id,acceptingstatus=0)
        if(queryset.count()>0):
            serializer=acceptingserializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'all accepting data  set' ,'success':1},status=status.HTTP_200_OK)
        else:
            return Response({'data':'no datas avaialable ','success':0},status=status.HTTP_201_CREATED)   




# ________________________________________accepting order__________________________

class donarApprove_orderAPIView(GenericAPIView):
    def post(self, request, id):
        serializer_class =acceptingserializer
        accept = accepting.objects.get(pk=id)
        accept.acceptingstatus = 1
        accept.save()
        serializer = serializer_class(accept)
        return Response({'data':serializer.data,'message':'donar Approved order', 'success':True}, status=status.HTTP_200_OK)
    



class donationapproved(GenericAPIView):
    serializer_class=acceptingserializer
    def get(self,request,id):
        queryset=accepting.objects.filter(receiverid=id, acceptingstatus=1)
        if(queryset.count()>0):
            serializer=acceptingserializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'all accepting data  set' ,'success':1},status=status.HTTP_200_OK)
        else:
            return Response({'data':'no datas avaialable ','success':0},status=status.HTTP_201_CREATED) 
        





class donationpending(GenericAPIView):
    serializer_class=acceptingserializer
    def get(self,request,id):
        queryset=accepting.objects.filter(receiverid=id, acceptingstatus=0)
        if(queryset.count()>0):
            serializer=acceptingserializer(queryset,many=True)
            return Response({'data':serializer.data,'message':'all accepting data  set' ,'success':1},status=status.HTTP_200_OK)
        else:
            return Response({'data':'no datas avaialable ','success':0},status=status.HTTP_201_CREATED) 
        


