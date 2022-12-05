#pip3 install -q z3-solver
import re
import time

from z3 import *

def csp(input: str, limit=None, unique=True):
    start_time  = time.perf_counter()
    solver      = Solver()
    token_words = re.findall(r'\b[a-zA-Z]\w*\b', input)  

    letters = { l: Int(l) for l in list("".join(token_words)) }
    words   = { w: Int(w) for w in list(token_words)          }

    for l,s in letters.items():
        solver.add(0 <= s, s <= 9)
    if unique and len(letters) <= 10:
        solver.add(Distinct(*letters.values()))
    solver.add(Distinct(*words.values()))

    for word in words.keys():
        solver.add( letters[word[0]] != 0 )

    for word, word_symbol in words.items():
        solver.add(word_symbol == Sum(*[letter_symbol * 10**index
            for index,letter_symbol in enumerate(reversed([
                letters[l] for l in list(word)])) ]))

    solver.add(eval(input, None, words))
    solutions = []
    print(input)
    while str(solver.check()) == 'sat':
        solutions.append({ str(s): 
                          solver.model()[s] for w,s in words.items() })
        
        print(solutions[-1])
        solver.add(Or(*[ s != solver.model()[s] for w,s in words.items() ]))
        if limit and len(solutions) >= limit: 
            break

    run_time = round(time.perf_counter() - start_time, 1)
    print(f'== {len(solutions)} solutions found in {run_time}s ==\n')
csp('TWO + TWO == FOUR')
