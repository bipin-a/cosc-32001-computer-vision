# **Video Feature Tracking and Motion Analysis App (Assignment 5 + Project)**

## **Objective**

Build a **Streamlit application** with a **FastAPI backend** to load `.mp4` video files and analyze motion by tracking or detecting features across frames. You’ll choose one of three options: track a user-selected point, detect algorithm-suggested features, or identify objects from text input. The app must be deployed to **Google Cloud Run** (**or any other cloud platform**) using **Docker Compose** to manage the Streamlit frontend and FastAPI backend. Preprocessing is optional but recommended to improve results.

**NOTE:** Remember it’s okay if your methods do not yield perfect results. As said in class, explain to me if it is not performing well, why so? Pros and cons. **You will not be marked on how perfect your application is**!

- 
> **This app requires deployment to Google Cloud Run. Local testing is fine for development, but you must submit deployment instructions.**

---

## **Functional Requirements**

### 1. **Video Loading**
- Upload an `.mp4` file using `st.file_uploader` in Streamlit.
- Read frames with `cv2.VideoCapture` (a simple OpenCV function to load video frames).
- Save time by sampling frames smartly:
  - Skip frames (e.g., process every 5th frame) to avoid using all 30 frames per second.
  - Let users pick a start and end time (in seconds) with Streamlit sliders.
- Send the video or frame data to the FastAPI backend for processing.

---

### 2. **Preprocessing (Optional but Recommended)**
- Preprocessing can clean up video frames to make tracking or detection easier. You can choose what’s needed based on your option:
  - **Image Stabilization**: Fix shaky videos by aligning frames (e.g., find matching points between frames using ORB, a simple feature detector).
  - **Color Adjustment**: Use histogram equalization to boost contrast (makes objects stand out, especially in dim videos).
  - **Smoothing**: Apply Gaussian Blur to reduce noise (like graininess) with a slider for blur strength.
  - **Edge Detection**: Use Canny to highlight outlines of objects (helps with feature tracking).
- Add Streamlit checkboxes or sliders to turn preprocessing steps on/off or adjust settings (e.g., blur amount).
- If you skip preprocessing, explain why in your video (e.g., video was clear enough).

> **Why preprocess?** Noisy or shaky videos can confuse tracking algorithms. These steps are like cleaning a blurry photo before analyzing it.

---

### 3. **Implementation Options**
Pick **one** of these two options to analyze motion in the video. Each uses the video frames and optional preprocessing.

#### **Option 1: User-Selected Feature Tracking**
- Show a video frame in Streamlit and let users click to pick a small area (e.g., 50x50 pixels) to track, like a person’s head or a car’s wheel.
- Track that area across frames using a simple method:
  - Try **Lucas-Kanade optical flow** (it follows pixel movement by comparing brightness changes).
  - Or use **KCF tracker** (a basic tracker in OpenCV that follows a boxed area).
- **Motion Speed Analysis**:
  - Calculate speed by measuring how far the area moves between frames (in pixels per frame).
  - Convert to pixels per second using the video’s frame rate (e.g., 30 frames per second).
  - Show speed as a number (e.g., “50 pixels/second”) or a small graph.
- Show the tracked area with a box around it in each frame.

> **What’s this like?** Imagine pointing at a moving dog in a video and having the app follow it, telling you how fast it’s running.

#### **Option 2: Algorithm-Suggested Features**
- Let the app pick important points to track, like corners or faces, using:
  - **Shi-Tomasi corner detection** (finds sharp corners, like edges of a window).
  - **Haar cascade for faces** (a simple face detector in OpenCV).
- Show 2–3 suggested points in Streamlit (e.g., thumbnails or dots on a frame) and let users pick one, or auto-select the strongest one.
- Track the point across frames using Lucas-Kanade or KCF (same as Option 1).
- **Motion Speed Analysis**:
  - Measure speed (pixels per frame, then pixels per second) like in Option 1.
  - Display speed as text or a graph.
- Show the tracked point with a dot or box in each frame.

> **Why corners or faces?** Corners move predictably, and faces are easy to spot. It’s like the app saying, “Hey, this corner is clear—let’s follow it!”

---

### 4. **Streamlit Interface**
- Make the app easy to use with:
  - A button to upload a video (`st.file_uploader`).
  - Video player (`st.video`) to show the original video.
  - Image display (`st.image`) for processed frames with boxes or dots on tracked/detected objects.
  - Widgets:
    - Sliders for start/end time of video.
    - Checkboxes or sliders for preprocessing (e.g., “Turn on blur,” “Blur strength: 3–15”).
    - (Option 1) Clickable frame to select a point.
    - (Option 2) List of suggested points to pick from.
    - (Option 3) Text box for object name (e.g., “Enter object: bike”).
- Show side-by-side views:
  - Original frame next to tracked/detected frame.
  - (Options 1 and 2) Small speed graph or number below the frames.
