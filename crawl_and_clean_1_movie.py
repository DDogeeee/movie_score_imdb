import imdb
import pandas as pd
import numpy as np 
moviesDB = imdb.IMDb()

# print(dir(moviesDB))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_defModFunct', '_getRefs', '_get_infoset', '_get_keyword', '_get_list_content', '_get_movie_list', '_get_real_characterID', '_get_real_companyID', '_get_real_movieID', '_get_real_personID', '_get_search_content', '_get_search_movie_advanced_content', '_get_top_bottom_movies', '_http_logger', '_keywordsResults', '_mdparse', '_normalize_characterID', '_normalize_companyID', '_normalize_movieID', '_normalize_personID', '_purge_seasons_data', '_reraise_exceptions', '_results', '_retrieve', '_searchIMDb', '_search_character', '_search_company', '_search_episode', '_search_keyword', '_search_movie', '_search_movie_advanced', '_search_person', 'accessSystem', 'character2imdbID', 'compProxy', 'company2imdbID', 'del_cookies', 'do_adult_search', 'get_bottom100_movies', 'get_character', 'get_character_infoset', 'get_company', 'get_company_infoset', 'get_company_main', 'get_episode', 'get_imdbCharacterID', 'get_imdbCompanyID', 'get_imdbID', 'get_imdbMovieID', 'get_imdbPersonID', 'get_imdbURL', 'get_keyword', 'get_movie', 'get_movie_airing', 'get_movie_akas', 'get_movie_alternate_versions', 'get_movie_awards', 'get_movie_connections', 'get_movie_crazy_credits', 'get_movie_critic_reviews', 'get_movie_episodes', 'get_movie_external_reviews', 'get_movie_external_sites', 'get_movie_faqs', 'get_movie_full_credits', 'get_movie_goofs', 'get_movie_infoset', 'get_movie_keywords', 'get_movie_list', 'get_movie_locations', 'get_movie_main', 'get_movie_misc_sites', 'get_movie_news', 'get_movie_official_sites', 'get_movie_parents_guide', 'get_movie_photo_sites', 'get_movie_plot', 'get_movie_quotes', 'get_movie_recommendations', 'get_movie_release_dates', 'get_movie_release_info', 'get_movie_reviews', 'get_movie_sound_clips', 'get_movie_soundtrack', 'get_movie_synopsis', 'get_movie_taglines', 'get_movie_technical', 'get_movie_trivia', 'get_movie_tv_schedule', 'get_movie_video_clips', 'get_movie_vote_details', 'get_person', 'get_person_awards', 'get_person_biography', 'get_person_filmography', 'get_person_genres_links', 'get_person_infoset', 'get_person_keywords_links', 'get_person_main', 'get_person_news', 'get_person_official_sites', 'get_person_other_works', 'get_person_publicity', 'get_popular100_movies', 'get_popular100_tv', 'get_proxy', 'get_special_methods', 'get_top250_indian_movies', 'get_top250_movies', 'get_top250_tv', 'listProxy', 'mProxy', 'name2imdbID', 'new_character', 'new_company', 'new_movie', 'new_person', 'pProxy', 'scompProxy', 'search_character', 'search_company', 'search_episode', 'search_keyword', 'search_movie', 'search_movie_advanced', 'search_person', 'set_cookies', 'set_imdb_urls', 'set_proxy', 'set_timeout', 'skProxy', 'smProxy', 'smaProxy', 'spProxy', 'title2imdbID', 'topBottomProxy', 'update', 'update_series_seasons', 'urlOpener', 'urls']

table = pd.DataFrame()
title_arr =[]
year_arr = []
rating_arr = []
director_arr = []
cast_arr = []
genre_arr = []
plot_arr = []
actor_arr = []
keyword_arr = []
language_arr = []
budget_arr = []
gross_arr = []
runtime_arr = []
##############################
akas_arr = []
animation_department_arr = []
art_department_arr = []
art_directors_arr = []
aspect_ratio_arr = []
assistant_directors_arr = []
box_office_arr = []
camera_department_arr = []
canonical_title_arr = []

