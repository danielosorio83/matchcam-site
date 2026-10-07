"""Builds the static HTML pages of the MatchCam site.

Usage (from the repository root or anywhere):
    python3 scripts/build_site.py

Pages are written to the repository root, because their URLs are public
(App Store, Google Play, Google OAuth consent screen and in-app links).
Styles, fonts and images live in assets/ and are not generated.
"""
import pathlib
UPDATED = "September 29, 2026"
EMAIL = "support@matchcam.app"
POLICY_VERSION = "1.0"
PRIVACY_VERSION = "1.0"
PRIVACY_UPDATED = "October 1, 2026"
PAGES = [("index.html","Home"),("features.html","Features"),("how-to.html","How to"),("pro.html","Pro"),("support.html","Support")]

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
<a class="skip" href="#content">Skip to content</a>
<header class="site-header">
  <div class="inner">
    <a class="brand" href="index.html" aria-label="MatchCam home"><img src="assets/images/logo.png" alt="" width="44" height="44"><span class="wordmark"><span class="match">Match</span><span class="cam">Cam</span></span></a>
    <nav aria-label="Main">{nav}</nav>
  </div>
</header>
<main id="content">
{body}
</main>
<footer>
  <div class="inner">
    <p class="links"><a href="features.html">Features</a><a href="how-to.html">How to</a><a href="pro.html">Pro</a><a href="support.html">Support</a><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Use</a></p>
    <p>© 2026 Daniel Osorio · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </div>
</footer>
</body>
</html>
'''

CONSENT_POINTS = '''<ul>
    <li>Recordings are for personal use.</li>
    <li>I have the permission of everyone involved, including the parents or guardians of minors.</li>
    <li>I will not use MatchCam to upload content other than what it is designed for: volleyball matches and their highlights.</li>
  </ul>'''

index = f'''<section class="hero">
  <div>
    <h1>Record every match with the score on screen.</h1>
    <p class="lead">MatchCam films volleyball on your iPhone or Android phone with a live scoreboard burned into the video. Mark the rallies that matter and turn them into clips you can share.</p>
    <div class="cta">
      <a class="button" href="features.html">See what it does</a>
      <a class="button ghost" href="how-to.html">How it works</a>
    </div>
  </div>
  <div class="court" role="img" aria-label="Illustration of a MatchCam scoreboard over a volleyball court">
    <div class="rec"><i></i>REC 24:31</div>
    <div class="scoreboard">
      <div class="team"><span class="swatch" style="background:#E5384B"></span>APEX</div>
      <div class="pts">18<span class="sets">SET 2</span>15</div>
      <div class="team right">BNSS<span class="swatch" style="background:#1F6FEB"></span></div>
    </div>
  </div>
</section>

<h2>Three ways to play a match</h2>
<div class="modes">
  <div class="mode"><h3>Record</h3><p>Film the match with the scoreboard in the video. Free.</p></div>
  <div class="mode"><h3>Scorekeeper</h3><p>Keep score without the camera, then add video later. Free.</p></div>
  <div class="mode"><h3>Remote</h3><p>Score from a second phone while the first one records. Free to control; the recording phone needs Pro.</p></div>
</div>

<h2>On the court</h2>
<div class="features">
  <div class="card"><h3>Live scoreboard in the video</h3><p>Team names and colors, points, sets and the match clock are drawn into every frame, so every clip shows the score.</p></div>
  <div class="card"><h3>Sharp, in one file</h3><p>Record in 4K, 1080p or 720p with zoom and audio. Pause and resume without splitting the video.</p></div>
  <div class="card"><h3>Volleyball rules built in</h3><p>Best of 3 or 5, or your own sets and points. Sets and matches end on their own, with a side-swap button and a 60-second timeout.</p></div>
  <div class="card"><h3>Apple Watch</h3><p>Score, run the timer, call timeouts and mark rallies from your wrist.</p></div>
</div>

<h2>After the whistle</h2>
<div class="features">
  <div class="card"><h3>Rally highlights</h3><p>Tap the heart during the match to mark a rally. Afterwards, trim each one and save it as its own clip.</p></div>
  <div class="card"><h3>Teams, seasons and rivals</h3><p>Set up your team once with its colors for each season. Rivals are remembered as you play them.</p></div>
  <div class="card"><h3>Tournaments</h3><p>Plan rounds and matches, see what is next on Home, and have results saved back to the tournament.</p></div>
  <div class="card"><h3>History and stats</h3><p>Every match keeps its set scores, duration, video and rallies. Link a YouTube video to any match.</p></div>
</div>

