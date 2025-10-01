import random
import requests
import streamlit as st

# Verse references + encouragement messages
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

    # Guilt / Shame
    {"verse": "1 John 1:9", "message": "🧼 Confess your sins—God forgives and cleanses you."},
    {"verse": "Psalm 103:12", "message": "🌊 Your sins are removed as far as east is from west."},
    {"verse": "Micah 7:19", "message": "💙 God hurls your sins into the depths of the sea."},
    {"verse": "Hebrews 10:17", "message": "📖 God chooses to remember your sins no more."}
]

verses += [
    # Money / Needs
    {"verse": "Philippians 4:19", "message": "💰 God will supply every need of yours in Christ Jesus."},
    {"verse": "Matthew 6:33", "message": "👑 Seek first God’s kingdom, and all else will follow."},
    {"verse": "2 Corinthians 9:6-8", "message": "🌱 Sow generously and you will reap generously."},
    {"verse": "Psalm 37:25", "message": "🍞 The righteous are never forsaken nor begging bread."},
    {"verse": "Malachi 3:10", "message": "🔑 Bring your tithe—see if God won’t open heaven’s windows."},

    # Friendships / Relationships
    {"verse": "1 Corinthians 15:33", "message": "⚠️ Bad company corrupts good character—choose wisely."},
    {"verse": "Proverbs 27:17", "message": "🪓 Iron sharpens iron—true friends strengthen one another."},
    {"verse": "Amos 3:3", "message": "🚶 How can two walk together unless they agree?"},
    {"verse": "Ecclesiastes 4:9-10", "message": "🤝 Two are better than one—they lift each other up."},
    {"verse": "John 15:13", "message": "❤️ True love is laying down one’s life for a friend."},

    # Forgiveness / Hurt
    {"verse": "Ephesians 4:32", "message": "💞 Forgive one another as God forgave you."},
    {"verse": "Matthew 6:14-15", "message": "🤲 Forgive others so your Father forgives you."},
    {"verse": "Colossians 3:13", "message": "🧩 Bear with one another and forgive grievances."},
    {"verse": "Luke 6:37", "message": "🚪 Forgive, and you will be forgiven."},
    {"verse": "Psalm 86:5", "message": "💙 God is forgiving and abounding in love to all who call."},

    # Patience / Waiting on God
    {"verse": "Psalm 27:14", "message": "⏳ Wait for the Lord—be strong and take heart."},
    {"verse": "James 1:4", "message": "🌱 Let perseverance finish its work in you."},
    {"verse": "Lamentations 3:25-26", "message": "🕊️ The Lord is good to those who wait for Him."},
    {"verse": "Isaiah 40:31", "message": "🦅 Those who wait on the Lord will renew their strength."},
    {"verse": "Romans 8:25", "message": "🌾 Hope that is seen is no hope—wait patiently for it."},

    # Direction / Decisions
    {"verse": "Proverbs 3:5-6", "message": "🧭 Trust the Lord and He will make your paths straight."},
    {"verse": "Psalm 119:105", "message": "💡 God’s word is a lamp to your feet and a light to your path."},
    {"verse": "Isaiah 30:21", "message": "👂 You’ll hear His voice: 'This is the way, walk in it.'"},
    {"verse": "James 1:5", "message": "🧠 Ask God for wisdom—He gives generously."},
    {"verse": "Psalm 32:8", "message": "🖊️ The Lord will instruct and teach you the way to go."},

    # Peace / Rest
    {"verse": "Isaiah 26:3", "message": "🕊️ God keeps in perfect peace the mind that trusts Him."},
    {"verse": "John 16:33", "message": "⚔️ In this world you’ll have trouble—but take heart, Jesus overcame."},
    {"verse": "Psalm 4:8", "message": "😴 I will lie down and sleep in peace, for God keeps me safe."},

    # Grief / Loss
    {"verse": "Revelation 21:4", "message": "😭 God will wipe away every tear—no more death or pain."},
    {"verse": "John 14:1-3", "message": "🏠 Jesus prepares a place for you—do not let your heart be troubled."},
    {"verse": "1 Thessalonians 4:13-14", "message": "🌅 We grieve with hope—because Jesus rose, we will too."},
    {"verse": "Psalm 147:3", "message": "💔 God heals the brokenhearted and binds their wounds."},
    {"verse": "Matthew 5:4", "message": "🌹 Blessed are those who mourn, for they will be comforted."},

    # Justice / Feeling Wronged
    {"verse": "Romans 12:19", "message": "⚖️ Leave room for God’s justice—He repays."},
    {"verse": "Micah 6:8", "message": "🤲 Do justice, love kindness, and walk humbly with God."},
    {"verse": "Psalm 37:7-9", "message": "🌱 Wait on the Lord—evildoers will fade like grass."},
    {"verse": "Isaiah 1:17", "message": "🛡️ Learn to do good, seek justice, defend the oppressed."},
    {"verse": "Proverbs 21:15", "message": "😊 Justice brings joy to the righteous."},

    # Doubt / Weak Faith
    {"verse": "Mark 9:24", "message": "🙏 'I believe—help my unbelief!' is a prayer God hears."},
    {"verse": "Hebrews 11:1", "message": "🌌 Faith is confidence in what we hope for, unseen."},
    {"verse": "James 1:5-6", "message": "🌊 Ask in faith without doubting—God will give wisdom."},
    {"verse": "Matthew 21:22", "message": "📖 Whatever you ask in prayer, believe and you will receive."},
    {"verse": "Romans 10:17", "message": "👂 Faith comes by hearing the word of Christ."},

    # Feeling Unworthy
    {"verse": "2 Corinthians 5:17", "message": "🌱 In Christ, you are a new creation."},
    {"verse": "Psalm 139:13-14", "message": "🧵 You are fearfully and wonderfully made."},
    {"verse": "Romans 5:8", "message": "❤️ Christ died for you while you were still a sinner."},
    {"verse": "1 Peter 2:9", "message": "👑 You are chosen, royal, holy, and belong to God."},

    # Strength / Tiredness
    {"verse": "Philippians 4:13", "message": "💪 You can do all things through Christ who strengthens you."},
    {"verse": "Isaiah 40:29", "message": "⚡ God gives power to the faint and strengthens the weak."},
    {"verse": "Nehemiah 8:10", "message": "🎉 The joy of the Lord is your strength."},
    {"verse": "Exodus 15:2", "message": "🛡️ The Lord is your strength and your song."},
    {"verse": "Psalm 46:1", "message": "🏔️ God is your refuge and strength, ever-present help."},

    # Spiritual Warfare
    {"verse": "James 4:7", "message": "⚔️ Submit to God, resist the devil, and he will flee."},
    {"verse": "Ephesians 6:11-18", "message": "🛡️ Put on the full armor of God to stand firm."},
    {"verse": "2 Corinthians 10:3-5", "message": "🏹 Take captive every thought to obey Christ."},
    {"verse": "1 Peter 5:8-9", "message": "🦁 Be alert—the enemy prowls like a lion, but resist him."},
    {"verse": "Romans 8:37", "message": "👑 In Christ, you are more than a conqueror."}
]
verses += [
    # Hope
    {"verse": "Lamentations 3:22-23", "message": "🌅 God’s mercies are new every morning—great is His faithfulness."},
    {"verse": "Romans 8:28", "message": "🔗 God works all things together for the good of those who love Him."},

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



# Bible API fetch
def fetch_verse(reference, translation="kjv"):
    url = f"https://bible-api.com/{reference}?translation={translation}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()["text"].strip()
    return "(Verse not found)"

# Streamlit UI
st.title("📖 Random Scripture Generator")

if st.button("✨ Get a Random Verse"):
    choice = random.choice(verses)
    ref = choice["verse"]
    msg = choice["message"]
    verse_text = fetch_verse(ref)

    st.markdown(
        f"""
        <div style="background-color:black;color:white;padding:30px;border-radius:15px;text-align:center;">
            <h2>{ref} (KJV)</h2>
            <p style="font-size:20px;">{verse_text}</p>
            <p style="font-size:18px;"><i>{msg}</i></p>
        </div>
        """,
        unsafe_allow_html=True
    )


