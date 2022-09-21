# Weather-data

This script was written in Python using the selenium library. It collects weather data for Chicago for the span of one year by updating the date field on the page and then scraping values for that day. Since there are multiple recordings for one hour, I chose to pick up the reading at the 53rd minute of every hour as a reading for that minute was available for every hour of the day. Inserting numbers 0 to 11 manually will produce the file for the provided month, whereas letting it run through in a loop while give the readings in celsius for the whole year. 

For purposes unique to the project, entries corresponding to each hour of the day were assumed to be representative of the conditions prevailing during the entire hour.
