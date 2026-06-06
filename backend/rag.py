# Read FAQ data

with open("data/faq.txt", "r", encoding="utf-8") as file:
    faq_lines = file.readlines()


def retrieve_answer(query):

    query = query.lower()

    for line in faq_lines:

        line_lower = line.lower()

        # Skip empty lines
        if line.strip() == "":
            continue

        # Match query words
        if any(word in line_lower for word in query.split()):

            return line.strip()

    return "Sorry, I could not find an answer."

    
    