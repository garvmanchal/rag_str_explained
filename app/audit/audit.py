

audit_log : list[dict]= []

def log_rag_trace(question: str, chunks : list[dict], answer : dict):
    audit_log.append({
        "question" : question,
        "retrieved_chunks_id" : [c["chunk_id"] for c in chunks],
        "re_ranker_score" : [round(c.get("re_ranker_scores",0),3)for c in chunks],
        "citations": answer.get("citations",[])

    })


'''
Audit means systematically checking and recording
what happened in a process to make sure it is correct, traceable, and follows the required rules.


Simple difference

Citation → “Where did this information come from?”

Audit → “What happened throughout the process, and can we trace and verify it?”
'''