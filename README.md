# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

The biggest learning moment during this project was seeing how a simple scoring system can behave like a real recommendation engine. By comparing features such as genre, mood, and energy, the system was able to produce results that often matched my expectations. This helped me understand that many recommendation systems begin with simple logic before becoming more advanced.

Using AI tools like Copilot helped me move faster when writing and organizing code, especially for generating function structures and explanations. However, I still needed to double-check the logic and test the results to make sure the recommendations behaved correctly. Sometimes the AI suggested code that worked technically but did not match the scoring logic I intended.

One surprising part of the project was how small changes in feature weights could noticeably change the recommendations. Even though the algorithm was simple, the results still felt meaningful because the scoring captured patterns between user preferences and song attributes.

If I continued developing this project, I would expand the dataset with many more songs and genres, include more features like lyrics or popularity, and experiment with machine learning approaches that learn user preferences automatically rather than using fixed weights.

---

## How The System Works

Explain your design in plain language.

This project simulates a simple **content-based music recommendation system**.  
The system recommends songs by comparing the attributes of each song with a user's music preferences. Each song receives a score based on how closely it matches the user’s taste profile, and the songs with the highest scores are recommended.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo

Each `Song` object contains several attributes that describe the musical characteristics of the track. These features help the system understand the "vibe" of the song.

The main features used in the system are:

- `genre` – the category of music (pop, lofi, rock, jazz, etc.)
- `mood` – the emotional tone of the song (happy, chill, intense, focused)
- `energy` – how intense or energetic the song is (value between 0 and 1)
- `tempo_bpm` – the speed of the song measured in beats per minute
- `valence` – how positive or happy the song sounds
- `danceability` – how suitable the song is for dancing
- `acousticness` – how acoustic or electronic the song sounds

These attributes help represent the overall style and feel of each song.

- What information does your `UserProfile` store

The `UserProfile` object stores the listener’s music preferences. These preferences describe the type of songs the user enjoys.

The profile includes:

- `preferred_genre`
- `preferred_mood`
- `preferred_energy`
- `preferred_tempo_bpm`
- `preferred_valence`

These values represent the user’s preferred musical style and vibe.

- How does your `Recommender` compute a score for each song

For each song in the dataset, the recommender calculates a **matching score** based on how closely the song matches the user’s preferences.

Two types of scoring are used:

**Exact match scoring (categorical features)**  
If the song’s genre or mood matches the user’s preference, the song receives full points.
Example: genre_score = 1 if song.genre == user.preferred_genre else 0
**Closeness scoring (numerical features)**  
For numerical features such as energy, valence, and tempo, the system rewards songs whose values are closer to the user’s preferred values.
Example: energy_score = 1 - abs(song.energy - user.preferred_energy)

Each feature score is multiplied by a **weight** representing how important that feature is. The weighted scores are then added together to produce the final score for the song.

- How do you choose which songs to recommend
You can include a simple diagram or bullet list if helpful.

Once every song receives a score:

1. The recommender calculates scores for all songs in the dataset.
2. Songs are sorted from **highest score to lowest score**.
3. The system returns the **top N songs** as recommendations.

### Algorithm Recipe

The recommender uses a point-based scoring system to evaluate each song.

Scoring rules:

- +2.0 points if the song's **genre** matches the user's favorite genre
- +1.0 point if the song's **mood** matches the user's preferred mood
- Energy similarity points based on how close the song’s energy is to the user’s target energy
- A small bonus if the song matches the user’s acoustic preference

Energy similarity is calculated using:

energy_score = max(0, 1 - abs(song_energy - target_energy))

The final score is the sum of these values. Songs are then ranked from highest score to lowest score.

### Potential Bias

This simplified recommender may introduce some bias:

- The system prioritizes **genre heavily**, which might ignore songs from other genres that still match the user's mood.
- The dataset is very small, so recommendations may repeat similar styles.
- The system only uses predefined features instead of learning from real user behavior.

Real recommendation systems often combine content-based filtering with collaborative filtering to reduce these limitations.

