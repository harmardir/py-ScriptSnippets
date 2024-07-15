# pip install gtts
# pip install pypdf2 gtts

from gtts import gTTS
import PyPDF2

def pdf_to_mp3(pdf_file, language='en'):
    # Open the PDF file
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        
        # Extract text from each page
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText()

    # Convert text to speech
    tts = gTTS(text, lang=language)

    # Save the audio file
    audio_file = pdf_file.replace('.pdf', '.mp3')
    tts.save(audio_file)
    print(f"Saved audio file as {audio_file}")

# Replace 'yourfile.pdf' with the path to your PDF file
pdf_to_mp3('yourfile.pdf')
