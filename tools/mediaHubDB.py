import urllib.request, urllib.parse, json, os, sys
import xml.etree.ElementTree as ET
from mediaHub import secret

#reads xml updates database

proj_loc = os.path.dirname(os.path.realpath(__file__))
sys.path.append(proj_loc)
os.environ["DJANGO_SETTINGS_MODULE"] = "mediaHub.settings"
import django
django.setup()

from hub.models import MovieGenre, Movie

with urllib.request.urlopen("https://api.themoviedb.org/3/configuration?api_key="+secret.mdb_api) as url:
    data = json.loads(url.read().decode())
    #print (data)
    sec_img_url = (data['images']['secure_base_url'])

genres = {}
with urllib.request.urlopen("https://api.themoviedb.org/3/genre/movie/list?api_key="+secret.mdb_api+"&language=en-US") as url:
    data = json.loads(url.read().decode())
    for g in data['genres']:
        genres[g['id']] = g['name']

for g in genres.keys():
    MovieGenreOBJ, created = MovieGenre.objects.get_or_create(
        movieGenre_id=g,
        movieGenre_name=genres[g],
    )
    print(genres[g]+" Created = "+str(created))

# g=MovieGenre(movieGenre_id="80",movieGenre_name="crime")
# g.save()


tree = ET.parse('MoviesMediaData.xml')
root = tree.getroot()
movieData = []

for child in root:
    #print(child[0].text+" "+child[1].text)
    q = str(child[0].text).lower()
    y = child[1].text
    movieData.append(str(child[0].text).lower())
    surl = "https://api.themoviedb.org/3/search/movie?api_key="+secret.mdb_api+"&language=en-US&query="+\
       urllib.parse.quote_plus(q)+"&page=1&include_adult=false&primary_release_year="+urllib.parse.quote_plus(y)
    with urllib.request.urlopen(surl) as url:
        data = json.loads(url.read().decode())
        if data['results']:
            r = data['results'][0]

            MovieOBJ, created = Movie.objects.get_or_create(
                movieTitle=r['title'],
                movieRelYear=y,
                moviePoster=sec_img_url + "w500" + r['poster_path'],
                movieBackDrop=sec_img_url + "w1280" + r['backdrop_path'],
                movieOverview=r['overview'],
                tmdb_id=r['id']
            )
            print(r['title'] + " Created = " + str(created))

            for g in r['genre_ids']:
                MovieOBJ.genres.add(MovieGenre.objects.filter(movieGenre_id=g)[0])

            req = urllib.request.Request("https://api.themoviedb.org/3/movie/"+urllib.parse.quote_plus(str(r['id']))+"?api_key="+secret.mdb_api+"&language=en-US")
            try:
                with urllib.request.urlopen(req) as url:
                    data = json.loads(url.read().decode())
                    MovieOBJ.movieRuntime = data['runtime']
                    MovieOBJ.save()
            except urllib.error.URLError as e:
                print(e.reason)



        else:
            print(q+"   not found")
