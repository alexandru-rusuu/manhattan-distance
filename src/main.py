import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.manhattan import manhattan_manual, manhattan_scipy, parse_vector_from_line


def read_vectors_from_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        if len(lines) < 2:
            raise ValueError("Fisierul trebuie sa contina cel putin 2 vectori")
        
        vector_x = parse_vector_from_line(lines[0])
        vector_y = parse_vector_from_line(lines[1])
        
        return vector_x, vector_y
    
    except FileNotFoundError:
        print(f"Eroare: Fisierul '{filename}' nu a fost gasit.")
        sys.exit(1)
    except ValueError as e:
        print(f"Eroare: {e}")
        sys.exit(1)


def main():
    input_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'input.txt')
    
    print("=== Calculul Distantei Manhattan ===\n")
    
    X, Y = read_vectors_from_file(input_file)
    
    print(f"Vector X: {X}")
    print(f"Vector Y: {Y}\n")
    
    distance_manual = manhattan_manual(X, Y)
    distance_scipy = manhattan_scipy(X, Y)
    
    print(f"Distanta Manhattan (manual): {distance_manual}")
    print(f"Distanta Manhattan (scipy): {distance_scipy}")
    print(f"Rezultatele sunt identice: {distance_manual == distance_scipy}")


if __name__ == "__main__":
    main()
