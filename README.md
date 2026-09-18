# 🍽️ Restaurant QR & Luxury Table Standee Hub

Is platform par aap ek hi GitHub repository me **multiple restaurants** ke luxury QR codes, mobile landing pages aur printable table standees manage kar sakte hain.

👉 **GitHub Pages URL:** `https://namangarg-06.github.io/All-Restaurants-QR-/`

---

## 🏛️ Folder Structure (100% Isolated Architecture)

Har restaurant ka apna **alag self-contained folder** hai. Kisi ek restaurant me change karne par kisi dusre restaurant par 0% asar hoga:

```
All-Restaurants-QR-/
├── index.html                   # Master Hub (28 Paarroo par auto-redirect ya directory)
├── new_restaurant.py            # Naya restaurant 5 second me add karne ka script
└── 28-paarroo/                  # 🌴 28 Paarroo (Old Palasia, Indore)
    ├── config.js                # Is restaurant ki settings & links
    ├── index.html               # Mobile Landing Page
    ├── standee.html             # Printable Web Standee (Ctrl+P ready)
    ├── generate_qr.py           # Auto-generator script
    ├── table_standee_printable.png   # 300 DPI Luxury Standee
    ├── standee_dual_direct_static.png# Dual QR Standee (Google + Insta side-by-side)
    ├── standee_google_direct.png     # Google 5-Star Only Standee
    └── standee_instagram_direct.png  # Instagram Only Standee
```

---

## 🎯 Har Restaurant Me 4 Standee Options (Print Whichever You Want!)

Har restaurant folder ke andar 4 alag-alag ready-to-print 300 DPI standees generate hote hain:

1. **`table_standee_printable.png` (Single QR Landing Page)**:
   - Ek hi QR code jo restaurant ka luxury landing page kholta hai, jisme customer Google Review de sakta hai ya Instagram follow kar sakta hai.

2. **`standee_dual_direct_static.png` (Dual QR Standee - Side by Side)**:
   - Ek hi standee par 2 alag-alag direct QR codes:
     - **Left QR:** Direct Google Review (5-Stars)
     - **Right QR:** Direct Instagram Profile

3. **`standee_google_direct.png` (Google 5-Star Review Only)**:
   - Standee par sirf Google Review ka direct static QR code.

4. **`standee_instagram_direct.png` (Instagram Only)**:
   - Standee par sirf Instagram ka direct static QR code.

---

## ⚙️ Kisi Ek Restaurant Me Change Kaise Karein?

Agar aapko kisi particular restaurant (jaise `28-paarroo`) ki details badalni hain:
1. Us restaurant ke folder me jaakar `config.js` open karein.
2. Link, phone number ya text change karein.
3. Us folder ke andar run karein:
   ```bash
   python generate_qr.py
   ```
4. Bas! Sirf usi restaurant ke QR codes aur standees update honge, baaki sab restaurants safe rahenge.

---

## ➕ Naya Restaurant Kaise Add Karein? (5 Seconds)

Jab bhi koi naya restaurant add karna ho:
1. Root folder me command run karein:
   ```bash
   python new_restaurant.py "Chef Bhupis Kitchen"
   ```
2. Ye automatically `chef-bhupis-kitchen` naam ka folder bana dega.
3. Us folder me restaurant ka `logo.png` rakhein aur `config.js` me links daal dein.
4. Run karein: `cd chef-bhupis-kitchen && python generate_qr.py`!
