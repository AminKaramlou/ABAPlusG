myAsm(a).
myAsm(b).
myAsm(c).
myAsm(d).
myAsm(e).
contrary(a, C(a)).
contrary(b, C(b)).
contrary(c, C(c)).
contrary(d, C(d)).
contrary(e, C(e)).
myRule(C(b), [c, d]).
myRule(C(c), [a, d]).
myRule(C(a), [c, d]).
myRule(C(d), [d]).
myRule(C(e), []).
myPrefLT(c, a).

% Unique grounded and preferred extension {a, b}, has consequence C(e)
% No (set-)stable extension