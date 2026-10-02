"""Builds the static HTML pages of the MatchCam site.

Usage (from the repository root or anywhere):
    python3 scripts/build_site.py

Pages are written to the repository root, because their URLs are public
(App Store, Google Play, Google OAuth consent screen and in-app links).
Styles and images live in assets/ and are not generated.
"""
import pathlib
UPDATED = "September 29, 2026"
EMAIL = "matchcam2026@gmail.com"
POLICY_VERSION = "1.0"
PRIVACY_VERSION = "1.0"
PRIVACY_UPDATED = "October 1, 2026"
PAGES = [("index.html","Home"),("features.html","Features"),("support.html","Support"),("privacy.html","Privacy"),("terms.html","Terms")]

def page(file, title, desc, body):
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{f}"{cur if f==file else ""}>{n}</a>' for f,n in PAGES)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="assets/css/style.css">
<link rel="icon" type="image/png" href="assets/icons/favicon.png">
<link rel="apple-touch-icon" href="assets/icons/apple-touch-icon.png">
</head>
<body>
<header class="site-header">
  <div class="inner">
    <a class="brand" href="index.html"><img src="assets/images/wordmark.png" alt="MatchCam" height="44"></a>
    <nav>{nav}</nav>
  </div>
</header>
<main>
{body}
</main>
<footer>
  <p>© 2026 Daniel Osorio · <a href="features.html">Features</a> · <a href="privacy.html">Privacy Policy</a> · <a href="terms.html">Terms of Use</a> · <a href="support.html">Support</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</footer>
</body>
</html>
'''

index = f'''<div class="hero">
  <img src="assets/images/logo.png" alt="MatchCam app icon" width="120" height="120">
  <div class="text">
    <h1>Record every match with a live scoreboard.</h1>
    <p class="lead">MatchCam records volleyball matches on your iPhone or Android phone with the score burned into the video, marks every rally, and turns them into highlights you can share.</p>
    <p><a class="button" href="features.html">See all features and Free vs Pro</a></p>
  </div>
</div>

<h2>Record</h2>
<div class="features">
  <div class="card"><h3>Live scoreboard in the video</h3><p>Team names and colors, score, sets and match timer are recorded into the video, so every clip shows the score. A small MatchCam watermark sits in the corner.</p></div>
  <div class="card"><h3>Sharp recording</h3><p>1080p on iPhone and up to 4K on Android, with zoom, pause/resume and audio.</p></div>
  <div class="card"><h3>Crash recovery</h3><p>If the app is interrupted while recording, the recorded segments are recovered into one video on the next launch.</p></div>
  <div class="card"><h3>Pause and timeouts</h3><p>Pause and resume without splitting the video. A 30-second timeout pauses the recording until the next point.</p></div>
</div>

<h2>Keep score</h2>
<div class="features">
  <div class="card"><h3>Scorekeeper mode</h3><p>Keep score without recording, with set history and a scoreboard you can share as an image.</p></div>
  <div class="card"><h3>Be the remote</h3><p>Use your phone as a wireless remote for a phone recording with MatchCam Pro. Pair with a QR code and a 6-digit PIN; iPhone and Android work together.</p></div>
  <div class="card"><h3>Apple Watch</h3><p>Score, run the timer, call timeouts and mark rallies from your wrist.</p></div>
  <div class="card"><h3>Volleyball rules</h3><p>Official best-of-3 or best-of-5, or custom sets, points, tie-break and cap. Automatic set and match detection and a side-swap button.</p></div>
</div>

<h2>After the match</h2>
<div class="features">
  <div class="card"><h3>Rallies</h3><p>Mark the rallies that matter during the match, then review, favorite and trim each clip.</p></div>
  <div class="card"><h3>Match history</h3><p>Every match is saved with per-set scores, duration, video and rallies. Link a YouTube or other video link to any match.</p></div>
  <div class="card"><h3>Annotate a video from another camera</h3><p>Kept score without recording? Link a video from your library and add the points while you watch it.</p></div>
  <div class="card"><h3>Tournaments</h3><p>Organize matches by tournament and round, with brackets and results saved automatically.</p></div>
