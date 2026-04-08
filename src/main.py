"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.4},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.95},
        "Edge Case: Sad but High Energy": {"genre": "blues", "mood": "sad", "energy": 0.9},
    }

    for profile_name, user_prefs in profiles.items():
        print("\n" + "=" * 60)
        print(f"{profile_name}")
        print(f"Preferences: {user_prefs}")
        print("=" * 60)

        recommendations = recommend_songs(user_prefs, songs, k=5)

        for i, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"\n{i}. {song['title']} by {song['artist']}")
            print(f"   Genre : {song['genre']}")
            print(f"   Mood  : {song['mood']}")
            print(f"   Score : {score:.2f}")
            print(f"   Why   : {explanation}")

if __name__ == "__main__":
    main()
