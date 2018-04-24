words = ['a', 'b', 'ba', 'bca', 'bda', 'bdca']
words = ['a', 'zxb', 'ba', 'bca', 'bda', 'bdca', 'zxbe', 'azxbe', 'azxpbe']


def longestChain(words):
    words.sort(key=len)
    min_len = len(words[0])
    max_len = len(words[-1])

    # {word_length: list_of_words}
    words_of_length = {i: set() for i in range(min_len, max_len+1)}
    for word in words:
        words_of_length[len(word)].add(word)

    # {word: length_of_longest_chain_from_here}
    longest_chains = {word: 1 for word in words_of_length[min_len]}

    for i in range(min_len+1, max_len+1):
        these_words = words_of_length[i]
        for word in these_words:
            subwords = {word[:n] + word[n+1:] for n in range(i)}
            best_chain = max(1 + longest_chains.get(w, 0) for w in subwords)
            longest_chains[word] = best_chain

    best = max(longest_chains.values())
    return best


result = longestChain(words)

print(result)
assert result == 4