casting_department_arr = []
casting_directors_arr = []
certificates_arr = []
cinematographers_arr = []
color_info_arr = []
composers_arr = []
costume_departmen_arr = []
costume_designers_arr = []
countries_arr = []
country_codes_arr = []
cover_url_arr = []
director_arr = []
directors_arr = []
distributors_arr = []
editorial_department_arr = []
editors_arr = []
full_size_cover_url_arr = []
genres_arr = []
kind_arr = []
language_codes_arr = []

location_management_arr = []
long_imdb_canonical_title_arr = []
long_imdb_title_arr = []
make_up_department_arr = []
miscellaneous_arr = []
music_department_arr = []
original_air_date_arr = []
other_companies_arr = []

plot_outline_arr = []
producers_arr = []
production_companies_arr = []
production_designers_arr = []
production_managers_arr = []

script_department_arr = []
set_decorators_arr = []
smart_canonical_title_arr = []
smart_long_imdb_canonical_title_arr = []
sound_department_arr = []
sound_mix_arr = []
special_effects_arr = []
special_effects_companies_arr = []
stunts_arr = []
synopsis_arr = []

top_250_rank_arr = []
transportation_department_arr = []
visual_effects_arr = []
votes_arr = []
writer_arr = []
writers_arr = []

###########################
movie_names = input("Please enter a movie name: ")
movie_names = str(movie_names)
# print(type(movie_names))

# movie_names = "Operation Fortune: Ruse de guerre"
movies = moviesDB.search_movie(movie_names)
movie = movies[0]
if(1>0):
    id = movie.getID()
    movie= moviesDB.get_movie(id)


    title = movie['title']

    try:
        year = movie['year']
    except:
        year = ''
    try:
        rating = movie['rating']
    except:
        rating = ''
    try:
        directors = movie['directors']
    except:
        directors = ''
    try:
        cast = movie['cast']
    except:
        cast =' '

    try:
        language = movie['language']
    except:
        language = ''

    # print(f'{title} - {year}')
    # print(rating)
    #
    # direcSTR = ', '.join(map(str,directors))
    # print(f'directors:{direcSTR}')
    #
    # ACTORSTR = ', '.join(map(str,cast))
    # print(f'actors:{ACTORSTR}')

    try:
        genre = movie['genre']
    except:
        genre=''
    # print(f'genres:{genre}')
    try:
        plot = movie['plot']
    except:
        plot =''
    # print(plot)
    # try:
    #     akas = movie['akas']
    # except:
    #     akas = ''
    #     print(akas)

    try:
        keyword = movie['keyword']
    except:
        keyword =''
    try:
        runtime = movie['runtime']
    except:
        runtime = ''

