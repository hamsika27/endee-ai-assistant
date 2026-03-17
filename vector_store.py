import os
import json
import numpy as np

class SearchResult:
    def __init__(self, id, score, metadata):
        self.id = id
        self.score = score
        self.metadata = metadata


class EndeeVectorStore:

    def __init__(self, dim):
        self.dim = dim
        self.vectors = []
        self.metadata = []
        self.ids = []

    def add(self, id, embedding, metadata):
        self.ids.append(id)
        self.vectors.append(np.array(embedding))
        self.metadata.append(metadata)

    def search(self, query_embedding, k=3):

        query = np.array(query_embedding)

        scores = []

        for i, vec in enumerate(self.vectors):
            score = np.dot(query, vec) / (
                np.linalg.norm(query) * np.linalg.norm(vec)
            )
            scores.append((i, score))

        scores.sort(key=lambda x: x[1], reverse=True)

        results = []
        for i, score in scores[:k]:
            results.append(
                SearchResult(
                    self.ids[i],
                    score,
                    self.metadata[i]
                )
            )

        return results

    def save(self, path):

        os.makedirs(path, exist_ok=True)

        np.save(os.path.join(path, "vectors.npy"), self.vectors)

        with open(os.path.join(path, "metadata.json"), "w") as f:
            json.dump({
                "ids": self.ids,
                "metadata": self.metadata
            }, f)

    @classmethod
    def load(cls, path):

        vectors = np.load(os.path.join(path, "vectors.npy"))

        with open(os.path.join(path, "metadata.json"), "r") as f:
            data = json.load(f)

        store = cls(dim=len(vectors[0]))
        store.vectors = list(vectors)
        store.ids = data["ids"]
        store.metadata = data["metadata"]

        return store