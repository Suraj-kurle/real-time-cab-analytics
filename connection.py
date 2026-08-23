import random
import uuid
import json
from datetime import datetime, timedelta
from faker import Faker
from azure.eventhub import EventHubProducerClient, EventData
import logging
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
import os
import time

# Pulling Data Generator Function
from data import generate_uber_ride_confirmation

# CONNECTION_STRING = os.getenv("CONNECTION_STRING")
# EVENT_HUBNAME = os.getenv("EVENT_HUBNAME")

CONNECTION_STRING = "Cant share this link sorry"
EVENT_HUBNAME = "Cant share this as well"




# def send_to_event_hub(ride_data=None, batch_size=1):

#     try:
#         # Initialize Event Hub Producer Client
#         producer = EventHubProducerClient.from_connection_string(
#             CONNECTION_STRING,
#             eventhub_name=EVENT_HUBNAME
#         )
        
#         # Prepare ride records
#         ride_json = json.dumps(ride_data) 
        
#         # Create batch of events
#         event_batch = producer.create_batch()

            
#         # Create event with ride data 
#         event = EventData(ride_json)
            
#         # Add event to batch
#         event_batch.add(event)

#         # Send batch to Event Hub
#         producer.send_batch(event_batch)
        
#         producer.close()

#         return "Successfully sent to Event Hub"
        
#     except Exception as e:
#         print(f"Error sending data to Event Hub: {str(e)}")
#         return False

# Initialize Event Hub Producer ONCE
producer = EventHubProducerClient.from_connection_string(
    CONNECTION_STRING,
    eventhub_name=EVENT_HUBNAME
)
 
 
def send_to_event_hub(ride_data=None):
    try:
        ride_json = json.dumps(ride_data)
 
        event_batch = producer.create_batch()
 
        event = EventData(ride_json)
        event_batch.add(event)
 
        producer.send_batch(event_batch)
 
        return "Successfully sent to Event Hub"
 
    except Exception as e:
        print(f"Error sending data to Event Hub: {str(e)}")
        return False
 
 
# Your continuous producer
try:
    while True:
 
        for _ in range(5):
            ride = generate_uber_ride_confirmation()
 
            result = send_to_event_hub(ride)
 
            print(f"Ride sent: {ride['ride_id']} | {result}")
 
        time.sleep(1)
 
except KeyboardInterrupt:
    print("\nProducer stopped.")
    producer.close()



# if __name__ == "__main__":
    
#     print("=" * 80)
#     print("SINGLE RIDE CONFIRMATION")
#     print("=" * 80)
#     ride = generate_uber_ride_confirmation()
#     print(json.dumps(ride, indent=2))

    
#     print("\n" + "=" * 80)
#     print("SENDING SINGLE RIDE TO EVENT HUB")
#     result = send_to_event_hub(ride)
#     print(f"Single ride sent to Event Hub: {result}")

if __name__ == "__main__":
 
    print("=" * 80)
    print("CONTINUOUS UBER RIDE PRODUCER")
    print("=" * 80)
    print("Generating 5 ride every 1 seconds...")
    print("Press Ctrl+C to stop.")
 
    try:
        while True:

            for _ in range(5):
                ride = generate_uber_ride_confirmation()

                result = send_to_event_hub(ride)
 
            # Generate a new Uber ride
            # ride = generate_uber_ride_confirmation()
 
            # Send it to Event Hub
            # result = send_to_event_hub(ride)
 
                print(f"Ride sent: {ride['ride_id']} | {result}")
 
            # Wait  seconds before generating the next event
                time.sleep(1)
 
    except KeyboardInterrupt:
        print("\nProducer stopped.")
 
    
    
