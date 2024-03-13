import streamlit as st
from dotenv import load_dotenv
import io
load_dotenv() ##load all the nevironment variables
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

### Set Streamlit page configuration
st.set_page_config(page_title="YouTube Video Summarizer", layout="wide")

### getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]
        return transcript

    except Exception as e:
        st.sidebar.error(f"An error occurred: {e}")
        return None
    
## getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text,prompt,api_key):
    try:
        genai.configure(api_key=api_key)
        model=genai.GenerativeModel("gemini-pro")
        response=model.generate_content(prompt+transcript_text)
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def create_pdf(summary_text):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=(1440, 1056))
    c.drawString(72, 800, "Summary")
    text = c.beginText(40, 780)
    text.setFont("Helvetica", 12)
    for line in summary_text.split('\n'):
        text.textLine(line)
    c.drawText(text)
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer.getvalue()

def main():
    google_api_key = st.text_input("Enter your Google API Key: ", type="password")
    youtube_link = st.text_input("Enter Youtube Video Link: ")
    summary_len = st.select_slider("Select Summary Length: ", 
                                options=['250','500','1000','2000','5000'], value='1000')
    
    #Title
    st.title("YouTube Video Summarizer")

    # Display video thumbnail
    if youtube_link:
        video_id = youtube_link.split("=")[1]
        video_thumbnail = f"http://img.youtube.com/vi/{video_id}/0.jpg"
        st.image(video_thumbnail, caption="Video Thumbnail", use_column_width=True)

    # Process and display summary
    if google_api_key and youtube_link and st.button("Get Detailed Notes"):
        transcript_text = extract_transcript_details(youtube_link)
        if transcript_text:
            prompt = """You are a YouTube video summarizer. Summarize the video content into key points within 1500 words."""
            customized_prompt = f"{prompt} Please generate a {summary_len} summary."
            summary = generate_gemini_content(transcript_text, customized_prompt, google_api_key)
            if summary:
                st.success("Transcript extracted and summary generated successfully!")
                st.subheader("Detailed Notes:")
                st.write(summary)
                # PDF download
                pdf_bytes = create_pdf(summary)
                st.download_button(label="Download Summary as PDF",
                                data=pdf_bytes,
                                file_name="YouTube_Summary.pdf",
                                mime="application/pdf")
            else:
                st.error("Failed to generate summary.")
        else:
            st.error("Failed to extract transcript.")

if __name__ == "__main__":
    main()