#################################
    try:
        akas = movie['akas']
    except:
        akas = None
    try:
        animation_department = movie['animation department']
    except:
        animation_department = ''
    try:
        art_department = movie['art department']
    except:
        art_department = ''
    try:
        art_directors = movie['art directors']
    except:
        art_directors = ''
    try:
        aspect_ratio = movie['aspect ratio']
    except:
        aspect_ratio = ''
    try:
        assistant_directors = movie['assistant directors']
    except:
        assistant_directors = ''
    try:
        box_office = movie['box office']
    except:
        box_office = ''
    try:
        camera_department = movie['camera department']
    except:
        camera_department = ''
    try:
        canonical_title = movie['canonical title']
    except:
        canonical_title = ''

    try:
        casting_department = movie['casting department']
    except:
        casting_department = ''
    try:
        casting_directors = movie['casting directors']
    except:
        casting_directors = ''
    try:
        certificates = movie['certificates']
    except:
        certificates = ''
    try:
        cinematographers = movie['cinematographers']
    except:
        cinematographers = ''
    try:
        color_info = movie['color info']
    except:
        color_info = ''
    try:
        composers = movie['composers']
    except:
        composers = ''
    try:
        costume_departmen = movie['costume departmen']
    except:
        costume_departmen = ''
    try:
        costume_designers = movie['costume designers']
    except:
        costume_designers = ''
    try:
        countries = movie['countries']
    except:
        countries = ''
    try:
        country_codes = movie['country codes']
    except:
        country_codes = ''
    try:
        cover_url = movie['cover url']
    except:
        cover_url = ''

    try:
        distributors = movie['distributors']
    except:
        distributors = ''
    try:
        editorial_department = movie['editorial department']
    except:
        editorial_department = ''
    try:
        editors = movie['editors']
    except:
        editors = ''
    try:
        full_size_cover_url = movie['full-size cover url']
    except:
        full_size_cover_url = ''

    try:
        kind = movie['kind']
    except:
        kind = ''
    try:
        language_codes = movie['language codes']
    except:
        language_codes = ''

    try:
        location_management = movie['location management']
    except:
        location_management = ''
    try:
        long_imdb_canonical_title = movie['long imdb canonical title']
    except:
        long_imdb_canonical_title = ''
    try:
        long_imdb_title = movie['long imdb title']
    except:
        long_imdb_title = ''
    try:
        make_up_department = movie['make up department']
    except:
        make_up_department = ''
    try:
        miscellaneous = movie['miscellaneous']
    except:
        miscellaneous = ''
    try:
        music_department = movie['music department']
    except:
        music_department = ''
    try:
        original_air_date = movie['original air date']
    except:
        original_air_date = ''
    try:
        other_companies = movie['other companies']
    except:
        other_companies = ''

    try:
        plot_outline = movie['plot outline']
    except:
        plot_outline = ''
    try:
        producers = movie['producers']
    except:
        producers = ''
    try:
        production_companies = movie['production companies']
    except:
        production_companies = ''
    try:
        production_designers = movie['production designers']
    except:
        production_designers = ''
    try:
        production_managers = movie['production managers']
    except:
        production_managers = ''

    try:
        script_department = movie['script department']
    except:
        script_department = ''
    try:
        set_decorators = movie['set decorators']
    except:
        set_decorators = ''
    try:
        smart_canonical_title = movie['smart canonical title']
    except:
        smart_canonical_title = ''
    try:
        smart_long_imdb_canonical_title = movie['smart long imdb canonical title']
    except:
        smart_long_imdb_canonical_title = ''
    try:
        sound_department = movie['sound department']
    except:
        sound_department = ''
    try:
        sound_mix = movie['sound mix']
    except:
        sound_mix = ''
    try:
        special_effects = movie['special effects']
    except:
        special_effects = ''
    try:
        special_effects_companies = movie['special effects companies']
    except:
        special_effects_companies = ''
    try:
        stunts = movie['stunts']
    except:
        stunts = ''
    try:
        synopsis = movie['synopsis']
    except:
        synopsis = ''

    try:
        top_250_rank = movie['top 250 rank']
    except:
        top_250_rank = ''
    try:
        transportation_department = movie['transportation department']
    except:
        transportation_department = ''
    try:
        visual_effects = movie['visual effects']
    except:
        visual_effects = ''
    try:
        votes = movie['votes']
    except:
        votes = ''
    try:
        writer = movie['writer']
    except:
        writer = ''
    try:
        writers = movie['writers']
    except:
        writers = ''

#######################


    try:
        budget = movie['box office']['Budget']
    except:
        budget = 'none'

    try:
        gross = movie['box office']['Cumulative Worldwide Gross']
    except:
        gross = 'none'
# movie_names = 'avengers'
# movies = moviesDB.search_movie(movie_names)
# # for movie in movies:
# id =movies[0].getID()
# movie = moviesDB.get_movie_release_info(id)
# print(id, movie)
    title_arr.append(title)
    year_arr.append(year)
    rating_arr.append(rating)
    director_arr.append(str(directors))
    cast_arr.append(str(cast))
    genre_arr.append(str(genre))
    plot_arr.append(str(plot))
    keyword_arr.append(str(keyword))
    language_arr.append(str(language))
    budget_arr.append((budget))
    gross_arr.append(str(gross))
