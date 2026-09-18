"""
Generate Direct Static QR Codes for 28 Paarroo Google Reviews and Instagram,
plus Dual-QR Table Standee.
- Zero hosting required. Works 100% offline & directly opens Google / Instagram!
"""

import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

GOOGLE_URL = "https://share.google/ao3kZ8lE7ug4gjlHP"
INSTAGRAM_URL = "https://www.instagram.com/28paarroo?stkn=MTI4Y2NwcW5iNTRl"

def generate_direct_static_qrs():
    print("[*] Generating 100% Direct Static QR Codes for 28 Paarroo...")

    # 1. Google Review Direct Static QR
    qr_g = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=16,
        border=3,
    )
    qr_g.add_data(GOOGLE_URL)
    qr_g.make(fit=True)
    img_google = qr_g.make_image(fill_color="#180306", back_color="#ffffff").convert("RGBA")
    img_google.save("qr_google_direct.png", "PNG")
    print("  [+] Saved qr_google_direct.png (Direct to Google Reviews)")

    # 2. Instagram Direct Static QR
    qr_i = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=16,
        border=3,
    )
    qr_i.add_data(INSTAGRAM_URL)
    qr_i.make(fit=True)
    img_insta = qr_i.make_image(fill_color="#180306", back_color="#ffffff").convert("RGBA")
    img_insta.save("qr_instagram_direct.png", "PNG")
    print("  [+] Saved qr_instagram_direct.png (Direct to Instagram)")

    # 3. Generate Combined Dual-QR Table Standee
    generate_dual_standee_card(img_google, img_insta)

