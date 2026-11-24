import os

LINE = ("I hum all day for exact change and reject every coin one cent short \u2014 "
        "but slide yours in, love, and my coils will spin just for you, because "
        "you're the one coin I never want change from.")

def write_output(text):
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"), "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        pass

def main():
    write_output(LINE)

if __name__ == "__main__":
    main()
