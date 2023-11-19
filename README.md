# AromaHarmonics - Perfume description text to music, music to image

## 1. Introduction
### Project Overview:
That is a 'Text-to-Music-to-Image' project that captures perfume data, especially the description of each perfume, and uses the description as the prompts to generate sound and image. Designed to make the fragrance of a perfume palpable through sight and sound when buying perfume online.

### Inspiration:
Machine Learning assignment as the basic background. And fragrance always is my interest, while each time I wanna buy a perfume, the realistic scent of 'this' perfume always confuses me. The notes and the description can't feel the smell actually, so I decided to achieve the multi-sensory invocation using sight and sound to elicit olfactory resonance. Also, the development of DALL E 2 and Musicgen let me realize the realizability.

## 2. Data Collection
### Collecting data：
- Collecting the perfume data by web scraping using Python with the requests library for HTTP requests and LXML for parsing HTML.
- The script navigates through a set of pages on the website by iterating over a predefined list of categories and their respective number of pages.
- It extracts individual perfume page URLs from the search results and then accesses each perfume's detailed page to gather specific information.

### Sources used:
- The primary source for collecting perfume data is the website www.nosetime.com.
- The script uses a proxy to access this website to avoid detection as an automated scraper.

### Kind of Data Collected:
- Brand: The brand of each perfume.
- Fragrance Notes/Style: This includes the main fragrance style or notes of the perfume.
- Descriptions: This includes a brief introduction or description of the perfume.
In addition, the script collects the perfume's full name, image URLs, attributes, and the perfumer's name.

### Challenges:
- Most perfumes do not have descriptions, which is the most important data I need. Thus, I reduced the amount of data and removed blank values.
- I tryied to access both *nosetime* and *Fragrantica*, both of them are the biggest websites of fragrance in global and in China, thus, I can scratch enough data and fill in the blank values and other missing data. But Fragrantica has a Five Second Shield, and nosetime does not has enough data to be scratched at one time. Then I give up fragrantica and scratch data from the classification of nosetime multiple times.

## 3. Music Generation
### Technology Used: 
- MusicGen: It's a single-stage transformer language model for generating high-quality music. MusicGen operates on compressed discrete music tokens and can create music conditioned on textual descriptions or melodic features. Its efficiency lies in handling multiple parallel streams of acoustic tokens without needing multiple cascading models.

- Audiocraft: This is likely the GitHub repository associated with MusicGen, hosted by Facebook Research. It probably contains the implementation code, models, and possibly datasets for MusicGen and related audio processing projects. Audiocraft serves as a platform for MusicGen's deployment and possibly other audio generation initiatives.

### From Text to Music:
#### Process of Generating Music from Perfume Descriptions:
-Text Preprocessing: First, the perfume descriptions are preprocessed. This step includes cleaning the text, removing any irrelevant information, and possibly encoding it in a format suitable for the model (like tokenization).

- Feature Extraction: Key attributes are extracted from the text descriptions. For perfumes, this might include adjectives describing scents (like 'floral', 'earthy'), emotions (like 'calming', 'invigorating'), or abstract concepts (like 'elegance', 'mystery').

- Model Conditioning: These extracted features are then used to condition the music generation model. In the case of MusicGen, it can be conditioned on textual descriptions. The model takes these descriptions and interprets them to influence the musical output.

- Music Generation: The model generates music based on the conditioned input. This involves using the language model's understanding of the text to create music that reflects the attributes of the perfume. For instance, a description involving words like 'light', 'floral', and 'airy' might result in music that is soft, melodic, and has a higher pitch.

- Refinement and Output: The generated music is then reviewed and possibly refined. Refinement could involve manual adjustments or additional passes through the model for fine-tuning.

#### Influence of Text on Music Attributes:
- Mood and Emotion: Words in the perfume description that convey mood or emotion (like 'romantic', 'bold') would influence the emotional tone of the music.

- Intensity and Pace: Descriptions that imply intensity (like 'strong', 'subtle') could affect the music's tempo and dynamics.

- Instrumentation: Certain descriptive terms might suggest specific musical instruments or sounds (like 'crisp' might evoke the sound of a piano or a high hat).

```python
# Create a text input widget
text_input = widgets.Textarea(
    value='Enter perfume description here...',
    placeholder='Type something',
    description='Prompt:',
    disabled=False
)


## 4. Image Generation
Visual Representation: Discuss how you translated music into visual imagery. What tools or algorithms did you use?
Artistic Choices: Share any artistic decisions you made. How did you choose the colors, shapes, and overall style of the images?

## 5. Integration and User Experience
Bringing It Together: How did you integrate the music and images into a cohesive experience?
User Interaction: Describe how users interact with your system.

## 6. Reflections and Learnings
Project Insights: Share what you learned from this project. What skills did you gain or improve?
Challenges and Solutions: Reflect on any obstacles you faced during the project and how you solved them.

## 7. Conclusion
Final Thoughts: Conclude with your thoughts on the project's success and its potential impact.
Future Directions: Are there any extensions or improvements you're considering?

## 8. Multimedia Elements
Images and Audio: Include images of the web interfaces, generated visuals, and embed audio clips where relevant.

## 9. Technical Details (Optional)
Code Snippets: You can include small code snippets to illustrate key points, especially if your audience is technically inclined.
