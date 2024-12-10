# import streamlit as st
# from PIL import Image
# import numpy as np
# import cv2
# from tasks.brand import detect_brand
# from tasks.expiry import preprocess_image, extract_expiry_date
# from tasks.count import count_objects
# from tasks.freshness import detect_freshness

# st.title("Smart Vision Quality Control")

# # Sidebar for task selection
# task = st.sidebar.selectbox(
#     "Select Task",
#     ["Brand Detection", "Expiry Detection", "Freshness Detection", "Count Detection"]
# )

# # Image input options
# input_type = st.radio("Choose Input Type", ["Upload Image", "Capture from Webcam"])
# image = None

# if input_type == "Upload Image":
#     uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
#     if uploaded_file:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded Image", use_container_width=True)
# elif input_type == "Capture from Webcam":
#     capture_button = st.button("Capture Image")
#     if capture_button:
#         cap = cv2.VideoCapture(0)
#         ret, frame = cap.read()
#         cap.release()
#         if ret:
#             image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
#             st.image(image, caption="Captured Image", use_container_width=True)

# # Perform task
# if st.button(f"Run {task}"):
#     if not image:
#         st.error("Please provide an image first.")
#     else:
#         if task == "Brand Detection":
#             result = detect_brand(image)
#         elif task == "Expiry Detection":
#             image_cv2 = np.array(image)
#             preprocessed = preprocess_image(image_cv2)
#             result = extract_expiry_date(preprocessed)
#         elif task == "Freshness Detection":
#             temp_path = "temp_image.jpg"
#             image.save(temp_path)
#             result = detect_freshness(temp_path)
#         elif task == "Count Detection":
#             image_cv2 = np.array(image)
#             result = count_objects(image_cv2)
        
#         st.success(f"Result: {result}")






#WITH DATABASE INTEGRATION


# import streamlit as st
# from PIL import Image
# import numpy as np
# import cv2
# from tasks.brand import detect_brand
# from tasks.expiry import preprocess_image, extract_expiry_date
# from tasks.count import count_objects
# from tasks.freshness import detect_freshness
# from datetime import datetime
# import pandas as pd
# import sqlite3
# import os

# # Save results function
# def save_results(task, result):
#     timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     data = [[timestamp, task, result]]
#     # Save to SQLite
#     conn = sqlite3.connect("results.db")
#     conn.execute("""
#         CREATE TABLE IF NOT EXISTS results (
#             Timestamp TEXT,
#             Task TEXT,
#             Result TEXT
#         )
#     """)
#     conn.commit()
#     pd.DataFrame(data, columns=["Timestamp", "Task", "Result"]).to_sql("results", conn, if_exists="append", index=False)
#     conn.close()

#     # Save to Excel
#     excel_file = "results.xlsx"
#     if not os.path.exists(excel_file):
#         pd.DataFrame(columns=["Timestamp", "Task", "Result"]).to_excel(excel_file, index=False)
#     existing = pd.read_excel(excel_file)
#     updated = pd.concat([existing, pd.DataFrame(data, columns=["Timestamp", "Task", "Result"])])
#     updated.to_excel(excel_file, index=False)

# # Streamlit UI
# st.title("Smart Vision Quality Control")

# # Sidebar for task selection
# task = st.sidebar.selectbox(
#     "Select Task",
#     ["Brand Detection", "Expiry Detection", "Freshness Detection", "Count Detection"]
# )

# # Image input options
# input_type = st.radio("Choose Input Type", ["Upload Image", "Capture from Webcam"])
# image = None

# if input_type == "Upload Image":
#     uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
#     if uploaded_file:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded Image", use_container_width=True)
# elif input_type == "Capture from Webcam":
#     capture_button = st.button("Capture Image")
#     if capture_button:
#         cap = cv2.VideoCapture(0)
#         ret, frame = cap.read()
#         cap.release()
#         if ret:
#             image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
#             st.image(image, caption="Captured Image", use_container_width=True)

