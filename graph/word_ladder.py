from list_graph import Graph


def get_word_buckets(word_file: str) -> dict:
    """
    Each bucket has a label with a four-letter word, except that one of the
    letters in the label has been replaced by an underscore. Put words in the
    matching bucket. We know all the word in the bucket must be connected.
    """
    buckets = {}
    with open(word_file) as fhand:
        for line in fhand:
            word = line.strip()
            for i in range(len(word)):
                label = ''.join((word[:i], '_', word[i + 1:]))
                if label in buckets:
                    buckets[label].append(word)
                else:
                    buckets[label] = [word]
    return buckets


def add_vertices_edges(buckets: dict) -> Graph:
    """
    Add all words as vertices, connect two words if they are in the same bucket
    :return: graph
    """
    graph = Graph()
    for label in buckets.keys():
        for word1 in buckets[label]:
            for word2 in buckets[label]:
                if word1 != word2:
                    graph.add_edge(word1, word2)
    return graph


if __name__ == "__main__":
    buckets = get_word_buckets("vocabulary.txt")

    graph = add_vertices_edges(buckets)
