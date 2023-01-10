#Mine Mate

Introduction
Small changes can make a big difference in any industry, and this is especially true in the mining industry. Our team at QDS Hacks 2023, sponsored by Teck Resources, set out to find areas where we could make small improvements to have a significant impact. After analyzing over 12 million records and 50 million data points, we identified queueing at shovels and dump sites as a major problem. Trucks spent over 190 tonnes of Carbon Dioxide, over $110,000, and over 540 hours idling in just one week. Projected to a year, this amounts to over 10,000 tonnes of Carbon Dioxide, over $5.8 million dollars, and over 28,281 hours of waiting.

#Approach
To tackle this problem, we first needed to make the data legible. We wrote Python scripts to convert the data into clean CSV files and then broke it down into individual truck trips. We visualized the data using Pygame and tabularized it using Google Cloud's Big Query platform, which allowed us to make complex queries and have them calculated faster. We isolated a number of variables to study, including velocity, fuel consumption, elevation, truck type, routes, and payload.

#Problem Statement
Our goal was to reduce the fuel consumption of trucks by having them drive slower both consistently and specifically to avoid queueing when heading to a shovel or dump site.

#Solution
We developed Mine Mate, an application for haul truck drivers that uses previously recorded data to compare the current truck speed with a dynamically recommended speed to save on fuel usage. The app also provides management with quick qualitative insight on data collected by Teck, including visual simulations of truck movement and graphs of important data insights.

#Demo
During the demo, we showed the following features of Mine Mate:

-The dashboard, which displays the recommended velocity, actual velocity, and estimated time of arrival at the shovel or dump site
-The schedule, which shows the route and timeslot for the current trip
-Visual simulations of truck movement and graphs of important data insights for management

#Conclusion
By using Mine Mate, haul truck drivers can make small adjustments to their speed and route to save on fuel and reduce greenhouse gas emissions. This, in turn, can lead to significant cost savings and a more sustainable mining operation overall.

#Tech Stack
-Python
-Google Cloud Big Query
-HTML
-CSS
-JavaScript

#Installation
TODO: Provide installation instructions

#Usage
TODO: Provide usage instructions

#QDPieS Team Members
-[Kale Letendre](https://github.com/kaleLetendre)
-[Harrison de Jong](https://github.com/HJackdeJong)
-[Cameron Fung](https://github.com/camfung)
-[Justin Viacrusis](https://github.com/JVViacrusis)
-[Cameron Walford](https://github.com/camwalford)