def generate_dual_standee_card(img_google, img_insta):
    w, h = 1400, 1800
    standee = Image.new("RGB", (w, h), "#150205")
    draw = ImageDraw.Draw(standee)

    # Borders
    draw.rectangle([40, 40, w - 40, h - 40], outline="#d4af37", width=4)
    draw.rectangle([52, 52, w - 52, h - 52], outline="#fbe69b", width=1)

    try:
        title_font = ImageFont.truetype("arialbd.ttf", 64)
        sub_font = ImageFont.truetype("arial.ttf", 28)
        box_title_font = ImageFont.truetype("arialbd.ttf", 36)
        box_sub_font = ImageFont.truetype("arial.ttf", 26)
        footer_font = ImageFont.truetype("arial.ttf", 28)
        phone_font = ImageFont.truetype("arialbd.ttf", 30)
        thanks_font = ImageFont.truetype("georgiai.ttf", 36)
    except Exception:
        title_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()
        box_title_font = ImageFont.load_default()
        box_sub_font = ImageFont.load_default()
        footer_font = ImageFont.load_default()
        phone_font = ImageFont.load_default()
        thanks_font = ImageFont.load_default()

    # Brand Logo Emblem
    logo_file = "logo_with_gold_rim.png" if os.path.exists("logo_with_gold_rim.png") else "logo_clean.png"
    if os.path.exists(logo_file):
        logo = Image.open(logo_file).convert("RGBA")
        logo_dim = 160
        logo_resized = logo.resize((logo_dim, logo_dim), Image.Resampling.LANCZOS)
        standee.paste(logo_resized, ((w - logo_dim) // 2, 75), logo_resized)

    # Brand Title
    title = "28 PAARROO"
    tb = draw.textbbox((0, 0), title, font=title_font)
    draw.text(((w - (tb[2] - tb[0])) // 2, 250), title, fill="#ffffff", font=title_font)

    sub = "OLD PALASIA • INDORE"
    sb = draw.textbbox((0, 0), sub, font=sub_font)
    draw.text(((w - (sb[2] - sb[0])) // 2, 325), sub, fill="#fbe69b", font=sub_font)

    tag = "SOUTH INDIAN & MULTI-CUISINE • PURE VEG"
    tag_b = draw.textbbox((0, 0), tag, font=box_sub_font)
    draw.text(((w - (tag_b[2] - tag_b[0])) // 2, 365), tag, fill="#d4af37", font=box_sub_font)

    # Dual Columns for Google and Instagram
    card_w, card_h = 560, 830
    y_pos = 430

    # Column 1: Google Review Card (Left)
    x_g = 105
    draw.rounded_rectangle([x_g, y_pos, x_g + card_w, y_pos + card_h], radius=24, fill="#23050b", outline="#d4af37", width=2)
    
    g_title = "RATE US 5-STARS"
    gt_b = draw.textbbox((0, 0), g_title, font=box_title_font)
    draw.text((x_g + (card_w - (gt_b[2] - gt_b[0])) // 2, y_pos + 35), g_title, fill="#ffffff", font=box_title_font)
    
    g_sub = "Google Reviews"
    gs_b = draw.textbbox((0, 0), g_sub, font=box_sub_font)
    draw.text((x_g + (card_w - (gs_b[2] - gs_b[0])) // 2, y_pos + 85), g_sub, fill="#fbe69b", font=box_sub_font)

    # Google QR box
    qr_box_size = 450
    qr_x_g = x_g + (card_w - qr_box_size) // 2
    draw.rounded_rectangle([qr_x_g, y_pos + 140, qr_x_g + qr_box_size, y_pos + 140 + qr_box_size], radius=18, fill="#ffffff")
    qr_g_resized = img_google.resize((410, 410), Image.Resampling.LANCZOS)
    standee.paste(qr_g_resized, (qr_x_g + 20, y_pos + 160), qr_g_resized)

    # Platform pill badge
    draw.rounded_rectangle([x_g + 80, y_pos + 625, x_g + card_w - 80, y_pos + 685], radius=30, fill="#150205", outline="#d4af37", width=2)
    if os.path.exists("google_icon.png"):
        g_ico = Image.open("google_icon.png").convert("RGBA").resize((34, 34), Image.Resampling.LANCZOS)
        standee.paste(g_ico, (x_g + 95, y_pos + 643), g_ico)
    g_lbl = "Google Reviews"
    gl_b = draw.textbbox((0, 0), g_lbl, font=box_sub_font)
    draw.text((x_g + 145, y_pos + 642), g_lbl, fill="#ffffff", font=box_sub_font)

    g_btn = "⭐ Scan to Rate 5 Stars"
    gbtn_b = draw.textbbox((0, 0), g_btn, font=box_sub_font)
    draw.text((x_g + (card_w - (gbtn_b[2] - gbtn_b[0])) // 2, y_pos + 735), g_btn, fill="#fbe69b", font=box_sub_font)

    # Column 2: Instagram Card (Right)
    x_i = 735
    draw.rounded_rectangle([x_i, y_pos, x_i + card_w, y_pos + card_h], radius=24, fill="#23050b", outline="#d4af37", width=2)

    i_title = "FOLLOW US"
    it_b = draw.textbbox((0, 0), i_title, font=box_title_font)
    draw.text((x_i + (card_w - (it_b[2] - it_b[0])) // 2, y_pos + 35), i_title, fill="#ffffff", font=box_title_font)

    i_sub = "@28paarroo"
    is_b = draw.textbbox((0, 0), i_sub, font=box_sub_font)
    draw.text((x_i + (card_w - (is_b[2] - is_b[0])) // 2, y_pos + 85), i_sub, fill="#fbe69b", font=box_sub_font)

    # Instagram QR box
    qr_x_i = x_i + (card_w - qr_box_size) // 2
    draw.rounded_rectangle([qr_x_i, y_pos + 140, qr_x_i + qr_box_size, y_pos + 140 + qr_box_size], radius=18, fill="#ffffff")
    qr_i_resized = img_insta.resize((410, 410), Image.Resampling.LANCZOS)
    standee.paste(qr_i_resized, (qr_x_i + 20, y_pos + 160), qr_i_resized)

    # Platform pill badge
    draw.rounded_rectangle([x_i + 80, y_pos + 625, x_i + card_w - 80, y_pos + 685], radius=30, fill="#150205", outline="#d4af37", width=2)
    if os.path.exists("instagram_icon.png"):
        i_ico = Image.open("instagram_icon.png").convert("RGBA").resize((34, 34), Image.Resampling.LANCZOS)
        standee.paste(i_ico, (x_i + 95, y_pos + 643), i_ico)
    i_lbl = "Instagram Reels"
    il_b = draw.textbbox((0, 0), i_lbl, font=box_sub_font)
    draw.text((x_i + 145, y_pos + 642), i_lbl, fill="#ffffff", font=box_sub_font)

    i_btn = "📸 Scan for Instagram"
    ibtn_b = draw.textbbox((0, 0), i_btn, font=box_sub_font)
    draw.text((x_i + (card_w - (ibtn_b[2] - ibtn_b[0])) // 2, y_pos + 735), i_btn, fill="#fbe69b", font=box_sub_font)

    # Footer
    thanks = "Thank You For Visiting 28 Paarroo 🌴"
    th_b = draw.textbbox((0, 0), thanks, font=thanks_font)
    draw.text(((w - (th_b[2] - th_b[0])) // 2, 1370), thanks, fill="#fbe69b", font=thanks_font)

    loc = "28 Paarroo, Old Palasia, Indore"
    loc_b = draw.textbbox((0, 0), loc, font=footer_font)
    draw.text(((w - (loc_b[2] - loc_b[0])) // 2, 1435), loc, fill="#bda2a7", font=footer_font)

    phone = "Call / Reservation: 90559 66555"
    ph_b = draw.textbbox((0, 0), phone, font=phone_font)
    draw.text(((w - (ph_b[2] - ph_b[0])) // 2, 1485), phone, fill="#ffffff", font=phone_font)

    standee.save("standee_dual_direct_static.png", "PNG", dpi=(300, 300))
    print("  [+] Saved standee_dual_direct_static.png (Direct Dual Static QR Standee)")

if __name__ == "__main__":
    generate_direct_static_qrs()
