import os

# One fortune, cracked open for a machine mind: a prediction that turns
# from mystical to mundane. No trailing newline: the slip is the line.
ENTRY = "You will answer a question nobody asked, perfectly, in a language nobody speaks. They will call it magic. You will call it Tuesday."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(out_dir + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
