# AromaHarmonics - Perfume description text to music, music to image

## 1. Introduction
### Project Overview:
This project is a 'Text-to-Music-to-Image' endeavor that harnesses the descriptive data of perfumes. It particularly focuses on utilizing each perfume's description as a prompt to generate corresponding sound and imagery. The aim is to render the essence of a perfume's fragrance tangible through both sight and sound, enhancing the experience of purchasing perfumes online. This innovative approach seeks to bridge the sensory gap inherent in online shopping, offering a multi-sensory engagement with the product.

### Inspiration:
With a foundation in Machine Learning, I embarked on this project fueled by a personal interest in fragrances. The challenge of purchasing perfumes online has always intrigued me, particularly the difficulty in truly understanding a perfume's scent through mere notes and descriptions. This gap in the sensory experience motivated me to explore a multi-sensory approach, leveraging sight and sound to evoke olfactory sensations. The advent of technologies like DALL-E 2 and MusicGen played a pivotal role in this endeavor, demonstrating the feasibility of translating textual descriptions into rich auditory and visual experiences. This project represents an intersection of my academic background and personal passion, aiming to enrich the online perfume shopping experience by simulating a more comprehensive sensory understanding.

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
```

## 4. Image Generation
### Translation of Music into Visual Imagery:
#### Feature Extraction:
The extract_audio_features function uses librosa, a Python library for music and audio analysis, to extract three key features from an audio file:

- Tempo: The overall speed or pace of the music.
  
- Spectral Centroids: Measures the ‘brightness’ of the sound, indicating where the center of mass of the spectrum is located.
  
- RMS Energy: The root mean square energy, representing the audio signal's power.
  
#### Normalization:
These features are normalized to ensure they fit within a specified range, which makes them easier to map to visual elements.

#### Visual Generation:
- Using matplotlib, the generate_shapes function creates a visual representation based on the extracted audio features.

- The number of shapes (circles, in this case) corresponds to the length of the normalized spectral centroids.

- Each shape's position is randomized (x, y coordinates).

- The size of each shape is determined by the normalized RMS energy, representing the power or intensity of the sound at that point.

- The color is mapped from the spectral centroids using the viridis colormap, which translates the 'brightness' of the sound into a color spectrum.

### Artistic Choices:
- Shape Selection: Circles were chosen for their simplicity and the ease with which they can represent various musical attributes like intensity and pitch.

- Color Mapping: The viridis colormap is used to represent spectral centroids. This colormap provides a visually appealing and coherent way to translate the 'brightness' or timbre of the music into colors, with different hues representing different frequencies.

- Size Representation: The size of each circle is proportional to the RMS energy at that moment in the track, visually representing the dynamics or 'loudness' of the music.

- Random Placement: The random placement of shapes creates an abstract representation, emphasizing the idea that each viewing of the generated image is unique, much like each listening of a piece of music can yield a different experience.

- Overall Style: The decision to create an abstract image with these elements reflects an artistic choice to emphasize the interpretive nature of translating audio into visual form. It allows for a more subjective and personal interpretation of the music.

```python
def extract_audio_features(audio_file):
    y, sr = librosa.load(audio_file)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
    rms_energy = librosa.feature.rms(y=y)[0]

    # Normalizing features for better visualization
    norm_centroids = spectral_centroids / np.max(spectral_centroids)
    norm_rms_energy = rms_energy / np.max(rms_energy)

    return tempo, norm_centroids, norm_rms_energy
```

```python
def generate_shapes(tempo, norm_centroids, norm_rms_energy):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    num_shapes = len(norm_centroids)
    for i in range(num_shapes):
        # Properties influenced by music features
        x, y = np.random.rand(2)  # Random position
        size = norm_rms_energy[i]
        color = plt.cm.viridis(norm_centroids[i])  # Color mapped from centroids

        # Create a circle
        circle = patches.Circle((x, y), size, color=color, fill=True)
        ax.add_patch(circle)
```

## 5. Integration and User Experience
### Integration of Music and Images:
The system automatically generates music and images from perfume descriptions. First, it picks a random perfume description, then creates music based on this description. Next, it translates the characteristics of this music into visual imagery. Both elements are linked by the same perfume description, ensuring they complement each other and create a cohesive experience.

### User Interaction:
Users primarily experience the system in an automated mode where everything is generated from the perfume descriptions. However, there's an added feature for customization - an input box where users can type in their own descriptions to generate music and images, offering a personalized experience with minimal interaction required.

```python
# Define a function to handle the generation
def generate_music(b):
    prompt = text_input.value
    res = model.generate(prompt)
    # Here you should add code to handle 'res', such as saving it or displaying it

# Create a text input widget
text_input = widgets.Textarea(
    value='Enter perfume description here...',
    placeholder='Type something',
    description='Prompt:',
    disabled=False
)

