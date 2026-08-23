# Real-Time Cab Analytics
 
An end-to-end data analytics project built using Snowflake and Power BI to analyze cab ride activity, revenue, payment methods, vehicle modes, trip duration, distance, and customer ratings.
 
## Project Overview
 
This project demonstrates a dimensional data model built in Snowflake and an interactive one-page Power BI dashboard for analyzing cab ride performance.
 
### Technologies Used
 
- Snowflake
- SQL
- Power BI
- DAX
- Dimensional Data Modeling
- Star Schema
 
## Data Model
 
The project follows a star-schema approach with:
 
### Fact Table
 
- FCT_RIDES
 
### Dimension Tables
 
- DIM_DATE
- DIM_VEHICLE
- DIM_LOCATION
- DIM_PICKUP_LOCATION
- DIM_DROPOFF_LOCATION
- DIM_PAYMENT
- DIM_RIDE
 
## Dashboard
 
The Power BI dashboard provides insights into:
 
- Total rides
- Total revenue
- Average fare
- Average trip duration
- Average trip distance
- Revenue trends
- Ride volume trends
- Rides by vehicle mode
- Rides by payment method
- Year and month filtering
 
## Key Metrics
 
The dashboard includes DAX measures for calculating:
 
- Total Rides
- Total Revenue
- Average Fare
- Average Duration
- Average Distance
- Total Tips
- Average Rating
- Tip Percentage
 
## Architecture
 
Source Data → Snowflake Bronze/Silver/Gold → Dimensional Model → Power BI → Interactive Dashboard
 
## Dashboard Preview
 
Dashboard screenshots will be added to this repository.
 
## Disclaimer
 
This project is created for learning and portfolio purposes using sample cab ride data.