<section class="consent" aria-labelledby="first-record">
  <h2 id="first-record">Before you record your first match</h2>
  <p>The first time you record, MatchCam asks you to confirm and accept the Terms of Use. You agree that:</p>
  {CONSENT_POINTS}
  <p>You can read this again any time in Settings &rarr; Help &rarr; Review recording terms. <a href="terms.html#recording-terms">Read the recording terms</a>.</p>
</section>

<h2>MatchCam Pro</h2>
<p>Recording and scoring a match is free. Pro adds the extras that publish, connect or protect your matches: YouTube upload, live streaming, the Clip Editor and highlight reel, Remote Connect and backup.</p>
<p><a class="button" href="pro.html">Compare Free and Pro</a></p>

<h2>Requirements</h2>
<ul>
  <li>iPhone with iOS 26 or later. Apple Watch is optional.</li>
  <li>Android phone with Android 8.0 or later.</li>
  <li>Remote control, live streaming and YouTube upload need Wi-Fi or an internet connection.</li>
</ul>
<p>Questions? Visit <a href="support.html">Support</a>.</p>'''

privacy = f'''<h1>Privacy Policy</h1>
<p class="meta"><span class="version">Version {PRIVACY_VERSION}</span>Effective {PRIVACY_UPDATED} · <a href="#version-history">Version history</a></p>
<p>MatchCam is made by Daniel Osorio ("we"). This policy explains what the app does with your data.</p>

<h2>Data stored on your device</h2>
<p>Match recordings, scores, rally marks and tournament data are stored only on your device, and videos are saved to your Camera Roll or Gallery. We do not run servers and we do not receive this data.</p>

<h2>Local network and Apple Watch</h2>
<p>When you connect a remote controller, match state (scores, team names, timer) is shared over your local Wi-Fi network between your own devices only. With an Apple Watch, the same match state is synced between your iPhone and your watch.</p>

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
<p>In MatchCam, go to Settings → Connections → Disconnect YouTube. This revokes MatchCam's access at Google immediately and deletes every YouTube datum MatchCam stored, including the links it created. You can also revoke access at any time at <a href="https://security.google.com/settings/security/permissions">security.google.com/settings/security/permissions</a>. Your videos and playlists stay on YouTube; manage them in YouTube Studio.</p>

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

<h2 id="recording-terms">Recording terms</h2>
<p>Before your first recording, MatchCam asks you to confirm and accept that:</p>
<ul>
  <li>Recordings are for personal use.</li>
  <li>You have the permission of everyone involved, including the parents or guardians of minors.</li>
  <li>You will not use MatchCam to upload content other than what it is designed for: volleyball matches and their highlights.</li>
</ul>
<p>You can read them again in the app under Settings &rarr; Help &rarr; Review recording terms. If these terms change, the app asks you to accept them again.</p>

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
<p class="lead">Need help? Email <a href="mailto:{EMAIL}">{EMAIL}</a>. Include your phone model, the app version (Settings &rarr; About) and what happened. We answer within 7 days.</p>
<p class="jump">Jump to: <a href="#start">Getting started</a> · <a href="#recording">Recording</a> · <a href="#scoring">Scoring and remote control</a> · <a href="#watch">Apple Watch</a> · <a href="#after">After the match</a> · <a href="#youtube">YouTube</a> · <a href="#pro">MatchCam Pro</a> · <a href="#data">Your data</a> · <a href="#trouble">Troubleshooting</a>. Step-by-step guides are in <a href="how-to.html">How to</a>.</p>

<h2 id="start">Getting started</h2>
<h3>How do I record my first match?</h3>
<p>On Home tap Start recording (or open the Record tab). In New match choose the Record mode, enter the team names and colors and choose the rules. Tap Start recording, hold the phone in landscape and keep score with the buttons next to the camera view. The first time, you read and accept the recording terms.</p>
<h3>Why does MatchCam ask me to accept terms before recording?</h3>
<p>To confirm that recordings are for personal use, that you have the permission of everyone involved (including the parents or guardians of minors) and that you will use MatchCam only for volleyball matches and their highlights. You see it once, and again only if the terms change. Read them in Settings &rarr; Help &rarr; Review recording terms or on the <a href="terms.html#recording-terms">Terms of Use</a>.</p>
<h3>Can I keep score without recording?</h3>
<p>Yes. Choose the Scorekeeper mode in New match. The match is saved to your history, and you can link or annotate a video later.</p>

