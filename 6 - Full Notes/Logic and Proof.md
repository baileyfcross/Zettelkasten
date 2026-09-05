
2026-09-01 00:10

Status: #baby

Tags: [[Formal Logic]]

# Logic and Proof

## Chapter 1

"The art of logic is to find an interesting conclusion and a chain of logical deductions that leads from the premises to that conclusion." (1)

- Chapter is mostly about the mechanics of logic
- Investigating logic as a branch of math, with its own symbols, formulas, and rules of computation
A [[Proposition]] is a statement that has a truth value. It can be either true or false

[[Logical Deduction]] is a kind of computation that is derived from a [[Premise]] and can lead to a [[Conclusion]]


### 1.1 Propositional Logic

We use symbolic names called a [[Propositional Variable]] to talk about propositions such as p, q, and r. When we use [[Propositional Variable]]s we are discussing and agreeing on a commonly understood term for the exercise or [[Logical Deduction]] evaluation. This variable has [[Mathematical Generality]] in that p can represent any statement, and the our discussion of p will be valid, no matter which statement p represents. 

We can combine our [[Proposition]] with [[Logical Operators]] to create a new [[Proposition]]. Our new truth value is determined by our [[Logical Operators]] within our new [[Proposition]].

| English | Logical Operator | Logical Names |
| ------- | ---------------- | ------------- |
| and     | ∧                | Conjunction   |
| or      | ∨                | Disjunction   |
| not     | ¬                | Negation      |
Let:
p and q be propositions

Then:
p ∧ q
p ∨ q
¬p

Means:
p ∧ q is true when both p is true and q is true, and in no other case
p ∨ q is true when either p is true, or q is true, or both p and q are true, and in no other case.
¬p is true when p is false, and in no other case.

[[Compound Propositions]] are created from simpler [[Proposition]]s and [[Logical Operators]]

#### Precedence Rules:

Parentheses can be used to show which propositions are grouped together

These are in order of the highest precedence when evaluating a [[Propositional Logic]] Equation
1. Not
2. And
3. Or

Example:
¬p ∨ q ∧ r is [[Logically Equivalent]] to  (¬p) ∨ (q ∧ r)

p ∨ q ∧ q ∨ r is [[Logically Equivalent]] to p ∨ (q ∧ q) ∨ r

# References

[[FoundationsOfComputation_2.3.2.pdf]]