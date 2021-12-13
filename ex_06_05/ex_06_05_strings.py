text = "X-DSPAM-Confidence:    0.8475"
spos = text.find(':')
piece = text[spos+1:]
value = float(piece)
print(value)
