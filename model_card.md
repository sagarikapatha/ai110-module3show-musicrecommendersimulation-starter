# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

**MoodBeat Finder**

MoodBeat Finder is a simple music recommendation system that suggests songs based on a user's preferred genre, mood, and energy level.

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This recommender system is designed to suggest songs that match a user's musical preferences based on simple features such as genre, mood, and energy level. The system compares these user preferences with the attributes of songs in the dataset and ranks songs that are most similar. It assumes that users can describe their musical taste using a few basic characteristics like preferred genre or desired energy level. 

This model is intended for classroom exploration to demonstrate how a basic content-based recommendation system works. It is not designed for real users or large-scale music recommendation platforms because the dataset is small and the scoring logic is simplified.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The model recommends songs by comparing user preferences with the features of each song in the dataset. Each song includes attributes such as genre, mood, energy level, and acousticness. The user profile also contains preferences like favorite genre, preferred mood, and a target energy level.

To generate recommendations, the system calculates a score for every song. Songs receive points when their genre matches the user’s preferred genre and when their mood matches the user’s preferred mood. The model also checks how close the song’s energy level is to the user’s target energy level. Songs with energy values closer to the user’s preference receive higher scores. In some cases, additional features such as acousticness may add small bonus points.

After calculating scores for all songs, the system ranks them from highest to lowest score. The top-ranked songs are returned as recommendations. Compared to the starter logic, I experimented with adjusting feature weights (for example increasing the importance of energy) to observe how the recommendations changed.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The recommender uses a small dataset of 20 songs stored in a CSV file. Each song contains several features such as title, artist, genre, mood, energy level, tempo, valence, danceability, and acousticness. The songs represent a mix of genres including pop, rock, lofi, ambient, electronic, folk, jazz, and blues, along with moods such as happy, chill, intense, relaxed, and sad.

I expanded the starter dataset by adding additional songs to increase variety in genres and moods. However, the dataset is still very small compared to real music platforms. Many aspects of musical taste are missing, such as lyrics, artist popularity, language, cultural preferences, and listening history. Because of these limitations, the recommendations are based only on a few audio features and may not fully represent a user's real music preferences.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition 

The system works well for users who have clear preferences for genre, mood, and energy level. For example, when testing the High-Energy Pop profile, the recommender correctly ranked songs like "Sunrise City" at the top because it matched the preferred genre, mood, and had a very similar energy level. 

The scoring system also captures useful patterns between energy and mood. For example, the Chill Lofi profile produced recommendations like "Library Rain" and "Midnight Coding", which are low-energy and relaxing songs that fit the user's expectations. 

Overall, the recommendations often matched my intuition when the user preferences were clear and aligned with the features available in the dataset. The system was able to distinguish between energetic listening preferences and calm, relaxed music styles.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

This recommender has several limitations because it uses a small dataset and a simple weighted scoring system. It only considers a few features such as genre, mood, energy, and acousticness, so it cannot capture other important parts of musical taste like lyrics, language, artist loyalty, or listening context. Some genres and moods are underrepresented in the dataset, which means users with those preferences may receive weaker or less diverse recommendations. During the experiment, I found that increasing the energy weight caused songs with similar energy to rank highly even when their genre did not match, showing that the system can overfit to one feature. This means the scoring logic may unintentionally favor users whose preferences are easy to represent with the current features, while giving less accurate results to users with more complex or mixed tastes.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I evaluated the recommender by testing several user profiles with different musical preferences. The profiles included High-Energy Pop, Chill Lofi, Deep Intense Rock, and an edge case profile called Sad but High Energy. For each profile, I looked at the top five recommended songs and checked whether they matched the expected genre, mood, and energy level.

For the High-Energy Pop profile, songs like "Sunrise City" ranked first because they matched both the pop genre and happy mood while having a very similar energy level. For the Chill Lofi profile, the system correctly recommended low-energy relaxing songs such as "Library Rain" and "Midnight Coding". The Deep Intense Rock profile also behaved as expected, prioritizing songs like "Storm Runner" that match both rock and intense energy.

One surprising result was that some songs from unrelated genres appeared in the recommendations when their energy values were very close to the user's target. This happened because the scoring system strongly rewards energy similarity. These comparisons helped confirm that the recommender follows the scoring rules, but also showed how feature weights influence the final rankings.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

In the future, the model could be improved by adding more song features such as lyrics, artist popularity, release year, and user listening history. These additional features would help capture more complex aspects of musical taste. Another improvement would be expanding the dataset to include many more songs and genres so the recommendations are more diverse. 

The system could also provide clearer explanations for why a song was recommended, such as highlighting which features contributed most to the score. Finally, the scoring system could be replaced with a machine learning approach that learns user preferences over time instead of relying on fixed weights.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

Building this project helped me understand how simple recommender systems work behind the scenes. I learned that even basic systems can generate useful recommendations by comparing user preferences with a few song features like genre, mood, and energy. One interesting thing I discovered was how strongly the feature weights influence the results—changing the weight of energy quickly changed which songs appeared at the top of the list. This made me realize that real music recommendation apps must carefully balance many signals to avoid repeating the same type of songs. It also changed how I think about music platforms like Spotify, because I now see that recommendations are often driven by patterns in data rather than human judgment.