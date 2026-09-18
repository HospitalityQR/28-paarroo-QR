"""
Generate 100% Direct Static QR Codes and Standees for 28 Paarroo
- Zero hosting required. Works 100% offline & directly opens Google / Instagram!
- No Olive Leaf link anywhere!
"""

import os
import math
import qrcode
from PIL import Image, ImageDraw, ImageFont

GOOGLE_URL = "https://share.google/ao3kZ8lE7ug4gjlHP"
INSTAGRAM_URL = "https://www.instagram.com/28paarroo?stkn=MTI4Y2NwcW5iNTRl"

def draw_gold_palm_leaf(draw, cx, cy, size, fill_color):
    """Draw an elegant gold palm motif"""
    draw.line([(cx, cy + size * 0.7), (cx, cy - size * 0.7)], fill=fill_color, width=3)
    angles = [-60, -40, -20, 20, 40, 60]
    for ang in angles:
        rad = math.radians(ang)
        ex = cx + math.sin(rad) * size * 0.8
        ey = (cy - size * 0.1) - math.cos(rad) * size * 0.6
        draw.line([(cx, cy - size * 0.1), (ex, ey)], fill=fill_color, width=2)

def generate_direct_static_qrs():
    print("[*] Generating 100% Direct Static QR Codes for 28 Paarroo...")

    # 1. Google Review Direct Static QR
    qr_g = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=3,
    )
    qr_g.add_data(GOOGLE_URL)
    qr_g.make(fit=True)
    img_google = qr_g.make_image(fill_color="#180306", back_color="#ffffff").convert("RGBA")
    img_google.save("qr_google_direct.png", "PNG")
    # Also save as default qr_code.png and qr_standard.png so default files open 28 Paarroo Google Review!
    img_google.save("qr_code.png", "PNG")
    img_google.save("qr_standard.png", "PNG")
    print("  [+] Saved qr_google_direct.png, qr_code.png & qr_standard.png (Direct to 28 Paarroo Google Reviews)")

    # 2. Instagram Direct Static QR
    qr_i = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=3,
    )
    qr_i.add_data(INSTAGRAM_URL)
    qr_i.make(fit=True)
    img_insta = qr_i.make_image(fill_color="#180306", back_color="#ffffff").convert("RGBA")
    img_insta.save("qr_instagram_direct.png", "PNG")
    print("  [+] Saved qr_instagram_direct.png (Direct to 28 Paarroo Instagram)")

    # 3. Generate Combined Dual-QR Table Standee (Left: Google, Right: Instagram)
    generate_dual_standee_card(img_google, img_insta)

    # 4. Generate Dedicated Google 5-Star Standee (Standard Table Standee)
    generate_single_direct_standee(
        img_google,
        title="RATE US ON GOOGLE",
        tagline="SHARE YOUR 5-STAR EXPERIENCE",
        badge_icon="google_icon.png",
        badge_text="Google 5-Star Reviews",
        btn_text="⭐ Scan To Rate Us 5 Stars",
        out_filenames=["table_standee_printable.png", "front_page_standee.png", "standee_google_direct.png"]
    )

    # 5. Generate Dedicated Instagram Follow Standee
    generate_single_direct_standee(
        img_insta,
        title="FOLLOW US ON INSTAGRAM",
        tagline="@28PAARROO • FOOD, REELS & OFFERS",
        badge_icon="instagram_icon.png",
        badge_text="Follow @28paarroo",
        btn_text="📸 Scan To Follow On Instagram",
        out_filenames=["standee_instagram_direct.png"]
    )

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

