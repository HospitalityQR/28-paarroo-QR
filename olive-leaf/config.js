// =============================================================================
// 🌿 OLIVE LEAF - RESTAURANT & QR CODE CONFIGURATION SETTINGS
// =============================================================================
// Sirf yahan details badlein — Poora webpage, standee aur links automatically update ho jayenge!
// Is restaurant ka kisi dusre restaurant se koi lena-dena nahi hai (100% Isolated).
// =============================================================================

var RESTAURANT_CONFIG = {
    // 1. Restaurant Basic Details
    restaurantId: "olive-leaf",
    restaurantName: "Olive Leaf",
    tagline: "Pure Vegetarian • Fine Dining",
    logoImage: "logo.png",

    // 2. Standee & QR Mode:
    // "dual_link"   -> Single QR opens the Landing Page (both Google & Instagram buttons)
    // "google_only" -> Single QR opens Google Review directly (Static)
    // "insta_only"  -> Single QR opens Instagram directly (Static)
    qrMode: "dual_link",

    // 3. Standee Premium Text
    standeeHeading: "SCAN TO CONNECT",
    standeeSubheading: "Rate Us on Google • Follow Us on Instagram",

    // 4. Google Review Link & Luxury Text
    googleReviewLink: "https://share.google/CAuKpe2Po706mPhkI",
    googleRatingText: "Rate Us on Google",
    googleRatingSubtext: "Share your experience on Google",

    // 5. Instagram Link & Profile Handle
    instagramLink: "https://www.instagram.com/oliveleafindore?stkn=MXduZGk2ZzU3emZjdw==",
    instagramUsername: "@oliveleafindore",
    instagramActionText: "Follow Us on Instagram",
    instagramSubtext: "@oliveleafindore • Food, Reels & Updates",

    // 6. Contact & Location Details
    phoneNumber: "9993896969",
    phoneButtonText: "Call / Reservation: 9993896969",
    address: "Shop No.9, 10 Ground Floor, Skye Corporate Park, Scheme No. 78, Vijay Nagar, Indore",

    // 7. Footer Message (Italic Gold)
    footerThanks: "Thank You For Dining With Us 🌿",
    footerCity: "Crafted with care in Indore",

    // 8. Hosted Landing Page URL on all-restaurant-qr-
    landingPageUrl: "https://namangarg-06.github.io/all-restaurant-qr-/olive-leaf/"
};

if (typeof module !== 'undefined' && module.exports) {
    module.exports = RESTAURANT_CONFIG;
}
