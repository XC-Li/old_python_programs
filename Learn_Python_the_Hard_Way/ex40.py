class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"


thing = MyStuff()
thing.apple()
print thing.tangerine


class Song(object):
    def __init__(self, lyrics):
        print "I'll sing a song:"
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

# happy_bday.sing_me_a_song()

# bulls_on_parade.sing_me_a_song()
song_list = [happy_bday, bulls_on_parade]
for song_name in song_list:
    song_name.sing_me_a_song()