</div>

<h2>MatchCam Pro</h2>
<div class="features">
  <div class="card"><h3>YouTube upload</h3><p>Upload a match to your own channel with the title, description and set chapters filled in, and keep a tournament's matches in one playlist.</p></div>
  <div class="card"><h3>Live streaming</h3><p>Stream the match with the scoreboard to YouTube Live, Twitch or any RTMP server while you record.</p></div>
  <div class="card"><h3>Remote Connect</h3><p>Let other phones control the score and recording over Wi-Fi. The phones that connect as a remote don't need Pro.</p></div>
  <div class="card"><h3>Highlight reel</h3><p>Export your marked rallies as a single highlight video.</p></div>
  <div class="card"><h3>Scoreboard export</h3><p>Export an annotated video from another camera with the scoreboard burned in.</p></div>
  <div class="card"><h3>Backup &amp; restore</h3><p>Export your match history to iCloud Drive, Google Drive or any cloud storage and restore it on a new phone.</p></div>
</div>
<p>MatchCam Pro is a monthly or yearly subscription. Compare <a href="features.html#compare">Free and Pro</a>, or see the <a href="terms.html">Terms of Use</a>.</p>

<h2>Requirements</h2>
<ul>
  <li>iPhone with iOS 26 or later. Apple Watch is optional.</li>
  <li>Android phone with Android 8.0 or later.</li>
  <li>Remote control and live streaming need a Wi-Fi or internet connection.</li>
</ul>
<p>Questions? Visit <a href="support.html">Support</a>.</p>'''

privacy = f'''<h1>Privacy Policy</h1>
<p class="meta"><span class="version">Version {PRIVACY_VERSION}</span>Effective {PRIVACY_UPDATED} · <a href="#version-history">Version history</a></p>
<p>MatchCam is made by Daniel Osorio ("we"). This policy explains what the app does with your data.</p>

<h2>Data stored on your device</h2>
<p>Match recordings, scores, rally marks and tournament data are stored only on your device, and videos are saved to your Camera Roll or Gallery. We do not run servers and we do not receive this data.</p>

<h2>Local network and Apple Watch</h2>
<p>When you pair a remote controller, match state (scores, team names, timer) is shared over your local Wi-Fi network between your own devices only, protected by a 6-digit PIN. With an Apple Watch, the same match state is synced between your iPhone and your watch.</p>

<h2>Live streaming (optional)</h2>
<p>If you start a live stream, the video and audio are sent directly from your device to the streaming server you configure (for example YouTube Live or Twitch). The stream URL and key you enter are stored only on your device. We do not receive the stream; the streaming service's own terms and privacy policy apply.</p>

<h2>Backups and sharing (optional)</h2>
<p>When you export a backup, share a scoreboard image or share a video, the file goes only where you choose (for example iCloud Drive, Google Drive or a messaging app). We do not receive it.</p>

<h2>YouTube uploads (MatchCam Pro, optional)</h2>
<p>If you choose to connect a YouTube account, MatchCam uses YouTube API Services. By using this feature you agree to the <a href="https://www.youtube.com/t/terms">YouTube Terms of Service</a>. Google's use of your data is described in the <a href="http://www.google.com/policies/privacy">Google Privacy Policy</a>.</p>
<h3>What MatchCam accesses, and why</h3>
<ul>
  <li><strong>Upload videos to your YouTube channel</strong> (youtube.upload): to upload the match video you select, with the title, description and settings you review before each upload. MatchCam never uploads anything without your action.</li>
  <li><strong>Manage your YouTube account</strong> (youtube): to show which channel is connected and whether it can upload videos longer than 15 minutes, to list your playlists and create a playlist when you ask for one, to add the uploaded video to the playlist you choose, to show YouTube's processing result for videos MatchCam uploaded, and to check that those videos and playlists still exist. MatchCam does not change or delete any other content in your account.</li>
  <li><strong>Your Google account email</strong>: to show which account is connected.</li>
