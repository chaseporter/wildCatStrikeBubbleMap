# Project Description # 
This project creates a visualization of wild cat strikes that started in March in response to Covid-19. The visualization is in the same style of Maps generated to show the outbreaks of virus across the country with the intent to broadcast hope and express solidarity with those striking for better working conditions both during and after the pandemic. The relative size of the bubbles represent the relative size of the strikes happening and the different colors indicate broad categories of workers on strike. Visualization eventually used by Sunrise Movement.   

Data was pulled from   
https://paydayreport.com/covid-19-strike-wave-interactive-map/
at the end of April 2019 and the data used now is likely out of date.


![Alt text](wildCatStrikeMap.png?raw=true "Wild Cat Strike Map in response to Covid-19, April 2020")

## Implementation Details ##
The general flow for the generation of data went like this:  
- downloaded the kml file  
- run parse.py to extract longitudinal and latitudinal data from the kml file into file called parsedTxt.csv   
- I then manually added to parsedTxt.csv additional information I was not able to extract in an efficient way from the kml file. Information on the who was striking, how large the strike was, and what category of strike it was.  
- I then ran sort.py which took parsedTxt.csv and sorted it based on categories as well as generated indices for bucket sizes of the categories which were needed for the library I used to generate the actual bubble map.   
- Finally I ran bubbleMap.py which used pandas and plotly graph_objects to create the bubble Map.  
I would like to note that this is not the most clean project I have ever worked on, but I was working on a very tight timeline. This was only compounded by the fact that to retreive information on who was striking and the size of the strike, I needed to manually read local news reports. If given a longer time to do this, (longer than the day and a half or so I had) I would have liked to automate the data collection process, either by making a scraper of some kind or digging deeper into the kml file.



