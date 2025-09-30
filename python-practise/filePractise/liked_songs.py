#using for loop and function to write a dictionary to a file.

songs = {
  'Bad Habits': 'Ed Sheeran',
  "I'm Just Ken": 'Ryan Gosling',
  'Mastermind': 'Taylor Swift',
  'Uptown Funk': 'Mark Ronson ft. Bruno Mars',
  'Ghost': 'Justin Bieber'
  }

def write_liked_songs_to_file(songs, file_name):
  with open(file_name, 'w') as file:
    file.write('Liked songs:\n')
    for song, artist in songs.items():
      file.write(f' {song} by {artist}\n')

write_liked_songs_to_file(songs, 'likedSongs')

#practising opening and closing file. Also reading them

try:
  file = open('example.txt', 'r')

finally:
  file.close()

with open('example.txt', 'r') as file:
  content = file.read()
  print(content)