#################
    akas_arr.append(str(akas))
    animation_department_arr.append(str(animation_department))
    art_department_arr.append(str(art_department))
    art_directors_arr.append(str(art_directors))
    aspect_ratio_arr.append(str(aspect_ratio))
    assistant_directors_arr.append(str(assistant_directors))
    box_office_arr.append(str(box_office))
    camera_department_arr.append(str(camera_department))
    canonical_title_arr.append(str(canonical_title))

    casting_department_arr.append(str(casting_department))
    casting_directors_arr.append(str(casting_directors))
    certificates_arr.append(str(certificates))
    cinematographers_arr.append(str(cinematographers))
    color_info_arr.append(str(color_info))
    composers_arr.append(str(composers))
    costume_departmen_arr.append(str(costume_departmen))
    costume_designers_arr.append(str(costume_designers))
    countries_arr.append(str(countries))
    country_codes_arr.append(str(country_codes))
    cover_url_arr.append(str(cover_url))

    distributors_arr.append(str(distributors))
    editorial_department_arr.append(str(editorial_department))
    editors_arr.append(str(editors))
    full_size_cover_url_arr.append(str(full_size_cover_url))

    kind_arr.append(str(kind))
    language_codes_arr.append(str(language_codes))

    location_management_arr.append(str(location_management))
    long_imdb_canonical_title_arr.append(str(long_imdb_canonical_title))
    long_imdb_title_arr.append(str(long_imdb_title))
    make_up_department_arr.append(str(make_up_department))
    miscellaneous_arr.append(str(miscellaneous))
    music_department_arr.append(str(music_department))
    original_air_date_arr.append(str(original_air_date))
    other_companies_arr.append(str(other_companies))

    plot_outline_arr.append(str(plot_outline))
    producers_arr.append(str(producers))
    production_companies_arr.append(str(production_companies))
    production_designers_arr.append(str(production_designers))
    production_managers_arr.append(str(production_managers))

    script_department_arr.append(str(script_department))
    set_decorators_arr.append(str(set_decorators))
    smart_canonical_title_arr.append(str(smart_canonical_title))
    smart_long_imdb_canonical_title_arr.append(str(smart_long_imdb_canonical_title))
    sound_department_arr.append(str(sound_department))
    sound_mix_arr.append(str(sound_mix))
    special_effects_arr.append(str(special_effects))
    special_effects_companies_arr.append(str(special_effects_companies))
    stunts_arr.append(str(stunts))
    synopsis_arr.append(str(synopsis))

    top_250_rank_arr.append(str(top_250_rank))
    transportation_department_arr.append(str(transportation_department))
    visual_effects_arr.append(str(visual_effects))
    votes_arr.append(str(votes))
    writer_arr.append(str(writer))
    writers_arr.append(str(writers))
    runtime_arr.append(str(runtime))
#########################

# for i, item in enumerate(title_arr):
for i, item in enumerate(title_arr):
    table.loc[i, 'title'] = title_arr[i]
    try:
        table.loc[i, 'year'] = year_arr[i]
    except:
        table.loc[i, 'year'] = None
    try:
        table.loc[i, 'rating'] = rating_arr[i]
    except:
        table.loc[i, 'rating'] = None
    try:
        table.loc[i, 'director'] = director_arr[i]
    except:
        table.loc[i, 'director'] = None
    try:
        table.loc[i, 'cast'] = cast_arr[i]
    except:
        table.loc[i, 'cast'] = None
    try:
        table.loc[i, 'genre'] = genre_arr[i]
    except:
        table.loc[i, 'genre'] = None
    try:
        table.loc[i, 'plot'] = plot_arr[i]
    except:
        table.loc[i, 'plot'] = None
    try:
        table.loc[i, 'keyword'] = keyword_arr[i]
    except:
        table.loc[i, 'keyword'] =None
    try:
        table.loc[i, 'language'] = language_arr[i]
    except:
        table.loc[i, 'language'] =None
    try:
        table.loc[i, 'budget'] = budget_arr[i]
    except:
        table.loc[i, 'budget'] = None
    try:
        table.loc[i, 'gross'] = gross_arr[i]
    except:
        table.loc[i, 'gross'] = None
    try:
        table.loc[i, 'runtime'] = runtime_arr[i]
    except:
        table.loc[i, 'runtime'] = None
