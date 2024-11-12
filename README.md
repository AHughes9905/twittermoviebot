# twittermoviebot
Check it out on Twitter: @HM_Takes
This program first webscrapes IMDb's top 250 movies. The console interface lets the user choose a movie by number, or lets a random movie be chosen.
Next the webscraper goes to the movie page and gets it name, IMDb rating out of 10, and its ranking in the top 250, and saves this information in a list.
Then it goes to the negative reviews page for the movie and selects a random negative review.
The review is then formatted tweets. Since tweets have character limit it saves all these tweets in a list. 
Then it uses the tweepy library to tweet these tweets into a thread.
