import cv2
import numpy as np

# Read the video
video_capture = cv2.VideoCapture('sample_video.mp4') # Change your video filename

# Get the size of the frame (frame)
frame_width = int(video_capture.get(3)) # Width
frame_height = int(video_capture.get(4)) # Height

# Number of frames in the video
frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

# Create a result matrix
video_matrix = np.empty((frame_count, frame_width * frame_height), dtype=np.uint8)

frame_index = 0

whileTrue:
    ret, frame = video_capture.read()
    if not returned:
        break. break
    
    # Convert the frame to a pixel matrix (grayscale)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Transform the pixel matrix into a row and add to the resulting matrix
    video_matrix[frame_index] = frame_gray.flatten()
    
    frame_index += 1

video_capture.release()

# The resulting matrix has the number of rows as the number of frames and the number of columns as M x N
print(video_matrix.shape)
df = pd.DataFrame(video_matrix)