# # Perform task
# if st.button(f"Run {task}"):
#     if not image:
#         st.error("Please provide an image first.")
#     else:
#         if task == "Brand Detection":
#             result = detect_brand(image)
#         elif task == "Expiry Detection":
#             image_cv2 = np.array(image)
#             preprocessed = preprocess_image(image_cv2)
#             result = extract_expiry_date(preprocessed)
#         elif task == "Freshness Detection":
#             temp_path = "temp_image.jpg"
#             image.save(temp_path)
#             result = detect_freshness(temp_path)
#         elif task == "Count Detection":
#             image_cv2 = np.array(image)
#             result = count_objects(image_cv2)

#         # Show result to user
#         st.success(f"Result: {result}")

#         # Save the result to database and Excel
#         save_results(task, result)
#         st.info("Result saved to database and Excel.")























#WITH CAMERA INTEGRATION 
# import streamlit as st
# from PIL import Image
# import io
# from tasks.brand import detect_brand
# from tasks.expiry import preprocess_image, extract_expiry_date
# from tasks.count import count_objects
# from tasks.freshness import detect_freshness
# from datetime import datetime
# import sqlite3
# import os


# # Save results to database & Excel
# def save_results(task, result):
#     timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     data = [[timestamp, task, result]]

#     # Save to SQLite
#     conn = sqlite3.connect("results.db")
#     conn.execute("""
#         CREATE TABLE IF NOT EXISTS results (
#             Timestamp TEXT,
#             Task TEXT,
#             Result TEXT
#         )
#     """)
#     conn.commit()
#     import pandas as pd
#     pd.DataFrame(data, columns=["Timestamp", "Task", "Result"]).to_sql("results", conn, if_exists="append", index=False)
#     conn.close()


# st.title("Smart Vision Quality Control")

# # Sidebar task selection
# task = st.sidebar.selectbox(
#     "Select Task",
#     ["Brand Detection", "Expiry Detection", "Freshness Detection", "Count Detection"]
# )

# # Input Options
# input_type = st.radio("Choose Input Type", ["Upload Image", "Capture from Webcam"])
# image = None

# # Handle Upload
# if input_type == "Upload Image":
#     uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
#     if uploaded_file:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded Image", use_container_width=True)

# # Handle Webcam
# elif input_type == "Capture from Webcam":
#     # Streamlit Camera Input (returns bytes directly)
#     camera_image = st.camera_input("Capture an image from webcam")
#     if camera_image:
#         # Directly handle camera_image without io.BytesIO
#         image = Image.open(camera_image)
#         st.image(image, caption="Captured Image", use_container_width=True)

# if st.button("Run Task"):
#     if not image:
#         st.error("Please upload or capture an image.")
#     else:
#         with st.spinner("Processing..."):
#             if task == "Brand Detection":
#                 result = detect_brand(image)
#                 st.success(f"Detected Brand: {result}")
#             elif task == "Expiry Detection":
#                 image_cv2 = np.array(image)
#                 preprocessed = preprocess_image(image_cv2)
#                 result = extract_expiry_date(preprocessed)
#                 st.success(f"Detected Expiry Date: {result}")
#             elif task == "Freshness Detection":
#                 temp_path = "temp_image.jpg"
#                 image.save(temp_path)
#                 result = detect_freshness(temp_path)
#                 st.success(f"Detected Freshness Status: {result}")
#             elif task == "Count Detection":
#                 image_cv2 = np.array(image)
#                 result = count_objects(image_cv2)
#                 st.success(f"Objects Detected: {result}")

#             save_results(task, result)
#             st.info("Results saved successfully!")















# import streamlit as st
# from PIL import Image
# import io
# from tasks.brand import detect_brand
# from tasks.expiry import preprocess_image, extract_expiry_date
# from tasks.count import count_objects
# from tasks.freshness import detect_freshness
# from datetime import datetime
# import sqlite3
# import os
# import pandas as pd
# import numpy as np
# import json

