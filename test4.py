# age,name,sex,religon,ethnicity,height,degree
#there are 7 values

labels = ["age","name","sex","religion","ethnicity","height","degree"]

profiles = [[21,"nathan","m","hindu","indian",5.3,"computer-science"],
            [20,"baro","m","muslim","indian",6.5,"maths"],
            [19,"Hanna","f","christian","german",5.1,"maths"],
            [18,"riza","f","athiest","indian",4.5,"computer-science"],
            [17,"mohammed","m","muslim","indian",5.5,"computer-science"],
            [23,"hammna","f","hindu","italian",5.10,"computer-science"],
            [21,"boris","m","muslim","german",5.5,"maths"],
            [19,"rico","m","hindu","indian",5.11,"bio-chem"],
            [25,"maeze","f","athiest","indian",6.2,"computer-science"],
            [20,"warren","m","muslim","german",5.5,"maths"],
            [18,"reuben","m","hindu","indian",5.7,"computer-science"],
            [19,"bubz","m","hindu","german",5.11,"bio-chem"],
            [22,"holly","f","christian","indian",5.3,"computer-science"],
            [19,"louis","m","hindu","italian",5.9,"cmaths"],
            [18,"rish","m","hindu","italian",5.4,"computer-science"],
            [19,"shophie","f","athiest","indian",6.0,"maths"],
            [24,"phillip","m","athiest","italian",6.1,"bio-chem"],
            [21,"musin","f","christian","indian",6.5,"computer-science"],
            [20,"jiwoo","f","hindu","italian",5.1,"computer-science"],
            [22,"anton","m","hindu","indian",5.6,"maths"],
            [18,"kota","m","christian","german",5.8,"bio-chem"],
            [19,"kush","m","hindu","italian",5.3,"computer-science"],
            [20,"tree","m","hindu","indian",5.2,"maths"],
            [19,"eda","f","muslim","indian",5.2,"computer-science"],
            [20,"sahitya","f","hindu","german",5.4,"computer-science"],
            [22,"bhavik","m","christian","german",5.10,"maths"],
            [19,"charles","m","athiest","indian",5.4,"computer-science"],
            [23,"Luka","f","athiest","german",5.11,"computer-science"],
            [19,"sophie","f","christian","italian",5.9,"bio-chem"],
            [21,"nathan","m","hindu","italian",5.2,"bio-chem"]]


for profile in profiles:
    print("\n\n new profile \n ")
    for x in range(len(labels)):
        print(profile[x])
