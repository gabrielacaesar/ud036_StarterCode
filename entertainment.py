# importing our .py files
import fresh_tomatoes
import media

# each film has its content inside a variable
# the info follows an order defined in media.py

danish_girl = media.Movie(
    "A garota dinamarquesa",
    "The danish girl",
    "119min",
    "2015",
    "https://bit.ly/2w2r9Ia",
    "https://bit.ly/1N03wTX")

help = media.Movie(
    "Histórias cruzadas",
    "The help",
    "137min",
    "2011",
    "https://bit.ly/2QwJ4j5",
    "https://www.youtube.com/watch?v=Cqn4XN21O1g")

jagten = media.Movie(
    "A caça",
    "Jagten",
    "115min",
    "2012",
    "https://bit.ly/2QwlRNR",
    "https://www.youtube.com/watch?v=gwxYwb7NbDI")

spotlight = media.Movie(
    "Spotlight",
    "Spotlight",
    "129min",
    "2015",
    "https://bit.ly/2C9N5Vr",
    "https://www.youtube.com/watch?v=zgicIR5Skwc")

vorleser = media.Movie(
    "O leitor",
    "Der Vorleser",
    "124min",
    "2008",
    "https://bit.ly/2SErv2e",
    "https://www.youtube.com/watch?v=I50ZKFCqr8g")

laerte_se = media.Movie(
    "Laerte-se",
    "Laerte-se",
    "100min",
    "2017",
    "https://bit.ly/2LYue49",
    "https://www.youtube.com/watch?v=eKHqtmd1_xg")

movies = [danish_girl, help, jagten, spotlight, vorleser, laerte_se]

fresh_tomatoes.open_movies_page(movies)