### Recommendation Flow
User Preferences
↓
Compare with Song Features
↓
Compute Weighted Score
↓
Rank Songs by Score
↓
Return Top Recommendations

### Note on Real-World Systems

Real-world recommendation systems used by platforms like Spotify or YouTube operate at a much larger scale and often combine **content-based filtering** with **collaborative filtering**, which learns from the listening behavior of millions of users. This simulation focuses on the core concept by using song attributes and a simple scoring algorithm to generate personalized recommendations.

## CLI Output Example

The recommender system can be run from the command line using:

python -m src.main

Below is an example of the recommendations generated for the default user profile (genre: pop, mood: happy, energy: 0.8).

![CLI Output](Images\CLI_output.png)

## Phase 4: Evaluation with Multiple Profiles

I tested the recommender with multiple user profiles to see how well the scoring logic handled different musical preferences.

### High-Energy Pop
![High-Energy Pop Output](Images\High_Energy_Pop.png)

### Chill Lofi
![Chill Lofi Output](Images\Chill_Lofi.png)

### Deep Intense Rock
![Deep Intense Rock Output](Images\Deep_Intense_Rock.png)

### Edge Case: Sad but High Energy
![Edge Case Output](Images\Sad_but_High_Energy.png)

## Accuracy and Surprises

For the default profile (genre = pop, mood = happy, energy = 0.8), the results felt correct. The song "Sunrise City" ranked first because it matched the user's preferred genre and mood, and its energy level was very close to the target value.

Other songs like "Gym Hero" also ranked high because they matched the pop genre and had similar energy levels. This shows that the recommender is correctly using the scoring rules to rank songs based on user preferences.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

### Experiment 1: Changing Feature Weights

I ran an experiment where I reduced the weight of the genre match and increased the importance of the energy similarity score. After this change, songs with energy levels closer to the user’s target moved higher in the rankings, even when the genre did not match exactly. This showed that the recommender becomes more flexible when numerical features like energy are emphasized.

### Experiment 2: Testing Different User Profiles

I tested several different user profiles including High-Energy Pop, Chill Lofi, Deep Intense Rock, and an edge case profile called Sad but High Energy. Each profile produced noticeably different recommendation lists. For example, the Chill Lofi profile ranked relaxing low-energy songs such as "Library Rain" and "Midnight Coding" at the top, while the High-Energy Pop profile favored songs like "Sunrise City" and "Gym Hero".

### Experiment 3: Edge Case Testing

I also tested a less common profile that requested sad songs with high energy. The system still returned a blues song that matched both the genre and mood, but it also recommended other high-energy songs from different genres. This experiment showed that when exact matches are limited, the system relies more heavily on energy similarity to produce recommendations.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

This recommender system has several limitations because it uses a very small catalog of songs. With only a limited number of tracks and genres available, the recommendations may repeat similar songs or fail to represent many types of music. The model also relies only on a few features such as genre, mood, energy, and acousticness. It does not understand lyrics, language, artist popularity, or the context in which someone listens to music.

Another limitation is that the scoring system uses fixed weights. This means the algorithm may over-favor certain features, such as genre or energy, depending on how the weights are set. As a result, some users may receive less diverse recommendations. Because of these limitations, this system is best viewed as a simple demonstration of how recommendation algorithms work rather than a full real-world music recommendation engine.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

This project helped me understand how recommendation systems turn user data and item features into predictions. By comparing song attributes like genre, mood, and energy with a user’s preferences, the system calculates a score for each song and ranks the best matches. Even though the algorithm was simple, the results often felt meaningful because the scoring captured patterns between user preferences and song characteristics.

I also learned that bias or unfairness can appear in recommendation systems depending on the data and scoring rules. For example, if the dataset contains more songs from certain genres, the system may recommend those genres more often. Similarly, if one feature like energy is weighted too heavily, it can dominate the ranking and reduce diversity in recommendations. This showed me that real-world recommendation systems must carefully balance features and datasets to avoid creating filter bubbles or unfair recommendations.

---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

