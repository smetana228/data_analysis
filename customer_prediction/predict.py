import pandas as pd
import pycountry_convert as pc

df = pd.read_csv('customer_booking.csv',encoding='ISO-8859-1')


mapping = {
    "Mon": 1,
    "Tue": 2,
    "Wed": 3,
    "Thu": 4,
    "Fri": 5,
    "Sat": 6,
    "Sun": 7,   
}

df["flight_day"] = df["flight_day"].map(mapping)


mapp = {
	"Internet":1,
	'RoundTrip':1
}

mapp_={
	'Mobile':1,
	'CircleTrip':1
}

y={
	'OneWay':1
}


g=[]
t=[]

for x in df['booking_origin']:
	if x not in g:
		g.append(x)

t = {}
u=0

for i in g:
	u=0
	for o in df['booking_origin']:
		if i==o:
			u=u+1
		t[i]=u

sorted_t = dict(reversed((sorted(t.items(), key=lambda item: item[1]))))


def country_to_continent(country_name):
	country_alpha2 = pc.country_name_to_country_alpha2(country_name)
	country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
	country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
	return country_continent_name

continents = {
	'Africa':0, 
	'Antarctica':0, 
	'Asia':0, 
	'Europe':0, 
	'North America':0, 
	'Oceania':0, 
	'South America':0
}


for x in sorted_t:
	try:
		if country_to_continent(x) in continents:
			continents[country_to_continent(x)]+=sorted_t[x]
	except KeyError:
		pass


for x in continents:
	df[f'booking_origin_{x}']=int(continents[x])
	
df['sales_channel_Internet'] = df['sales_channel'].map(mapp)
df['sales_channel_Mobile'] = df['sales_channel'].map(mapp_)
df['trip_type_RoundTrip']=df['trip_type'].map(mapp)
df['trip_type_CircleTrip']=df['trip_type'].map(mapp_)
df['trip_type_OneWay']=df['trip_type'].map(y)
print(continents)
print(df.info())
df.describe().to_csv("sum.csv")
