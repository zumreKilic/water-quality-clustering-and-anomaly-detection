# Water Quality Analysis

Bu proje, su kalitesi verileri üzerinde anomali tespiti ve kümeleme analizi yapar. Farklı makine öğrenmesi algoritmaları ile potansiyel içilebilirlik tahmini yapılmıştır.

## 🚀 Kullanılan Teknolojiler
- Python (pandas, scikit-learn, matplotlib, seaborn)
- Anomali Tespiti: Isolation Forest, LOF, One-Class SVM
- Kümeleme: KMeans, DBSCAN, Hierarchical clustering
- PCA ile boyut indirgeme ve görselleştirme

## ⚙️ Kurulum
```bash
git clone <repo-url>
cd water_quality_analysis
pip install -r requirements.txt
```

## ▶️ Kullanım
```bash
python main.py
```

## 📊 Sonuçlar
- İçilebilirlik tahmini için anomali tespiti yapılmıştır.  
- Kümeleme algoritmaları ile su kalitesi segmentleri oluşturulmuştur.

## 📂 Veri Seti Kaynağı
[5] A. Kharwal, "Water Quality Analysis," amanxai.com, Aug. 19, 2021.  
Accessed: Aug. 1, 2025. [Online]. Available: [Link](https://amanxai.com/2021/08/19/water-quality-analysis/)