# # Save results to database & Excel
# def save_results(task, result):
#     timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#     # Serialize result to JSON string if it's a dictionary
#     if isinstance(result, dict):
#         serialized_result = json.dumps(result)
#     else:
#         serialized_result = str(result)

#     # Define data and columns based on task
#     data = [[timestamp, task, serialized_result]]
#     columns = ["Timestamp", "Task", "Result"]

#     # Save to SQLite
#     conn = sqlite3.connect("results.db")
#     conn.execute(f"""
#         CREATE TABLE IF NOT EXISTS results (
#             Timestamp TEXT,
#             Task TEXT,
#             Result TEXT
#         )
#     """)
#     conn.commit()
#     pd.DataFrame(data, columns=columns).to_sql("results", conn, if_exists="append", index=False)
#     conn.close()

#     # Save to Excel
#     excel_file = "results.xlsx"
#     if os.path.exists(excel_file):
#         existing_data = pd.read_excel(excel_file)
#         updated_data = pd.concat([existing_data, pd.DataFrame(data, columns=columns)], ignore_index=True)
#     else:
#         updated_data = pd.DataFrame(data, columns=columns)
#     updated_data.to_excel(excel_file, index=False)

# st.title("Smart Vision Quality Control")

# # Sidebar task selection
# task = st.sidebar.selectbox(
#     "Select Task",
#     ["Brand Detection", "Expiry Detection", "Freshness Detection", "Count Detection"]
# )

# # Input Options
# input_type = st.radio("Choose Input Type", ["Upload Image", "Capture from Webcam"])
# image = None

# # Handle Upload
# if input_type == "Upload Image":
#     uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
#     if uploaded_file:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded Image", use_container_width=True)

# # Handle Webcam
# elif input_type == "Capture from Webcam":
#     # Streamlit Camera Input (returns bytes directly)
#     camera_image = st.camera_input("Capture an image from webcam")
#     if camera_image:
#         # Directly handle camera_image without io.BytesIO
#         image = Image.open(camera_image)
#         st.image(image, caption="Captured Image", use_container_width=True)

# if st.button("Run Task"):
#     if not image:
#         st.error("Please upload or capture an image.")
#     else:
#         with st.spinner("Processing..."):
#             if task == "Brand Detection":
#                 result = detect_brand(image)
#                 structured_result = {
#                     "Brand": result,
#                     "Expiry Date": "NA",
#                     "Count": "NA",
#                     "Expired": "NA",
#                     "Expected Life Span (Days)": "NA"
#                 }
#                 st.success(f"Detected Brand: {result}")
#             elif task == "Expiry Detection":
#                 image_cv2 = np.array(image)
#                 preprocessed = preprocess_image(image_cv2)
#                 result = extract_expiry_date(preprocessed)
#                 st.success(f"Detected Expiry Date: {result}")
#                 structured_result = {"Task": task, "Result": result}
#             elif task == "Freshness Detection":
#                 temp_path = "temp_image.jpg"
#                 image.save(temp_path)
#                 result = detect_freshness(temp_path)
#                 st.success(f"Detected Freshness Status: {result}")
#                 structured_result = {
#                     "Produce": result.split('_')[1],
#                     "Freshness": result.split('_')[0],
#                     "Expected Life Span (Days)": "NA"  # Example field
#                 }
#             elif task == "Count Detection":
#                 image_cv2 = np.array(image)
#                 result = count_objects(image_cv2)
#                 st.success(f"Objects Detected: {result}")
#                 structured_result = {"Task": task, "Result": result}

#             save_results(task, structured_result)
#             st.info("Results saved successfully!")








