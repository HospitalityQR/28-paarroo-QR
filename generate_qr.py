"""
QR Code & Standee Front Page Generator for 28 Paarroo Restaurant
- Pure solid black high-contrast QR code
- Luxury royal velvet maroon & gold theme
- Official Google & Instagram badges
- Elegant Italic Gold 'Thank You For Visiting 28 Paarroo 🌴'
"""

import sys
import os
import re
import math
import qrcode
from PIL import Image, ImageDraw, ImageFont

def load_config():
    config = {
        "landingPageUrl": "https://namangarg-06.github.io/Restaurants-QR-Design/",
        "restaurantName": "28 Paarroo",
        "tagline": "SOUTH INDIAN & MULTI-CUISINE • PURE VEG",
        "phoneNumber": "9055966555",
        "phoneButtonText": "Call / Reservation: 90559 66555",
        "address": "28 Paarroo, Old Palasia, Indore",
        "instagramUsername": "@28paarroo",
        "footerThanks": "Thank You For Visiting 28 Paarroo 🌴"
    }
    if os.path.exists("config.js"):
        try:
            with open("config.js", "r", encoding="utf-8") as f:
                content = f.read()
            for key in config.keys():
                m = re.search(rf'{key}\s*:\s*["\']([^"\']+)["\']', content)
                if m:
                    config[key] = m.group(1)
        except Exception as e:
            print("Notice: Could not parse config.js, using defaults:", e)
    return config

def create_qr_codes(custom_url=None):
    cfg = load_config()
    target_url = custom_url if custom_url else cfg["landingPageUrl"]
    
    os.makedirs("output", exist_ok=True)
    print(f"[*] Generating Solid High-Contrast QR Code for URL: {target_url}")

    # Pure Solid High-Contrast QR Code (Maximum Instant Scanning)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=20,
        border=3,
    )
    qr.add_data(target_url)
    qr.make(fit=True)

    # 1. Solid Black on White
    qr_black = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
    qr_black.save("qr_standard.png", "PNG")
    qr_black.save("qr_code.png", "PNG")
    
    # 2. Royal Velvet Maroon variant
    qr_maroon = qr.make_image(fill_color="#220408", back_color="white").convert("RGBA")
    qr_maroon.save("qr_luxury.png", "PNG")
    print("  [+] Saved qr_code.png, qr_standard.png & qr_luxury.png")

    # 3. Generate Standee Card with Solid Black QR
    generate_standee_card(qr_black, cfg)

def draw_gold_palm_leaf(draw, cx, cy, size, fill_color):
    """Draw an elegant gold palm motif"""
    # Central stem
    draw.line([(cx, cy + size * 0.7), (cx, cy - size * 0.7)], fill=fill_color, width=3)
    # Palm fronds
    angles = [-60, -40, -20, 20, 40, 60]
    for ang in angles:
        rad = math.radians(ang)
        ex = cx + math.sin(rad) * size * 0.8
        ey = (cy - size * 0.1) - math.cos(rad) * size * 0.6
        draw.line([(cx, cy - size * 0.1), (ex, ey)], fill=fill_color, width=2)