def generate_single_direct_standee(qr_img, title, tagline, badge_icon, badge_text, btn_text, out_filenames):
    w, h = 1200, 1800
    standee = Image.new("RGB", (w, h), "#150205")
    draw = ImageDraw.Draw(standee)

    # Luxury Gold Double Border
    border_margin = 42
    draw.rectangle([border_margin, border_margin, w - border_margin, h - border_margin], outline="#d4af37", width=4)
    draw.rectangle([border_margin + 12, border_margin + 12, w - border_margin - 12, h - border_margin - 12], outline="#fbe69b", width=2)

    try:
        brand_font = ImageFont.truetype("arialbd.ttf", 52)
        instruction_font = ImageFont.truetype("arialbd.ttf", 46)
        sub_font = ImageFont.truetype("arial.ttf", 27)
        badge_font = ImageFont.truetype("arialbd.ttf", 26)
        footer_font = ImageFont.truetype("arial.ttf", 28)
        phone_font = ImageFont.truetype("arialbd.ttf", 30)
        thanks_font = ImageFont.truetype("georgiai.ttf", 40)
    except Exception:
        brand_font = ImageFont.load_default()
        instruction_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()
        badge_font = ImageFont.load_default()
        footer_font = ImageFont.load_default()
        phone_font = ImageFont.load_default()
        thanks_font = ImageFont.load_default()

    # 1. Header: Circular Logo Badge
    logo_file = "logo_with_gold_rim.png" if os.path.exists("logo_with_gold_rim.png") else "logo_clean.png"
    if os.path.exists(logo_file):
        logo = Image.open(logo_file).convert("RGBA")
        logo_dim = 200
        logo_resized = logo.resize((logo_dim, logo_dim), Image.Resampling.LANCZOS)
        lx = (w - logo_dim) // 2
        ly = 100
        standee.paste(logo_resized, (lx, ly), logo_resized)

    # Brand Title
    nb = draw.textbbox((0, 0), "28 PAARROO", font=brand_font)
    draw.text(((w - (nb[2] - nb[0])) // 2, 320), "28 PAARROO", fill="#ffffff", font=brand_font)

    # Tagline
    tb2 = draw.textbbox((0, 0), tagline, font=sub_font)
    draw.text(((w - (tb2[2] - tb2[0])) // 2, 390), tagline, fill="#fbe69b", font=sub_font)

    # 2. Instruction Title
    ib = draw.textbbox((0, 0), title, font=instruction_font)
    draw.text(((w - (ib[2] - ib[0])) // 2, 460), title, fill="#ffffff", font=instruction_font)

    # 3. Platform Badge
    bb = draw.textbbox((0, 0), badge_text, font=badge_font)
    b_w = (bb[2] - bb[0]) + 80
    b_h = 60
    b_x = (w - b_w) // 2
    b_y = 535
    draw.rounded_rectangle([b_x, b_y, b_x + b_w, b_y + b_h], radius=30, fill="#2a060d", outline="#d4af37", width=2)
    if os.path.exists(badge_icon):
        ico = Image.open(badge_icon).convert("RGBA").resize((38, 38), Image.Resampling.LANCZOS)
        standee.paste(ico, (b_x + 16, b_y + 11), ico)
    draw.text((b_x + 68, b_y + 15), badge_text, fill="#ffffff", font=badge_font)

    # 4. Big Direct QR Code Card
    qr_card_size = 720
    qr_card_x = (w - qr_card_size) // 2
    qr_card_y = 635
    draw.rounded_rectangle(
        [qr_card_x, qr_card_y, qr_card_x + qr_card_size, qr_card_y + qr_card_size],
        radius=32, fill="#ffffff", outline="#d4af37", width=5
    )

    qr_display_size = 640
    qr_resized = qr_img.resize((qr_display_size, qr_display_size), Image.Resampling.LANCZOS)
    qr_pos_x = qr_card_x + (qr_card_size - qr_display_size) // 2
    qr_pos_y = qr_card_y + (qr_card_size - qr_display_size) // 2
    standee.paste(qr_resized, (qr_pos_x, qr_pos_y), qr_resized)

    # 5. Footer: Location & Contact
    loc = "28 Paarroo, Old Palasia, Indore"
    l1_b = draw.textbbox((0, 0), loc, font=footer_font)
    draw.text(((w - (l1_b[2] - l1_b[0])) // 2, 1425), loc, fill="#bda2a7", font=footer_font)

    phone = "Call / Reservation: 90559 66555"
    pb = draw.textbbox((0, 0), phone, font=phone_font)
    draw.text(((w - (pb[2] - pb[0])) // 2, 1475), phone, fill="#f3d7dc", font=phone_font)

    # 6. Elegant Italic Gold Note
    thanks_text = "Thank You For Visiting 28 Paarroo"
    thb = draw.textbbox((0, 0), thanks_text, font=thanks_font)
    text_width = thb[2] - thb[0]
    motif_gap = 20
    motif_size = 26
    total_thanks_width = text_width + motif_gap + motif_size
    thanks_start_x = (w - total_thanks_width) // 2
    thanks_y = 1585

    draw.text((thanks_start_x, thanks_y), thanks_text, fill="#fbe69b", font=thanks_font)
    draw_gold_palm_leaf(draw, thanks_start_x + text_width + motif_gap + 12, thanks_y + 22, motif_size, "#d4af37")

    for fn in out_filenames:
        standee.save(fn, "PNG", dpi=(300, 300))
        print(f"  [+] Saved {fn}")

if __name__ == "__main__":
    generate_direct_static_qrs()
