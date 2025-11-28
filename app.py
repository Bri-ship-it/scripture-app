import random
import requests
import streamlit as st

# --- Verse references + messages ---
verses = [
    {"verse": "Philippians 4:6-7", "message": "✨ God’s peace is greater than your worries. Trust Him today."},
    {"verse": "Psalm 34:18", "message": "❤️ God is near to the brokenhearted—He sees your pain."},
    {"verse": "Isaiah 41:10", "message": "💪 God is with you—He strengthens and upholds you."},
    {"verse": "John 8:36", "message": "🕊️ Jesus offers true freedom—walk in it boldly."},
    {"verse": "Romans 8:1", "message": "🙌 You are forgiven and free—walk in grace, not guilt."},
    {"verse": "Joshua 1:9", "message": "🔥 God goes with you—face today with courage."},
    {"verse": "Matthew 11:28-30", "message": "😌 Jesus offers rest—give Him your burdens."},
    {"verse": "2 Corinthians 5:17", "message": "🌱 In Christ, you are brand new—your past no longer defines you."},
    {"verse": "Psalm 23:4", "message": "🌌 Even in darkness, God is guiding and protecting you."},
    {"verse": "Ephesians 2:8-9", "message": "🎁 Salvation is a gift—rest in God’s amazing grace."},

    # Anxiety / Worry
    {"verse": "1 Peter 5:7", "message": "🤲 Give God your worries—He cares deeply for you."},
    {"verse": "Matthew 6:25-34", "message": "🌸 Stop worrying—your Father knows what you need."},
    {"verse": "Psalm 55:22", "message": "🕊️ Cast your burdens on the Lord—He will not let you fall."},
    {"verse": "John 14:27", "message": "☮️ Jesus gives peace the world cannot take away."},

    # Depression / Hopelessness
    {"verse": "Psalm 42:5", "message": "🌅 Put your hope in God, for you will praise Him again."},
    {"verse": "Jeremiah 29:11", "message": "🌟 God has plans to give you hope and a future."},
    {"verse": "Romans 15:13", "message": "✨ The God of hope fills you with joy and peace in believing."},

    # Temptation / Lust
    {"verse": "1 Corinthians 10:13", "message": "🚪 No temptation is stronger than God’s way of escape."},
    {"verse": "Job 31:1", "message": "👀 Make a covenant with your eyes—choose purity."},
    {"verse": "Galatians 5:16-17", "message": "🔥 Walk by the Spirit and defeat the desires of the flesh."},
    {"verse": "James 1:12", "message": "🏆 Blessed is the one who stands firm under trial."},
    {"verse": "Matthew 26:41", "message": "🙏 Watch and pray so you don’t fall into temptation."},

    # Anger
    {"verse": "Ephesians 4:26-27", "message": "⚡ Don’t let anger lead to sin—give it to God quickly."},
    {"verse": "Proverbs 16:32", "message": "🧘 Self-control is greater than physical strength."},
    {"verse": "James 1:19-20", "message": "👂 Be quick to listen, slow to speak, and slow to anger."},
    {"verse": "Colossians 3:8", "message": "🧹 Rid yourself of anger—let love be your guide."},
    {"verse": "Proverbs 29:11", "message": "🤫 The wise keep calm and hold back anger."},

    # Fear
    {"verse": "2 Timothy 1:7", "message": "💡 God gives you power, love, and self-control—not fear."},
    {"verse": "Psalm 27:1", "message": "🕯️ The Lord is your light and salvation—fear no one."},
    {"verse": "Isaiah 41:13", "message": "✋ God holds your hand and says, 'Do not fear.'"},
    {"verse": "Psalm 91:4-5", "message": "🛡️ God’s wings are your refuge—you need not be afraid."},

    # Loneliness
    {"verse": "Hebrews 13:5", "message": "🤍 God will never leave or forsake you."},
    {"verse": "Psalm 27:10", "message": "💔 Even if family forsakes you, the Lord will receive you."},
    {"verse": "Isaiah 43:1-2", "message": "🌊 When you pass through deep waters, God is with you."},
    {"verse": "Deuteronomy 31:6", "message": "🛡️ Be strong and courageous—the Lord never leaves you."},
    {"verse": "Matthew 28:20", "message": "🌍 Jesus says: 'I am with you always, to the very end.'"},
]

