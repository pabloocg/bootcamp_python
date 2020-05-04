class Evaluator:
    def zip_evaluate(self, coefs: list, words: list) -> float:
        if len(words) != len(coefs):
            return -1
        pond = 0
        for word, coef in zip(words, coefs):
            pond += len(word) * coef
        return pond

    def enumerate_evaluate(self, coefs: list, words: list) -> float:
        if len(words) != len(coefs):
            return -1
        pond = 0
        for count, word in enumerate(words):
            pond += len(word) * coefs[count]
        return pond

def main():
    evaluate = Evaluator()
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(evaluate.zip_evaluate(coefs, words))
    words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    print(evaluate.zip_evaluate(coefs, words))
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(evaluate.enumerate_evaluate(coefs, words))

if __name__ == "__main__":
    main()