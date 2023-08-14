# Emote Recommender [[presentation](https://docs.google.com/presentation/d/1-vDMK1vmKV7w2So8sbAKd6_02oleM0RGWwuZ70pL-uc/edit?usp=sharing)]

##### Motivation

* NLP on online livestream conversations needs further exploration 
* Important to understand and analyze language used in online communication 
* Twitch offers documentations of these live conversations 
* Understand impact of social media and anonymity on communication

##### Data

* Chat logs of past stream videos (VODs) from Twitch streamer Joe Bartolozzi
* Removed timestamps, usernames, bot commands, mentions, and links 
* Roughly 37,000 lines of chat from 8 VODs
* Labeled with one of five labels: joebartbusiness, joebartlongneck, joebartwebelieve, lul, catjam

##### Methods

* Labeled chat rows used to fine-tune Bidirectional Encoder Representations from Transformers (BERT) base model 
* To address overfitting we froze all embeddings layers and first five encoding layers
* Trained model used for classification on new individual lines of chat data

##### Results

**Accuracy:** 0.84
**Precision:** 0.75
**Recall:** 0.27
**F1-score:** 0.37
**AUROC:**
* joebartbusiness: 0.73298
* joebartlongneck: 0.71129
* joebartwebelieve: 0.7687
* lul: 0.74796
* catjam: 0.85962

##### Conclusion

* In-person and online communication differ: 
  * Online platforms afford anonymity 
  * Presence of different language patterns
  * Can extend to future research regarding online communication
* Help understand the impact of these online communities on sensitive topics
* Future steps:
  * Scale up data volume: more Twitch communities and more diverse genres
  * Expanding the model beyond classification to reveal patterns in content and speech of various communities

##### Poster

![poster](https://github.com/jjessicaf/CAIS-Proj-Emote/blob/main/poster.jpg?raw=true)