# 1) txt fayl o`quvchi va uni ichidagi so'zlarni sonni qaytaruvchi raqamni yozing.

# fayl_nomi = 'fayl.txt'
# with open(fayl_nomi, 'w') as fayl:g
#     fayl.write("qalesan boy ozning yaxshimi.")

# def fayldagi_sozlar_soni(fayl_nomi):
#     with open(fayl_nomi, 'r') as fayl:
#         mazmuni = fayl.read()
#         sozlar = mazmuni.split()
#         return len(sozlar)

# soz_soni = fayldagi_sozlar_soni(fayl_nomi)
# print(f"Fayldagi so'zlar soni: {soz_soni}")

# 2) txt fayl o`quvchi va uni ichidagi so'zlarni eng kattasini qaytaruvchi kod yozing. 

# fayl_nomi = 'fayl.txt'

# with open(fayl_nomi, 'w') as fayl:
#     fayl.write("qalesan boy ozning yaxshimisan")

# def eng_katta_soz(fayl_nomi):
#     with open(fayl_nomi, 'r') as fayl:
#         mazmuni = fayl.read()
#         sozlar = mazmuni.split()
#         eng_katta = max(sozlar, key=len)
#         return eng_katta

# eng_katta = eng_katta_soz(fayl_nomi)
# print(f"Fayldagi eng katta so'z: {eng_katta}")

# 3) raqamlardan iborat list bor. Ushbu listni ichidagi raqamlarni o`shish holatiga ko`ra 
# buzilganlik holatini topuvchi va o`sha buzilgan raqamni qaytaruvchi kod yozing

# raqamlar = [1, 2, 3, 4, 5]

# def buzilgan_raqam(raqamlar):
#     for i in range(len(raqamlar) - 1):
#         if raqamlar[i] > raqamlar[i + 1]:
#             return raqamlar[i]
#     return None

# buzilgan = buzilgan_raqam(raqamlar)
# if buzilgan is not None:
#     print(f"Buzilgan raqam: {buzilgan}")
# else:
#     print("Buzilgan raqam topilmadi.")

# 4) sizda listni ichida ma`lumotlar bor, shularning ichida gmaillarni saralovchi kod yozing

# malumotlar = ['www.kun.uz', 'nbahromov@gmail.com', 'nasimbek@email.com', 'dunyo@gmail.com']

# # Gmail pochtalarni ajratib chiqish
# gmail_list = []
# for email in malumotlar:
#     if email.endswith('@gmail.com'):
#         gmail_list.append(email)

# print("Gmail pochtalari:")
# for gmail in gmail_list:
#     print(gmail)