class All_in_One():
    def Subfields():
        print("Sub-fields in AI are :")
        fields=["ML","Neural Networks","Vision","Robotics","Speech Processing","NLP"]
        for i in fields:
            print(i)
    def find():
        num=int(input("Enter a number :"))
        if num%2==0:
            print(f"{num} is Even number")
            know="Even"
        else:
            print(f"{num} is odd number.")
            know="odd"
        return know
    def elegible():
        gender=input("Enter your gender :")
        age=int(input("Enter your age :"))
        if gender=='male' and age<21 :
            print("not elegible for marrige")
        elif gender=='female' and age<18:
            print("not elegible for marrige")
        else:
            print("Eligible for marrige")
    def percentage(s1=63,s2=48,s3=74,s4=89,s5=54):
        percentage=(s1+s2+s3+s4+s4)*(100/500)
        print(f"subject_1={s1}\nsubject_2={s2}\nsubject_3={s3}\nsubject_4={s4}\nsubject_5={s5}\n\nPercentage : {percentage}%")
   
    def formula():
        height_1=int(input("enter height 1 :"))
        breadth=int(input("enter breath of the triangle :"))
        decide=input("Enter which formula ('area(a)' or 'perimeter(p)'")
        if decide=='area' or decide=="a":
            area=((height_1*breadth)/2)
            print(f"Area is : {area}.")
            return area
        elif decide=="perimeter" or decide=='p':
            height_2=int(input("enter height 2 :"))
            perimeter=height_1+height_2+breadth
            print(f"Perimeter : {perimeter}.")
            return perimeter
        else:
            print("Invalid value,try again...")
            return None


