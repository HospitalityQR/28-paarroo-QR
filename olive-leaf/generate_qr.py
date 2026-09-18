"""
All-in-One Luxury QR Code & Standee Generator for Olive Leaf Restaurant
- 100% Isolated to Olive Leaf
- Supports 4 Standee Types:
  1. Primary Standee (Dual Link Landing Page or Single Mode) -> table_standee_printable.png
  2. Dual Direct Static Standee (Google & Insta side-by-side) -> standee_dual_direct_static.png
  3. Google Review Only Standee -> standee_google_direct.png
  4. Instagram Only Standee -> standee_instagram_direct.png
"""

import sys
import os
import re
import math
import qrcode
from PIL import Image, ImageDraw, ImageFont

def load_config():
    config = {
        "restaurantName": "Olive Leaf",
        "tagline": "PURE VEGETARIAN • FINE DINING",
        "qrMode": "dual_link",
        "landingPageUrl": "https://namangarg-06.github.io/all-restaurant-qr-/olive-leaf/",
        "googleReviewLink": "https://share.google/CAuKpe2Po706mPhkI",
        "instagramLink": "https://www.instagram.com/oliveleafindore?stkn=MXduZGk2ZzU3emZjdw==",
        "phoneNumber": "9993896969",
        "phoneButtonText": "Call / Reservation: 9993896969",
        "address": "Shop 9, 10 Ground Floor, Skye Corporate Park, Scheme No. 78, Vijay Nagar, Indore",
        "footerThanks": "Thank You For Dining With Us 🌿"
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

def draw_gold_leaf(draw, cx, cy, size, fill_color):
    draw.polygon([
        (cx - size * 0.7, cy + size * 0.5),
        (cx - size * 0.2, cy - size * 0.3),
        (cx + size * 0.9, cy - size * 0.8),
        (cx + size * 0.4, cy + size * 0.1)
    ], fill=fill_color)
    draw.polygon([
        (cx - size * 0.4, cy + size * 0.7),
        (cx - size * 0.7, cy + size * 0.2),
        (cx - size * 0.1, cy - size * 0.1),
        (cx + size * 0.1, cy + size * 0.3)
    ], fill=fill_color)
    draw.line([(cx - size * 0.9, cy + size * 0.85), (cx + size * 0.3, cy - size * 0.2)], fill=fill_color, width=2)

def make_qr_image(url, fill_color="#08130d", back_color="#ffffff", box_size=20):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=3,
    )
    qr.add_data(url)
    qr.make(fit=True)
    return qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGBA")

def generate_all_assets():
    cfg = load_config()
    print(f"[*] Generating assets for {cfg['restaurantName']} (Mode: {cfg['qrMode']})...")

    landing_url = cfg["landingPageUrl"]
    google_url = cfg["googleReviewLink"]
    insta_url = cfg["instagramLink"]

    img_landing = make_qr_image(landing_url, fill_color="#000000")
    img_landing.save("qr_landing_page.png", "PNG")

    img_google = make_qr_image(google_url, fill_color="#08130d")
    img_google.save("qr_google_direct.png", "PNG")

    img_insta = make_qr_image(insta_url, fill_color="#08130d")
    img_insta.save("qr_instagram_direct.png", "PNG")

    # Luxury styled QR
    img_lux = make_qr_image(landing_url, fill_color="#10251a")
    img_lux.save("qr_olive_leaf_luxury.png", "PNG")

    mode = cfg.get("qrMode", "dual_link").lower()
    if mode == "google_only":
        primary_qr = img_google
        primary_inst = "RATE US 5-STARS ON GOOGLE"
        primary_badge_ico = "google_icon.png"
        primary_badge_txt = "Google 5-Star Reviews"
    elif mode == "insta_only":
        primary_qr = img_insta
        primary_inst = "FOLLOW US ON INSTAGRAM"
        primary_badge_ico = "instagram_icon.png"
        primary_badge_txt = "Follow @oliveleafindore"
    else: # "dual_link"
        primary_qr = img_landing
        primary_inst = "SCAN TO CONNECT"
        primary_badge_ico = None
        primary_badge_txt = "Google Reviews • Instagram"

    primary_qr.save("qr_code.png", "PNG")
    primary_qr.save("qr_standard.png", "PNG")

    # 2. Generate Primary Standee
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

    # 3. Generate Dual Direct Static Standee (Google & Insta side-by-side)
    generate_dual_standee_card(img_google, img_insta, cfg)

    # 4. Generate Dedicated Google Standee
    generate_single_direct_standee(
        img_google,
        title="RATE US ON GOOGLE",
        tagline="SHARE YOUR 5-STAR EXPERIENCE",
        badge_icon="google_icon.png",
        badge_text="Google 5-Star Reviews",
        out_filenames=["standee_google_direct.png"]
    )

    # 5. Generate Dedicated Instagram Standee
    generate_single_direct_standee(
        img_insta,
        title="FOLLOW US ON INSTAGRAM",
        tagline="@OLIVELEAFINDORE • REELS & UPDATES",
        badge_icon="instagram_icon.png",
        badge_text="Follow @oliveleafindore",
        out_filenames=["standee_instagram_direct.png"]
    )

    print("  [+] All standees and QR codes generated successfully for Olive Leaf!")

