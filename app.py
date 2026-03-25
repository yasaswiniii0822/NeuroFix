import streamlit as st
import difflib

st.set_page_config(page_title="NeuroFix AI", layout="centered")
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #38bdf8;
}
.subtitle {
    text-align: center;
    color: #94a3b8;
}
.box {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)
st.markdown("<div class='title'> NeuroFix AI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Context-Aware Text Correction System</div>", unsafe_allow_html=True)
st.markdown("---")
dictionary = [
    "i","have","a","dream","this","is","my","project",
    "hello","world","python","code","artificial","intelligence",
    "machine","learning","student","college"
]

def autocorrect(sentence):
    words = sentence.lower().split()
    corrected = []
    changes = 0

    for word in words:
        match = difflib.get_close_matches(word, dictionary, n=1, cutoff=0.6)
        if match:
            corrected.append((word, match[0]))
            if word != match[0]:
                changes += 1
        else:
            corrected.append((word, word))

    return corrected, changes
text = st.text_area(" Enter text to analyze:")

if st.button(" Run Correction Engine"):
    if text.strip() == "":
        st.warning("Enter something first.")
    else:
        corrected, changes = autocorrect(text)
        st.markdown("### 📝 Original")
        st.code(text)
        st.markdown("### ⚡ Corrected")

        output = ""
        for original, new in corrected:
            if original != new:
                output += f"**:green[{new}]** "
            else:
                output += new + " "

        st.markdown(output)
        total_words = len(corrected)
        accuracy = int(((total_words - changes) / total_words) * 100)

        st.markdown("---")
        st.markdown(f"###  Confidence Score: **{accuracy}%**")

        if accuracy > 80:
            st.success("High confidence correction")
        elif accuracy > 50:
            st.info("Moderate confidence")
        else:
            st.warning("Low confidence – limited vocabulary")
st.markdown("---")
st.caption("Built with Python | NLP | Approximate String Matching")