#################################################
    try:
        table.loc[i, 'akas'] = akas_arr[i]
    except:
        table.loc[i, 'akas'] = None
    try:
        table.loc[i, 'animation_department'] = animation_department_arr[i]
    except:
        table.loc[i, 'animation_department'] = None
    try:
        table.loc[i, 'art_department'] = art_department_arr[i]
    except:
        table.loc[i, 'art_department'] = None
    try:
        table.loc[i, 'art_directors'] = art_directors_arr[i]
    except:
        table.loc[i, 'art_directors'] = None
    try:
        table.loc[i, 'aspect_ratio'] = aspect_ratio_arr[i]
    except:
        table.loc[i, 'aspect_ratio'] =  None
    try:
        table.loc[i, 'assistant_directors'] = assistant_directors_arr[i]
    except:
        table.loc[i, 'assistant_directors'] = None
    try:
        table.loc[i, 'box_office'] = box_office_arr[i]
    except:
        table.loc[i, 'box_office'] = None
    try:
        table.loc[i, 'camera_department'] = camera_department_arr[i]
    except:
        table.loc[i, 'camera_department'] = None
    try:
        table.loc[i, 'canonical_title'] = canonical_title_arr[i]
    except:
        table.loc[i, 'canonical_title'] = None
    try:
        table.loc[i, 'casting_department'] = casting_department_arr[i]
    except:
        table.loc[i, 'casting_department'] = None
    try:
        table.loc[i, 'casting_directors'] = casting_directors_arr[i]
    except:
        table.loc[i, 'casting_directors'] = None
    try:
        table.loc[i, 'certificates'] = certificates_arr[i]
    except:
        table.loc[i, 'certificates'] = None
    try:
        table.loc[i, 'cinematographers'] = cinematographers_arr[i]
    except:
        table.loc[i, 'cinematographers'] = None
    try:
        table.loc[i, 'color_info'] = color_info_arr[i]
    except:
        table.loc[i, 'color_info'] = None
    try:
        table.loc[i, 'composers'] = composers_arr[i]
    except:
        table.loc[i, 'composers'] = None
    try:
        table.loc[i, 'costume_departmen'] = costume_departmen_arr[i]
    except:
        table.loc[i, 'costume_departmen'] = None
    try:
        table.loc[i, 'costume_designers'] = costume_designers_arr[i]
    except:
        table.loc[i, 'costume_designers'] = None
    try:
        table.loc[i, 'countries'] = countries_arr[i]
    except:
        table.loc[i, 'countries'] =  None
    try:
        table.loc[i, 'country_codes'] = country_codes_arr[i]
    except:
        table.loc[i, 'country_codes'] = None
    try:
        table.loc[i, 'cover_url'] = cover_url_arr[i]
    except:
        table.loc[i, 'cover_url'] = None
    try:
        table.loc[i, 'distributors'] = distributors_arr[i]
    except:
        table.loc[i, 'distributors'] = None
    try:
        table.loc[i, 'editorial_department'] = editorial_department_arr[i]
    except:
        table.loc[i, 'editorial_department'] = None
    try:
        table.loc[i, 'editors'] = editors_arr[i]
    except:
        table.loc[i, 'editors'] = None
    try:
        table.loc[i, 'full_size_cover_url'] = full_size_cover_url_arr[i]
    except:
        table.loc[i, 'full_size_cover_url'] = None
    try:
        table.loc[i, 'kind'] = kind_arr[i]
    except:
        table.loc[i, 'kind'] = None
    try:
        table.loc[i, 'language_codes'] = language_codes_arr[i]
    except:
        table.loc[i, 'language_codes'] =None
    try:
        table.loc[i, 'location_management'] = location_management_arr[i]
    except:
        table.loc[i, 'location_management'] =None
    try:
        table.loc[i, 'long_imdb_canonical_title'] = long_imdb_canonical_title_arr[i]
    except:
        table.loc[i, 'long_imdb_canonical_title'] =None
    try:
        table.loc[i, 'long_imdb_title'] = long_imdb_title_arr[i]
    except:
        table.loc[i, 'long_imdb_title'] =None
    try:
        table.loc[i, 'make_up_department'] = make_up_department_arr[i]
    except:
        table.loc[i, 'make_up_department'] =None
    try:
        table.loc[i, 'miscellaneous'] = miscellaneous_arr[i]
    except:
        table.loc[i, 'miscellaneous'] =None
    try:
        table.loc[i, 'music_department'] = music_department_arr[i]
    except:
        table.loc[i, 'music_department'] =None
    try:
        table.loc[i, 'original_air_date'] = original_air_date_arr[i]
    except:
        table.loc[i, 'original_air_date'] =None
    try:
        table.loc[i, 'other_companies'] = other_companies_arr[i]
    except:
        table.loc[i, 'other_companies'] =None
    try:
        table.loc[i, 'plot_outline'] = plot_outline_arr[i]
    except:
        table.loc[i, 'plot_outline'] =None
    try:
        table.loc[i, 'producers'] = producers_arr[i]
    except:
        table.loc[i, 'producers'] =None
    try:
        table.loc[i, 'production_companies'] = production_companies_arr[i]
    except:
        table.loc[i, 'production_companies'] =None
    try:
        table.loc[i, 'production_designers'] = production_designers_arr[i]
    except:
        table.loc[i, 'production_designers'] =None
    try:
        table.loc[i, 'production_managers'] = production_managers_arr[i]
    except:
        table.loc[i, 'production_managers'] =None

    try:
        table.loc[i, 'script_department'] = script_department_arr[i]
    except:
        table.loc[i, 'script_department'] =None
    try:
        table.loc[i, 'set_decorators'] = set_decorators_arr[i]
    except:
        table.loc[i, 'set_decorators'] =None
    try:
        table.loc[i, 'smart_canonical_title'] = smart_canonical_title_arr[i]
    except:
        table.loc[i, 'smart_canonical_title'] =None
    try:
        table.loc[i, 'smart_long_imdb_canonical_title'] = smart_long_imdb_canonical_title_arr[i]
    except:
        table.loc[i, 'smart_long_imdb_canonical_title'] =None
    try:
        table.loc[i, 'sound_department'] = sound_department_arr[i]
    except:
        table.loc[i, 'sound_department'] =None
    try:
        table.loc[i, 'sound_mix'] = sound_mix_arr[i]
    except:
        table.loc[i, 'sound_mix'] =None
    try:
        table.loc[i, 'special_effects'] = special_effects_arr[i]
    except:
        table.loc[i, 'special_effects'] =None
    try:
        table.loc[i, 'special_effects_companies'] = special_effects_companies_arr[i]
    except:
        table.loc[i, 'special_effects_companies'] =None
    try:
        table.loc[i, 'stunts'] = stunts_arr[i]
    except:
        table.loc[i, 'stunts'] =None
    try:
        table.loc[i, 'synopsis'] = synopsis_arr[i]
    except:
        table.loc[i, 'synopsis'] =None

    try:
        table.loc[i, 'top_250_rank'] = top_250_rank_arr[i]
    except:
        table.loc[i, 'top_250_rank'] =None
    try:
        table.loc[i, 'transportation_department'] = transportation_department_arr[i]
    except:
        table.loc[i, 'transportation_department'] =None
    try:
        table.loc[i, 'visual_effects'] = visual_effects_arr[i]
    except:
        table.loc[i, 'visual_effects'] =None
    try:
        table.loc[i, 'votes'] = votes_arr[i]
    except:
        table.loc[i, 'votes'] =None
    try:
        table.loc[i, 'writers'] = writers_arr[i]
    except:
        table.loc[i, 'writers'] =None

