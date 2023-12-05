bakiye = 0
while True:
    
    print("1. Para çek")
    print("2. Para yatır")
    print("3. Bakiye Sorgula")
    print("4. Çıkış")

    secim = input("Lütfen bir işlem seçin (1-4): ")

    if secim == "1":
        miktar = float(input("Çekilecek miktarı girin: "))
      
        if bakiye >= miktar:
            bakiye -= miktar
            print(f"Bakiyeniz başarıyla çekildi. Güncel bakiye: {bakiye} TL")
        else:
            print("Bakiye yetersiz")
    elif secim == "2":
      
        miktar = float(input("Yatırılacak miktarı girin: "))
        bakiye += miktar
        print(f"Bakiye başarıyla yatırıldı. Güncel bakiye: {bakiye} TL")
    elif secim == "3":
        print(f"Bakiyeniz:{bakiye} TL")
    elif secim == "4":
        print("Çıkış yapılıyor.")
        break
    else:
        print("Geçersiz seçim. Lütfen 1-4 arasında bir rakam girin.")
