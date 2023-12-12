# Write a simple facts for the statement and querying it.

% Facts
likes(john, susie).
likes(john, mary).
likes(jane, susie).
likes(susie, john).
likes(susie, mary).
likes(mary, john).
likes(mary, susie).

father_of(joe, paul).
father_of(joe, mary).
mother_of(jane, paul).
mother_of(jane, mary).
male(paul).
male(joe).
female(mary).
female(jane).

% Rules
friends(X, Y) :- likes(X, Y), likes(Y, X).
hates(X, Y) :- \+(likes(X, Y)).
enemies(X, Y) :- \+(likes(X, Y)), \+(likes(Y, X)).
