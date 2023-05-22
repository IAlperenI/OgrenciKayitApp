import tkinter as tk

pc = tk.Tk()
pc.geometry("500x500")
pc.title("Öğrenci Girşi")
r1 = tk.Label(text="Lütfen tüm işlemleri yapınız", fg="red")

l1 = tk.Label(text="isim:")
l1.place(x=70, y=50)

l2 = tk.Label(text="Soyisim:")
l2.place(x=50, y=80)

l3 = tk.Label(text="Kimlik no:")
l3.place(x=40, y=110)

l4 = tk.Label(text="Okul:")
l4.place(x=260, y=50)

a1 = tk.Entry()
a1.place(x=100, y=50)

a2 = tk.Entry()
a2.place(x=100, y=80)

a3 = tk.Entry()
a3.place(x=100, y=110)

a4 = tk.Entry()
a4.place(x=300, y=50)

q1 = tk.Label(text="")

q2 = tk.Label(text="")

q3 = tk.Label(text="")

q4 = tk.Label(text="")

q5 = tk.Label(text="")

q6 = tk.Label(text="")

q7 = tk.Label(text="")

q8 = tk.Label(text="Öğrenci bilgileri")
sec3 = ["Sınıf seçiniz", "9A", "9B", "9C", "9D", "10A", "10B", "10C", "10D", "11A", "11B", "11C", "11D", "12A", "12B",
        "12C", "12D"]
secili3 = tk.StringVar(pc)
secili3.set(sec3[0])
om3 = tk.OptionMenu(pc, secili3, *sec3)
om3.place(x=300, y=110)

sec2 = ["Cinsiyet seçiniz", "Erkek", "Kadın"]
secili2 = tk.StringVar(pc)
secili2.set(sec2[0])
om2 = tk.OptionMenu(pc, secili2, *sec2)
om2.place(x=300, y=75)

sec = ["İlçe seçiniz", "Alpu", "Beylikova", "Çifteler", "Günyüzü", "Han", "İnönü", "Mahmudiye", "Mihalgazi",
       "Mihalıççık", "Tepebaşı", "Sarıcakaya", "Seyitgazi", "Sivrihisar", "Odunpazarı"]
secili = tk.StringVar(pc)
secili.set(sec[0])
om1 = tk.OptionMenu(pc, secili, *sec)
om1.place(x=100, y=140)


def d1():
    s1 = secili.get()
    s2 = secili2.get()
    s3 = secili3.get()
    w1 = a1.get()
    w2 = a2.get()
    w3 = a3.get()
    w4 = a4.get()
    if s1 != "İlçe seçiniz":
        print("İlçe giriş başarılı")
        if s2 != "Cinsiyet seçiniz":
            print("Cinsiyet girişi başarılı")
            if s3 != "Sınıf seçiniz":
                print("Sınıf girişi başarılı")
                if len(w1) >= 4:
                    print("w1 girişi başarılı")
                    if len(w2) >= 2:
                        print("w2 girişi başarılı")
                        if len(w3) >= 2:
                            print("w3 girişi başarılı")
                            if len(w4) >= 2:
                                print("w4 girişi başarılı")
                                q1.config(text="İsim: " + w1)
                                q2.config(text="Soyisim: " + w2)
                                q3.config(text="Kimlik no: " + w3)
                                q4.config(text="Okul: " + w4)
                                q5.config(text="İlçe: " + s1)
                                q6.config(text="Cinsiyet: " + s2)
                                q7.config(text="Sınfı: " + s3)
                                q1.place(x=200, y=250)
                                q2.place(x=200, y=270)
                                q3.place(x=200, y=290)
                                q4.place(x=200, y=310)
                                q5.place(x=200, y=330)
                                q6.place(x=200, y=350)
                                q7.place(x=200, y=370)
                                q8.place(x=200, y=210)
                                b2.place(x=350, y=310)
                                b2.config(text="Öğrenci bilgilerini sil", command=sil2)
                            else:
                                r1.place(x=300, y=280)
                                b2.place(x=400, y=310)
                                b2.config(text="Uyarıyı sil", command=sil)
                                b2.place(x=400, y=450)
                                b2.config(text="Öğrenci bilgilerini sil", command=sil2)

                        else:
                            r1.place(x=300, y=280)
                            b2.place(x=400, y=310)
                            b2.config(text="Uyarıyı sil", command=sil)
                            b2.place(x=400, y=450)
                            b2.config(text="Öğrenci bilgilerini sil", command=sil2)
                    else:
                        r1.place(x=300, y=280)
                        b2.place(x=400, y=310)
                        b2.config(text="Uyarıyı sil", command=sil)
                        b2.place(x=400, y=450)
                        b2.config(text="Öğrenci bilgilerini sil", command=sil2)
                else:
                    r1.place(x=300, y=280)
                    b2.place(x=400, y=310)
                    
                    b2.config(text="Uyarıyı sil", command=sil)
                    b2.place(x=400, y=450)
                    b2.config(text="Öğrenci bilgilerini sil", command=sil2)
            else:
                r1.place(x=300, y=280)
                b2.place(x=400, y=310)
                b2.config(text="Uyarıyı sil", command=sil)
                b2.place(x=400, y=450)
                b2.config(text="Öğrenci bilgilerini sil", command=sil2)
        else:
            r1.place(x=300, y=280)
            b2.place(x=400, y=310)
            b2.config(text="Uyarıyı sil", command=sil)
            b2.place(x=400, y=450)
    else:
        r1.place(x=300, y=280)
        b2.place(x=400, y=310)
        b2.config(text="Uyarıyı sil", command=sil)


def sil():
    r1.place(x=33221334, y=111111)
    b2.place(x=1212, y=223232)


def sil2():
    q8.place(x=23350, y=200)
    q1.place(x=333300, y=250)
    q2.place(x=3033330, y=270)
    q3.place(x=30333330, y=290)
    q4.place(x=3333300, y=310)
    q5.place(x=3333300, y=330)
    q6.place(x=3333333, y=350)
    q7.place(x=333333300, y=370)
    b2.place(x=1212, y=223232)


b2 = tk.Button(text="Uyarıyı sil", command=sil)
b1 = tk.Button(text="Kaydet", command=d1, fg="white", bg="green")
b1.place(x=350, y=150)
pc.mainloop()