</ul>
<h3>What MatchCam stores, and for how long</h3>
<ul>
  <li>An access grant managed by Google's sign-in library on your device (iOS Keychain or Google Play services).</li>
  <li>For each video MatchCam uploaded: the YouTube video ID and link, the upload date and YouTube's processing status. For playlists you use with a tournament: the playlist ID and title. This stays on your device. It is refreshed at least every 30 days while your account is connected, and deleted if the video or playlist no longer exists or if it has not been refreshed for 30 days.</li>
  <li>The video file is read from your device and sent directly to YouTube. It is never sent to us.</li>
</ul>
<h3>What MatchCam does not do</h3>
<ul>
  <li>It does not send your YouTube data or videos to us or to any third party other than Google/YouTube.</li>
  <li>It does not use your data for advertising or tracking.</li>
</ul>
<p>MatchCam's use and transfer of information received from Google APIs adheres to the <a href="https://developers.google.com/terms/api-services-user-data-policy">Google API Services User Data Policy</a>, including the Limited Use requirements.</p>
<h3>Deleting your data and revoking access</h3>
<p>In MatchCam, go to Settings → YouTube → Disconnect YouTube. This revokes MatchCam's access at Google immediately and deletes every YouTube datum MatchCam stored, including the links it created. You can also revoke access at any time at <a href="https://security.google.com/settings/security/permissions">security.google.com/settings/security/permissions</a>. Your videos and playlists stay on YouTube; manage them in YouTube Studio.</p>

<h2>Purchases</h2>
<p>MatchCam Pro subscriptions are processed by Apple (App Store) or Google (Google Play). We do not receive your payment details.</p>

<h2>Children</h2>
<p>MatchCam is a tool for coaches, parents and players who record matches. It does not knowingly collect personal data from children. If you record or publish minors, you are responsible for having the consent of their parents or guardians and of your club.</p>

<h2>Changes</h2>
<p>When MatchCam's data practices change, we publish a new version of this policy with a new version number and effective date, and list what changed below. If a change affects data already collected, we will also tell you in the app.</p>

<h2>Contact</h2>
<p>Questions, complaints or deletion requests: <a href="mailto:{EMAIL}">{EMAIL}</a>. We answer within 7 days.</p>

<h2 id="version-history">Version history</h2>
<table>
  <tr><th>Version</th><th>Effective</th><th>Changes</th></tr>
  <tr><td>{PRIVACY_VERSION}</td><td>{PRIVACY_UPDATED}</td><td>First published version.</td></tr>
</table>'''

terms = f'''<h1>Terms of Use</h1>
<p class="meta"><span class="version">Version {POLICY_VERSION}</span>Effective {UPDATED} · <a href="#version-history">Version history</a></p>
<p>These terms apply to the MatchCam app for iPhone, Apple Watch and Android ("MatchCam"), made by Daniel Osorio ("we"). By using MatchCam you agree to them. If you downloaded MatchCam from the App Store, Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Standard End User License Agreement</a> also applies; if these terms conflict with it, the Apple agreement prevails for App Store users.</p>

<h2>License</h2>
<p>We grant you a personal, non-exclusive, non-transferable license to use MatchCam on devices you own or control. You may not copy, modify, reverse engineer or resell the app, except where the law allows it.</p>

<h2>MatchCam Pro subscriptions</h2>
<ul>
  <li>MatchCam Pro is an auto-renewable subscription, offered monthly or yearly. The price is shown in the app before you buy.</li>
  <li>Payment is charged to your Apple ID or Google Play account when you confirm the purchase.</li>
  <li>The subscription renews automatically unless you turn off auto-renew at least 24 hours before the end of the current period. Your account is charged for renewal within 24 hours before the end of the current period.</li>
  <li>You can manage or cancel your subscription in your App Store or Google Play account settings. Refunds are handled by Apple or Google under their policies.</li>