- Keep the layout clean—use columns or tabs if needed.

---

### 5. **FastAPI Backend**
- Build a simple FastAPI backend to do the heavy work:
  - Endpoints for:
    - Taking the uploaded video.
    - Running preprocessing (if used).
    - Doing tracking or detection (based on the option).
    - (Options 1 and 2) Calculating speed.
  - Send back processed frames and results (like speed numbers) to Streamlit.
- Use JSON to talk between Streamlit and FastAPI. For frames, send images as base64 strings (a simple way to encode pictures).
- Don’t process huge videos all at once—work on frames one by one to avoid crashes.

---

### 6. **Deployment**
- Deploy to **Google Cloud Run** using **Docker Compose** to run two parts:
  - **Streamlit container**: Shows the app’s interface.
  - **FastAPI container**: Does the video processing.
- Write a `docker-compose.yml` file to:
  - Set up both containers.
  - Open ports (8501 for Streamlit, 8000 for FastAPI).
  - Add environment variables (like Google Cloud keys).
- Create a `Dockerfile` for each:
  - Install Python, OpenCV, Streamlit (for frontend), FastAPI (for backend), and YOLO/PyTorch if needed (Option 3).
  - Keep it simple—use a basic Python image (e.g., `python:3.9-slim`).
- Steps to deploy:
  1. Build Docker images: `docker-compose build`.
  2. Push to Google Container Registry: `gcloud builds submit`.
  3. Deploy to Cloud Run: `gcloud run deploy`.
- Share the public URL from Cloud Run in your submission.

**Docker Compose Resources**:
- [Official Docker Compose Docs](https://docs.docker.com/compose/) – Explains basics of `docker-compose.yml`.
- [Docker Compose for Python Apps](https://docs.docker.com/compose/gettingstarted/) – Simple guide with Python examples.
- [Google Cloud Run with Docker Compose](https://cloud.google.com/run/docs/quickstarts/build-and-deploy) – Steps for Cloud Run deployment.

---

### 7. **Visualization**
- Show results clearly:
  - Draw boxes or dots on tracked points/objects in each frame.
  - (Options 1 and 2) Show speed as a number (e.g., “Speed: 45 pixels/sec”) or a small line graph.
  - (Option 3) Show the object’s name and box (e.g., “Bike detected”).
- Display stats:
  - How many frames the point/object was tracked.
  - (Options 1 and 2) Highest and average speed.
- Highlight frames with big motion (e.g., speed > 50 pixels/sec) with a red border (optional).

---

## **Demonstration Video Requirements**

Record a **5–7 minute** video showing your app. Focus on:
- **The app in action**: Upload a video, pick an option, show tracking/detection, and (if Options 1 or 2) speed results.
- **Deployment**: Open the app’s Cloud Run URL to prove it works online.
- **Algorithms explained**:
  - Which option you picked and why (e.g., “I chose Option 1 because it’s simpler”).
  - How your tracking/detection works in simple terms (e.g., “Lucas-Kanade looks at pixel brightness to follow a point”).
  - Pros and cons (e.g., “KCF tracks well but struggles if the object changes shape”).
- **System overview**:
  - How Streamlit talks to FastAPI (e.g., “Streamlit sends the video, FastAPI processes it, then sends back frames”).
  - How preprocessing helped (or why you skipped it).
- **Insights**: What you learned (e.g., “Stabilization fixed shaky tracking!”) and any limits (e.g., “YOLO missed bikes in dark frames”).
- Be **precise**—don’t ramble. Plan your points but don’t read a script. Talk like you’re explaining to a friend who knows Python but not computer vision.
- Reminder you are not marked based on how well you communicate. It is okay to stumble while speaking, just continue where u left off! 
---

## **Testing Instructions**

Test your app with these videos:

1. **People Walking by a Cafe**  
   Source: Pexels (Video by Taryn Elliott)  
   [People at a Cafe](https://www.pexels.com/video/people-sitting-at-a-cafe-5309395/)

2. **Bikes on a City Street**  
   Source: Videvo  
   [Cyclists in City](https://www.videvo.net/video/cyclists-in-city/457890/#rs=video-box)

Use them to:
- Check if tracking/detection works on clear vs. busy scenes.
- See if preprocessing makes a difference (e.g., blur helps with noise).
- Confirm the deployed app runs smoothly on Cloud Run.

---

## **Submission Requirements**
- Source code (Streamlit frontend, FastAPI backend).
- `docker-compose.yml` and `Dockerfile`(s).
- Deployment instructions (how to build, push, and deploy to Cloud Run).
- Demonstration video (5–7 minutes).
- Remember it's okay if your methods do not yield perfect results. As said in class, explain to me if it is not performing well, why so? Pros and Cons. You will not be marked on how perfect your application is!