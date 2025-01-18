def logic_circuit_with_bits(A, B, C):
 
    A, B, C = A & 1, B & 1, C & 1

    AND1 = A & B
    AND2 = B & C
    OR1 = A | C
    NOT1 = ~AND2 & 1 
    AND3 = OR1 & NOT1
    Q = AND1 | AND3

    return Q

A, B, C = 1, 0, 1  
Q = logic_circuit_with_bits(A, B, C)
print(f"Inputs: A={A}, B={B}, C={C}")
print(f"Output: Q={Q}")