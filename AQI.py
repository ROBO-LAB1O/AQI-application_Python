import requests



geourl_=  "https://geocoding-api.open-meteo.com/v1/search"
def get_coordinates(url,city):
    url_=url
    params={
        "name":city,
        "count":1
    }
    response=requests.get(url_,params=params,timeout=5)
    data=response.json()

    
    if "results" not in data:
        return None
    else:
        place=data["results"][0]
        longitude=place["longitude"]
        latitude=place["latitude"]
        return longitude,latitude



AQI_url="https://air-quality-api.open-meteo.com/v1/air-quality"
def get_aqi(longitude,latitude,url):
    params_={
        "longitude" : longitude,
        "latitude" : latitude,
        "current" : "us_aqi,european_aqi,pm2_5,pm10,nitrogen_dioxide,sulphur_dioxide,carbon_monoxide,ozone"
    }
    response=requests.get(url,params=params_,timeout=5)
    data=response.json()
    return data



def main():
    while True:

        city=input("Enter Your City name: ").lower()

        if city=="":
                print('------Thankyou For using our Aqi Application------')
                break
        coords=get_coordinates(geourl_,city)



        if coords is None:
            print("City Not Found!")

        else:
            long ,lat=coords
            data=get_aqi(long ,lat,AQI_url)
            place=data["current"]


            print("=========AQI APPLICATION=============")
            print(f"NAME:        {city.title()}")
            print(f"US AQI:      {place['us_aqi']}")
            print(f"Europe AQI:  {place['european_aqi']}")
            print(f"PM2_5:        {place['pm2_5']} µg/m³")
            print(f"PM10:        {place['pm10']} µg/m³")
            print(f"Carbon Mono: {place['carbon_monoxide']} µg/m³")
            print(f"Nitrogen Di: {place['nitrogen_dioxide']} µg/m³")
            print(f"Sulphur Di:  {place['sulphur_dioxide']} µg/m³")
            print(f"Ozone:       {place['ozone']} µg/m³")
            print("=====================================")


if __name__=="__main__":
    main()
      