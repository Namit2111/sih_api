import tokenize
import io
import difflib

def tokenize_file(file_path):
    with open(file_path, 'rb') as file:
        tokens = []
        for token in tokenize.tokenize(io.BytesIO(file.read().replace(b'\r\n', b'\n')).readline):
            if token.type == tokenize.COMMENT:
                continue
            tokens.append(token.string)
        return tokens

def calculate_structure_similarity(file1_path, file2_path):
    tokens1 = tokenize_file(file1_path)
    tokens2 = tokenize_file(file2_path)

    # Calculate structural similarity using the SequenceMatcher
    similarity_ratio = difflib.SequenceMatcher(None, tokens1, tokens2).ratio()

    return similarity_ratio

if __name__ == "__main__":
    file1_path = "one.py"  # Replace with the path to your first Python file
    file2_path = "two.py"  # Replace with the path to your second Python file

    similarity = calculate_structure_similarity(file1_path, file2_path)

    print(f"Structural Similarity: {similarity}")