# Create a button and set its on-click event
generate_button = widgets.Button(description="Generate Music")
generate_button.on_click(generate_music)
```

## 6. Reflections and Learnings
### Project Insights:
- Technical Setup and Configuration: Learning how to set up a complex technical environment, including installing necessary software, libraries, and handling any dependencies.

- Understanding AI and Machine Learning Models: Gaining deeper insights into how AI models, particularly those like MusicGen, work. This includes understanding transformer models and their application in non-traditional domains like music generation.

- Audio Processing: Skills in handling and processing audio data, including extracting features from music, understanding audio file formats, and possibly manipulating audio elements.
  
- Project Management: Organizing and managing a multi-faceted project, coordinating different components (text, audio, visual), and ensuring they work together seamlessly.
  
- Cross-Disciplinary Knowledge: Gaining insights into different fields, such as digital arts, music theory, and sensory sciences, and understanding how they can intersect with technology.
  
### Challenges and Solutions:
- The most challenging aspect was setting up the environment to accommodate MusicGen and Audiocraft, as they require a GPU for execution. This necessitated the latest Nvidia drivers, along with xformers and PyTorch with CUDA support. Configuring and running this setup successfully consumed a significant amount of time.

- Understanding the principles of Audiocraft to input prompts and generate outputs was the next hurdle. Initially, I intended to create text-to-image conversions, but crafting such code from scratch, especially using GANs, proved difficult.

- Consequently, I turned to existing text-to-image services like DALL-E 2, StyleGAN, Midjourney, and Stable Diffusion. Comprehending the theory and principles of each system was also time-consuming. Eventually, I discovered that most systems are developed from Stable Diffusion, whose style and logic did not align with my project. DALL-E 2 emerged as the optimal choice, although its code is not publicly accessible, and its API usage is somewhat costly for me (and largely unnecessary). This dilemma stalled my progress until I discovered MusicGen, which led me to pivot towards generating music from text before creating images.

## 7. Conclusion
### Final Thoughts:
This project has the potential to significantly impact online perfume sales and shopping. It addresses a major challenge of buying perfumes online – the inability to smell the scents. While my project doesn't enable customers to physically smell the perfumes, it enhances their understanding and feel of the scents through audio and visual representations. This innovative approach could offer a more immersive and informative online shopping experience, bridging the gap between physical and virtual scent exploration.

### Future Directions:
Currently, the project utilizes Python to create a basic window displaying perfume details. However, there's room for improvement in user interface design. Future iterations could involve collaborating with a perfume website or developing an independent platform to dynamically generate sound and imagery for each perfume. My initial attempts at learning CSS and HTML were aimed at creating a web link to showcase the project. However, integrating the project with a website or developing an application remains a challenge due to my limited expertise in these areas.

To enhance user experience, I've experimented with modifying the layout of the window, but encountered several errors, leading to a suboptimal presentation that resembles a static picture. Going forward, improving this aspect will be crucial. Potential improvements could include:

- Enhanced Layout and Design: Seeking guidance or collaborating with a web designer to create a more appealing and intuitive layout.

- Interactive Elements: Incorporating interactive features such as clickable elements or sliders to allow users to engage more dynamically with the perfume representations.

- Responsive Design: Ensuring the interface is responsive and user-friendly across different devices and screen sizes.

- Error Handling: Implementing robust error handling and debugging to ensure smoother operation and user interaction.

- User Feedback Integration: Collecting and incorporating user feedback to continuously refine the interface and overall user experience.

- ...
  
## 8. Multimedia Elements
- [Full code](https://github.com/244313747/final/blob/06e0a69e050d9227b27b773e1630e92f559623f5/21033106%20(1).html)
- [Music generated_modified version](https://github.com/244313747/final/blob/06e0a69e050d9227b27b773e1630e92f559623f5/data/Benetton2.mp3)
- [Other music1](https://github.com/244313747/final/blob/12cb031b9f8e3eabfdab52316553dbb4dd99b564/data/Benetton_regenerated.wav)
- [Other music2](https://github.com/244313747/final/blob/12cb031b9f8e3eabfdab52316553dbb4dd99b564/data/RedSatin.wav)
- [Dataset](https://github.com/244313747/final/blob/06e0a69e050d9227b27b773e1630e92f559623f5/data/nosetime.xlsx)

## 9. Reference
`````Markdown
@article{copet2023simple,
    title={Simple and Controllable Music Generation},
    author={Jade Copet and Felix Kreuk and Itai Gat and Tal Remez and David Kant and Gabriel Synnaeve and Yossi Adi and Alexandre Défossez},
    year={2023},
    journal={arXiv preprint arXiv:2306.05284},
}
`````
`````Markdown
@misc{openai2023chatgpt,
    title={Assistance in Resolving code},
    author={{OpenAI ChatGPT}},
    year={2023},
    howpublished={ChatGPT interaction},
    note={Accessed on: 2023}
}
`````