</ul>

<h2>Your content and the people you record</h2>
<p>You own the videos and data you create with MatchCam. You are responsible for having the right to record, keep and publish them, including the consent of the players you record and, for minors, of their parents or guardians and of your club or league. Follow the rules of the venue and the competition.</p>

<h2>YouTube</h2>
<p>The YouTube upload feature uses YouTube API Services. When you use it, you also agree to the <a href="https://www.youtube.com/t/terms">YouTube Terms of Service</a>, and your uploads are subject to YouTube's policies, including its rules on content made for kids. You choose the title, description, visibility, audience and playlist of every upload. See our <a href="privacy.html">Privacy Policy</a> for the data involved.</p>

<h2>Availability and changes</h2>
<p>We may update, change or stop features, including features that depend on third-party services such as YouTube. We will try to give notice of changes that affect paid features.</p>

<h2>Disclaimer</h2>
<p>MatchCam is provided "as is". We do not guarantee that it will be error-free or that recordings will never be lost. Keep backups of videos that matter to you.</p>

<h2>Limitation of liability</h2>
<p>To the extent the law allows, we are not liable for indirect or consequential damages, or for lost recordings or data. Our total liability is limited to the amount you paid for MatchCam in the 12 months before the claim.</p>

<h2>Governing law</h2>
<p>These terms are governed by the laws of the Province of British Columbia and the federal laws of Canada that apply there, without affecting consumer rights you have where you live.</p>

<h2>Contact</h2>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>

<h2 id="version-history">Version history</h2>
<table>
  <tr><th>Version</th><th>Effective</th><th>Changes</th></tr>
  <tr><td>{POLICY_VERSION}</td><td>{UPDATED}</td><td>First published version.</td></tr>
</table>'''

support = f'''<h1>Support</h1>
<p class="lead">Need help? Email <a href="mailto:{EMAIL}">{EMAIL}</a>. Include your phone model, the app version (Settings → About) and what happened. We answer within 7 days.</p>
<p>Jump to: <a href="#start">Getting started</a> · <a href="#recording">Recording</a> · <a href="#scoring">Scoring and remote control</a> · <a href="#watch">Apple Watch</a> · <a href="#after">After the match</a> · <a href="#youtube">YouTube</a> · <a href="#pro">MatchCam Pro</a> · <a href="#data">Your data</a> · <a href="#trouble">Troubleshooting</a></p>

<h2 id="start">Getting started</h2>
<h3>How do I record my first match?</h3>
<p>On the Game Setup screen, enter the team names and colors and choose the rules (official best-of-3 or best-of-5, or custom). Tap to start recording, hold the phone in landscape, and keep score with the buttons next to the camera view.</p>
<h3>Can I keep score without recording?</h3>
<p>Yes. Use Scorekeeper mode. The match is saved to your history, and you can link a video later.</p>

<h2 id="recording">Recording</h2>
<h3>Where are my videos saved?</h3>
<p>In your Camera Roll (iPhone) or Gallery (Android). Scores, rallies and match details are saved in the app.</p>
<h3>What video quality does MatchCam record?</h3>
<p>1080p on iPhone, and up to 4K on Android. A full match can take several GB, so make sure you have free space before you start.</p>
<h3>Can I pause the recording?</h3>
<p>Yes. Pause and resume during the match; it stays one video. Calling a 30-second timeout also pauses the recording until the next point.</p>
<h3>The app closed while recording. Did I lose the video?</h3>
<p>Usually not. Open MatchCam again: it detects the recorded segments and lets you recover them into one video or discard them.</p>
<h3>Why is there a MatchCam watermark?</h3>
<p>A small watermark in the corner is part of every recorded video.</p>
<h3>How do I live stream a match?</h3>
<p>Live streaming is a MatchCam Pro feature. In Settings → Live Streaming, enter the RTMP server URL and stream key from YouTube Live, Twitch or another service. The stream includes the scoreboard. You need a stable internet connection.</p>

