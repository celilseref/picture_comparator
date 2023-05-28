import cv2
import numpy as np
import os

# Celil Seref -1210505053-
# Bu kodu çalıştırmak için opencv kütüphanesini import etmelisiniz!
# İki görüntü arasındaki benzerlik yüzdesini hesaplayan fonksiyon
def calculate_similarity(img1, img2):
    diff = cv2.absdiff(img1, img2)
    diff = diff.astype(np.float32)
    similarity = 1.0 - (np.sum(diff) / (img1.shape[0] * img1.shape[1] * 255))
    return similarity * 100

# Resimlerin bulunduğu klasörün yolu
folder_path = r"images"

# Klasördeki resimleri tutacak liste
images = []

# Klasördeki resimleri yükleyin
# Bu örnekte, resimlerin isimleri 1.png, 2.png, 3.png, ... gibi sıralıdır.
image_count = 150
for i in range(1, image_count+1):
    image_path = os.path.join(folder_path, str(i) + ".png")
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        print("Resim yüklenemedi:", image_path)
        continue
    images.append(image)

# Benzerlik matrisini oluşturun
similarity_matrix = np.zeros((image_count, image_count), dtype=np.float64)
for i in range(image_count):
    for j in range(i + 1, image_count):
        # Resimlerin parçaları üzerinden benzerliği hesaplayın
        roi = (0, 0, 20, 20)  # Parça boyutu: 20x20 piksel
        patch1 = images[i][roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]
        patch2 = images[j][roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]
        similarity = calculate_similarity(patch1, patch2)

        # Benzerlik matrisine değeri kaydedin
        similarity_matrix[i, j] = similarity
        similarity_matrix[j, i] = similarity

# En benzer resimleri bulun ve yüzdelik oranıyla listele
print("En çok benzeyen resimler:")
for i in range(image_count):
    max_similarity = 0.0
    similar_image_index = -1

    for j in range(image_count):
        if i != j and similarity_matrix[i, j] > max_similarity:
            max_similarity = similarity_matrix[i, j]
            similar_image_index = j

    if similar_image_index != -1:
        print("Resim", i + 1, "ve Resim", similar_image_index + 1, ": ", end="")
        print("Benzerlik Oranı:", max_similarity, "%")