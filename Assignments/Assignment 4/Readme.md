# **Motion Speed Analysis App**

## **Objective**

Design and implement a **Streamlit application** that performs motion speed analysis on `.mp4` video files using OpenCV. The app should allow users to upload a video, preprocess it to reduce noise, isolate moving regions by removing the background, and compute motion speed using `cv2.calcOpticalFlowFarneback`. The interface must provide interactive visualization of the original video, motion masks, and calculated speed, all running locally.

> **Deployment is not required. This application must be executed locally via Streamlit.**

---

## **Functional Requirements**

### 1. **Video Loading**
- Upload `.mp4` file via `st.file_uploader`.
- Use `cv2.VideoCapture` to read frames.
- Implement frame selection strategies:
  - Specific time ranges (start and end frame)
  - Frame sampling (e.g., process every 5th frame)

---

### 2. **Preprocessing**
- Convert all frames to grayscale (required for optical flow).
- Add Gaussian Blur with a configurable kernel size (via slider).
- Optional preprocessing features:
  - Histogram equalization for contrast enhancement.
  - Frame differencing to suppress static background noise.
- All parameters must be exposed through Streamlit widgets for dynamic tuning.

---

### 3. **Background Removal**
- Apply `cv2.createBackgroundSubtractorMOG2` to extract foreground motion.
- Customize and control:
  - Mask threshold to suppress small, irrelevant motion.
  - Learning rate for MOG2.
  - Morphological operations (optional):
    - Erosion
    - Dilation
- Provide visual feedback:
  - Display raw mask and post-processed mask per frame.
  - Allow inspection of mask quality interactively.

---

### 4. **Motion Speed Analysis**
- Compute dense optical flow between consecutive frames using `cv2.calcOpticalFlowFarneback`.
- Derive motion speed as the **magnitude of motion vectors**.
- (Optional) Directional analysis of motion vectors.
- Restrict calculation to foreground mask areas (this way background noise is ignored).
- Feel free to explore other techniques like video stabilization! 

---

### 5. **Streamlit Interface**
- Provide the following interface elements:
  - Video upload (`st.file_uploader`)
  - Display of original video (`st.video`)
  - Display of processed masks and speed overlays (`st.image`)
  - Sliders for:
    - Mask threshold
    - Optical flow parameters (e.g., window size, pyramid levels)
    - Preprocessing parameters (blur kernel, learning rate, etc.)
- Support side-by-side comparisons:
  - Original frame vs. mask
  - Original frame vs. optical flow overlay
- (Optional) Tabbed or segmented UI layout for different visualization modes.

---

### 6. **Analysis and Visualization**
- Compute and visualize:
  - Motion vector heatmaps (optional)
  - Motion speed statistics:
    - Minimum
    - Maximum
    - Average
  - Highlight frames with motion exceeding a user-defined threshold.

---

### 7. **Local Execution**
- The app must run locally via:
  ```bash
  streamlit run app.py
  ```
- No cloud deployment is required (e.g., no GCP integration needed).

---

## **Demonstration Video Requirements**

Create a **5–7 minute** video presenting the application. The video must:
- Walk through the application interface and core features.
- Explain:
  - Key challenges (e.g., noise handling, motion misclassification).
  - How specific parameter adjustments improved outcomes.
- Do NOT read a script ; present authentically and conversationally.
- Discuss insights gained or limitations encountered.

---

## **Testing Instructions**

Use the following sample videos for evaluation:

1. **People Moving in a Crowded Scene**  
   Source: Videvo  
   [Tourists Sitting in a Busy Street](https://www.videvo.net/video/tourists-sat-outside-in-busy-street/457475/#rs=video-box)

2. **Fast Car Driving Through a Scene**  
   Source: Pexels (Video by Taryn Elliott)  
   [Driving Fast on the Street](https://www.pexels.com/video/a-person-driving-fast-on-the-street-5309394/)

Test with these to:
- Compare performance across clean vs. noisy scenes.
- Analyze sensitivity of your algorithm to different motion types.

