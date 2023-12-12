% Facts
male(jonathan).
male(john).
male(kelly).
male(arnold).
male(louise).
female(marry).
female(alies).
female(martha).
female(nancy).


parent(jonathan, john).
parent(jenifer, john).
parent(jonathan, arnold).
parent(jonathan, martha).
parent(marry, kelly).
parent(john, kelly).
parent(john, alies).
parent(marry, alies).
parent(arnold, nancy).
parent(arnold, louise).


% Rules
mother(M, C) :- female(M), parent(M, C).
son(S, P) :- male(S), parent(P, S).
daughter(D, P) :- female(D), parent(P, D).
grandfather(GF, C) :- male(GF), parent(GF, M), parent(M, C).
grandmother(GM, M) :- female(GM), parent(GM, M).
brother(B, S) :- male(B), parent(P, B), parent(P, S), B \= S.
sister(S, B) :- female(S), parent(P, S), parent(P, B), S \= B.
uncle(U, P) :- brother(U, GP), parent(GP, P).