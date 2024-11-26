from sentence_transformers import SentenceTransformer
from data.journal_entries import test_entries

def vectorize_entries(model):
    sentences = []
    for entry in test_entries:
        sentences.append(entry["entry"])
    embeddings = model.encode(sentences)
    return embeddings, sentences

def get_top_n_similar(query, n=3):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = model.encode(query)
    entry_embeddings, sentences = vectorize_entries(model)
    similarity_scores = model.similarity(query_embedding, entry_embeddings)
    top_entries = []
    for i in range(n):
        max_index = similarity_scores[0].argmax()
        top_entries.append(sentences[max_index])
        similarity_scores[0][max_index] = 0
    return top_entries

def main():
    query = "Places I've been"
    top_entries = get_top_n_similar(query)
    for entry in top_entries:
        print(entry)

if __name__ == "__main__":
    main()
