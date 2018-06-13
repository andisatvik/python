import webbrowser #line-15 

class Movie():
    
    def __init__(self, title, trailer_youtube_url, poster_image_url, cast, rating):
        # initializes all of the default parameters for this class' constructor
        
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.cast = cast
        self.rating = rating

    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
