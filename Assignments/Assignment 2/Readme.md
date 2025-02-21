## **Assignment 2: Multi-Fruit Detection & Method Comparison**

---

### **Objective**
Extend your existing apple detection application (Assignment 1) to detect **apples and bananas** using two distinct classical computer vision methods:
1. **Color/Shape Analysis** (from Assignment 1).
2. **Template Matching** (new).

Compare both methods in different scenarios and analyze why they might succeed or fail.

---

### **Requirements**
1. **Extend your existing FastAPI application** with a new endpoint `/detect_fruits` that:
   - Returns **two annotated images**:  
     - One using color/shape analysis (label `[Color]`).  
     - One using template matching (label `[Template]`).  
   - Returns fruit counts from both methods in JSON, for example:
     ```json
     {
       "color": {"apple": 3, "banana": 2},
       "template": {"apple": 2, "banana": 3}
     }
     ```
2. **Implement Template Matching**:
   - Use **2 pre-made templates per fruit** (e.g., `apple1.jpg`, `apple2.jpg`, `banana1.jpg`, `banana2.jpg`).  
   - Handle **scaling** (template resizing). Ignore rotational changes.
3. **Test the system** on at least **4 scenarios**:
   - Simple image (no occlusions).
   - Mixed lighting conditions (shadows, etc.).
   - Partial occlusion.
4. **Video Submission** (5 minutes):
   - Show the system detecting apples and bananas under different scenarios.
   - Explain the trade-offs between color/shape analysis and template matching.

---

### **Video Submission**
Record a **5-minute** demo:
- Show how you upload images to the `/detect_fruits` endpoint via FastAPI’s UI.
- Present the returned annotated images and JSON results.
- Briefly discuss successes, failures, and improvements.

---

## **Guiding Questions**

### **Step 1: Extending Color/Shape Analysis to Bananas**
- What color thresholds or shape constraints are needed to isolate bananas (e.g., elongated contours)?
- How might **lighting** (e.g., greenish bananas or strong shadows) affect color-based detection?
- Now you must count how many bananas and apples exist. Here are some hints:
  ```python
  def detect_apples_and_bananas(image_path):
      # 1. Load the image.
      # 2. Convert from BGR to HSV.
      #
      # 3. Create masks:
      #    - One mask for apples (e.g., red/green range).
      #    - One mask for bananas (e.g., yellow range).
      #
      # 4. Clean masks using morphological operations (e.g., opening/closing).
      #
      # 5. Find contours for each mask.
      #
      # 6. For apple contours:
      #    - Filter out noise based on size/shape.
      #    - Increment apple count.
      #    - Optionally draw bounding boxes or circles on the image.
      #
      # 7. For banana contours:
      #    - Filter out noise based on size/shape.
      #    - Increment banana count.
      #    - Optionally draw bounding boxes or circles on the image.
      #
      # 8. Return the annotated image and counts (e.g., {"apple": X, "banana": Y}).
      pass
  ```
- **Additional Hints**:
  - **Overlapping Fruits**: Overlaps can merge contours, so consider splitting them if they exceed expected size/shape thresholds.  
  - **Color Variability**: Bananas may be greenish or have brown spots—use slightly broader hue ranges or adaptive preprocessing.  
  - **Scaling Template Range**: For the subsequent template matching step, you might test a few scale factors (e.g., 0.8× to 1.2×) and compare correlation scores.

### **Step 2: Implementing Template Matching**
- How do you resize templates to handle different fruit sizes?
- Under which conditions is template matching **prone to false positives** (e.g., similar shapes, occlusions)?
- **Additional Hint**: Consider a **threshold** to decide when a match is “good enough” (e.g., 0.7+ correlation).

### **Step 3: Comparing Methods**
- Which method is generally **faster**? Why?
- Which handles **occlusion/rotation** more robustly?
- Where might **color analysis** fail compared to template matching, and vice versa?
- **Additional Hint**: If the shapes are distinct (e.g., curved bananas vs. round apples), color-based detection might be faster and sufficient in simpler scenes.

### **Step 4: Analyzing Failures & Improvements**
- If a **non-fruit** object shares color or shape characteristics, how do you reduce misdetections?
- How do shadows or partial views affect detection accuracy for each method?
- Could a **combined approach** (e.g., color → shape → template) be more reliable?
- **Additional Hint**: You might employ a **multi-stage pipeline** where you first isolate potential fruit regions by color, then refine detection with templates to reduce false positives.

---

### **Deliverables**
1. **FastAPI code** extending the existing apple detection to apples+bananas using two methods.  
2. **Annotated images** showing both `[Color]` and `[Template]` results.  
3. **JSON output** indicating apple/banana counts from each method.  
4. **5-minute video** demonstration covering:
   - Strengths/weaknesses of each method.
   - Endpoint usage via FastAPI UI.
   - Example detections (images with bounding boxes/labels).
   - Discussion of trade-offs and lessons learned.