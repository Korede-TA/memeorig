from timeit import default_timer as timer
import cloudinary
from cloudinary import uploader

cloudinary.config(
    cloud_name="dyewzifzu",
    api_key="866191258759256",
    api_secret="IB7PRXrbzLO2zb03mjNQ1z7IxYQ"
)

def imgcomp(img1, img2):
    cimg1 = uploader.upload(img1, phash=True)
    cimg2 = uploader.upload(img2, phash=True)
    ph1 = cimg1["phash"]
    ph2 = cimg2["phash"]
    dist = bin(ph1 != ph2).count("1")
    return dist # 0.5 <= dist <= 1

if __name__ == "__main__":
    img1 = "https://pbs.twimg.com/media/DX1sklvW0AA0-1y.jpg"
    img2 = "https://pbs.twimg.com/media/DZBfNpPU0AASVx-.jpg"
    print(imgcomp(img1, img2))
