# sqlalchemy-challenge
Module 10 Challenge

# Background
The project's aim is to do a climate analysis of Honolulu, Hawaii. The following sections include the analysis. 

**Part 1: Analyse and Explore the Climate Data**
This section uses Python and SQLAlchemy to do a fundamental climate analysis and data exploration of the climate database. Specifically, use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:
1. use the provided files (climate_starter.ipynb and hawaii.sqlite) to complete climate analysis and data exploration.
2. Use the SQLAlchemy create_engine() function to connect to SQLite database.
3. Use the SQLAlchemy automap_base() function to reflect tables into classes, and then save references to the classes named station and measurement.
4. Link Python to the database by creating a SQLAlchemy session.
5. Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

**Precipitation Analysis**
1. Find the most recent date in the dataset.
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Select only the "date" and "prcp" values.
4. Load the query results into a Pandas DataFrame. Explicitly set the column names.
5. Sort the DataFrame values by "date".
6. Plot the results by using the DataFrame plot method.\
  ![image](https://github.com/lakigit/sqlalchemy-challenge/assets/138610916/83a8450c-b637-4999-b544-56b69831d87a)
7. Use Pandas to print the summary statistics for the precipitation data.

**Station Analysis**
1. Design a query to calculate the total number of stations in the dataset.
2. Design a query to find the most active stations (that is, the stations that have the most rows). To do so, complete the following steps:
  - List the stations and observation counts in descending order.
  - which station ID has the greatest number of observations?
  - Using the most active station ID, calculate the lowest, highest, and average temperatures.
3. Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
  - Filter by the station that has the greatest number of observations.
  - Query the previous 12 months of TOBS data for that station.
  - Plot the results as a histogram with bins=12.\
  ![image](https://github.com/lakigit/sqlalchemy-challenge/assets/138610916/7de2bf11-3a48-4361-b4c9-f4b23dc5d1b2)
4. Close the session.


