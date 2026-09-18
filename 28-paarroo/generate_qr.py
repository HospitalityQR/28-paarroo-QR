"""
All-in-One Luxury QR Code & Standee Generator for 28 Paarroo
- Refined Design:
  1. Thinner 1px gold outline on Google/Instagram buttons + cleaner minimal look
  2. Tighter, harmonious vertical spacing for bottom address and phone
  3. Very subtle dark burgundy radial gradient + micro-texture background (no flat background)
"""

import sys
import os
import re
import math
import numpy as np
import qrcode
from PIL import Image, ImageDraw, ImageFont

def load_config():
    config = {
        "restaurantName": "28 Paarroo",
        "tagline": "SOUTH INDIAN & MULTI-CUISINE • PURE VEG",
        "qrMode": "google_only",
        "landingPageUrl": "https://hospitalityqr.github.io/28-paarroo-QR/",
        "googleReviewLink": "https://share.google/ao3kZ8lE7ug4gjlHP",
        "instagramLink": "https://www.instagram.com/28paarroo?stkn=MTI4Y2NwcW5iNTRl",
        "phoneNumber": "9055966555",
        "phoneButtonText": "Call / Reservation: 90559 66555",
        "address": "28 Paarroo, Old Palasia, Indore",
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

def create_luxury_burgundy_background(w, h):
    """
    Generate a rich, velvety dark burgundy radial gradient with subtle texture.
    No flat solid color.
    """
    cx, cy = w / 2.0, h * 0.38
    max_r = math.sqrt(cx**2 + (h - cy)**2)

    y, x = np.ogrid[:h, :w]
    dist = np.sqrt((x - cx)**2 + ((y - cy) * 0.88)**2)
    norm_dist = np.clip(dist / (max_r * 0.92), 0.0, 1.0)

    # Velvet burgundy gradient stops
    # Center: Rich Velvet Crimson-Burgundy (44, 8, 16)
    # Mid: Deep Wine Burgundy (24, 4, 8)
    # Edge: Midnight Dark Wine (11, 2, 4)
    c_center = np.array([44, 8, 16], dtype=np.float32)
    c_mid = np.array([24, 4, 8], dtype=np.float32)
    c_edge = np.array([11, 2, 4], dtype=np.float32)

    t = norm_dist[..., None]
    img_arr = np.where(t < 0.5, c_center * (1.0 - t*2.0) + c_mid * (t*2.0), c_mid * (2.0 - t*2.0) + c_edge * (t*2.0 - 1.0))

    # Subtle micro-texture (linen/velvet grain)
    np.random.seed(42)
    noise = np.random.normal(0, 1.8, (h, w, 1))
    img_arr = np.clip(img_arr + noise, 0, 255).astype(np.uint8)

    return Image.fromarray(img_arr, mode="RGB")

def draw_gold_palm_leaf(draw, cx, cy, size, fill_color):
    """Draw a refined luxury gold palm leaf motif"""
    draw.line([(cx, cy + size * 0.7), (cx, cy - size * 0.7)], fill=fill_color, width=2)
    angles = [-60, -40, -20, 20, 40, 60]
    for ang in angles:
        rad = math.radians(ang)
        ex = cx + math.sin(rad) * size * 0.75
        ey = (cy - size * 0.1) - math.cos(rad) * size * 0.55
        draw.line([(cx, cy - size * 0.1), (ex, ey)], fill=fill_color, width=1)

def make_qr_image(url, fill_color="#180306", back_color="#ffffff", box_size=20):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=3,
    )
    qr.add_data(url)
    qr.make(fit=True)
    return qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGBA")

def get_fonts():
    try:
        brand_font = ImageFont.truetype("arialbd.ttf", 54)
        instruction_font = ImageFont.truetype("arialbd.ttf", 44)
        sub_font = ImageFont.truetype("arial.ttf", 26)
        badge_font = ImageFont.truetype("arialbd.ttf", 24)
        footer_font = ImageFont.truetype("arial.ttf", 26)
        phone_font = ImageFont.truetype("arialbd.ttf", 29)
        thanks_font = ImageFont.truetype("georgiai.ttf", 36)
    except Exception:
        brand_font = ImageFont.load_default()
        instruction_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()
        badge_font = ImageFont.load_default()
        footer_font = ImageFont.load_default()
        phone_font = ImageFont.load_default()
        thanks_font = ImageFont.load_default()
    return brand_font, instruction_font, sub_font, badge_font, footer_font, phone_font, thanks_font

