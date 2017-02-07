import media
import fresh_tomatoes
# object of class Movie
guardians = media.Movie("Gardians of the Galaxy 2",
                        "The Guardians must fight to keep their newfound" +
                        "family together as they unravel the mystery of" +
                        "Peter Quill's true parentage.",
                        "https://images-na.ssl-images-amazon.com/" +
                        "images/I/61AZ0FAdLvL._SX342_.jpg",
                        "https://www.youtube.com/watch?v=2cv2ueYnKjg")

john_wick = media.Movie("JOHN WICK:Chapter 2",
                        "After returning to the criminal underworld to" +
                        "repay a debt, John Wick discovers that a " +
                        "large bounty has been put on his life.",
                        "https://i.ytimg.com/vi/Gn_wtpnDsn0/movieposter.jpg",
                        "https://www.youtube.com/watch?v=XGk2EfbD_Ps")

thor = media.Movie("THOR:Ragnarok",
                   "After returning to the criminal underworld to " +
                   "repay a debt, John Wick discovers that a large" +
                   "bounty has been put on his life.",
                   "https://images-na.ssl-images-amazon.com/images/I" +
                   "/91l0JSI-WRL._SY445_.jpg",
                   "https://www.youtube.com/watch?v=XGk2EfbD_Ps")

bruce_almighty = media.Movie("Bruce Almighty",
                             "A guy who complains about God too often" +
                             "is given almighty powers to teach him how" +
                             "difficult it is to run the world.",
                             "https://images-na.ssl-images-amazon.com/" +
                             "images/M/MV5BNzMyZDhiZDUtYWUyMi00ZDQxLWE" +
                             "4NDQtMWFlMjI1YjVjMjZiXkEyXkFqcGdeQXVyNjU0" +
                             "OTQ0OTY@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
                             "https://www.youtube.com/watch?v=JjEm2wjz0K0")

incredibles = media.Movie("Incredibles 2", "Bob Par (Mr. Incredible) is" +
                          "left to care for Jack-Jack while Helen" +
                          "(Elastigirl) is out saving the world.",
                          "https://i0.wp.com/teaser-trailer.com/wp-content/" +
                          "uploads/The-Incredibles-2-Teaser-Poster.jpg?ssl=1",
                          "https://www.youtube.com/watch?v=X6waHtSgCTc")

whiplash = media.Movie("WHIPLASH", "A promising young drummer enrolls at a" +
                       "cut-throat music conservatory where his dreams of" +
                       "greatness are mentored by an instructor who will" +
                       "stop at nothing to realize a student's potential.",
                       "https://images-na.ssl-images-amazon.com/images/" +
                       "M/MV5BOTVhMWQ5MDktMGE3OS00MjVlLWExZWYtMzY2MTg4ZGF" +
                       "iZDQ5L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182" +
                       "_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/" +
                       "watch?v=7d_jQycdQGo")
# puting them inside an array
movies = [guardians, john_wick, thor, bruce_almighty, incredibles, whiplash]

# passing the array to open_movies_page method in fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