<h2 id="recording">Recording</h2>
<h3>Where are my videos saved?</h3>
<p>In your Camera Roll (iPhone) or Gallery (Android). Scores, rallies and match details are saved in the app.</p>
<h3>What video quality does MatchCam record?</h3>
<p>iPhone: 4K, 1080p or 720p, depending on what your iPhone supports. Android: 720p, 1080p or 4K. Both start at 1080p, record in HEVC at 30 fps on iPhone, and use HEVC or H.264 on Android. A full match can take several GB, and MatchCam will not start a recording with less than 3 GB free.</p>
<h3>Can I pause the recording?</h3>
<p>Yes. Pause and resume during the match; it stays one video.</p>
<h3>How do timeouts work?</h3>
<p>A timeout lasts 60 seconds. The video keeps the first 3 seconds with a timeout banner, then the recording pauses. It resumes after 60 seconds, as soon as a point is scored, or when you tap Resume Now.</p>
<h3>The app closed while recording. Did I lose the video?</h3>
<p>Usually not. Home shows the unsaved recording with a Review button. There you can re-merge the segments into one video or delete them.</p>
<h3>Why is there a MatchCam watermark?</h3>
<p>A small watermark in the corner is part of every recorded video, including with MatchCam Pro.</p>
<h3>How do I live stream a match?</h3>
<p>Live streaming is a MatchCam Pro feature. In Settings &rarr; Live Streaming, enter the RTMP server URL and stream key from YouTube Live, Twitch or another service. Then tap Go Live while recording. The stream includes the scoreboard. You need a stable internet connection.</p>

<h2 id="scoring">Scoring and remote control</h2>
<h3>How do I use a second phone as a remote?</h3>
<p>Both phones need MatchCam and the same Wi-Fi network. The recording phone needs MatchCam Pro; the phone used as a remote doesn't. On the recording phone, open the Remote chip and tap Start Remote Server (Start Server on Android). On the other phone, choose the Remote mode in New match, tap Connect, then pick the recorder under Found Recorders or enter its IP address. iPhone and Android phones can control each other.</p>
<h3>The controller can't find the recorder.</h3>
<p>Check that both phones are on the same Wi-Fi (not a guest network that isolates devices), that MatchCam has Local Network permission on iPhone (Settings &rarr; Privacy &amp; Security &rarr; Local Network), and try Enter IP Address instead of the list.</p>
<h3>Can the remote mark rallies?</h3>
<p>No. The remote controls points, sets, the timer, timeouts, swapping sides and recording. Mark rallies on the recording phone or on the Apple Watch.</p>
<h3>How do I fix a wrong point or swap sides?</h3>
<p>Use the minus button to remove a point. The swap button flips the home and guest sides without changing names or scores.</p>

<h2 id="watch">Apple Watch</h2>
<h3>How do I link my Apple Watch?</h3>
<p>Install MatchCam on the Watch paired with your iPhone and open it. There is no pairing step: when you start a match on the iPhone, the Watch moves into it. New match on the iPhone shows Watch Connected.</p>
<h3>What can I do from the Watch?</h3>
<p>Keep score, run the timer, start, pause and stop the recording, call timeouts (while the iPhone is recording), finish or undo sets and mark rallies. To score a match on the Watch alone, tap Start on Watch.</p>

<h2 id="after">After the match</h2>
<h3>How do I mark and review rallies?</h3>
<p>Tap the heart while recording and choose Previous Rally (the one that just ended) or This Rally (the one in play, saved when it ends). On the Watch, tap Mark Rally. After the match, open History, choose the match and tap View Rallies.</p>
<h3>How do I save a rally as a clip?</h3>
<p>In Rallies, open a rally and choose Trim Clip. Set the start and end within 30 seconds of the recorded rally, tap Save, then Export Clip to save it to Photos or Gallery. This is free. The Clip Editor (MatchCam Pro) combines several rallies into one video in 16:9 or vertical 9:16.</p>
<h3>How do I make a highlight reel?</h3>
<p>In Rallies, tap Highlight Reel to join all your marked rallies into one video (MatchCam Pro).</p>
<h3>I kept score but recorded with another camera. Can I add the scoreboard?</h3>
<p>Yes. Open the match in History and choose Annotate External Video, pick the video from your library and tap the points while it plays. Exporting the finished video with the scoreboard is a MatchCam Pro feature.</p>
<h3>How do I link or unlink a video?</h3>
<p>In the match details, Link Video lets you paste a link for free. With MatchCam Pro you can also choose a video from your YouTube account. Unlink removes the link from the match; the video itself is not deleted.</p>
<h3>How do tournaments work?</h3>
<p>Create a tournament, add rounds, then add matches to each round. Open a scheduled match's menu and choose Start Recording or Scorekeeper Only. The result is saved to the tournament, whose status moves from Upcoming to In progress to Completed. The next scheduled match appears on Home as Next up.</p>

