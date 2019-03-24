import pandas as pd
import xlrd
from sklearn import tree
#reading excel file
pdf=pd.read_excel("C:\\Users\\Vipin\\Documents\\Machine Learning Project\\Restaurant-Data\\restaurant-data-with-consumer-ratings\\compare.xlsx")
#print column names
pdf.columns
userID=pdf.userID
latitude=pdf.latitude
longitude=pdf.longitude
smoker=pdf.smoker
drink_level=pdf.drink_level
dress_preference=pdf.dress_preference
ambience=pdf.ambience
transport=pdf.transport
martial_status=pdf.marital_status
hijos=pdf.hijos
birth_year=pdf.birth_year
interest=pdf.interest
personality=pdf.personality
religion=pdf.religion
activity=pdf.activity
color=pdf.color
weight=pdf.weight
budget=pdf.budget
height=pdf.height
rcuisine=pdf.Rcuisine
rating=pdf.rating
food_rating=pdf.food_rating
service_rating=pdf.service_rating
pd.set_option('display.max_rows',200)
pd.set_option('display.max_columns',50)
dframe=pd.DataFrame(pdf)
#dframe.to_csv('testfile.csv')
#Functions for replacing values
#Drink Level
def tran_drinklevel(x):
    if x == 'abstemious':
        return 0
    if x == 'casual drinker':
        return 1
    if x == 'social drinker':
        return 2
def tran_dress(x):
    if x == 'elegant':
        return 0
    if x == 'formal':
        return 1
    if x == 'informal':
        return 2
    if x == 'no preference':
        return 3
def tran_ambience(x):
    if x == 'family':
        return 0
    if x == 'friends':
        return 1
    if x == 'solitary':
        return 2
def tran_transport(x):
    if x == 'on foot':
        return 0
    if x == 'public':
        return 1
    if x == 'car owner':
        return 2
def tran_martial_status(x):
    if x == 'widow':
        return 0
    if x == 'single':
        return 1
    if x == 'married':
        return 2
def tran_hijos(x):
    if x == 'kids':
        return 0
    if x == 'independent':
        return 1
    if x == 'dependent':
        return 2
def tran_interest(x):
    if x == 'none':
        return 0
    if x == 'eco-friendly':
        return 1
    if x == 'retro':
        return 2
    if x == 'technology':
        return 3
    if x == 'variety':
        return 4
def tran_personality(x):
    if x == 'thrifty-protector':
        return 0
    if x == 'conformist':
        return 1
    if x == 'hard-worker':
        return 2
    if x == 'hunter-ostentatious':
        return 3
def tran_religion(x):
    if x == 'none':
        return 0
    if x == 'Catholic':
        return 1
    if x == 'Christian':
        return 2
    if x == 'Jewish':
        return 3
    if x == 'Mormon':
        return 4
def tran_activity(x):
    if x == 'unemployed':
        return 0
    if x == 'working-class':
        return 1
    if x == 'student':
        return 2
    if x == 'professional':
        return 3
def tran_color(x):
    if x == 'black':
        return 0
    if x == 'blue':
        return 1
    if x == 'green':
        return 2
    if x == 'orange':
        return 3
    if x == 'purple':
        return 4
    if x == 'red':
        return 5
    if x == 'white':
        return 6
    if x == 'yellow':
        return 7
def tran_budget(x):
    if x == 'low':
        return 0
    if x == 'medium':
        return 1
    if x == 'high':
        return 2
def tran_smoke(x):
    if(x==0):
        return 'no'
    if(x==1):
        return 'yes'
def tran_rating(x):
    if(x==0):
        return 'Average'
    if(x==1):
        return 'Good'
    if(x==2):
        return 'Excellent'
def tran_foodrating(x):
    if(x==0):
        return 'Average'
    if(x==1):
        return 'Good'
    if(x==2):
        return 'Excellent'
def tran_servicerating(x):
    if(x==0):
        return 'Average'
    if(x==1):
        return 'Good'
    if(x==2):
        return 'Excellent'

