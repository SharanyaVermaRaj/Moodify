import webbrowser


def get_song_search_url(mood):
    mood_map = {
        "happy": "upbeat feel good songs",
        "sad": "emotional slow songs",
        "angry": "hard rock angry songs",
        "relaxed": "chill lofi music",
        "romantic": "romantic love songs",
        "study": "focus study music",
        "party": "party dance hits",
        "workout": "intense workout playlist"
    }
    mood = mood.lower().strip()
    if mood in mood_map:
        query = mood_map[mood].replace(" ", "+")
        return f"https://www.youtube.com/results?search_query={query}"
    return None


def main():
    print("🎵 Welcome to Moodify – Mood Based Music Suggester 🎵\n")
    print("Available moods: happy, sad, angry, relaxed, romantic, study, party, workout")

    mood = input("Enter your current mood: ")
    url = get_song_search_url(mood)

    if url:
        print(f"\nLaunching YouTube for mood: {mood.capitalize()} 🎶")
        webbrowser.open(url)
    else:
        print("❌ Oops! Mood not recognized. Try one from the list.")


if __name__ == "__main__":
    main()