<h2 id="youtube">YouTube</h2>
<h3>How do I upload a match to YouTube?</h3>
<p>With MatchCam Pro, open the match in History and tap Upload to YouTube. The first time, connect your YouTube account. Review the title, description, visibility, audience and playlist, then upload. Matches upload one at a time in a queue, and an upload resumes after a lost connection.</p>
<h3>Where do I follow my uploads?</h3>
<p>On Home while uploads are running, or in Settings &rarr; Connections &rarr; Upload Queue, where you can pause, retry, reorder or cancel.</p>
<h3>Why is my YouTube upload private?</h3>
<p>MatchCam uploads as Private by default so you can review the video first. Until YouTube completes its review of MatchCam, uploads also stay private if you pick Public or Unlisted. Change the visibility in YouTube Studio when you're ready to share it.</p>
<h3>"This YouTube account can't upload videos longer than 15 minutes"</h3>
<p>YouTube only accepts videos longer than 15 minutes from accounts that verified a phone number, and match videos are almost always longer. You can:</p>
<ul>
  <li>Verify the account at <a href="https://www.youtube.com/verify">youtube.com/verify</a> (free, takes a minute) and tap I Verified It &mdash; Check Again in MatchCam.</li>
  <li>Or connect a different YouTube account that is already verified (Use Another Account).</li>
</ul>
<h3>My channel doesn't appear when I connect</h3>
<p>Extra channels on a Google account are Brand Accounts. Google only lists the ones where you are an Owner or Manager of the Brand Account at <a href="https://myaccount.google.com/brandaccounts">myaccount.google.com/brandaccounts</a>; access given only in YouTube Studio is not enough. Ask the channel owner to add you there, then disconnect and connect again in MatchCam.</p>
<h3>"Your Google account has no YouTube channel yet"</h3>
<p>Create a channel at <a href="https://www.youtube.com/create_channel">youtube.com/create_channel</a> and try again.</p>
<h3>Can I upload with the YouTube app instead?</h3>
<p>Yes. Copy YouTube Details gives you the suggested title and a description with the set timestamps to paste in the YouTube app.</p>
<h3>Is this video made for kids?</h3>
<p>You decide. "Made for kids" turns off comments, notifications and personalized ads on the video. Publish players only with the consent of their parents or guardians and your club.</p>

<h2 id="pro">MatchCam Pro</h2>
<h3>What does MatchCam Pro include?</h3>
<p>YouTube upload, live streaming, the Clip Editor and highlight reel, Remote Connect (the recording phone accepts remotes), scoreboard export of videos from another camera, and backup and restore. See <a href="pro.html">Free vs Pro</a>.</p>
<h3>How do I restore MatchCam Pro on a new phone?</h3>
<p>Open Settings and tap Upgrade to Pro, then Restore Purchases, signed in with the same Apple ID or Google account you used to buy it. If you are already Pro, open MatchCam Pro in Settings and choose Restore purchases.</p>
<h3>How do I cancel?</h3>
<p>On iPhone: Settings app &rarr; your name &rarr; Subscriptions. On Android: Google Play &rarr; Profile &rarr; Payments &amp; subscriptions &rarr; Subscriptions.</p>
<h3>Do you have promo codes?</h3>
<p>If you received one, tap Upgrade to Pro in Settings, then Redeem Promo Code.</p>

