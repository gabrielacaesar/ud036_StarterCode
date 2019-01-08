# importing our .py files
import fresh_tomatoes
import media

# each film has its content inside a variable
# the info follows an order defined in media.py

danish_girl = media.Movie("A garota dinamarquesa", "The danish girl", "119min", "2015", "https://upload.wikimedia.org/wikipedia/en/f/f2/The_Danish_Girl_%28film%29_poster.jpg", "https://www.youtube.com/watch?v=d88APYIGkjk")

help = media.Movie("Histórias cruzadas", "The help", "137min", "2011", "https://upload.wikimedia.org/wikipedia/pt/b/b5/Help_poster.jpg", "https://www.youtube.com/watch?v=Cqn4XN21O1g")

jagten = media.Movie("A caça", "Jagten", "115min", "2012", "https://upload.wikimedia.org/wikipedia/pt/8/88/A_Ca%C3%A7a_%282012%29.jpg", "https://www.youtube.com/watch?v=gwxYwb7NbDI")

spotlight = media.Movie("Spotlight", "Spotlight", "129min", "2015", "https://upload.wikimedia.org/wikipedia/pt/f/f4/Spotlight_%28filme%29.jpg", "https://www.youtube.com/watch?v=zgicIR5Skwc")

vorleser = media.Movie("O leitor", "Der Vorleser", "124min", "2008", "https://upload.wikimedia.org/wikipedia/en/6/6c/Reader_ver2.jpg", "https://www.youtube.com/watch?v=I50ZKFCqr8g")

laerte_se = media.Movie("Laerte-se", "Laerte-se", "100min", "2017", "https://media.fstatic.com/dfDqTtm-l7PDUzLQJkmJekFiIZQ=/fit-in/290x478/smart/media/movies/covers/2017/05/C_fwxM1XgAA3U1I.jpg", "https://www.youtube.com/watch?v=eKHqtmd1_xg")

movies = [danish_girl, help, jagten, spotlight, vorleser, laerte_se]

fresh_tomatoes.open_movies_page(movies)