<h2 id="scoring">Scoring and remote control</h2>
<h3>How do I use a second phone as a remote?</h3>
<p>Both phones need MatchCam and the same Wi-Fi network. The recording phone needs MatchCam Pro (Remote Connect); the phones used as a remote don't. On the recording phone start the remote server; on the other phone choose the controller role and scan the QR code or pick the recorder from the list, then enter the 6-digit PIN. iPhone and Android phones can pair with each other.</p>
<h3>The controller can't find the recorder.</h3>
<p>Check that both phones are on the same Wi-Fi (not a guest network that isolates devices), that MatchCam has Local Network permission on iPhone (Settings → Privacy &amp; Security → Local Network), and try the QR code instead of the list.</p>
<h3>How do I fix a wrong point or swap sides?</h3>
<p>Use the minus button to remove a point. The swap button flips the home and guest sides without changing names or scores.</p>

<h2 id="watch">Apple Watch</h2>
<h3>What can I do from the watch?</h3>
<p>Keep score, run the timer, call timeouts and mark rallies. The watch stays in sync with your iPhone while the iPhone app is open.</p>

<h2 id="after">After the match</h2>
<h3>How do I mark and review rallies?</h3>
<p>Tap the heart during the match (on the phone, the watch or the remote). After the match, open the match in History → Rallies to watch, favorite and trim each clip.</p>
<h3>How do I make a highlight reel?</h3>
<p>In Rallies, tap Highlight Reel to export all your marked rallies as one video (MatchCam Pro).</p>
<h3>I kept score but recorded with another camera. Can I add the scoreboard?</h3>
<p>Yes. Open the match in History and choose Annotate External Video, pick the video from your library and tap the points while it plays. Exporting the finished video with the scoreboard is a MatchCam Pro feature.</p>
<h3>How do I link or unlink a video link?</h3>
<p>In the match details, Link Video attaches a YouTube or other link. Unlink removes the link from the match; the video itself is not deleted.</p>
<h3>How do tournaments work?</h3>
<p>Create a tournament, add rounds and matches, and start each match from the bracket. Results are saved to the tournament automatically.</p>

<h2 id="youtube">YouTube</h2>
<h3>How do I upload a match to YouTube?</h3>
<p>With MatchCam Pro, open a match with a video and tap Upload to YouTube. The first time, connect your YouTube account. Review the title, description, visibility, audience and playlist, then upload. You can leave the app while it uploads.</p>
<h3>Why is my YouTube upload private?</h3>
<p>MatchCam uploads as Private by default so you can review the video first. Change the visibility in YouTube Studio when you're ready to share it.</p>
<h3>"This YouTube account can't upload videos longer than 15 minutes"</h3>
<p>YouTube only accepts videos longer than 15 minutes from accounts that verified a phone number, and match videos are almost always longer. You can:</p>
<ul>
  <li>Verify the account at <a href="https://www.youtube.com/verify">youtube.com/verify</a> (free, takes a minute) and tap Check Again in MatchCam.</li>
  <li>Or connect a different YouTube account that is already verified (Use Another Account).</li>
</ul>
<h3>My channel doesn't appear when I connect</h3>
<p>Extra channels on a Google account are Brand Accounts. Google only lists the ones where you are an Owner or Manager of the Brand Account at <a href="https://myaccount.google.com/brandaccounts">myaccount.google.com/brandaccounts</a>; access given only in YouTube Studio is not enough. Ask the channel owner to add you there, then disconnect and connect again in MatchCam.</p>
<h3>"Your Google account has no YouTube channel yet"</h3>
<p>Create a channel at <a href="https://www.youtube.com/create_channel">youtube.com/create_channel</a> and try again.</p>
<h3>Can I upload with the YouTube app instead?</h3>
<p>Yes. Copy YouTube Details gives you the suggested title and a description with the set timestamps to paste in the YouTube app.</p>
<h3>Is this video made for kids?</h3>
<p>You decide. "Made for kids" turns off comments, notifications and personalized ads on the video. For Private uploads you can set it later in YouTube Studio. Publish players only with the consent of their parents or guardians and your club.</p>