<h2 id="data">Your data</h2>
<h3>How do I move my matches to a new phone?</h3>
<p>Settings &rarr; Data &rarr; Export backup on the old phone, save the file to a cloud drive, then Import backup on the new phone (MatchCam Pro). Videos move with your photo library, not with the backup.</p>
<h3>How do I disconnect YouTube or delete MatchCam's YouTube data?</h3>
<p>Settings &rarr; Connections &rarr; Disconnect YouTube. See the <a href="privacy.html">Privacy Policy</a> for details.</p>
<h3>Can I delete all my data?</h3>
<p>Settings &rarr; Delete all data removes match history and tournaments from the app. Videos in your Camera Roll or Gallery are not affected.</p>

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
    feat("Scoreboard overlay", "free", [P, A], "<p>Team names and colors, points, sets won and the match clock are drawn into every frame. A small MatchCam watermark sits in the corner and stays on, even with Pro.</p>"),
    feat("4K, 1080p and 720p", "free", [P, A], "<ul><li>iPhone offers 4K, 1080p and 720p, depending on your device. Android offers 720p, 1080p and 4K.</li><li>Starts at 1080p. Zoom, audio, pause and resume in one video.</li></ul>"),
    feat("Timeouts", "free", [P, A, W], "<p>A 60-second timeout. The video keeps 3 seconds with a banner, then the recording pauses and resumes after 60 seconds, on the next point, or when you tap Resume Now.</p>"),
    feat("Crash recovery", "free", [P, A], "<p>If the app closes mid-match, Home shows the unsaved recording. Review it to re-merge the segments into one video, or delete them.</p>"),
    feat("Live streaming", "pro", [P, A], "<p>Stream the camera with the scoreboard to YouTube Live, Twitch or any RTMP server. Add the server URL and stream key in Settings, then tap Go Live while recording.</p>"),
  ]),
  ("score", "Keep score", "Volleyball rules built in.", [
    feat("Match setup", "free", [P, A], "<ul><li>Practice or Tournament matches.</li><li>Official rules: best of 3 or best of 5, sets to 25 and the deciding set to 15, win by 2.</li><li>Custom rules: 1 to 7 sets, points per set, tie-break points and a hard cap.</li></ul>"),
    feat("Scorekeeper mode", "free", [P, A], "<p>Keep score without the camera. Set wins are detected for you, with Finish Set, Undo Set, a Scoreboard tab and a shareable scoreboard image.</p>"),
    feat("Side swap", "free", [P, A], "<p>Flip home and guest sides when teams change ends, without changing names or scores.</p>"),
  ]),
  ("teams", "Teams and rivals", "Set up once, reuse every match.", [
    feat("My team and seasons", "free", [P, A], "<p>Create your team in the Teams tab, then add a season with its category, year and two colors. In New match, pick the season and whether your team plays as Home or Guest.</p>"),
    feat("Rivals", "free", [P, A], "<p>Each rival keeps its name, background color and text color. Add them by hand, or let MatchCam remember them when a match starts. Rival names are suggested as you type.</p>"),
  ]),
  ("devices", "Watch and remotes", "Score from your wrist or from another phone.", [
    feat("Apple Watch", "free", [W], "<ul><li>Add points, finish and undo sets, swap sides.</li><li>Start, pause and stop the iPhone recording and see the timer.</li><li>Mark rallies and call timeouts while the iPhone records.</li><li>Start on Watch scores a match on the Watch alone.</li></ul>"),
    feat("Phone as a remote", "free", [P, A], "<p>Control a recording phone from another phone over Wi-Fi: points, finish or undo a set, timer, timeouts, swapping sides, and start, pause and stop. Find the recorder in the list or enter its IP address. iPhone and Android work together.</p>"),
    feat("Remote Connect", "pro", [P, A], "<p>Let other phones control the recording phone. Pro is needed only on the phone that records; the phones used as a remote stay free.</p>"),
  ]),
  ("review", "Review", "Find the plays that matter.", [
    feat("Rally marking", "free", [P, A, W], "<p>Tap the heart while recording and choose Previous Rally (the one that just ended) or This Rally (the one in play). On the Watch, tap Mark Rally.</p>"),
    feat("Trim a rally clip", "free", [P, A], "<p>Watch every marked rally in View Rallies, trim it within 30 seconds either side, and Export Clip to Photos or Gallery.</p>"),
    feat("Clip Editor", "pro", [P, A], "<p>Pick rallies, reorder and trim them, and choose Standard 16:9 or Short 9:16 (up to 3 minutes). Preview, then save to Photos, share or upload to YouTube.</p>"),
    feat("Highlight reel", "pro", [P, A], "<p>Join all marked rallies of a match into one video, in order, ready to share.</p>"),
    feat("Match stats", "free", [P, A], "<p>Score progression and a set-by-set breakdown for each saved match.</p>"),
    feat("Annotate a video from another camera", "free", [P, A], "<p>Link a video from your library to a scorekeeper match, play it at 1× or 2× and tap the points as they happen. MatchCam suggests the end of each set and warns when the score doesn't match.</p>"),
    feat("Scoreboard export", "pro", [P, A], "<p>Export that annotated video with the scoreboard burned in: whole match or one set, up to 1080p, original audio kept. Keeps going in the background.</p>"),
  ]),
  ("history", "History and tournaments", "Every match is saved automatically.", [
    feat("Match history", "free", [P, A], "<p>Set-by-set scores, duration, the recorded video, the rules used, the recording log and the rallies of each match.</p>"),
    feat("Tournaments", "free", [P, A], "<p>Build a tournament from rounds and matches. Start a scheduled match from its menu as Start Recording or Scorekeeper Only, and its status moves from Upcoming to In progress to Completed. Home shows your next scheduled match.</p>"),
    feat("Video links", "free", [P, A], "<p>Paste a link to attach a video to a match, and unlink when needed. The video itself is never deleted.</p>"),
  ]),
  ("share", "Share", "From the court to YouTube.", [
    feat("YouTube upload", "pro", [P, A], "<ul><li>Upload from a match in History or from the Clip Editor.</li><li>Title and description with the result and set chapters, ready to edit.</li><li>Private by default; pick a playlist or create one.</li><li>A queue sends matches one at a time and resumes after a lost connection. Wi-Fi only option.</li></ul>"),
    feat("Copy YouTube details", "pro", [P, A], "<p>Prefer the YouTube app? Get the title and a description with set timestamps (for example “0:42 Set 1 (25-21)”), edit them and copy.</p>"),
    feat("Choose a video from your YouTube", "pro", [P, A], "<p>Link a video you already uploaded to a match. Pasting a link instead is free.</p>"),
    feat("Scoreboard image", "free", [P, A], "<p>Share a clean image of the final scoresheet.</p>"),
  ]),
  ("data", "Your data", "Stays on your device unless you move it.", [
    feat("Backup &amp; restore", "pro", [P, A], "<p>Export match history to any cloud storage and import it on a new phone from Settings &rarr; Data. Videos move with your photo library.</p>"),
    feat("Export and delete", "free", [P, A], "<p>Export match history as a JSON file, or delete all matches and tournaments. Videos in Photos or Gallery are not touched.</p>"),
  ]),
]

