# Twitter Movie Review Bot

This program first webscrapes IMDb's top 250 movies and tweets a random bad review left by a user. It is written in Python and uses BeautifulSoup and Playwright to scrape IMDb to obtain the movie and review.

The review is formatted into a tweet which includes the movies name, overall rating, and where it is on the top 250 list. If the review is long than the alotted tweet length it replies to creaete a thread and include the length of the thread.

It stores past review and a list of recently tweeted movies to avoid tweeting the same movie too frequently.

It currently containerized with Docker and runs regularly.

@HM_Takes on Twitter/X -> https://twitter.com/HM_Takes