def generate_standee_card(qr_img, cfg):
    w, h = 1200, 1800
    standee = Image.new("RGB", (w, h), "#150205")
    draw = ImageDraw.Draw(standee)

    # Luxury Gold Double Border
    border_margin = 42
    draw.rectangle([border_margin, border_margin, w - border_margin, h - border_margin], outline="#d4af37", width=4)
    draw.rectangle([border_margin + 12, border_margin + 12, w - border_margin - 12, h - border_margin - 12], outline="#fbe69b", width=2)

    try:
        title_font = ImageFont.truetype("arialbd.ttf", 52)
        instruction_font = ImageFont.truetype("arialbd.ttf", 46)
        sub_font = ImageFont.truetype("arial.ttf", 27)
        badge_font = ImageFont.truetype("arialbd.ttf", 25)
        footer_font = ImageFont.truetype("arial.ttf", 28)
        phone_font = ImageFont.truetype("arialbd.ttf", 30)
        thanks_font = ImageFont.truetype("georgiai.ttf", 40)
    except Exception:
        title_font = ImageFont.load_default()
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
        ly = 110
        standee.paste(logo_resized, (lx, ly), logo_resized)

    # Brand Title
    name_text = cfg.get("restaurantName", "28 PAARROO").upper()
    nb = draw.textbbox((0, 0), name_text, font=title_font)
    draw.text(((w - (nb[2] - nb[0])) // 2, 335), name_text, fill="#ffffff", font=title_font)

    # Tagline Badge
    tag_text = cfg.get("tagline", "SOUTH INDIAN & MULTI-CUISINE • PURE VEG").replace("*", "•")
    tb2 = draw.textbbox((0, 0), tag_text, font=sub_font)
    draw.text(((w - (tb2[2] - tb2[0])) // 2, 405), tag_text, fill="#fbe69b", font=sub_font)

    # 2. Instruction Title
    inst_text = "SCAN TO CONNECT"
    ib = draw.textbbox((0, 0), inst_text, font=instruction_font)
    draw.text(((w - (ib[2] - ib[0])) // 2, 475), inst_text, fill="#ffffff", font=instruction_font)

    # 3. Google Logo & Instagram Logo Pill Badges
    g_text = "Rate Us on Google"
    i_text = "Follow Us on Instagram"

    gb_box = draw.textbbox((0, 0), g_text, font=badge_font)
    g_badge_w = (gb_box[2] - gb_box[0]) + 74 + 24
    g_badge_h = 62

    ib_box = draw.textbbox((0, 0), i_text, font=badge_font)
    i_badge_w = (ib_box[2] - ib_box[0]) + 74 + 24
    i_badge_h = 62

    gap = 22
    total_badges_w = g_badge_w + i_badge_w + gap
    start_badges_x = (w - total_badges_w) // 2
    badges_y = 548

    # Badge 1: Google
    draw.rounded_rectangle(
        [start_badges_x, badges_y, start_badges_x + g_badge_w, badges_y + g_badge_h],
        radius=31, fill="#2a060d", outline="#d4af37", width=2
    )
    if os.path.exists("google_icon.png"):
        g_ico = Image.open("google_icon.png").convert("RGBA").resize((38, 38), Image.Resampling.LANCZOS)
        standee.paste(g_ico, (start_badges_x + 18, badges_y + 12), g_ico)
    draw.text((start_badges_x + 72, badges_y + 16), g_text, fill="#ffffff", font=badge_font)

    # Badge 2: Instagram
    insta_x = start_badges_x + g_badge_w + gap
    draw.rounded_rectangle(
        [insta_x, badges_y, insta_x + i_badge_w, badges_y + i_badge_h],
        radius=31, fill="#2a060d", outline="#d4af37", width=2
    )
    if os.path.exists("instagram_icon.png"):
        i_ico = Image.open("instagram_icon.png").convert("RGBA").resize((38, 38), Image.Resampling.LANCZOS)
        standee.paste(i_ico, (insta_x + 18, badges_y + 12), i_ico)
    draw.text((insta_x + 72, badges_y + 16), i_text, fill="#ffffff", font=badge_font)

    # 4. Main Solid High-Contrast QR Code Card
    qr_card_size = 700
    qr_card_x = (w - qr_card_size) // 2
    qr_card_y = 650
    
    draw.rounded_rectangle(
        [qr_card_x, qr_card_y, qr_card_x + qr_card_size, qr_card_y + qr_card_size],
        radius=32,
        fill="#ffffff",
        outline="#d4af37",
        width=5
    )

    qr_display_size = 620
    qr_resized = qr_img.resize((qr_display_size, qr_display_size), Image.Resampling.LANCZOS)
    qr_pos_x = qr_card_x + (qr_card_size - qr_display_size) // 2
    qr_pos_y = qr_card_y + (qr_card_size - qr_display_size) // 2
    standee.paste(qr_resized, (qr_pos_x, qr_pos_y), qr_resized)

    # 5. Footer: Location & Contact
    address_text = cfg.get("address", "28 Paarroo, Old Palasia, Indore")
    l1_b = draw.textbbox((0, 0), address_text, font=footer_font)
    draw.text(((w - (l1_b[2] - l1_b[0])) // 2, 1435), address_text, fill="#bda2a7", font=footer_font)

    phone_text = cfg.get("phoneButtonText", "Call / Reservation: 90559 66555")
    pb = draw.textbbox((0, 0), phone_text, font=phone_font)
    draw.text(((w - (pb[2] - pb[0])) // 2, 1485), phone_text, fill="#f3d7dc", font=phone_font)

    # 6. Elegant Italic Gold 'Thank You For Visiting 28 Paarroo 🌴'
    thanks_text = "Thank You For Visiting 28 Paarroo"
    thb = draw.textbbox((0, 0), thanks_text, font=thanks_font)
    text_width = thb[2] - thb[0]
    
    motif_gap = 20
    motif_size = 26
    total_thanks_width = text_width + motif_gap + motif_size
    thanks_start_x = (w - total_thanks_width) // 2
    thanks_y = 1590

    draw.text((thanks_start_x, thanks_y), thanks_text, fill="#fbe69b", font=thanks_font)
    draw_gold_palm_leaf(draw, thanks_start_x + text_width + motif_gap + 12, thanks_y + 22, motif_size, "#d4af37")

    # Save outputs
    standee.save("table_standee_printable.png", "PNG", dpi=(300, 300))
    standee.save("front_page_standee.png", "PNG", dpi=(300, 300))
    print("  [+] Saved table_standee_printable.png & front_page_standee.png (300 DPI Luxury Standee)")

if __name__ == "__main__":
    url_arg = sys.argv[1] if len(sys.argv) > 1 else None
    create_qr_codes(url_arg)
