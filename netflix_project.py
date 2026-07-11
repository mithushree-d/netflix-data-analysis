#Immporting libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading dataset
df = pd.read_csv("netflix_titles.csv")

#Analysing data
print(df.head(3))                             
print(df.shape)                                
print(df.info())                              
print(df.isnull().sum())                       
print(df.describe())                           

#Data Cleaning
print(df.duplicated().sum())                   
print(df.dtypes)


#Exploratory Data Analysis

#1. TV Shows VS Movies
ax = sns.countplot(x='type', data=df)
for container in ax.containers:
    ax.bar_label(container)

plt.title("TV Shows VS Movies on Netflix")
plt.xlabel("Content type")
plt.ylabel("Number of Titles")
plt.savefig("graphs/movies_vs_tvshows.png", dpi=300, bbox_inches='tight')
plt.show()


#2. Ratings distribution
rating = df['rating'].value_counts()
plt.figure(figsize=(10,6))
rating.plot(kind='bar')

plt.title("Distribution of netflix content rating")
plt.xlabel("Ratings")
plt.ylabel("Number of titles")

#Adding values on top of bars
for i, value in enumerate(rating):
    plt.text(i, value+20, str(value), ha='center')

plt.savefig("graphs/ratings_distribution.png", dpi=300, bbox_inches='tight')
plt.show()



#3. highest netflix content in a year
plt.figure(figsize=(12,6))

plt.plot(df['release_year'].value_counts().sort_index(), marker='o')
plt.title("Highest Distribution of netflix content")
plt.xlabel("Release Year")
plt.ylabel("Number of titles")

plt.savefig("graphs/release_year_distribution.png", dpi=300, bbox_inches='tight')
plt.show()



#4. Country with highest netflix content
# explode() is used to seperate the strings

top_countries = (df['country'].dropna().str.split(" , ").explode().value_counts().head(10))
plt.figure(figsize=(6,4))

bars = plt.bar(top_countries.index, top_countries.values)
plt.title("Country with highest netflix content.")
plt.xlabel("Country")
plt.ylabel("Number of titles")

plt.bar_label(bars, padding=3)
plt.xticks(rotation=30)

plt.savefig("graphs/country_with_highest_content.png", dpi=300, bbox_inches='tight')
plt.show()



#5. Top 10 directors
top_directors = (df['director'].dropna().str.split(" , ").explode().value_counts().head(10))

plt.figure(figsize=(6,4))
bars = plt.barh(top_directors.index, top_directors.values)

plt.title("Top 10 directors")
plt.xlabel("Number of titles")
plt.ylabel("Directors")

plt.bar_label(bars, padding=3)
plt.savefig("graphs/top_directors.png")
plt.show()


#6. Top 10 genres
top_genres = (df['listed_in'].str.split(" , ").explode().value_counts().head(10))

plt.figure(figsize=(6,4))
bars = plt.barh(top_genres.index, top_genres.values)

plt.title("Top 10 Genres")
plt.xlabel("Number of titles")
plt.ylabel("Genre")

plt.bar_label(bars)
plt.yticks(rotation=45)
plt.savefig("graphs/top_genres.png", dpi=300, bbox_inches='tight')
plt.show()


#7. Distribution of movie duration

movies = df[df['type'] == 'Movie'].copy()
movies = movies.dropna(subset=['duration'])

duration = (movies['duration'].str.replace("min", "",regex=False).astype(int))

plt.figure(figsize=(6,4))
plt.hist(duration, bins=30, edgecolor='black')
plt.title("Duration of movie")
plt.xlabel("Duration")
plt.ylabel("Number of titles")

plt.savefig("graphs/Duration_of_movies.png", dpi=300,bbox_inches='tight')
plt.show()



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