################################################
# table.to_csv('1_movie.csv')

df = table

def get_director_id(s):
    s1 = s
    s2 = 'Person id:'
    start = s1.index(s2) + len(s2)
    if s1[start:start+7].isnumeric():
        return s1[start:start+7]
    else:
        return np.nan

def get_director_name(s):
    s1 = s
    s2 = 'name:_'
    s3 = '_>]'
    start = s1.index(s2) + len(s2)
    end = s1.index(s3)
    try:
        return s1[start:end]
    except:
        return np.nan
    
def find(s, ch):
    l = []
    i = s.find(ch)
    while i!= -1:
        l.append(i)
        i = s.find(ch,i+1)
    return l

def get_cast_ids(s):
    start = find(s, '<Person id:')
    end = find(s, '[http]')
    id_list = []
    for i in range(len(end)):
        id_list.append(s[start[i]+11:end[i]])
    return id_list

def get_cast_names(s):
    start = find(s, 'name:_')
    end = find(s, '_>')
    name_list = []
    for i in range(len(end)):
        name_list.append(s[start[i]+6:end[i]])
    return name_list

def get_budget(s):
    start = s.find('$')
    end = s.find(' ')
    return int(s[start+1:end].replace(',',''))

def apply_genre(s):
    s = s.replace('\'','').replace('[','').replace(']','').split(sep = ', ')
    return s

