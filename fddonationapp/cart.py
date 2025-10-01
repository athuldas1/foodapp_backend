from datetime import date

class acceptingAPIView(GenericAPIView):
    serializer_class = acceptingserializer

    def post(self, request):
        

        
        receiver = request.data.get('receiverid')
        donar=request.data.get("donarid")
        food=request.data.get('foodid')
        acceptingdate = date.today()
        print(food)
        acceptingstatus="0"
        
        accept =  accepting.objects.filter(receiverid=receiver, foodid=food)
        if  accept.exists():
            return Response({'message':'food is already in accepted','success':False}, status=status.HTTP_400_BAD_REQUEST)

        else:
            data=food.objects.all().filter(id=food).values()
            for i in data:
                print(i)
                foodname=i['foodname']
                foodtype=i['foodtype']
                cookingtime=i['cookingtime']
                address=i['address']
                phone=i['phone']
             


            # fooddata=food.objects.get(id=food)
            # quant=fooddata.quantity
            # foodcount=int(quant)


            # fooddata.quantity=foodcount-bkquantity
            # fooddata.save()


            data2=user2.objects.all().filter(id=user2).values()
            for i in data:
                print(i)
                receivername=i['uname']
            data3= user.objects.all().filter(id=user).values()
            for i in data:
                print(i)
                donarname=i['uname']




            foodz = food.objects.get(id=food)
            food_image = foodz.image
            print( food_image)
                

    
            serializer = self.serializer_class(data= {' receiverid': receiver,'donarname':donarname,'donarid':donar,'foodid':food,'foodname':foodname,' receivername': receivername,'image':food_image,' foodtype': foodtype,'cookingtime': cookingtime,' address': address,'phone':phone})
            print(serializer)
            if serializer.is_valid():
                print("hi")
                serializer.save()   
                return Response({'data':serializer.data,'message':'food added successfully', 'success':True}, status = status.HTTP_201_CREATED)