def get_fonts():
    try:
        instruction_font = ImageFont.truetype("arialbd.ttf", 46)
        sub_font = ImageFont.truetype("arial.ttf", 28)
        badge_font = ImageFont.truetype("arialbd.ttf", 26)
        footer_font = ImageFont.truetype("arial.ttf", 27)
        thanks_font = ImageFont.truetype("georgiai.ttf", 40)
        box_title_font = ImageFont.truetype("arialbd.ttf", 36)
        box_sub_font = ImageFont.truetype("arial.ttf", 26)
    except Exception:
        instruction_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()
        badge_font = ImageFont.load_default()
        footer_font = ImageFont.load_default()
        thanks_font = ImageFont.load_default()
        box_title_font = ImageFont.load_default()
        box_sub_font = ImageFont.load_default()
    return instruction_font, sub_font, badge_font, footer_font, thanks_font, box_title_font, box_sub_font

def generate_dual_link_standee(qr_img, cfg):
    w, h = 1200, 1800
    standee = Image.new("RGB", (w, h), "#08130d")
    draw = ImageDraw.Draw(standee)

    border_margin = 45
    draw.rectangle([border_margin, border_margin, w - border_margin, h - border_margin], outline="#d4af37", width=4)
    draw.rectangle([border_margin + 12, border_margin + 12, w - border_margin - 12, h - border_margin - 12], outline="#f7e092", width=2)

    instruction_font, sub_font, badge_font, footer_font, thanks_font, _, _ = get_fonts()

    if os.path.exists("logo.png"):
        logo = Image.open("logo.png").convert("RGBA")
        logo_w = 420
        logo_h = int(logo_w * (logo.height / logo.width))
        logo_resized = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
        card_pad = 18
        cw = logo_w + card_pad * 2
        ch = logo_h + card_pad * 2
        cx = (w - cw) // 2
        cy = 125
        draw.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=20, fill="#ffffff", outline="#d4af37", width=3)
        standee.paste(logo_resized, (cx + card_pad, cy + card_pad), logo_resized)

    tag_text = cfg.get("tagline", "PURE VEGETARIAN • FINE DINING").replace("*", "•")
    tb2 = draw.textbbox((0, 0), tag_text, font=sub_font)
    draw.text(((w - (tb2[2] - tb2[0])) // 2, 365), tag_text, fill="#f7e092", font=sub_font)

    inst_text = "SCAN TO CONNECT"
    ib = draw.textbbox((0, 0), inst_text, font=instruction_font)
    draw.text(((w - (ib[2] - ib[0])) // 2, 435), inst_text, fill="#ffffff", font=instruction_font)

    g_text = "Rate Us on Google"
    i_text = "Follow Us on Instagram"
    gb_box = draw.textbbox((0, 0), g_text, font=badge_font)
    g_badge_w = (gb_box[2] - gb_box[0]) + 72 + 24
    g_badge_h = 62

    ib_box = draw.textbbox((0, 0), i_text, font=badge_font)
    i_badge_w = (ib_box[2] - ib_box[0]) + 72 + 24
    i_badge_h = 62

    gap = 24
    total_badges_w = g_badge_w + i_badge_w + gap
    start_badges_x = (w - total_badges_w) // 2
    badges_y = 515

    draw.rounded_rectangle(
        [start_badges_x, badges_y, start_badges_x + g_badge_w, badges_y + g_badge_h],
        radius=31, fill="#0f251a", outline="#d4af37", width=2
    )
    if os.path.exists("google_icon.png"):
        g_ico = Image.open("google_icon.png").convert("RGBA").resize((40, 40), Image.Resampling.LANCZOS)
        standee.paste(g_ico, (start_badges_x + 16, badges_y + 11), g_ico)
    draw.text((start_badges_x + 72, badges_y + 16), g_text, fill="#ffffff", font=badge_font)

    insta_x = start_badges_x + g_badge_w + gap
    draw.rounded_rectangle(
        [insta_x, badges_y, insta_x + i_badge_w, badges_y + i_badge_h],
        radius=31, fill="#0f251a", outline="#d4af37", width=2
    )
    if os.path.exists("instagram_icon.png"):
        i_ico = Image.open("instagram_icon.png").convert("RGBA").resize((40, 40), Image.Resampling.LANCZOS)
        standee.paste(i_ico, (insta_x + 16, badges_y + 11), i_ico)
    draw.text((insta_x + 72, badges_y + 16), i_text, fill="#ffffff", font=badge_font)

    qr_card_size = 710
    qr_card_x = (w - qr_card_size) // 2
    qr_card_y = 630
    draw.rounded_rectangle(
        [qr_card_x, qr_card_y, qr_card_x + qr_card_size, qr_card_y + qr_card_size],
        radius=30, fill="#ffffff", outline="#d4af37", width=5
    )
    qr_resized = qr_img.resize((630, 630), Image.Resampling.LANCZOS)
    standee.paste(qr_resized, (qr_card_x + 40, qr_card_y + 40), qr_resized)

    line1 = "Shop 9, 10 Ground Floor, Skye Corporate Park"
    l1_b = draw.textbbox((0, 0), line1, font=footer_font)
    draw.text(((w - (l1_b[2] - l1_b[0])) // 2, 1445), line1, fill="#8ca398", font=footer_font)

    line2 = "Scheme No. 78, Vijay Nagar, Indore - 452010"
    l2_b = draw.textbbox((0, 0), line2, font=footer_font)
    draw.text(((w - (l2_b[2] - l2_b[0])) // 2, 1490), line2, fill="#8ca398", font=footer_font)

    phone_text = cfg.get("phoneButtonText", "Call / Reservation: 9993896969")
    pb = draw.textbbox((0, 0), phone_text, font=footer_font)
    draw.text(((w - (pb[2] - pb[0])) // 2, 1538), phone_text, fill="#c9d8d0", font=footer_font)

    thanks_text = "Thank You For Dining With Us"
    thb = draw.textbbox((0, 0), thanks_text, font=thanks_font)
    text_width = thb[2] - thb[0]
    total_thanks_width = text_width + 20 + 28
    thanks_start_x = (w - total_thanks_width) // 2
    thanks_y = 1625
    draw.text((thanks_start_x, thanks_y), thanks_text, fill="#f7e092", font=thanks_font)
    draw_gold_leaf(draw, thanks_start_x + text_width + 30, thanks_y + 20, 28, "#d4af37")

    standee.save("table_standee_printable.png", "PNG", dpi=(300, 300))
    standee.save("front_page_standee.png", "PNG", dpi=(300, 300))

def generate_single_direct_standee(qr_img, title, tagline, badge_icon, badge_text, out_filenames):
    cfg = load_config()
    w, h = 1200, 1800
    standee = Image.new("RGB", (w, h), "#08130d")
    draw = ImageDraw.Draw(standee)

    border_margin = 45
    draw.rectangle([border_margin, border_margin, w - border_margin, h - border_margin], outline="#d4af37", width=4)
    draw.rectangle([border_margin + 12, border_margin + 12, w - border_margin - 12, h - border_margin - 12], outline="#f7e092", width=2)

    instruction_font, sub_font, badge_font, footer_font, thanks_font, _, _ = get_fonts()

    if os.path.exists("logo.png"):
        logo = Image.open("logo.png").convert("RGBA")
        logo_w = 420
        logo_h = int(logo_w * (logo.height / logo.width))
        logo_resized = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
        card_pad = 18
        cw = logo_w + card_pad * 2
        ch = logo_h + card_pad * 2
        cx = (w - cw) // 2
        cy = 125
        draw.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=20, fill="#ffffff", outline="#d4af37", width=3)
        standee.paste(logo_resized, (cx + card_pad, cy + card_pad), logo_resized)

    tb2 = draw.textbbox((0, 0), tagline, font=sub_font)
    draw.text(((w - (tb2[2] - tb2[0])) // 2, 365), tagline, fill="#f7e092", font=sub_font)

    ib = draw.textbbox((0, 0), title, font=instruction_font)
    draw.text(((w - (ib[2] - ib[0])) // 2, 435), title, fill="#ffffff", font=instruction_font)

    bb = draw.textbbox((0, 0), badge_text, font=badge_font)
    b_w = (bb[2] - bb[0]) + 80
    b_h = 62
    b_x = (w - b_w) // 2
    b_y = 515
    draw.rounded_rectangle([b_x, b_y, b_x + b_w, b_y + b_h], radius=31, fill="#0f251a", outline="#d4af37", width=2)
    if badge_icon and os.path.exists(badge_icon):
        ico = Image.open(badge_icon).convert("RGBA").resize((40, 40), Image.Resampling.LANCZOS)
        standee.paste(ico, (b_x + 16, b_y + 11), ico)
    draw.text((b_x + 72, b_y + 16), badge_text, fill="#ffffff", font=badge_font)

    qr_card_size = 710
    qr_card_x = (w - qr_card_size) // 2
    qr_card_y = 630
    draw.rounded_rectangle(
        [qr_card_x, qr_card_y, qr_card_x + qr_card_size, qr_card_y + qr_card_size],
        radius=30, fill="#ffffff", outline="#d4af37", width=5
    )
    qr_resized = qr_img.resize((630, 630), Image.Resampling.LANCZOS)
    standee.paste(qr_resized, (qr_card_x + 40, qr_card_y + 40), qr_resized)

    line1 = "Shop 9, 10 Ground Floor, Skye Corporate Park"
    l1_b = draw.textbbox((0, 0), line1, font=footer_font)
    draw.text(((w - (l1_b[2] - l1_b[0])) // 2, 1445), line1, fill="#8ca398", font=footer_font)

    line2 = "Scheme No. 78, Vijay Nagar, Indore - 452010"
    l2_b = draw.textbbox((0, 0), line2, font=footer_font)
    draw.text(((w - (l2_b[2] - l2_b[0])) // 2, 1490), line2, fill="#8ca398", font=footer_font)

    phone_text = cfg.get("phoneButtonText", "Call / Reservation: 9993896969")
    pb = draw.textbbox((0, 0), phone_text, font=footer_font)
    draw.text(((w - (pb[2] - pb[0])) // 2, 1538), phone_text, fill="#c9d8d0", font=footer_font)

    thanks_text = "Thank You For Dining With Us"
    thb = draw.textbbox((0, 0), thanks_text, font=thanks_font)
    text_width = thb[2] - thb[0]
    total_thanks_width = text_width + 20 + 28
    thanks_start_x = (w - total_thanks_width) // 2
    thanks_y = 1625
    draw.text((thanks_start_x, thanks_y), thanks_text, fill="#f7e092", font=thanks_font)
    draw_gold_leaf(draw, thanks_start_x + text_width + 30, thanks_y + 20, 28, "#d4af37")

    for fn in out_filenames:
        standee.save(fn, "PNG", dpi=(300, 300))

def generate_dual_standee_card(img_google, img_insta, cfg):
    w, h = 1400, 1800
    standee = Image.new("RGB", (w, h), "#0c1812")
    draw = ImageDraw.Draw(standee)

    draw.rectangle([40, 40, w - 40, h - 40], outline="#d4af37", width=4)
    draw.rectangle([52, 52, w - 52, h - 52], outline="#f7e092", width=1)

    try:
        title_font = ImageFont.truetype("times.ttf", 82)
        sub_font = ImageFont.truetype("arial.ttf", 32)
        box_title_font = ImageFont.truetype("arialbd.ttf", 36)
        box_sub_font = ImageFont.truetype("arial.ttf", 26)
        footer_font = ImageFont.truetype("arial.ttf", 28)
    except Exception:
        title_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()
        box_title_font = ImageFont.load_default()
        box_sub_font = ImageFont.load_default()
        footer_font = ImageFont.load_default()

    title = "OLIVE LEAF"
    tb = draw.textbbox((0, 0), title, font=title_font)
    draw.text(((w - (tb[2] - tb[0])) // 2, 140), title, fill="#f7e092", font=title_font)

    sub = "RESTAURANT & CAFE • INDORE"
    sb = draw.textbbox((0, 0), sub, font=sub_font)
    draw.text(((w - (sb[2] - sb[0])) // 2, 250), sub, fill="#c9d8d0", font=sub_font)

    tag = "PURE VEGETARIAN • FINE DINING"
    tag_b = draw.textbbox((0, 0), tag, font=box_sub_font)
    draw.text(((w - (tag_b[2] - tag_b[0])) // 2, 310), tag, fill="#d4af37", font=box_sub_font)

    card_w, card_h = 550, 820
    y_pos = 430

    # Google Card (Left)
    x_g = 110
    draw.rounded_rectangle([x_g, y_pos, x_g + card_w, y_pos + card_h], radius=24, fill="#142c20", outline="#d4af37", width=2)
    g_title = "RATE US 5-STARS"
    gt_b = draw.textbbox((0, 0), g_title, font=box_title_font)
    draw.text((x_g + (card_w - (gt_b[2] - gt_b[0])) // 2, y_pos + 40), g_title, fill="#ffffff", font=box_title_font)
    g_sub = "Google Reviews"
    gs_b = draw.textbbox((0, 0), g_sub, font=box_sub_font)
    draw.text((x_g + (card_w - (gs_b[2] - gs_b[0])) // 2, y_pos + 95), g_sub, fill="#f7e092", font=box_sub_font)

    qr_box_size = 440
    qr_x_g = x_g + (card_w - qr_box_size) // 2
    draw.rounded_rectangle([qr_x_g, y_pos + 160, qr_x_g + qr_box_size, y_pos + 160 + qr_box_size], radius=16, fill="#ffffff")
    qr_g_resized = img_google.resize((400, 400), Image.Resampling.LANCZOS)
    standee.paste(qr_g_resized, (qr_x_g + 20, y_pos + 180), qr_g_resized)

    g_btn = "⭐ Scan For Review"
    gbtn_b = draw.textbbox((0, 0), g_btn, font=box_sub_font)
    draw.text((x_g + (card_w - (gbtn_b[2] - gbtn_b[0])) // 2, y_pos + 720), g_btn, fill="#ffffff", font=box_sub_font)

    # Instagram Card (Right)
    x_i = 740
    draw.rounded_rectangle([x_i, y_pos, x_i + card_w, y_pos + card_h], radius=24, fill="#142c20", outline="#d4af37", width=2)
    i_title = "FOLLOW US"
    it_b = draw.textbbox((0, 0), i_title, font=box_title_font)
    draw.text((x_i + (card_w - (it_b[2] - it_b[0])) // 2, y_pos + 40), i_title, fill="#ffffff", font=box_title_font)
    i_sub = "@oliveleafindore"
    is_b = draw.textbbox((0, 0), i_sub, font=box_sub_font)
    draw.text((x_i + (card_w - (is_b[2] - is_b[0])) // 2, y_pos + 95), i_sub, fill="#f7e092", font=box_sub_font)

    qr_x_i = x_i + (card_w - qr_box_size) // 2
    draw.rounded_rectangle([qr_x_i, y_pos + 160, qr_x_i + qr_box_size, y_pos + 160 + qr_box_size], radius=16, fill="#ffffff")
    qr_i_resized = img_insta.resize((400, 400), Image.Resampling.LANCZOS)
    standee.paste(qr_i_resized, (qr_x_i + 20, y_pos + 180), qr_i_resized)

    i_btn = "📸 Scan For Instagram"
    ibtn_b = draw.textbbox((0, 0), i_btn, font=box_sub_font)
    draw.text((x_i + (card_w - (ibtn_b[2] - ibtn_b[0])) // 2, y_pos + 720), i_btn, fill="#ffffff", font=box_sub_font)

    thanks = "Thank You For Visiting Olive Leaf!"
    th_b = draw.textbbox((0, 0), thanks, font=box_title_font)
    draw.text(((w - (th_b[2] - th_b[0])) // 2, 1420), thanks, fill="#f7e092", font=box_title_font)

    loc = "Ground Floor, Skye Corporate Park, Scheme 78, Vijay Nagar, Indore"
    loc_b = draw.textbbox((0, 0), loc, font=footer_font)
    draw.text(((w - (loc_b[2] - loc_b[0])) // 2, 1500), loc, fill="#8ca398", font=footer_font)

    standee.save("standee_dual_direct_static.png", "PNG", dpi=(300, 300))

if __name__ == "__main__":
    generate_all_assets()