def get_date(s):
    day = s[0:2]
    month = s[3:6]
    return day, month

def get_country(s):
    start = find(s, '(')
    end = find(s, ')')
    return s[start[0]+1:end[0]]

def get_runtime(s):
    s2 = s[2:]
    s3 = s2[:len(s2)-2]
    return int(s3)

for i in df.index:
    s = df.loc[i,'director']
    try:
        df.loc[i,'director_name'] = get_director_name(s)
    except:
        df.loc[i,'director_name'] = np.nan
    try:
        df.loc[i,'director_id'] = get_director_id(s)
    except:
        df.loc[i,'director_name'] = np.nan
        
    s = df.loc[i,'cast']
    try:
        df.loc[i,'cast_names'] = [[get_cast_names(s)]]
    except:
        df.loc[i,'cast_names'] = np.nan
    try:
        df.loc[i,'cast_ids'] = [[get_cast_ids(s)]]
    except:
        df.loc[i,'cast_names'] = np.nan

for i in df.index:
    s = df.loc[i,'original_air_date']
    # print(s)
    try:
        df.loc[i,'country'] = get_country(s)
        d,m = get_date(s)
        df.loc[i,'day'] = d 
        df.loc[i,'month'] = m
    except:
        df.loc[i,'country'] = np.nan
        df.loc[i,'day'] = np.nan
        df.loc[i,'month'] = np.nan

for i in df.index:
    try:
        s = df.loc[i, 'runtime']
        df.loc[i, 'runtime'] = get_runtime(s)
    except:
        s = np.nan

for i in df.index:
    try:
        s = df.loc[i, 'color_info']
        if "Black" in s:
            df.loc[i, 'color_info'] = "Black and White"
        if "Color" in s:
            df.loc[i, 'color_info'] = "Color"
    except:
        s = np.nan

for i in df.index:
    try:
        s = df.loc[i, 'sound_mix']
        if "Silent" in s:
            df.loc[i, 'sound_mix'] = "Silent"
        elif "Mono" in s:
            df.loc[i, 'sound_mix'] = "Mono"
        elif "Dolby" in s:
            df.loc[i, 'sound_mix'] = "Dolby"
        elif "DTS" in s:
            df.loc[i, 'sound_mix'] = "DTS"
        else:
            df.loc[i, 'sound_mix'] = "Others"
    except:
        s = np.nan

df = df[['title','year','rating','runtime','kind','color_info','sound_mix','director_name', 'genre','director_id', 'cast_names', 
         'cast_ids','votes','country','day','month']]

df.to_csv('1_movie_preprocessing.csv', index =False)

# print(moviesDB.get_movie_infoset())
# movies = moviesDB.search_movie('avenger')
# name = moviesDB.get_movie_keywords(movies)
# print(name)