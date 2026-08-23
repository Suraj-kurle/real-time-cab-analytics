# Near-Real-Time Cab Analytics

An end-to-end near-real-time cab analytics project demonstrating a
streaming data pipeline from event generation through cloud processing,
data warehousing, and business intelligence.

## Architecture

``` text
Python
   ↓
Azure Event Hubs
   ↓
Azure Stream Analytics
   ↓
ADLS Gen2
   ↓
Databricks Structured Streaming / PySpark
   ↓
Snowflake
   ↓
Power BI
```

## Project Overview

This project processes cab ride events through a near-real-time data
pipeline and transforms them into an analytics-ready dimensional model
in Snowflake.

The final Power BI dashboard provides insights into:

-   Total rides
-   Total revenue
-   Average fare
-   Average trip duration
-   Average distance
-   Revenue trends
-   Ride volume over time
-   Rides by vehicle mode
-   Rides by payment method

## Technology Stack

-   Python
-   Azure Event Hubs
-   Azure Stream Analytics
-   Azure Data Lake Storage Gen2 (ADLS Gen2)
-   Azure Databricks
-   Databricks Structured Streaming
-   PySpark
-   Snowflake
-   SQL
-   Dimensional Data Modeling
-   Star Schema
-   Power BI
-   DAX

## Data Warehouse Model

The Snowflake analytical layer uses a dimensional/star-schema design.

### Fact Table

`FCT_RIDES`

Contains ride-level transactional data such as booking timestamp, date
key, vehicle information, pickup and drop-off locations, distance, fare,
trip duration, driver rating, and payment/cancellation attributes.

### Dimension Tables

-   `DIM_DATE`
-   `DIM_VEHICLE`
-   `DIM_RIDE`
-   `DIM_PAYMENT`
-   `DIM_PICKUP_LOCATION`
-   `DIM_DROPOFF_LOCATION`

## Power BI Dashboard

The project includes a one-page Power BI dashboard designed to provide a
high-level view of cab activity.

### Key KPIs

-   Total Rides
-   Total Revenue
-   Average Fare
-   Average Duration
-   Average Distance

### Visualizations

-   Revenue Trend
-   Rides Over Time
-   Rides by Vehicle Mode
-   Rides by Payment Method

Year and Month filters provide interactive analysis.

## Key Engineering Concepts Demonstrated

-   Event-driven data ingestion
-   Near-real-time data processing
-   Structured Streaming with PySpark
-   Cloud data lake architecture
-   Snowflake dimensional modeling
-   Star schema design
-   Analytical SQL
-   DAX measures
-   Power BI dashboard development
-   End-to-end data pipeline architecture

## Repository Contents

``` text
real-time-cab-analytics/
│
├── README.md
├── snowflake_schema.sql
├── data-model.png
└── Power_bi_dashboard.png
```

## Project Outcome

The project demonstrates how cab ride events can flow through Azure and
Databricks, be modeled in Snowflake, and be presented through Power BI
for business-oriented analytics.

## Author

Suraj Kurle
