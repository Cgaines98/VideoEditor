import cv2

filterColor = {
    "grayscale": cv2.COLOR_BGR2GRAY,
    "rainbow": cv2.COLORMAP_RAINBOW
}

def applyFilter(path, filter):
    # Open the video file
    video_path = path
    cap = cv2.VideoCapture(video_path)

    # Check if the video file was opened successfully
    if not cap.isOpened():
        print("Error opening video file")
        exit()
    
    # Get video frame dimensionss
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Define the codec and create a VideoWriter object to save the output
    output_path = 'output_filtered_video.mp4'
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height), isColor=False)

    # Loop through each frame in the video
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Apply a grayscale filter to the frame
        gray_frame = cv2.cvtColor(frame, filterColor[filter])

        # Write the grayscale frame to the output video
        out.write(gray_frame)

        # Display the grayscale frame
        cv2.imshow('Grayscale Video', gray_frame)

        # Press 'q' to exit the video display
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release video objects and close windows
    cap.release()
    out.release()
    cv2.destroyAllWindows()

