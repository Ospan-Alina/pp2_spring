# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def truem(movie):
    return [movie.get('imdb', 0.0) > 5.5 for movie in movies]
        
print(truem(movies))


#2
def get_high_rated_movies(movies):
    high_rated_movies = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            high_rated_movies.append(movie)
    return high_rated_movies

high_rated_movies = get_high_rated_movies(movies)
print("Movies with IMDB score above 5.5:")
for movie in high_rated_movies:
    print(movie)


#3
def category(movies, category):
    return [movie for movie in movies if movie['category'] == category]

print(category(movies, 'Thriller'))

#4
def aveimdb(movies):
    if not movies:
        return 0
    total = sum(movie['imdb'] for movie in movies)
    return total / len(movies)

#5
def acategory(movies, category):
    categormov = (category(movies, category))
    return aveimdb(categormov)