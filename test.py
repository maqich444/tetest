# Fənlər və qiymətlər
imtahan_neticeleri = {
    "Riyaziyyat": 85,
    "Fizika": 78,
    "Kimya": 90,
    "İngilis dili": 88,
    "Tarix": 76
}

# Orta qiyməti hesabla
ortalama = sum(imtahan_neticeleri.values()) / len(imtahan_neticeleri)

# Nəticəni çap et
print(f"Tələbənin orta qiyməti: {ortalama:.2f}")