dframe['drinklevel_trans']=dframe['drink_level'].apply(tran_drinklevel)
drinklevel=dframe['drinklevel_trans']
dframe['dresspreference_trans']=dframe['dress_preference'].apply(tran_dress)
dressprefer=dframe['dresspreference_trans']
dframe['ambience_trans']=dframe['ambience'].apply(tran_ambience)
ambience=dframe['ambience_trans']
dframe['transport_trans']=dframe['transport'].apply(tran_transport)
transport=dframe['transport_trans']
dframe['martial_trans']=dframe['marital_status'].apply(tran_martial_status)
martial=dframe['martial_trans']
dframe['hijos_trans']=dframe['hijos'].apply(tran_hijos)
hijos=dframe['hijos_trans']
dframe['interest_trans']=dframe['interest'].apply(tran_interest)
interest=dframe['interest_trans']
dframe['personality_trans']=dframe['personality'].apply(tran_personality)
personality=dframe['personality_trans']
dframe['religion_trans']=dframe['religion'].apply(tran_religion)
religion=dframe['religion_trans']
dframe['activity_trans']=dframe['activity'].apply(tran_activity)
activity=dframe['activity_trans']
dframe['color_trans']=dframe['color'].apply(tran_color)
color=dframe['color_trans']
dframe['budget_trans']=dframe['budget'].apply(tran_budget)
budget=dframe['budget_trans']
dframe['rating_trans']=dframe['rating'].apply(tran_rating)
rating=dframe['rating_trans']
dframe['foodrating_trans']=dframe['food_rating'].apply(tran_foodrating)
food_rating=dframe['foodrating_trans']
dframe['servicerating_trans']=dframe['service_rating'].apply(tran_servicerating)
service_rating=dframe['servicerating_trans']
d={'latitude':latitude,'longitude':longitude,'smoke':smoker,'drink_level':drinklevel,'dress_preference':dressprefer,'ambience':ambience,'transport':transport,'martial_status':martial,'hijos':hijos,'birth_year':birth_year,'interest':interest,'personality':personality,'religion':religion,'activity':activity,'color':color,'weight':weight,'budget':budget,'height':height,'Rcuisine':rcuisine,'rating':rating,'food_rating':food_rating,'service_rating':service_rating}
dframe1=pd.DataFrame(data=d)
#print(dframe1)
import pandas as pdf
import xlrd
from sklearn import tree
#reading excel file
file=pdf.read_excel("C:\\Users\\Vipin\\Documents\\Machine Learning Project\\Restaurant-Data\\restaurant-data-with-consumer-ratings\\predict.xls")
df=pdf.DataFrame(data=file)
prsmoke=df['prsmoke']
prdrink=df['prdrink']
prdress=df['prdress']
prambience=df['prambience']
prtransport=df['prtransport']
prmartial=df['prmartial']
prhijos=df['prhijos']
printerest=df['printerest']
prpersonality=df['prpersonality']
prreligion=df['prreligion']
practivity=df['practivity']
prweight=df['prweight']
prbudget=df['prbudget']
prheight=df['prheight']

pr=[]
for i in range(len(prdress)):
    pr.append([prsmoke[i],prdrink[i],prdress[i],prambience[i],prtransport[i],prmartial[i],prhijos[i],printerest[i],prpersonality[i],prreligion[i],practivity[i],prweight[i],prbudget[i],prheight[i]])
X1=[]
Y1=[]
#Decision Tree for Rating 
for i in range(len(latitude)):
    X1.append([smoker[i],drinklevel[i],dressprefer[i],ambience[i],transport[i],martial[i],hijos[i],interest[i],personality[i],religion[i],activity[i],weight[i],budget[i],height[i]])
    Y1.append(rating[i])
#print(X)
print("Testing data of Rating:")
print(X1)
print("Training data of Rating:")
print(Y1)
clf=tree.DecisionTreeClassifier()
clf=clf.fit(X1,Y1)
rsum1=0;
rsum2=0;
rsum3=0;
for i in range(len(pr)):
    prediction=clf.predict([pr[i]])
    print("Rating given by customer for  Mexican restaurant is:")
    print(prediction)
    if prediction == 'Good':
        rsum1=rsum1+1
    if prediction == 'Average':
        rsum2=rsum2+1
    if prediction == 'Excellent':
        rsum3=rsum3+1
X2=[]
Y2=[]
#Decision Tree for Food Rating
for i in range(len(latitude)):
    X2.append([smoker[i],drinklevel[i],dressprefer[i],ambience[i],transport[i],martial[i],hijos[i],interest[i],personality[i],religion[i],activity[i],weight[i],budget[i],height[i]])
    Y2.append(food_rating[i])
#print(X2)
print("Testing data of Food Rating:")
print(X2)
print("Training data of Food Rating:")
print(Y2)
clf=tree.DecisionTreeClassifier()
clf=clf.fit(X2,Y2)
frsum1=0;
frsum2=0;
frsum3=0;
for i in range(len(pr)):
    prediction1=clf.predict([pr[i]])
    print("Food Rating given by customer for Mexican restaurant is:")
    print(prediction1)
    if prediction1 == 'Good':
        frsum1=frsum1+1
    if prediction1 == 'Average':
        frsum2=frsum2+1
    if prediction1 == 'Excellent':
        frsum3=frsum3+1


X3=[]
Y3=[]
#Decision Tree for Rcusine
csum1=0;
csum2=0;
csum3=0;
csum4=0;
csum5=0;
csum6=0;
csum7=0;
csum8=0;
csum9=0;
csum10=0;
csum11=0;
csum12=0;
csum13=0;
csum14=0;
csum15=0;
csum16=0;
csum17=0;
csum18=0;
csum19=0;
csum20=0;
csum21=0;
csum22=0;
csum23=0;
csum24=0;


for i in range(len(latitude)):
    X3.append([smoker[i],drinklevel[i],dressprefer[i],ambience[i],transport[i],martial[i],hijos[i],interest[i],personality[i],religion[i],activity[i],weight[i],budget[i],height[i]])
    Y3.append(rcuisine[i])
#print(Y3)
#print(X3)
print("Testing data of Rcuisine:")
print(X3)
print("Training data of Rcuisine:")
print(Y3)
clf=tree.DecisionTreeClassifier()
clf=clf.fit(X3,Y3)

