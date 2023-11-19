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
Technology Used: Introduce MusicGen and Audiocraft. Explain briefly what these tools are and how they work.
From Text to Music: Detail how you used perfume descriptions to generate music. What was the process? How did the text influence the music's attributes?

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
