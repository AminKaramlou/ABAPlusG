myAsm(a).
myAsm(b).
myAsm(c).
myAsm(d).
contrary(a, C(a)).
contrary(b, C(b)).
contrary(c, C(c)).
contrary(d, C(d)).
myRule(a, [sent_b, sent_c]).
myRule(sent_b, [b]).
myRule(sent_c, [c]).
myRule(C(a), [d]).