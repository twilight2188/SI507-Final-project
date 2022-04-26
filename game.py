class Game:
    def __init__(self, name="No Name",summary="No Summary", id=0,rating = 0, release_year = "No Release Year",generes ='No genre',metacritic = None,image = None,url = 'No Url', json = None):
        if(json is None):
            self.name=name
            self.genres = genres
            self.release_year=release_year
            self.id=id
            self.metacritic=metacritic
            self.rating = rating
            self.summary = summary
            self.image = image
            self.url = url
        else:
            self.name = json["name"]
            try:
                self.image = json['background_image']
            except:
                self.image = 'No image'
            try:
                self.url  = json['url']
            except:
                self.url = 'No Url'
            try:
                self.summary = json['summary']
            except:
                self.summary = "No Summary"
            try:
                self.genres = json['genres']
            except:
                self.genres = []
            try:
                self.rating = json['total_rating']
            except:
                self.rating = 0
            if self.genres == []:
                self.genres = 'N/A'
            try:
                self.release_year=json["released"][:4]
            except:
                try:
                    self.release_year=json["release_dates"][:4]
                except:
                    self.release_year=None
            self.id = json['id']
            try:
                self.metacritic=json['metacritic']
            except:
                self.metacritic = None
            if self.metacritic == None:
                self.metacritic = 'N/A'