import simplejson, urllib.request

orig_lat = 51.50
orig_lng = 0.1749

dest_lat = 52.4798
dest_lng = 1.9150


orig_coord = orig_lat, orig_lng
orig_coord = dest_lat, dest_lng

orig_coord = 'Bobcaygeon'
orig_coord = 'Sussex'

url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=transit&language=en-EN&sensor=false&key=AIzaSyCp4AR-Tz26dtMI6GBrD3jzurmzdcjdYfk".format(str(orig_coord),str(dest_coord))
print()
result= urllib.request.urlopen(url)
#driving_time = result['rows'][0]['elements'][0]['duration']['value']

print(result)