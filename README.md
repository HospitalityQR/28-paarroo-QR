# 🌴 28 Paarroo (Old Palasia, Indore) - Dual Link QR Code & Luxury Table Standee

Ye project **28 Paarroo (Old Palasia, Indore)** ke liye specially design kiya gaya hai jisme customer table par rakhe QR code ko scan karke directly dono features access kar sakta hai:
1. ⭐ **Google Review (5-Star Rating)**: `https://share.google/ao3kZ8lE7ug4gjlHP`
2. 📸 **Instagram Profile**: `https://www.instagram.com/28paarroo?stkn=MTI4Y2NwcW5iNTRl`
3. 📞 **Contact / Reservation**: `90559 66555`

---

## 📁 Files Overview (Is Folder me kya-kya hai)

1. **`index.html`**
   - Premium Royal Burgundy / Maroon & Champagne Gold luxury mobile-responsive landing page.
   - 28 Paarroo ka enhanced circular logo with gold rim & subtle glow.
   - 2 Direct Action Cards: Google 5-Star Reviews & Instagram Profile.
   - 1-Tap Call button (`tel:9055966555`) & address badge ("28 Paarroo, Old Palasia, Indore").
   - Italic Gold Footer: *"Thank You For Visiting 28 Paarroo 🌴"*.

2. **`standee.html`**
   - Printable Table Tent / Standee web card.
   - Browser me open karke **Ctrl + P** press karein aur directly print ya PDF save kar sakte hain (A4 size ya standard 4x6 / 5x7 inches acrylic table standees ke liye perfectly sized).

3. **`config.js`**
   - Central configuration file. Agar aapko kabhi bhi phone number, address ya link badalna ho, to sirf is ek file me badlein — landing page aur standee apne aap update ho jayenge!

4. **`generate_qr.py`**
   - Python script jisse aap jab chahein kisi bhi URL ke liye high-resolution 300 DPI QR code aur table standee generate kar sakte hain.
   - Run command: `python generate_qr.py "Aapka_Web_Link"`

5. **`generate_direct_static.py`**
   - 100% Direct Offline Static QR Codes & Dual Standee generator (bina kisi web hosting ke chalne wale).
   - Generates:
     - `qr_google_direct.png`: Scan karte hi seedha Google Reviews khulega.
     - `qr_instagram_direct.png`: Scan karte hi seedha Instagram page khulega.
     - `standee_dual_direct_static.png`: Left me Google QR + Right me Instagram QR wala standee!

6. **Generated Ready-to-Print Standee Images (High-Resolution 300 DPI)**:
   - `table_standee_printable.png` / `front_page_standee.png`: High-resolution ready-to-print luxury standee card (Gold border, logo, badges, clear QR code, contact & address).
   - `standee_dual_direct_static.png`: Dual QR printable table card.

7. **Cleaned & Enhanced Logo Files**:
   - `logo_with_gold_rim.png`: Original embroidered logo ko perfectly circular crop karke royal gold metallic double rim aur subtle gold glow diya gaya hai.
   - `logo_clean.png` / `logo.png`: Transparent background wala clean circular logo (corners ka blur aur background hata diya gaya hai).
   - `logo_square_white.png` & `logo_square_dark.png`: Square badges for avatars and social media.

---

## 🌐 1 Minute Me Live Kaise Karein (Free Web Hosting)

Agar aap single QR code se landing page kholna chahte hain:

### Option 1: GitHub Pages (Recommended - 100% Free & Permanent)
1. GitHub par ek nayi repository banayein (jaise `28-Paarroo-QR`).
2. Is folder ke saare files usme push karein.
3. Settings > Pages me jaakar `main` branch select karke save karein.
4. Aapka URL ban jayega: `https://<username>.github.io/28-Paarroo-QR/`.
5. Us URL ke liye QR generate karne ke liye run karein:
   ```bash
   python generate_qr.py "https://<username>.github.io/28-Paarroo-QR/"
   ```

### Option 2: Netlify Drop (10 Seconds, Zero Setup)
1. Browser me open karein: [app.netlify.com/drop](https://app.netlify.com/drop)
2. Is poore `New QR Code` folder ko drag & drop kar dein.
3. Netlify turant live link provide kar dega.
   ```bash
   python generate_qr.py "https://aapka-netlify-link.netlify.app"
   ```

### Option 3: Bina Kisi Hosting Ke Seedha Print Karna (Direct Static)
Agar aapko koi website host nahi karni aur standee par dono QR alag-alag chahiye:
- Seedha **`standee_dual_direct_static.png`** ko print kar lijiye! Isme Google aur Instagram ke direct links embedded hain.
