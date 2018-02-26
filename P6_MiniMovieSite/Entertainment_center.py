import media
import fresh_tomatoes


wonder_woman = media.Movie("Wonder Woman",
                           "Wonder Woman, the story of Diana is told, who is the daughter of Hippolyta and grows up on the Amazon island of Themyscira. After American pilot and spy Steve Trevor crashes offshore of the island and is rescued by her, he tells the Amazons about the ongoing World War. Diana then leaves her home in order to end the conflict.",
                           "/Users/KarthikChowdary/Documents/Python/P6_MiniMovieSite/Images/ww.jpg",
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo")

suicide_squad = media.Movie("Suicide Squad",
                            "Suicide Squad, a secret government agency led by Amanda Waller recruits imprisoned supervillains to execute dangerous black ops missions and save the world from a powerful threat, in exchange for reduced sentences.",
                            "/Users/KarthikChowdary/Documents/Python/P6_MiniMovieSite/Images/ss.jpg",
                            "https://www.youtube.com/watch?v=CmRih_VtVAs")

batman_v_superman = media.Movie("Batman Vs Superman",
                                "Batman Vs Superman is the first live-action film to feature Batman and Superman together, as well as the first live-action cinematic portrayal of Wonder Woman. In the film, criminal mastermind Lex Luthor (Eisenberg) manipulates Batman (Affleck) into a preemptive battle with Superman (Cavill), whom Luthor is obsessed with defeating.",
                                "/Users/KarthikChowdary/Documents/Python/P6_MiniMovieSite/Images/bvs.jpg",
                                "https://www.youtube.com/watch?v=fis-9Zqu2Ro")

toy_story = media.Movie("Toy Story",
                        "Toy Story was the first feature-length computer-animated film and the first feature film produced by Pixar. Taking place in a world where anthropomorphic toys pretend to be lifeless whenever humans are present, the film's plot focuses on the relationship between Woody, an old-fashioned pullstring cowboy doll, and Buzz Lightyear, an astronaut action figure",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "The film is set in the mid-22nd century, when humans are colonizing Pandora, a lush habitable moon of a gas giant in the Alpha Centauri star system, in order to mine the mineral unobtanium,[9][10] a room-temperature superconductor.[11] The expansion of the mining colony threatens the continued existence of a local tribe of Na'vi – a humanoid species indigenous to Pandora.",
                     "/Users/KarthikChowdary/Documents/Python/P6_MiniMovieSite/Images/avatar.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

prestige = media.Movie("Prestige",
                       "Its story follows Robert Angier and Alfred Borden, rival stage magicians in London at the end of the 19th century. Obsessed with creating the best stage illusion, they engage in competitive one-upmanship with tragic results.",
                       "/Users/KarthikChowdary/Documents/Python/P6_MiniMovieSite/Images/prestige.jpg",
                       "https://www.youtube.com/watch?v=ijXruSzfGEc")

movies = [wonder_woman, batman_v_superman, suicide_squad, avatar, prestige, toy_story]
fresh_tomatoes.open_movies_page(movies)
