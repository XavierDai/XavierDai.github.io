import requests
from google.transit import gtfs_realtime_pb2

API_KEY = "b76c6c41-9c70-4195-bb3c-98b8abed4d4d"
ENDPOINT = "http://api.511.org/transit/vehiclepositions?api_key=" + API_KEY + "&agency=RG"

def get_vehicle_positions():
    response = requests.get(ENDPOINT)
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(response.content)
    
    positions = []
    for entity in feed.entity:
        if entity.HasField('vehicle'):
            positions.append({
                "latitude": entity.vehicle.position.latitude,
                "longitude": entity.vehicle.position.longitude
            })
    return positions
