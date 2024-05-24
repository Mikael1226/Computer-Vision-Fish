import os
import cv2
import datetime


global_frame_count = 0

def extract_images_from_folder(input_folder, output_folder, interval_seconds):
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    
    for video_file in os.listdir(input_folder):
        video_path = os.path.join(input_folder, video_file)
        if video_path.endswith(('.mp4', '.avi', '.mov')):  
            extract_images(video_path, output_folder, interval_seconds)

def extract_images(video_path, output_folder, interval_seconds):
    
    global global_frame_count

    
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Unable to Open this video {video_path}")
        return

    
    total_seconds = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)

    
    interval_frames = int(cap.get(cv2.CAP_PROP_FPS) * interval_seconds)

    
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    video_output_folder = os.path.join(output_folder, video_name)
    if not os.path.exists(video_output_folder):
        os.makedirs(video_output_folder)

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        
        if frame_count % interval_frames == 0 and frame_count / cap.get(cv2.CAP_PROP_FPS) < total_seconds:
            
            output_path = os.path.join(video_output_folder, f"frame_{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}.jpg")
            cv2.imwrite(output_path, frame)

        frame_count += 1

    cap.release()

    print(f"Extraction finished for video {video_path}. {frame_count} extracted images.")

if __name__ == "__main__":
    
    input_folder = "/path/to/your/input_folder"

    
    output_folder = "/path/to/your/output_folder"

    
    interval_seconds = 2  

    # Appeler la fonction pour extraire les images de toutes les vidéos dans le dossier spécifié
    extract_images_from_folder(input_folder, output_folder, interval_seconds)

