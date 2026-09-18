// =============================================================================
// 🌴 28 PAARROO - RESTAURANT & QR CODE CONFIGURATION SETTINGS
// =============================================================================
// Sirf yahan details badlein — Poora webpage, standee aur links automatically update ho jayenge!
// Is restaurant ka kisi dusre restaurant se koi lena-dena nahi hai (100% Isolated).
// =============================================================================

var RESTAURANT_CONFIG = {
    // 1. Restaurant Basic Details
    restaurantId: "28-paarroo",
    restaurantName: "28 Paarroo",
    tagline: "South Indian & Multi-Cuisine • Pure Veg",
    logoImage: "logo_with_gold_rim.png",

    // 2. Standee & QR Mode:
    // "dual_link"   -> Single QR opens the Landing Page (both Google & Instagram buttons)
    // "google_only" -> Single QR opens Google Review directly (Static)
    // "insta_only"  -> Single QR opens Instagram directly (Static)
    qrMode: "google_only",

    // 3. Standee Premium Text
    standeeHeading: "SCAN TO CONNECT",
    standeeSubheading: "Rate Us on Google • Follow Us on Instagram",

    // 4. Google Review Link & Luxury Text
    googleReviewLink: "https://share.google/ao3kZ8lE7ug4gjlHP",
    googleRatingText: "Rate Us on Google",
    googleRatingSubtext: "Share your 5-Star experience on Google",

    // 5. Instagram Link & Profile Handle
    instagramLink: "https://www.instagram.com/28paarroo?stkn=MTI4Y2NwcW5iNTRl",
    instagramUsername: "@28paarroo",
    instagramActionText: "Follow Us on Instagram",
    instagramSubtext: "@28paarroo • Food, Reels & Updates",

    // 6. Contact & Location Details
    phoneNumber: "9055966555",
    phoneDisplay: "90559 66555",
    phoneButtonText: "Call / Reservation: 90559 66555",
    address: "28 Paarroo, Old Palasia, Indore",
    fullAddress: "UG-01, Nikita Apartment, Old Palasia / AB Road, Indore, Madhya Pradesh",

    // 7. Footer Message (Italic Gold)
    footerThanks: "Thank You For Visiting 28 Paarroo 🌴",
    footerCity: "Crafted with care in Indore",

    // 8. Hosted Landing Page URL on All-Restaurants-QR-
    landingPageUrl: "https://namangarg-06.github.io/All-Restaurants-QR-/28-paarroo/"
};

if (typeof module !== 'undefined' && module.exports) {
    module.exports = RESTAURANT_CONFIG;
}