COMPARE = [
  ("Recording with scoreboard overlay, timeouts, crash recovery", True),
  ("Scorekeeper mode, rules setup, side swap", True),
  ("My team, seasons and rivals", True),
  ("Tournaments and match history", True),
  ("Apple Watch scoring and recording control", True),
  ("Using your phone as a remote", True),
  ("Rally marking and trimming a rally clip", True),
  ("Match stats, scoreboard image, video links by pasting a link", True),
  ("Annotating a video from another camera", True),
  ("Export history as JSON, delete all data", True),
  ("YouTube upload, upload queue and Copy YouTube details", False),
  ("Choosing a video from your own YouTube", False),
  ("Clip Editor (Standard and Short formats)", False),
  ("Highlight reel", False),
  ("Live streaming", False),
  ("Remote Connect (the recording phone accepts remotes)", False),
  ("Scoreboard export of videos from another camera", False),
  ("Backup &amp; restore", False),
]

jump = " · ".join(f'<a href="#{gid}">{name}</a>' for gid, name, _, _ in FEATURE_GROUPS)
groups_html = "\n".join(
    f'<h2 id="{gid}">{name}</h2>\n<p class="muted">{sub}</p>\n<div class="features">\n  ' + "\n  ".join(items) + "\n</div>"
    for gid, name, sub, items in FEATURE_GROUPS)
rows = "\n".join(
    f'  <tr><td>{label}</td><td class="c {"yes" if free else "no"}">{'<span aria-hidden="true">✓</span><span class="sr">Included</span>' if free else '<span aria-hidden="true">—</span><span class="sr">Not included</span>'}</td><td class="c yes"><span aria-hidden="true">✓</span><span class="sr">Included</span></td></tr>'
    for label, free in COMPARE)

features = f'''<h1>Features</h1>
<p class="lead">Everything MatchCam does on iPhone, Android and Apple Watch. Recording and scoring a match is free; <span class="tag pro">Pro</span> features publish, connect or protect your matches. See <a href="pro.html">Free vs Pro</a>.</p>
<p class="jump">{jump}</p>

{groups_html}

<h2>Requirements</h2>
<ul>
  <li>iPhone with iOS 26 or later. Apple Watch with watchOS 26 or later is optional.</li>
  <li>Android phone with Android 8.0 or later.</li>
  <li>Remotes, live streaming and YouTube upload need Wi-Fi or an internet connection. YouTube needs a verified account for videos longer than 15 minutes.</li>
</ul>
<p>Questions? Visit <a href="support.html">Support</a>.</p>'''

def howto(title, steps, note=""):
    li = "".join(f"<li>{s}</li>" for s in steps)
    extra = f"<p>{note}</p>" if note else ""
    return f'<details class="howto"><summary>{title}</summary><ol class="steps">{li}</ol>{extra}</details>'