def generate_all_assets():
    cfg = load_config()
    print(f"[*] Generating assets for {cfg['restaurantName']} (Mode: {cfg['qrMode']})...")

    # 1. Base QR Codes
    landing_url = cfg["landingPageUrl"]
    google_url = cfg["googleReviewLink"]
    insta_url = cfg["instagramLink"]

    img_landing = make_qr_image(landing_url, fill_color="#000000")
    img_landing.save("qr_landing_page.png", "PNG")

    img_google = make_qr_image(google_url, fill_color="#180306")
    img_google.save("qr_google_direct.png", "PNG")

    img_insta = make_qr_image(insta_url, fill_color="#180306")
    img_insta.save("qr_instagram_direct.png", "PNG")

    img_lux = make_qr_image(landing_url, fill_color="#220408")
    img_lux.save("qr_luxury.png", "PNG")

    mode = cfg.get("qrMode", "google_only").lower()
    if mode == "google_only":
        primary_qr = img_google
        primary_inst = "RATE US ON GOOGLE"
        primary_badge_ico = "google_icon.png"
        primary_badge_txt = "Google 5-Star Reviews"
    elif mode == "insta_only":
        primary_qr = img_insta
        primary_inst = "FOLLOW US ON INSTAGRAM"
        primary_badge_ico = "instagram_icon.png"
        primary_badge_txt = "Follow @28paarroo"
    else: # "dual_link"
        primary_qr = img_landing
        primary_inst = "SCAN TO CONNECT"
        primary_badge_ico = None
        primary_badge_txt = "Google Reviews • Instagram"

    primary_qr.save("qr_code.png", "PNG")
    primary_qr.save("qr_standard.png", "PNG")

    # 2. Primary Standee (table_standee_printable.png)
    if mode == "dual_link":
        generate_dual_link_standee(primary_qr, cfg)
    else:
        generate_single_direct_standee(
            primary_qr,
            title=primary_inst,
            tagline=cfg["tagline"],
            badge_icon=primary_badge_ico,
            badge_text=primary_badge_txt,
            out_filenames=["table_standee_printable.png", "front_page_standee.png"]
        )

    # 3. Dual Direct Static Standee
    generate_dual_standee_card(img_google, img_insta, cfg)

    # 4. Dedicated Google Standee
    generate_single_direct_standee(
        img_google,
        title="RATE US ON GOOGLE",
        tagline="SHARE YOUR 5-STAR EXPERIENCE",
        badge_icon="google_icon.png",
        badge_text="Google 5-Star Reviews",
        out_filenames=["standee_google_direct.png"]
    )

    # 5. Dedicated Instagram Standee
    generate_single_direct_standee(
        img_insta,
        title="FOLLOW US ON INSTAGRAM",
        tagline="@28PAARROO • FOOD, REELS & OFFERS",
        badge_icon="instagram_icon.png",
        badge_text="Follow @28paarroo",
        out_filenames=["standee_instagram_direct.png"]
    )

    print("  [+] All standees and QR codes generated with refined styling successfully!")