<h2 id="pro">MatchCam Pro</h2>
<h3>What does MatchCam Pro include?</h3>
<p>YouTube upload, live streaming, Remote Connect (other phones as remotes), highlight reels, scoreboard export of videos from another camera, and backup and restore.</p>
<h3>How do I restore MatchCam Pro on a new phone?</h3>
<p>Settings → Pro → Restore Purchases, signed in with the same Apple ID or Google account you used to buy it.</p>
<h3>How do I cancel?</h3>
<p>On iPhone: Settings app → your name → Subscriptions. On Android: Google Play → Profile → Payments &amp; subscriptions → Subscriptions.</p>
<h3>Do you have promo codes?</h3>
<p>If you received one, use Settings → Pro → Redeem Promo Code.</p>

<h2 id="data">Your data</h2>
<h3>How do I move my matches to a new phone?</h3>
<p>Settings → Backup → Export Backup on the old phone, save the file to a cloud drive, then Import Backup on the new phone (MatchCam Pro). Videos move with your photo library, not with the backup.</p>
<h3>How do I disconnect YouTube or delete MatchCam's YouTube data?</h3>
<p>Settings → YouTube → Disconnect YouTube. See the <a href="privacy.html">Privacy Policy</a> for details.</p>
<h3>Can I delete all my data?</h3>
<p>Settings → Data → Delete All Data removes match history and tournaments from the app. Videos in your Camera Roll or Gallery are not affected.</p>