HOWTOS = [
  howto("Record your first match", [
    "On Home tap <strong>Start recording</strong>, or open the <strong>Record</strong> tab. The New match sheet opens.",
    "Set Mode to <strong>Record</strong>.",
    "Enter the <strong>Home Team</strong> and <strong>Guest Team</strong> names and colors. To use a saved team, pick its season under <strong>My team</strong>.",
    "Under Game Format &rarr; <strong>Rules</strong>, choose Official (Best of 3 or 5) or Custom Rules.",
    "Tap <strong>Start recording</strong>. The first time, read <strong>Before you record</strong> and tap <strong>I agree</strong>.",
    "Hold the phone in landscape. Tap the score buttons for points and the heart to mark a rally.",
    "Stop when the match ends. It is saved in <strong>History</strong> and the video goes to Photos or Gallery.",
  ]),
  howto("Set up your team and season", [
    "Open the <strong>Teams</strong> tab, tap <strong>+</strong> and choose <strong>New team</strong>. Enter the name and tap <strong>Add</strong>.",
    "Open the team, then <strong>Manage seasons</strong> &rarr; <strong>Add season</strong>.",
    "Set the <strong>Category</strong>, <strong>Year</strong>, <strong>Color A</strong> and <strong>Color B</strong>, and check the <strong>Preview</strong>.",
    "In New match, choose the season under <strong>My team</strong> and set whether your team plays as Home or Guest.",
  ]),
  howto("Add rivals", [
    "Open <strong>Teams</strong> &rarr; your team &rarr; <strong>Manage rivals</strong>, tap <strong>+</strong> and choose <strong>Add rival</strong>.",
    "Set the name, <strong>Background color</strong> and <strong>Text color</strong>.",
    "Or just type an opponent's name in New match while a season is selected. MatchCam saves it as a rival when the match starts.",
  ]),
  howto("Create a tournament and start a scheduled match", [
    "Open the <strong>Tourneys</strong> tab, tap <strong>+</strong> &rarr; <strong>New Tournament</strong>, enter a name and tap <strong>Create</strong>.",
    "Tap <strong>+ Round</strong> &rarr; <strong>New Round</strong>. Name it, optionally use <strong>Copy Rules From</strong>, then <strong>Add</strong>.",
    "In the round tap <strong>+ Match</strong>, choose Source <strong>Schedule</strong>, pick the teams, turn on <strong>Set Scheduled Date/Time</strong> and tap <strong>Add</strong>.",
    "On match day, the <strong>Next up</strong> card on Home shows the match. <strong>Start this match</strong> opens the tournament.",
    "Open the match menu and choose <strong>Start Recording</strong> (or <strong>Scorekeeper Only</strong>). The result is saved back to the tournament.",
  ], "A tournament is Upcoming until its first match is played, In progress while matches remain, and Completed when none are left."),
  howto("Keep score with Scorekeeper", [
    "In New match, set Mode to <strong>Scorekeeper</strong>, enter the teams and rules, and tap <strong>Start scorekeeping</strong>.",
    "Use + and &minus; for points, and Finish Set or Undo Set when needed.",
    "Open the <strong>Scoreboard</strong> tab and tap <strong>Share scoreboard</strong> to send an image.",
    "Recorded the match on another camera? Later, in History, use <strong>Link Video</strong> or <strong>Annotate External Video</strong>.",
  ]),
  howto("Mark rallies and share a clip", [
    "While recording, tap the <strong>heart</strong> and choose <strong>Previous Rally</strong> (the one that just ended) or <strong>This Rally</strong> (the one in play). On the Apple Watch tap <strong>Mark Rally</strong>.",
    "After the match open <strong>History</strong> &rarr; the match &rarr; <strong>View Rallies</strong>.",
    "Free: open a rally, choose <strong>Trim Clip</strong>, adjust the start and end, tap <strong>Save</strong>, then <strong>Export Clip</strong> to save it to Photos or Gallery.",
    "Pro: open the <strong>Clip Editor</strong>, pick rallies and a format (Standard 16:9 or Short 9:16), then <strong>Share</strong>, <strong>Save to Photos</strong> or <strong>Upload to YouTube</strong>. <strong>Highlight Reel</strong> joins every marked rally into one video.",
  ]),
  howto("Control a match from a second phone (Remote)", [
    "Put both phones on the same Wi-Fi network.",
    "On the recording phone (needs Pro), start recording, open the <strong>Remote</strong> chip and tap <strong>Start Remote Server</strong> (<strong>Start Server</strong> on Android).",
    "On the second phone (free), open New match, set Mode to <strong>Remote</strong> and tap <strong>Connect</strong>. Choose the recording phone under <strong>Found Recorders</strong>, or tap <strong>Enter IP Address</strong>.",
    "Control points, sets, the timer, timeouts, swapping sides, and start, pause and stop recording.",
  ], "A remote phone can't mark rallies. Mark them on the recording phone or the Apple Watch."),
  howto("Link your Apple Watch", [
    "Install MatchCam on the Apple Watch paired with your iPhone. There is no pairing step in the app.",
    "Open the Watch app. It shows <strong>iPhone connected</strong>, and New match on the iPhone shows <strong>Watch Connected</strong>.",
    "Start a match on the iPhone and the Watch moves into it. To score on the Watch alone, tap <strong>Start on Watch</strong>.",
  ]),
  howto("Upload a match to YouTube (Pro)", [
    "Open <strong>History</strong> &rarr; the match &rarr; <strong>Upload to YouTube</strong>.",
    "The first time, <strong>connect your YouTube account</strong>, then set the default visibility, audience and Upload on Wi-Fi Only.",
    "Review the <strong>Title</strong>, <strong>Description</strong>, <strong>Visibility</strong>, <strong>Audience</strong> and <strong>Playlist</strong>, then tap <strong>Upload</strong>. The match joins the queue.",
    "Follow progress on Home or in Settings &rarr; <strong>Connections</strong> &rarr; <strong>Upload Queue</strong>.",
    "To upload with the YouTube app instead, use <strong>Copy YouTube Details</strong>.",
  ]),
  howto("Back up or export your data", [
    "On Home open the <strong>&hellip;</strong> menu &rarr; <strong>Settings</strong> &rarr; <strong>Data</strong>.",
    "Pro: tap <strong>Export backup</strong> and save the file to a cloud drive. On the new phone tap <strong>Import backup</strong>.",
    "Free: <strong>Export data</strong> saves a JSON file of your match history.",
  ], "Videos are not included in a backup. They stay in Photos or Gallery."),
]

