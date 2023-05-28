# picture_comparator
Bu algoritmanın amacı, bir klasördeki resimler arasındaki benzerlik oranını hesaplamaktır. Algoritma, resimlerin 20x20 piksellik kısımlarını kullanarak benzerlik değerlerini hesaplar ve sonuçları yüzdelik oranlarıyla birlikte listeler.

Bu algoritmayı görüntü işlemede benzer resimleri tespit etmek için kullanabiliriz örneğin telefon yüz kilidini açmak, resim sınıflandırması yapmak, benzer resimleri bulması için arama motoruna eklemek gibi vb.. alanlarda kullanılabilir.

Bu algoritmayı kullanmak için OpenCV kütüphanesini kurmanız gerekiyor basit bir şekilde Visual Studio Code terminaline "pip install opencv-pyhton" yazarak son sürümünü indirebilirsiniz.

Algoritmanın karmaşılık analizi O(image_count^2) dir. Yüklenen resimlerin bellek boyutuna bağlı olarak çalışma süresi de artar. 

