### **Apple Detection Assignment**  

#### **Objective**  
Build an apple (or any fruit) detection application using first principles of computer vision—without deep learning.  

#### **Requirements**  
1. The application must detect a chosen fruit from an uploaded image.  
2. It should be built using **FastAPI** and deployed locally.  
3. Users should be able to upload an image to the `/is_apple` endpoint via the FastAPI UI (`/docs`).  
4. The detection should use classical computer vision techniques (color space, segmentation, contour detection, etc.), **not neural networks**.  
5. The application must detect all apples in the image.  
6. The output image should have **bounding boxes** around detected apples.  
7. Submit a **Word document** with the pros/cons of your approach and recommendations for improvement.  

#### **Video Submission**  
Create a **5-minute video** demonstrating the working application.  

---

## **Guiding Questions**  

### **Step 1: Understanding the Problem**  
- What **first principles of computer vision** can be used (e.g., color segmentation, edge detection, template matching)?  
- What are the **unique visual features** of an apple? (Shape, color, texture, size)  
- How can we translate these features into an **algorithm**?  
  - What color spaces (HSV, LAB) help distinguish apples?  
  - What techniques help detect circular objects?  

---

### **Step 2: Building the FastAPI Application**  
- How do we create a FastAPI app that **accepts image uploads**?  
  - What libraries (OpenCV, PIL) can process images?  
  - How do we define an `/is_apple` API endpoint?  
- How do we **return an image with bounding boxes**?  
  - How can we modify and send the processed image in an HTTP response?  
  - What format should the output image be in?  

---

### **Step 3: Implementing Apple Detection**  
- **Color-based segmentation:**  
  - Which color space (HSV, LAB, RGB) is best for isolating red/green apples?  
  - How do we create a **mask** for apple-like colors?  
- **Shape-based techniques:**  
  - How can **contour detection** help identify apples?  
  - Can we use the **Hough Circle Transform** to detect round objects?  
- **Filtering false positives:**  
  - How do we differentiate apples from other red/green objects?  
  - What **size or shape constraints** can we apply?  
- **Drawing bounding boxes:**  
  - How do we find the **minimum enclosing rectangle** around apples?  
  - What OpenCV function draws bounding boxes?  

---

### **Step 4: Testing & Deployment**  
- How do we test the API using FastAPI's **interactive UI (`/docs`)**?  
  - How do we upload an image and check the response?  
- How do we ensure the application **runs without errors**?  
  - What common issues arise with image processing?  
  - How do we handle **edge cases** (e.g., different lighting, partially visible apples)?  

---

### **Step 5: Evaluation & Improvements**  
- What are the **strengths & limitations** of our non-ML approach?  
  - When does **color segmentation fail**?  
  - How does **lighting affect detection**?  
  - Can **template matching** improve detection?  
- How can we **improve the detection pipeline**?  
  - Can **texture or edge-based filtering** reduce false positives?  
  - Would a **lightweight ML model** improve accuracy?  
  - Could **combining multiple techniques** make detection more robust?  

---

### **Deliverables**  
✔ **FastAPI application** (local deployment)  
✔ **Word document** (pros/cons & improvement suggestions)  
✔ **5-minute video demo**  

