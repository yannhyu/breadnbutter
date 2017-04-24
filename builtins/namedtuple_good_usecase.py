# namedtuple_good_usecase.py
from collections import namedtuple

# The primitive approach
lat_lng = (37.78, -122.40)
print('The latitude is %f' % lat_lng[0])
print('The longitude is %f' % lat_lng[1])

# The glorious namedtuple
LatLng = namedtuple('LatLng', ['latitude', 'longitude'])
lat_lng = LatLng(37.78, -122.40)
print('The latitude is %f' % lat_lng.latitude)
print('The longitude is %f' % lat_lng.longitude)