how_to = f'''<h1>How to</h1>
<p class="lead">Short guides for the things people do most. Tap a title to open it. Anything else is in <a href="support.html">Support</a>.</p>
{chr(10).join(HOWTOS)}'''

pro = f'''<h1>MatchCam Pro</h1>
<p class="lead">Recording and scoring a match is free, with no time limit. Pro adds the extras that publish, connect or protect your matches.</p>

<h2>What Pro adds</h2>
<div class="features">
  <div class="card feat is-pro"><h3>YouTube upload</h3><p>Upload matches to your channel with chapters, playlists and a queue that resumes after a lost connection.</p></div>
  <div class="card feat is-pro"><h3>Clip Editor and highlight reel</h3><p>Combine rallies into one video in 16:9 or vertical 9:16, or join every marked rally automatically.</p></div>
  <div class="card feat is-pro"><h3>Live streaming</h3><p>Stream the match with the scoreboard to YouTube Live, Twitch or any RTMP server.</p></div>
  <div class="card feat is-pro"><h3>Remote Connect</h3><p>Let other phones control the recording phone. The phones used as a remote stay free.</p></div>
  <div class="card feat is-pro"><h3>Scoreboard export</h3><p>Burn the scoreboard into a video recorded with another camera.</p></div>
  <div class="card feat is-pro"><h3>Backup &amp; restore</h3><p>Move your match history to a new phone through any cloud storage.</p></div>
</div>

<h2 id="compare">Free vs Pro</h2>
<div class="table-wrap">
<table class="compare">
  <tr><th>Feature</th><th class="c">Free</th><th class="c">Pro</th></tr>
{rows}
</table>
</div>
<p>The MatchCam watermark stays on every video, with or without Pro.</p>

<h2>Subscription</h2>
<ul>
  <li>MatchCam Pro is an auto-renewable subscription, monthly or yearly. The price is shown in the app before you buy.</li>
  <li>Payment goes through the App Store or Google Play. You can cancel any time in your App Store or Google Play subscriptions.</li>
  <li>New phone? Open Settings, tap Upgrade to Pro, then Restore Purchases.</li>
  <li>Got a promo code? Tap Redeem Promo Code on the same screen.</li>
</ul>
<p>Details are in the <a href="terms.html">Terms of Use</a>. Questions? Visit <a href="support.html">Support</a>.</p>'''

out = pathlib.Path(__file__).resolve().parent.parent
for f, t, d, b in [
    ("index.html", "MatchCam", "Record volleyball matches with a live scoreboard, mark rallies and share highlights.", index),
    ("features.html", "MatchCam Features", "Every MatchCam feature on iPhone, Android and Apple Watch.", features),
    ("how-to.html", "MatchCam How to", "Step-by-step guides: record a match, set up teams, run tournaments, mark rallies, use a remote and upload to YouTube.", how_to),
    ("pro.html", "MatchCam Pro", "What MatchCam Pro adds, and a Free vs Pro comparison.", pro),
    ("privacy.html", "MatchCam Privacy Policy", "How the MatchCam app handles your data, including YouTube uploads.", privacy),
    ("terms.html", "MatchCam Terms of Use", "Terms of use for the MatchCam app and MatchCam Pro subscriptions.", terms),
    ("support.html", "MatchCam Support", "Help and answers for MatchCam.", support),
]:
    (out / f).write_text(page(f, t, d, b))
print(f"Built {len(PAGES) + 2} pages in {out}")
