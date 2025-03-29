### **Computer Vision Techniques API Assignment**  

#### **Objective**  
Build a comprehensive computer vision API using FastAPI that demonstrates various detection algorithms, feature matching, and face analysis techniques without relying on deep learning models.

The code should follow the examples provided in the GitHub repository: https://github.com/bipin-a/cosc-32001-computer-vision/blob/main/week_6/Week_6_interactive.ipynb as a starting point.

#### **Requirements**  
1. The application must implement **feature detection** using multiple algorithms:
   - Harris Corner Detector
   - Shi-Tomasi Corner Detector
   - FAST Detector
   - ORB Detector
2. It should implement **feature matching** between two images using:
   - Brute Force Matching
   - FLANN Matching
   - RANSAC for outlier detection and improved robustness
3. The application must include **face detection**:
   - Using pre-trained Haar Cascades (note It has many limitation: rotation, lighting etc.)
4. For extra credit, implement **facial landmark analysis** using `dlib` to detect smiles and eye states.
5. All algorithm parameters must be **exposed through the API endpoints**.
6. Built using **FastAPI** and deployed locally with interactive UI (`/docs`).

#### **Video Submission**  
Create a **10-minute video** demonstrating the working application. Be authentic, avoid reading from a script, and thoroughly showcase each API endpoint.

---

## **Guiding Questions**  

### **Step 1: Understanding the Techniques**  
- What are the **mathematical foundations** of each feature detector?  
  - How does the **Harris detector** calculate corner response using eigenvalues?
  - How does the **Shi-Tomasi detector** modify Harris's corner measure?
  - What makes **FAST** (Features from Accelerated Segment Test) efficient?
  - How does **ORB** (Oriented FAST and Rotated BRIEF) extend basic detection?
- What are the **key differences** between matching algorithms?
  - When is **Brute Force matching** preferred over FLANN?
  - How does **FLANN** (Fast Library for Approximate Nearest Neighbors) achieve speed?
  - How does **RANSAC** identify and remove incorrect matches?
- What are the **principles** behind Haar Cascade face detection?
  - How do Haar features identify facial structures?
  - What makes detection work across different orientations?

---

### **Step 2: Building the FastAPI Application**  
- How do we handle **image uploads** for different use cases?
  - What image formats should be supported?
  - How do we handle single vs. pair image uploads for matching?
- How do we **parameterize algorithms** effectively?
  - What data types and validation should we use for parameters?
  - How do we provide **sensible defaults** while allowing experimentation?
- How do we structure the **API response format**?
  - How can we include additional metadata (feature counts, etc.)?
---

### **Step 3: Implementing Feature Detection**  
- **Harris Corner Detector:**
  - How do we expose `blockSize`, `ksize`, and `k` parameters?
  - What thresholding technique works best for visualizing corners?
- **Shi-Tomasi Corner Detector:**
  - How do we control `maxCorners`, `qualityLevel`, and `minDistance`?
  - How can users compare Harris vs. Shi-Tomasi results?
- **FAST Detector:**
  - How does the `threshold` parameter affect detection sensitivity?
  - What visualization techniques highlight FAST keypoints effectively?
- **ORB Detector:**
  - What parameters control ORB's feature count and quality?
  - How can we visualize both keypoints and their descriptors?
- **Drawing and Visualization:**
  - What's the best way to mark detected features on images?
  - How do we ensure visibility against different backgrounds?

---

### **Step 4: Implementing Feature Matching**  
- **Brute Force Matching:**
  - How do we implement different distance metrics (L2, Hamming)?
  - What parameters control match filtering and quality?
- **FLANN Matching:**
  - How do we configure FLANN for different descriptor types?
  - What index parameters should be exposed to the API?
- **RANSAC Integration:**
  - How do we apply RANSAC to reject outlier matches?
  - Use the homography as we covered in class.
- **Match Visualization:**
  - How do we draw connecting lines between matched features?
- **Image Pair Handling:**
  - How do we allow users to upload image pairs?
  - What preprocessing might improve matching results?
---

### **Step 5: Implementing Face Detection**  
- **Haar Cascade Integration:**
  - How do we load and configure the pre-trained face detector?
  - What parameters (`scaleFactor`, `minNeighbors`) improve detection?
- **Rotation Handling:**
  - Why did it fail using Haar Cascade? (Note: You are not expected to make it work with rotation.)
- **Lighting Compensation:**
  - What preprocessing techniques improve detection in poor lighting?
  - How can histogram equalization or normalization help?
- **Face Visualization:**
  - What's the most effective way to draw face bounding boxes?
  - How can we indicate detection confidence?
- **Extra Credit - Facial Analysis:**
  - How do we integrate `dlib` facial landmark detection?
  - What geometric measurements determine smiles or eye states?
  - How can we visualize facial landmarks and expression results?

---

### **Step 6: Testing & Performance Optimization**  
- How do we test the API with **diverse image inputs**?
  - What edge cases might cause failures?
  - How do we handle images without detectable features or faces?
- How can we **optimize performance**?
  - What preprocessing steps improve algorithm speed?
  - How do we balance quality vs. computational cost?
- How do we test the API using FastAPI's **interactive UI**?
  - What sample images demonstrate each technique effectively?
  - How can we compare results across different parameter settings?
- How do we ensure the application **handles errors gracefully**?
  - What input validation prevents runtime issues?
  - How do we provide meaningful error messages?

---

### **Step 7: Analysis & Evaluation**  
- What are the **strengths and limitations** of each technique?
- How do **parameter adjustments** affect results?
- What **practical applications** benefit from each technique?
  - Which methods are suitable for real-time processing?
  - When would one algorithm be preferred over another?
- What **improvements** could enhance the system?
  - Could hybrid approaches combine strengths of different methods?
  - How might more recent computer vision techniques address limitations?
---

### **Deliverables**  
✔ **FastAPI application** (local deployment with interactive UI)  
✔ **10-minute video demo** (authentic demonstration of all endpoints **Do Not Read from a Script** )  