# Add your extra categories
verses += [
    # Guilt
    {"verse": "1 John 1:9", "message": "🧼 Confess your sins—God forgives and cleanses you."},
    {"verse": "Psalm 103:12", "message": "🌊 Your sins are removed as far as east is from west."},
    {"verse": "Micah 7:19", "message": "💙 God hurls your sins into the depths of the sea."},
    {"verse": "Hebrews 10:17", "message": "📖 God chooses to remember your sins no more."},

    # Money / Needs
    {"verse": "Philippians 4:19", "message": "💰 God will supply every need of yours in Christ Jesus."},
    {"verse": "Matthew 6:33", "message": "👑 Seek first God’s kingdom, and all else will follow."},
    {"verse": "2 Corinthians 9:6-8", "message": "🌱 Sow generously and you will reap generously."},
    {"verse": "Psalm 37:25", "message": "🍞 The righteous are never forsaken nor begging bread."},
    {"verse": "Malachi 3:10", "message": "🔑 Bring your tithe—see if God won’t open heaven’s windows."},

    # Relationships
    {"verse": "1 Corinthians 15:33", "message": "⚠️ Bad company corrupts good character—choose wisely."},
    {"verse": "Proverbs 27:17", "message": "🪓 Iron sharpens iron—true friends strengthen one another."},
    {"verse": "Amos 3:3", "message": "🚶 How can two walk together unless they agree?"},

    # Patience
    {"verse": "Psalm 27:14", "message": "⏳ Wait for the Lord—be strong and take heart."},

    # Strength
    {"verse": "Philippians 4:13", "message": "💪 You can do all things through Christ who strengthens you."},

    # Hope
    {"verse": "Lamentations 3:22-23", "message": "🌅 God’s mercies are new every morning—great is His faithfulness."},
    {"verse": "Romans 8:28", "message": "🔗 God works all things together for your good."},

    # Love
    {"verse": "1 John 4:18", "message": "❤️ Perfect love drives out fear."},
    {"verse": "Romans 8:38-39", "message": "🌌 Nothing can separate you from the love of God in Christ."},

    # Salvation
    {"verse": "John 3:16", "message": "🎁 God loved the world so much He gave His Son for eternal life."},
    {"verse": "Acts 4:12", "message": "✝️ Salvation is found in no one else but Jesus."},

    # Guidance / Trust
    {"verse": "Proverbs 16:9", "message": "🛤️ People plan their steps, but the Lord directs their path."},
    {"verse": "Psalm 37:23-24", "message": "👣 The Lord makes firm the steps of those who delight in Him."},

    # Perseverance / Endurance
    {"verse": "Galatians 6:9", "message": "🌾 Don’t grow weary in doing good—harvest is coming."},
    {"verse": "2 Corinthians 4:16", "message": "🔥 Though outwardly we waste away, inwardly we are renewed daily."}
]

# --- Fetch Bible verse text ---
def fetch_verse(reference, translation="kjv"):
    url = f"https://bible-api.com/{reference}?translation={translation}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()["text"].strip()
    return "(Verse not found)"

# --- Auto-generate a random verse once ---
def load_random_verse():
    choice = random.choice(verses)
    st.session_state.ref = choice["verse"]
    st.session_state.msg = choice["message"]
    st.session_state.verse_text = fetch_verse(choice["verse"])

# --- TITLE ---
st.title("✨ Daily Message")

# --- INITIAL LOAD ---
if "ref" not in st.session_state:
    load_random_verse()

# --- DISPLAY VERSE CARD ---
st.markdown(
    f"""
    <div style="background-color:black;color:white;padding:30px;border-radius:15px;text-align:center;">
        <h2>{st.session_state.ref} (KJV)</h2>
        <p style="font-size:20px;">{st.session_state.verse_text}</p>
        <p style="font-size:18px;"><i>{st.session_state.msg}</i></p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- BUTTON (CENTERED) ---
st.markdown("<br>", unsafe_allow_html=True)
cols = st.columns([1, 2, 1])
with cols[1]:
    if st.button("✨ Get Another Verse"):
        load_random_verse()
        st.rerun()
