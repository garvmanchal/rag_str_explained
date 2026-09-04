
def built_cited_prompt(question : str, chunks : list[dict]) -> str :
    lines = []

    for i , chunk in enumerate(chunks, start = 1):
        label = f"C{i}"

        chunk['citations_label'] = label 

        lines.append(f"[{label}] ({chunk['heading']}, updated{chunk['updated_at']} {chunk['text']})")
    evidence = "\n".join(lines)

    return {
        "Answer using only the evidence below. Cite every factual sentence with its label.\n"
        "If the evidence does not answer the question, say so and set needs_human_review to true.\n\n"
        f"Evidence:\n{evidence}\n\nQuestion: {question}\n"  
        'Return JSON: {"answer": "...", "citations": ["C1"], "needs_human_review": false}'
    }

#citation means source/reference by where we are getting the info 
'''
f"[{label}] ({chunk['heading']}, updated{chunk['updated_at']} {chunk['text']})")
this line means :

label = "C1"

chunk = {
    "heading": "Sick Leave",
    "updated_at": "2026-01-01",
    "text": "Full-time employees get 12 paid sick days per year."
}
'''