mood = input("How are you feeling? (happy/sad/stressed): ").lower()

music = {
    "happy": ["Party Song", "Dance Beat"],
    "sad": ["Slow Melody", "Soft Piano"],
    "stressed": ["Meditation Music", "Calm Waves"]
}

if mood in music:
    print("Recommended songs:")
    for song in music[mood]:
        print("-", song)
else:
    print("Mood not recognized")