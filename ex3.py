def read_songs(file_path):
    songs = []
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into components
            parts = line.strip().split()
            if len(parts) >= 3:
                singer = parts[0]
                title = ' '.join(parts[1:-1])  # Join all parts except the last one for the title
                count = int(parts[-1])  # The last part is the count
                songs.append((singer, title, count))
    return songs

def find_highest_played_song(songs, search_singer):
    highest_played_song = None
    highest_count = -1
    
    for singer, title, count in songs:
        if singer == search_singer and count > highest_count:
            highest_count = count
            highest_played_song = (singer, title, count)
    
    return highest_played_song

def main():
    file_path = 'songs.txt'
    songs = read_songs(file_path)
    
    search_singer = input("Enter the singer's name to search: ")
    result = find_highest_played_song(songs, search_singer)
    
    if result:
        singer, title, count = result
        print(f"Singer: {singer}, Title: '{title}', Count: {count}")
    else:
        print(f"No songs found for singer: {search_singer}")

if __name__ == "__main__":
    main()