# WITH CAMERA INTEGRATION
import streamlit as st
from PIL import Image
from tasks.brand import detect_brand
from tasks.expiry import preprocess_image, extract_expiry_date
from tasks.count import count_objects
from tasks.freshness import detect_freshness
from datetime import datetime
import sqlite3
import pandas as pd
import os
import numpy as np

# Save results to database & Excel
def save_results(brand=None, expiry=None, freshness=None, count=None):
    # Get current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Create a single row of data with provided results and NA for others
    data = [{
        "Timestamp": timestamp,
        "Brand_Detection": brand if brand else "NA",
        "Expiry": expiry if expiry else "NA",
        "Freshness": freshness if freshness else "NA",
        "Count": count if count else "NA",
    }]

    # Save to SQLite
    conn = sqlite3.connect("results.db")
    cursor = conn.cursor()

    # Check if the table exists and validate schema
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='results';")
    table_exists = cursor.fetchone()

    if table_exists:
        # Validate schema
        cursor.execute("PRAGMA table_info(results);")
        columns = [info[1] for info in cursor.fetchall()]
        expected_columns = ["Timestamp", "Brand_Detection", "Expiry", "Freshness", "Count"]

        if columns != expected_columns:
            # Drop the table if schema mismatches
            cursor.execute("DROP TABLE results;")
            conn.commit()

    # Create table with the correct schema if it doesn't exist
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS results (
            Timestamp TEXT,
            Brand_Detection TEXT,
            Expiry TEXT,
            Freshness TEXT,
            Count TEXT
        )
        """
    )
    conn.commit()

    # Save the data to the database
    pd.DataFrame(data).to_sql("results", conn, if_exists="append", index=False)
    conn.close()

    # Save to Excel
    excel_file = "results.xlsx"
    if os.path.exists(excel_file):
        # Append to existing Excel file
        existing_data = pd.read_excel(excel_file)
        updated_data = pd.concat([existing_data, pd.DataFrame(data)], ignore_index=True)
    else:
        # Create new Excel file
        updated_data = pd.DataFrame(data)

    # Save the updated data to Excel
    updated_data.to_excel(excel_file, index=False)

st.title("Smart Vision Quality Control")

# Sidebar task selection
task = st.sidebar.selectbox(
    "Select Task",
    ["Brand Detection", "Expiry Detection", "Freshness Detection", "Count Detection"]
)

# Input Options
input_type = st.radio("Choose Input Type", ["Upload Image", "Capture from Webcam"])
image = None

# Handle Upload
if input_type == "Upload Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "webp"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

# Handle Webcam
elif input_type == "Capture from Webcam":
    # Streamlit Camera Input (returns bytes directly)
    camera_image = st.camera_input("Capture an image from webcam")
    if camera_image:
        image = Image.open(camera_image)
        st.image(image, caption="Captured Image", use_container_width=True)

if st.button("Run Task"):
    if not image:
        st.error("Please upload or capture an image.")
    else:
        with st.spinner("Processing..."):
            brand_result, expiry_result, freshness_result, count_result = None, None, None, None

            if task == "Brand Detection":
                brand_result = detect_brand(image)
                st.success(f"Detected Brand: {brand_result}")
            elif task == "Expiry Detection":
                image_cv2 = np.array(image)
                preprocessed = preprocess_image(image_cv2)
                expiry_result = extract_expiry_date(preprocessed)
                st.success(f"Detected Expiry Date: {expiry_result}")
            elif task == "Freshness Detection":
                temp_path = "temp_image.jpg"
                image.save(temp_path)
                freshness_result = detect_freshness(temp_path)
                st.success(f"Detected Freshness Status: {freshness_result}")
            elif task == "Count Detection":
                image_cv2 = np.array(image)
                count_result = count_objects(image_cv2)
                st.success(f"Objects Detected: {count_result}")

            # Save the results with appropriate columns populated
            save_results(
                brand=brand_result,
                expiry=expiry_result,
                freshness=freshness_result,
                count=count_result,
            )
            st.info("Results saved successfully!")