def generate_single_direct_standee(qr_img, title, tagline, badge_icon, badge_text, out_filenames):
    cfg = load_config()
    w, h = 1200, 1800
    
    # 3. Very subtle dark burgundy gradient/texture background
    standee = create_luxury_burgundy_background(w, h)
    draw = ImageDraw.Draw(standee)

    # Crisp Double Gold Border
    border_margin = 42
    draw.rectangle([border_margin, border_margin, w - border_margin, h - border_margin], outline="#d4af37", width=3)
    draw.rectangle([border_margin + 10, border_margin + 10, w - border_margin - 10, h - border_margin - 10], outline="#fbe69b", width=1)

    brand_font, instruction_font, sub_font, badge_font, footer_font, phone_font, thanks_font = get_fonts()

    # Header: Logo
    logo_file = "logo_with_gold_rim.png" if os.path.exists("logo_with_gold_rim.png") else "logo.png"
    if os.path.exists(logo_file):
        logo = Image.open(logo_file).convert("RGBA").resize((195, 195), Image.Resampling.LANCZOS)
        standee.paste(logo, ((w - 195) // 2, 100), logo)

    # Brand Title
    nb = draw.textbbox((0, 0), "28 PAARROO", font=brand_font)
    draw.text(((w - (nb[2] - nb[0])) // 2, 318), "28 PAARROO", fill="#ffffff", font=brand_font)

    # Tagline
    tb2 = draw.textbbox((0, 0), tagline, font=sub_font)
    draw.text(((w - (tb2[2] - tb2[0])) // 2, 385), tagline, fill="#fbe69b", font=sub_font)

    # Instruction Title
    ib = draw.textbbox((0, 0), title, font=instruction_font)
    draw.text(((w - (ib[2] - ib[0])) // 2, 452), title, fill="#ffffff", font=instruction_font)

    # 1. Thinner gold outline (width=1) + cleaner look on button/badge
    bb = draw.textbbox((0, 0), badge_text, font=badge_font)
    b_w = (bb[2] - bb[0]) + 76
    b_h = 56
    b_x = (w - b_w) // 2
    b_y = 525
    # Thinner 1px gold outline + deeper clean fill
    draw.rounded_rectangle([b_x, b_y, b_x + b_w, b_y + b_h], radius=28, fill="#1c0408", outline="#d4af37", width=1)
    if badge_icon and os.path.exists(badge_icon):
        ico = Image.open(badge_icon).convert("RGBA").resize((34, 34), Image.Resampling.LANCZOS)
        standee.paste(ico, (b_x + 16, b_y + 11), ico)
    draw.text((b_x + 64, b_y + 14), badge_text, fill="#ffffff", font=badge_font)

    # Big Direct QR Card
    qr_card_size = 720
    qr_card_x = (w - qr_card_size) // 2
    qr_card_y = 625
    draw.rounded_rectangle(
        [qr_card_x, qr_card_y, qr_card_x + qr_card_size, qr_card_y + qr_card_size],
        radius=30, fill="#ffffff", outline="#d4af37", width=4
    )
    qr_resized = qr_img.resize((640, 640), Image.Resampling.LANCZOS)
    standee.paste(qr_resized, (qr_card_x + 40, qr_card_y + 40), qr_resized)

    # 2. Bottom address/phone spacing: tighter, elegant, and harmonious
    loc = cfg.get("address", "28 Paarroo, Old Palasia, Indore")
    l1_b = draw.textbbox((0, 0), loc, font=footer_font)
    draw.text(((w - (l1_b[2] - l1_b[0])) // 2, 1400), loc, fill="#cfb8bd", font=footer_font)

    phone = cfg.get("phoneButtonText", "Call / Reservation: 90559 66555")
    pb = draw.textbbox((0, 0), phone, font=phone_font)
    draw.text(((w - (pb[2] - pb[0])) // 2, 1442), phone, fill="#f5dbe1", font=phone_font)

    thanks_text = "Thank You For Visiting 28 Paarroo"
    thb = draw.textbbox((0, 0), thanks_text, font=thanks_font)
    text_width = thb[2] - thb[0]
    total_w = text_width + 18 + 24
    tx = (w - total_w) // 2
    draw.text((tx, 1500), thanks_text, fill="#fbe69b", font=thanks_font)
    draw_gold_palm_leaf(draw, tx + text_width + 28, 1520, 24, "#d4af37")

    for fn in out_filenames:
        standee.save(fn, "PNG", dpi=(300, 300))

def generate_dual_link_standee(qr_img, cfg):
    w, h = 1200, 1800
    standee = create_luxury_burgundy_background(w, h)
    draw = ImageDraw.Draw(standee)

    border_margin = 42
    draw.rectangle([border_margin, border_margin, w - border_margin, h - border_margin], outline="#d4af37", width=3)
    draw.rectangle([border_margin + 10, border_margin + 10, w - border_margin - 10, h - border_margin - 10], outline="#fbe69b", width=1)

    brand_font, instruction_font, sub_font, badge_font, footer_font, phone_font, thanks_font = get_fonts()

    logo_file = "logo_with_gold_rim.png" if os.path.exists("logo_with_gold_rim.png") else "logo.png"
    if os.path.exists(logo_file):
        logo = Image.open(logo_file).convert("RGBA").resize((195, 195), Image.Resampling.LANCZOS)
        standee.paste(logo, ((w - 195) // 2, 100), logo)

    name_text = cfg.get("restaurantName", "28 PAARROO").upper()
    nb = draw.textbbox((0, 0), name_text, font=brand_font)
    draw.text(((w - (nb[2] - nb[0])) // 2, 318), name_text, fill="#ffffff", font=brand_font)

    tag_text = cfg.get("tagline", "SOUTH INDIAN & MULTI-CUISINE • PURE VEG").replace("*", "•")
    tb2 = draw.textbbox((0, 0), tag_text, font=sub_font)
    draw.text(((w - (tb2[2] - tb2[0])) // 2, 385), tag_text, fill="#fbe69b", font=sub_font)

    inst_text = "SCAN TO CONNECT"
    ib = draw.textbbox((0, 0), inst_text, font=instruction_font)
    draw.text(((w - (ib[2] - ib[0])) // 2, 452), inst_text, fill="#ffffff", font=instruction_font)

    # 1. Thinner 1px gold outline on Google/Instagram badges
    g_text = "Rate Us on Google"
    i_text = "Follow Us on Instagram"
    gb_box = draw.textbbox((0, 0), g_text, font=badge_font)
    g_badge_w = (gb_box[2] - gb_box[0]) + 68 + 20
    g_badge_h = 56

    ib_box = draw.textbbox((0, 0), i_text, font=badge_font)
    i_badge_w = (ib_box[2] - ib_box[0]) + 68 + 20
    i_badge_h = 56

    gap = 18
    total_badges_w = g_badge_w + i_badge_w + gap
    start_badges_x = (w - total_badges_w) // 2
    badges_y = 525

    # Badge 1: Google (width=1 thin gold outline)
    draw.rounded_rectangle(
        [start_badges_x, badges_y, start_badges_x + g_badge_w, badges_y + g_badge_h],
        radius=28, fill="#1c0408", outline="#d4af37", width=1
    )
    if os.path.exists("google_icon.png"):
        g_ico = Image.open("google_icon.png").convert("RGBA").resize((34, 34), Image.Resampling.LANCZOS)
        standee.paste(g_ico, (start_badges_x + 16, badges_y + 11), g_ico)
    draw.text((start_badges_x + 64, badges_y + 14), g_text, fill="#ffffff", font=badge_font)

    # Badge 2: Instagram (width=1 thin gold outline)
    insta_x = start_badges_x + g_badge_w + gap
    draw.rounded_rectangle(
        [insta_x, badges_y, insta_x + i_badge_w, badges_y + i_badge_h],
        radius=28, fill="#1c0408", outline="#d4af37", width=1
    )
    if os.path.exists("instagram_icon.png"):
        i_ico = Image.open("instagram_icon.png").convert("RGBA").resize((34, 34), Image.Resampling.LANCZOS)
        standee.paste(i_ico, (insta_x + 16, badges_y + 11), i_ico)
    draw.text((insta_x + 64, badges_y + 14), i_text, fill="#ffffff", font=badge_font)

    # Main QR Card
    qr_card_size = 720
    qr_card_x = (w - qr_card_size) // 2
    qr_card_y = 625
    draw.rounded_rectangle(
        [qr_card_x, qr_card_y, qr_card_x + qr_card_size, qr_card_y + qr_card_size],
        radius=30, fill="#ffffff", outline="#d4af37", width=4
    )
    qr_resized = qr_img.resize((640, 640), Image.Resampling.LANCZOS)
    standee.paste(qr_resized, (qr_card_x + 40, qr_card_y + 40), qr_resized)

    # 2. Bottom address/phone spacing: tighter, elegant, and harmonious
    loc = cfg.get("address", "28 Paarroo, Old Palasia, Indore")
    l1_b = draw.textbbox((0, 0), loc, font=footer_font)
    draw.text(((w - (l1_b[2] - l1_b[0])) // 2, 1400), loc, fill="#cfb8bd", font=footer_font)

    phone = cfg.get("phoneButtonText", "Call / Reservation: 90559 66555")
    pb = draw.textbbox((0, 0), phone, font=phone_font)
    draw.text(((w - (pb[2] - pb[0])) // 2, 1442), phone, fill="#f5dbe1", font=phone_font)

    thanks_text = "Thank You For Visiting 28 Paarroo"
    thb = draw.textbbox((0, 0), thanks_text, font=thanks_font)
    text_width = thb[2] - thb[0]
    total_w = text_width + 18 + 24
    tx = (w - total_w) // 2
    draw.text((tx, 1500), thanks_text, fill="#fbe69b", font=thanks_font)
    draw_gold_palm_leaf(draw, tx + text_width + 28, 1520, 24, "#d4af37")

    standee.save("table_standee_printable.png", "PNG", dpi=(300, 300))
    standee.save("front_page_standee.png", "PNG", dpi=(300, 300))

def generate_dual_standee_card(img_google, img_insta, cfg):
    w, h = 1400, 1800
    standee = create_luxury_burgundy_background(w, h)
    draw = ImageDraw.Draw(standee)

    draw.rectangle([40, 40, w - 40, h - 40], outline="#d4af37", width=3)
    draw.rectangle([50, 50, w - 50, h - 50], outline="#fbe69b", width=1)

    try:
        title_font = ImageFont.truetype("arialbd.ttf", 62)
        sub_font = ImageFont.truetype("arial.ttf", 26)
        box_title_font = ImageFont.truetype("arialbd.ttf", 34)
        box_sub_font = ImageFont.truetype("arial.ttf", 24)
        footer_font = ImageFont.truetype("arial.ttf", 26)
        phone_font = ImageFont.truetype("arialbd.ttf", 28)
        thanks_font = ImageFont.truetype("georgiai.ttf", 34)
    except Exception:
        title_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()
        box_title_font = ImageFont.load_default()
        box_sub_font = ImageFont.load_default()
        footer_font = ImageFont.load_default()
        phone_font = ImageFont.load_default()
        thanks_font = ImageFont.load_default()

    logo_file = "logo_with_gold_rim.png" if os.path.exists("logo_with_gold_rim.png") else "logo.png"
    if os.path.exists(logo_file):
        logo = Image.open(logo_file).convert("RGBA").resize((150, 150), Image.Resampling.LANCZOS)
        standee.paste(logo, ((w - 150) // 2, 75), logo)

    title = "28 PAARROO"
    tb = draw.textbbox((0, 0), title, font=title_font)
    draw.text(((w - (tb[2] - tb[0])) // 2, 245), title, fill="#ffffff", font=title_font)

    sub = "OLD PALASIA • INDORE"
    sb = draw.textbbox((0, 0), sub, font=sub_font)
    draw.text(((w - (sb[2] - sb[0])) // 2, 315), sub, fill="#fbe69b", font=sub_font)

    tag = "SOUTH INDIAN & MULTI-CUISINE • PURE VEG"
    tag_b = draw.textbbox((0, 0), tag, font=box_sub_font)
    draw.text(((w - (tag_b[2] - tag_b[0])) // 2, 352), tag, fill="#d4af37", font=box_sub_font)

    card_w, card_h = 560, 830
    y_pos = 415

    # Google Column (Left)
    x_g = 105
    draw.rounded_rectangle([x_g, y_pos, x_g + card_w, y_pos + card_h], radius=24, fill="#1c0408", outline="#d4af37", width=1)
    g_title = "RATE US 5-STARS"
    gt_b = draw.textbbox((0, 0), g_title, font=box_title_font)
    draw.text((x_g + (card_w - (gt_b[2] - gt_b[0])) // 2, y_pos + 32), g_title, fill="#ffffff", font=box_title_font)
    g_sub = "Google Reviews"
    gs_b = draw.textbbox((0, 0), g_sub, font=box_sub_font)
    draw.text((x_g + (card_w - (gs_b[2] - gs_b[0])) // 2, y_pos + 78), g_sub, fill="#fbe69b", font=box_sub_font)

    qr_box_size = 450
    qr_x_g = x_g + (card_w - qr_box_size) // 2
    draw.rounded_rectangle([qr_x_g, y_pos + 130, qr_x_g + qr_box_size, y_pos + 130 + qr_box_size], radius=16, fill="#ffffff")
    qr_g_resized = img_google.resize((410, 410), Image.Resampling.LANCZOS)
    standee.paste(qr_g_resized, (qr_x_g + 20, y_pos + 150), qr_g_resized)

    # 1. Thinner 1px gold outline button pill
    draw.rounded_rectangle([x_g + 80, y_pos + 625, x_g + card_w - 80, y_pos + 685], radius=30, fill="#120205", outline="#d4af37", width=1)
    if os.path.exists("google_icon.png"):
        g_ico = Image.open("google_icon.png").convert("RGBA").resize((32, 32), Image.Resampling.LANCZOS)
        standee.paste(g_ico, (x_g + 95, y_pos + 644), g_ico)
    g_lbl = "Google Reviews"
    draw.text((x_g + 145, y_pos + 643), g_lbl, fill="#ffffff", font=box_sub_font)

    g_btn = "⭐ Scan to Rate 5 Stars"
    gbtn_b = draw.textbbox((0, 0), g_btn, font=box_sub_font)
    draw.text((x_g + (card_w - (gbtn_b[2] - gbtn_b[0])) // 2, y_pos + 735), g_btn, fill="#fbe69b", font=box_sub_font)

    # Instagram Column (Right)
    x_i = 735
    draw.rounded_rectangle([x_i, y_pos, x_i + card_w, y_pos + card_h], radius=24, fill="#1c0408", outline="#d4af37", width=1)
    i_title = "FOLLOW US"
    it_b = draw.textbbox((0, 0), i_title, font=box_title_font)
    draw.text((x_i + (card_w - (it_b[2] - it_b[0])) // 2, y_pos + 32), i_title, fill="#ffffff", font=box_title_font)
    i_sub = "@28paarroo"
    is_b = draw.textbbox((0, 0), i_sub, font=box_sub_font)
    draw.text((x_i + (card_w - (is_b[2] - is_b[0])) // 2, y_pos + 78), i_sub, fill="#fbe69b", font=box_sub_font)

    qr_x_i = x_i + (card_w - qr_box_size) // 2
    draw.rounded_rectangle([qr_x_i, y_pos + 130, qr_x_i + qr_box_size, y_pos + 130 + qr_box_size], radius=16, fill="#ffffff")
    qr_i_resized = img_insta.resize((410, 410), Image.Resampling.LANCZOS)
    standee.paste(qr_i_resized, (qr_x_i + 20, y_pos + 150), qr_i_resized)

    # 1. Thinner 1px gold outline button pill
    draw.rounded_rectangle([x_i + 80, y_pos + 625, x_i + card_w - 80, y_pos + 685], radius=30, fill="#120205", outline="#d4af37", width=1)
    if os.path.exists("instagram_icon.png"):
        i_ico = Image.open("instagram_icon.png").convert("RGBA").resize((32, 32), Image.Resampling.LANCZOS)
        standee.paste(i_ico, (x_i + 95, y_pos + 644), i_ico)
    i_lbl = "Instagram Reels"
    draw.text((x_i + 145, y_pos + 643), i_lbl, fill="#ffffff", font=box_sub_font)

    i_btn = "📸 Scan for Instagram"
    ibtn_b = draw.textbbox((0, 0), i_btn, font=box_sub_font)
    draw.text((x_i + (card_w - (ibtn_b[2] - ibtn_b[0])) // 2, y_pos + 735), i_btn, fill="#fbe69b", font=box_sub_font)

    # 2. Bottom address/phone spacing: tighter & elegant
    loc = cfg.get("address", "28 Paarroo, Old Palasia, Indore")
    loc_b = draw.textbbox((0, 0), loc, font=footer_font)
    draw.text(((w - (loc_b[2] - loc_b[0])) // 2, 1375), loc, fill="#cfb8bd", font=footer_font)

    phone = cfg.get("phoneButtonText", "Call / Reservation: 90559 66555")
    ph_b = draw.textbbox((0, 0), phone, font=phone_font)
    draw.text(((w - (ph_b[2] - ph_b[0])) // 2, 1415), phone, fill="#ffffff", font=phone_font)

    thanks = "Thank You For Visiting 28 Paarroo 🌴"
    th_b = draw.textbbox((0, 0), thanks, font=thanks_font)
    draw.text(((w - (th_b[2] - th_b[0])) // 2, 1475), thanks, fill="#fbe69b", font=thanks_font)

    standee.save("standee_dual_direct_static.png", "PNG", dpi=(300, 300))

if __name__ == "__main__":
    generate_all_assets()
