import plistlib


def find_duplicates(file_name):
    print('Finding duplicate tracks in %s...' % file_name)
    plist = plistlib.load(open(file_name, 'rb'))
    # get the tracks from the Tracks dictionary
    tracks = plist['Tracks']
    # create a track name dictionary
    track_names = {}
    # iterate through the tracks
    for track_id,track in tracks.items():
        try:
            print(track_id,track)
        except:
            pass


if __name__ == '__main__':
    find_duplicates('../data/mymusic.xml')
