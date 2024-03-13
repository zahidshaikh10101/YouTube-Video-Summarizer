#  YouTube Transcript Summarizer

This Streamlit application demonstrates how to create a YouTube video transcript summarizer using Google AI's Generative Pre-trained Transformer 3 (GPT-3) model (Gemini Pro).

##  Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Requirements](#requirements)
* [Demo Photos](#demo-photos)
* [How it Works](#how-it-works)
* [Running the App](#running-the-app)
* [Deployment](#deployment)
* [Project Creators](#project-creators)

##  Overview
This project allows users to enter a YouTube video link and summarize the content using Google Generative AI (formerly known as Meena). It extracts the transcript from the video and utilizes the provided prompt to generate a concise summary within a specified length. Additionally, the user can download the summary in PDF format for further reference.

##  Features
Extracts video transcript from YouTube
Generates summaries using Google AI's GPT-3 model
User-friendly interface with Streamlit
Customizable summary length 
Provides the option to download summaries as PDFs

## Requirements
Python 3.x
Streamlit (pip install streamlit)
YouTube Transcript API (pip install youtube-transcript-api)
Google Cloud Project with GPT-3 access (and API key)
dotenv (pip install python-dotenv) (optional, for environment variables)

##  Demo Photos
<img width="1007" alt="app" src="https://github.com/zahidshaikh10101/YouTube-Video-Summarizer/blob/main/app.png">

## ️ How it Works
The user enters a YouTube video link.
The application extracts the transcript text from the video using the YouTubeTranscriptApi library.
The user defines the desired summary length.
The transcript text is combined with a pre-defined prompt instructing the AI model to summarize the content.
Google Generative AI (Gemini Pro) processes the prompt and transcript, generating a concise summary within the specified length.
The generated summary is displayed on the Streamlit app interface.
The user has the option to download the summary as a PDF file.
    
## ‍ Running the App
Clone this repository.
Install required libraries (pip install -r requirements.txt).
Create a .env file (optional) and set GOOGLE_API_KEY with your Google Cloud API key.
Run the app using streamlit run app.py.
Enter a YouTube video link and press the "Get Detailed Notes" button.
Note: A Google Cloud Project with enabled GPT-3 access is required for this app to function.

## Deployment Optional
Link: https://youtube-video-summarizer-jhztaprxgx6kandjcynfbp.streamlit.app/
  
##  Project Creators
Made with ❤️ <br>
[@Zahid Salim Shaikh](https://www.linkedin.com/in/zahid-shaikh-7z8s6s/)