<h2 id="trouble">Troubleshooting</h2>
<h3>The camera or microphone doesn't work</h3>
<p>Allow Camera and Microphone for MatchCam in your phone's Settings, then reopen the app. Close other apps that may be using the camera.</p>
<h3>I don't see upload or export progress on Android</h3>
<p>Allow notifications for MatchCam. Uploads and exports keep running in the background with a progress notification.</p>
<h3>The phone gets hot or the battery drains during long matches</h3>
<p>Recording with a live scoreboard is demanding. Use a power bank, avoid direct sun and lower the screen brightness.</p>'''

def feat(title, tier, platforms, text):
    tag = '<span class="tag pro">Pro</span>' if tier == "pro" else '<span class="tag free">Free</span>'
    plats = "".join(f"<span>{x}</span>" for x in platforms)
    cls = "card feat is-pro" if tier == "pro" else "card feat"
    return f'<div class="{cls}"><div class="feat-top"><h3>{title}</h3>{tag}</div>{text}<div class="platforms">{plats}</div></div>'

P, A, W = "iPhone", "Android", "Apple Watch"
FEATURE_GROUPS = [
  ("record", "Record", "The scoreboard is burned into the video while you film.", [
    feat("Scoreboard overlay", "free", [P, A], "<p>Team names and colors, points, sets won, set history and the match clock are drawn into every frame, with the MatchCam watermark in the corner.</p>"),
    feat("HD and 4K recording", "free", [P, A], "<ul><li>iPhone: 1080p, ultra-wide camera when available.</li><li>Android: up to 4K (3840×2160), H.265 or H.264.</li><li>Zoom, audio, pause and resume in one video.</li></ul>"),
    feat("Timeout countdown", "free", [P, A, W], "<p>A 30-second countdown on screen. Recording pauses and resumes on the next point.</p>"),
    feat("Crash recovery", "free", [P, A], "<p>If the app closes mid-match, the recorded segments are found on the next launch and can be merged into one video or discarded.</p>"),
    feat("Live streaming", "pro", [P, A], "<p>Stream the camera with the scoreboard to YouTube Live, Twitch or any RTMP server. Add the server URL and stream key in Settings, then tap Go Live while recording.</p>"),
  ]),
  ("score", "Keep score", "Volleyball rules built in.", [
    feat("Match setup", "free", [P, A, W], "<ul><li>Home and guest names and colors, remembered between matches.</li><li>Official rules: best of 3 or best of 5.</li><li>Custom rules: sets, points per set, tie-break points, hard cap or win by 2.</li></ul>"),
    feat("Scorekeeper mode", "free", [P, A], "<p>Keep score without the camera. Set wins are detected for you, with Finish Set, Undo Set and a shareable scoreboard image with the match duration.</p>"),
    feat("Side swap", "free", [P, A], "<p>Flip home and guest sides when teams change ends, without changing names or scores.</p>"),
  ]),
  ("devices", "Watch and remotes", "Score from your wrist or from another phone.", [
    feat("Apple Watch", "free", [W], "<ul><li>Add or remove points, finish and undo sets.</li><li>Start, pause and stop the iPhone recording and timer.</li><li>Mark rallies and call timeouts.</li><li>Start Offline to score a match on the watch alone.</li></ul>"),
    feat("Phone as a remote", "free", [P, A], "<p>Control a recording phone from another phone over Wi-Fi: points, recording, timer, rallies and reset. Connect with a QR code, the nearby list or an IP address, and pair with a 6-digit PIN. iPhone and Android work together.</p>"),
    feat("Remote Connect", "pro", [P, A], "<p>Let other phones control the recording phone. Pro is needed only on the phone that records; the phones used as a remote stay free.</p>"),
  ]),
  ("review", "Review", "Find the plays that matter.", [
    feat("Rally marking", "free", [P, A, W], "<p>Tap the ♥ on the phone, the watch or a remote to mark a rally. Taps within 5 seconds count as one mark.</p>"),
    feat("Rallies and clips", "free", [P, A], "<p>Watch every marked rally, filter favorites, trim a clip within ±30 seconds and save it as its own video.</p>"),
    feat("Match stats", "free", [P, A], "<p>Score progression and a set-by-set breakdown for each saved match.</p>"),
    feat("Annotate a video from another camera", "free", [P, A], "<p>Link a video from your library to a scorekeeper match, play it at 1× or 2× and tap the points as they happen. MatchCam suggests the end of each set and warns when the score doesn't match.</p>"),
    feat("Highlight reel", "pro", [P, A], "<p>Join all marked rallies of a match into one video, in order, ready to share.</p>"),
    feat("Scoreboard export", "pro", [P, A], "<p>Export an annotated video from another camera with the scoreboard burned in: whole match or one set, up to 1080p, original audio kept. Keeps going in the background.</p>"),
  ]),
  ("history", "History and tournaments", "Every match is saved automatically.", [
    feat("Match history", "free", [P, A], "<p>Set-by-set scores, duration, the recorded video, the rules used and the rallies of each match.</p>"),
    feat("Tournaments", "free", [P, A], "<p>Build a tournament with rounds and matches, start a match from the bracket and get the result saved back automatically.</p>"),
    feat("Video links", "free", [P, A], "<p>Attach a YouTube, Vimeo or Drive link to a match, watch YouTube links inside the app, and unlink when needed. The video itself is never deleted.</p>"),
  ]),
  ("share", "Share", "From the court to YouTube.", [
    feat("YouTube upload", "pro", [P, A], "<ul><li>Upload to your channel from the match or right after recording.</li><li>Title and description with the result and set chapters, ready to edit.</li><li>Private by default; pick a playlist or create one (tournament name suggested).</li><li>Resumes after a lost connection; Wi-Fi only option.</li></ul>"),
    feat("Copy YouTube details", "pro", [P, A], "<p>Prefer the YouTube app? Get the title and a description with set timestamps (for example “0:42 Set 1 (25-21)”), edit them and copy.</p>"),
    feat("Scoreboard image", "free", [P, A], "<p>Share a clean image of the final scoresheet.</p>"),
  ]),
  ("data", "Your data", "Stays on your device unless you move it.", [
    feat("Backup &amp; restore", "pro", [P, A], "<p>Export match history to iCloud Drive, Google Drive or any cloud storage and import it on a new phone. Videos move with your photo library.</p>"),
    feat("Export and delete", "free", [P, A], "<p>Export match history as a JSON file, or delete all matches and tournaments. Videos in Photos or Gallery are not touched.</p>"),
  ]),
]

COMPARE = [
  ("Recording with scoreboard overlay, timeouts, crash recovery", True),
  ("Scorekeeper mode, rules setup, side swap", True),
  ("Apple Watch scoring and recording control", True),
  ("Using your phone as a remote", True),
  ("Rally marking, rally clips and trimming", True),
  ("Match history, stats, tournaments, video links", True),
  ("Annotating a video from another camera", True),
  ("Export history as JSON, delete all data", True),
  ("YouTube upload and Copy YouTube details", False),
  ("Live streaming", False),
  ("Remote Connect (the recording phone accepts remotes)", False),
  ("Highlight reel", False),
  ("Scoreboard export of videos from another camera", False),
  ("Backup &amp; restore", False),
]

jump = " · ".join(f'<a href="#{gid}">{name}</a>' for gid, name, _, _ in FEATURE_GROUPS) + ' · <a href="#compare">Free vs Pro</a>'
groups_html = "\n".join(
    f'<h2 id="{gid}">{name}</h2>\n<p class="muted">{sub}</p>\n<div class="features">\n  ' + "\n  ".join(items) + "\n</div>"
    for gid, name, sub, items in FEATURE_GROUPS)
rows = "\n".join(
    f'  <tr><td>{label}</td><td class="c {"yes" if free else "no"}">{"✓" if free else "—"}</td><td class="c yes">✓</td></tr>'
    for label, free in COMPARE)

features = f'''<h1>Features</h1>
<p class="lead">Everything MatchCam does on iPhone, Android and Apple Watch. Recording and scoring a match is free; <span class="tag pro">Pro</span> features publish, connect or protect your matches.</p>
<p class="jump">{jump}</p>