for i in range(len(pr)):
    prediction2=clf.predict([pr[i]])
    print("RCuisine choosen by customer in Mexican restaurant is:")
    print(prediction2)
    if prediction2 == 'American':
        csum1=csum1+1
    if prediction2 == 'Bakery':
        csum2=csum2+1
    if prediction2 == 'Bar':
        csum3=csum3+1
    if prediction2 == 'Barbecue':
        csum4=csum4+1
    if prediction2 == 'Breakfast-Brunch':
        csum5=csum5+1
    if prediction2 == 'Burgers':
        csum6=csum6+1
    if prediction2 == 'Cafe-Coffee_Shop':
        csum7=csum7+1
    if prediction2 == 'Cafeteria':
        csum8=csum8+1
    if prediction2 == 'Chinese':
        csum9=csum9+1
    if prediction2 == 'Contemporary':
        csum10=csum10+1
    if prediction2 == 'Cuban':
        csum11=csum11+1
    if prediction2 == 'Diner':
        csum12=csum12+1
    if prediction2 == 'Family':
        csum13=csum13+1
    if prediction2 == 'Italian':
        csum14=csum14+1
    if prediction2 == 'Japanese':
        csum15=csum15+1
    if prediction2 == 'Latin_American':
        csum16=csum16+1
    if prediction2 == 'Mexican':
        csum17=csum17+1
    if prediction2 == 'Middle_Eastern':
        csum18=csum18+1
    if prediction2 == 'Organic_Healthy':
        csum19=csum19+1
    if prediction2 == 'Pizzeria':
        csum20=csum20+1
    if prediction2 == 'Regional':
        csum21=csum21+1
    if prediction2 == 'Sushi':
        csum22=csum22+1
    if prediction2 == 'Tex-Mex':
        csum23=csum23+1
    if prediction2 == 'Turkish':
        csum24=csum24+1

X4=[]
Y4=[]
#Decision Tree for Service Rating
for i in range(len(latitude)):
    X4.append([smoker[i],drinklevel[i],dressprefer[i],ambience[i],transport[i],martial[i],hijos[i],interest[i],personality[i],religion[i],activity[i],weight[i],budget[i],height[i]])
    Y4.append(service_rating[i])
print("Testing data of Service Rating:")
print(X4)
print("Training data of Service Rating:")
print(Y4)
clf=tree.DecisionTreeClassifier()
clf=clf.fit(X4,Y4)
srsum1=0;
srsum2=0;
srsum3=0;
for i in range(len(pr)):
    prediction3=clf.predict([pr[i]])
    print("Service rating given by customer for the  Mexican restaurant is:")
    print(prediction3)
    if prediction3 == 'Good':
        srsum1=srsum1+1
    if prediction3 == 'Average':
        srsum2=srsum2+1
    if prediction3 == 'Excellent':
        srsum3=srsum3+1
print("Number of customers given  rating as Good is:")
print(rsum1)
print("Number of customers given  rating as Average is:")
print(rsum2)
print("Number of customers given  rating as Excellent is:")
print(rsum3)
print("Number of customers given Food rating as Good is:")
print(frsum1)
print("Number of customers given Food rating as Average is:")
print(frsum2)
print("Number of customers given Food rating as Excellent is:")
print(frsum3)
print("Number of customers choosed the American:")
print(csum1)
print("Number of customers choosed the Bakery :")
print(csum2)
print("Number of customers choosed the Bar :")
print(csum3)
print("Number of customers choosed the Barbecue :")
print(csum4)
print("Number of customers choosed the Breakfast-Brunch :")
print(csum5)
print("Number of customers choosed the Burgers :")
print(csum6)
print("Number of customers choosed the Cafe-Coffe-Shop :")
print(csum7)
print("Number of customers choosed the Cafeteria :")
print(csum8)
print("Number of customers choosed the Chinese :")
print(csum9)
print("Number of customers choosed the Contemporary :")
print(csum10)
print("Number of customers choosed the Cuban :")
print(csum11)
print("Number of customers choosed the Diner :")
print(csum12)
print("Number of customers choosed the Family :")
print(csum13)
print("Number of customers choosed the Italian :")
print(csum14)
print("Number of customers choosed the Japanese :")
print(csum15)
print("Number of customers choosed the Latin_American :")
print(csum16)
print("Number of customers choosed the Mexican :")
print(csum17)
print("Number of customers choosed the Middle_Eastern :")
print(csum18)
print("Number of customers choosed the Organic-Healthy Food :")
print(csum19)
print("Number of customers choosed the Pizzeria :")
print(csum20)
print("Number of customers choosed the Regional :")
print(csum21)
print("Number of customers choosed the Sushi :")
print(csum22)
print("Number of customers choosed the Tex-Mex :")
print(csum23)
print("Number of customers choosed the Turkish :")
print(csum24)

print("Number of customers given Service rating as Good is:")
print(srsum1)
print("Number of customers given Service rating as Average is:")
print(srsum2)
print("Number of customers given Service rating as Excellent is:")
print(srsum3)
    

