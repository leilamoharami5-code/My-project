#start
#az karbar dama hava begirad
weather = input("مقدار دماي هوا را وارد کنيد : ")
#tabdil be int
weather = int(weather)
#1 block shart 
import playsound3
if weather >= 30 :
    print("هوا گرم است")
elif weather >= 15 < 30 :
    print("هوا خوب است")
else :
    print("هوا سرد است")
#end