{groups_html}

<h2 id="compare">Free vs Pro</h2>
<div class="table-wrap">
<table class="compare">
  <tr><th>Feature</th><th class="c">Free</th><th class="c">Pro</th></tr>
{rows}
</table>
</div>
<p>MatchCam Pro is a monthly or yearly subscription through the App Store or Google Play. See the <a href="terms.html">Terms of Use</a>.</p>

<h2>Requirements</h2>
<ul>
  <li>iPhone with iOS 26 or later. Apple Watch with watchOS 26 or later is optional.</li>
  <li>Android phone with Android 8.0 or later.</li>
  <li>Remotes, live streaming and YouTube upload need Wi-Fi or an internet connection. YouTube needs a verified account for videos longer than 15 minutes.</li>
</ul>
<p>Questions? Visit <a href="support.html">Support</a>.</p>'''

out = pathlib.Path(__file__).resolve().parent.parent
for f, t, d, b in [
    ("index.html", "MatchCam", "Record volleyball matches with a live scoreboard, mark rallies and upload to YouTube.", index),
    ("features.html", "MatchCam Features", "Every MatchCam feature on iPhone, Android and Apple Watch, with a Free vs Pro comparison.", features),
    ("privacy.html", "MatchCam Privacy Policy", "How the MatchCam app handles your data, including YouTube uploads.", privacy),
    ("terms.html", "MatchCam Terms of Use", "Terms of use for the MatchCam app and MatchCam Pro subscriptions.", terms),
    ("support.html", "MatchCam Support", "Help and answers for MatchCam.", support),
]:
    (out / f).write_text(page(f, t, d, b))
print(f"Built {len(PAGES)} pages in {out}")
