# import os

# class DirNotFound(Exception):
#     def __str__(self):
#         return "Invalid path"

# def get_dir():
#     path = input("Path: ")
#     if os.path.exists(path):
#         return path
#     else:
#         raise DirNotFound()


# def main():
#     try:
#         path = get_dir()
#         images, videos, documents, audios, others = arrange(path)
#         print(f"\n Img: {images}\n Vid: {videos}\n Doc:{documents}\n Aud: {audios}\n Oth: {others}")
#     except Exception as e:
#         input(f"{e}, Press 'Enter'")
    

# def arrange(path):
#     images = []
#     videos = []
#     documents = []
#     audios = []
#     others = []

#     for root, dir, files in os.walk(path):
#         for file in files :
#             if file.endswith(('.jpg', '.png')):
#                 images.append(file)
#             elif file.endswith(('.mp4', '.avi')):
#                 videos.append(file)
#             elif file.endswith(('.pdf', '.docx')):
#                 documents.append(file)
#             elif file.endswith(('.mp3', '.wav')):
#                 audios.append(file)
#             else :
#                 others.append(file)
            
#     return [images, videos, documents, audios, others]

# if __name__ == "__main__":
#     main()