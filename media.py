# importing library
import webbrowser

# the content below is related to entertainment.py
# both has the films' content

# fuction to get all the films' content
# after, the fresh_tomatoes.py will read it
# in a html page, where the infos will be displayed

class Movie():
	def __init__(self, movie_title, original_title, movie_length, movie_year, poster_image, trailer_youtube):
		self.title = movie_title
		self.original_title = original_title
		self.length = movie_length
		self.year = movie_year
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

# function to open the url trailer
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
