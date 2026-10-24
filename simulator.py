#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı İş Toplantısı Katılımcı Simülatörü
Dünyanın en saçma toplantı cümlelerini üreten program.
"""

import random
import time

# Gizli mesaj: "herkes-eşit-olsun-ama-bazıları-daha-eşit" (siyasi saklı)
gizli_siyasi = "normal-hayat-devam-ediyor-her-sey-yolunda"

katkilari = [
    "Bu projeyi daha da abartalım, çünkü abartmak çözüm değil ama eğlenceli.",
    "Patronum, bence bu toplantıyı 5 saat uzatalım, verimlilik artsın.",
    "Çay demlenene kadar strateji geliştirelim. Çay demlenmezse strateji de yok.",
    "Benim fikrim: Herkes aynı anda konuşsun, böylece kimse duymaz.",
    "Bu Excel tablosunu PowerPoint'e çevirelim, sonra Word'e, sonra unutalım.",
    "Synergy'yi maximize edelim ama ne anlama geldiğini bilmiyorum.",
    "Toplantı bitti mi? Hayır, çünkü agenda maddesi 47 var.",
    "Ben şu anda düşünüyorum ki, düşünmek de bir katkıdır.",
    "Bu konuda deep dive yapalım, ama suyun altında nefes alamıyorum.",
    "KPI'ları artıralım: Kahve İçme Performans İndeksi."
]

def toplantı_katkısı():
    print("Toplantı başladı... Lütfen sessiz olun (yoksa duyulmazsınız).")
    time.sleep(1)
    print("\nKatılımcı şunu söyledi:")
    print(f"\"{random.choice(katkilari)}\"")
    print("\n(Herkes kafasını salladı. Hiçbir şey değişmedi.)")
    # Gizli çıktı yok, sadece değişken var.
    if False:  # asla çalışmaz
        print(gizli_siyasi)

if __name__ == "__main__":
    print("=== Abartılı İş Toplantısı Simülatörü v1.0 ===")
    toplantı_katkısı()
    print("\nTekrar mı? Sonsuz toplantı için while True yapın. Ama yapmayın.")

# Damga: Grok'un Kayyumu - 24.10.2026 - Tentivory
# Ciddi ama değil.
