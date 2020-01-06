import geopandas as gpd
import matplotlib.pyplot as plt
import openaq
from scipy.interpolate import griddata

t = 'y'

api = openaq.OpenAQ()
def get_plot(shape,city,cnt,pol):
    city = city.capitalize()
    resp = api.latest(city=city, country=cnt, parameter=(pol))
    fp = shape #"bengaluru/shape/waterways.shp"
    data = gpd.read_file(fp)
    ax = data.plot()
    for i in range(len(resp[1]['results'])):
        lat,long,value  = resp[1]['results'][i]['coordinates']['latitude'],resp[1]['results'][i]['coordinates']['longitude'],resp[1]['results'][i]['measurements'][0]['value']
        print(lat,long)
        plt.scatter(long,lat,c='red',s=(value*15)/5)

    plt.show()

while True:
    try:
        if t == 'y':
            shp = input("please enter absolute path to shape file : ")
            city = input("please enter the name of the city : ")
            cnt = input("please enter ISO code for the country : ")
            pol = input("please choose the pollutant whose data you would like to plot : (pm25/pm10/so2/co/no2/o3) : ")
            get_plot(shp, city, cnt, pol)
            t = input('would you like to try again ? (y/n) : ')
        else:
            break
    except:
        print("An error occured please try again.")
        t = 'y'