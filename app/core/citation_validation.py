
def validate_citation(answer : dict , retrieved_chunks : list[dict]):
    label_to_id = {c['citations_lable'] : c['chunk_id'] for c in retrieved_chunks }
    cited = set(answer.get('citations',[]))

    if not cited and not answer.get("needs_human_review"):
        raise ValueError("Answer contains no citations")

    unknown = cited - set(label_to_id.keys())
    if unknown :
        raise ValueError(f"Answer cites labels that were never retrieved : {unknown}")