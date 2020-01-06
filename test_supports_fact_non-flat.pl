myAsm(a).
myAsm(b).
myAsm(c).
contrary(a, C(a)).
contrary(b, C(b)).
contrary(c, C(c)).
myRule(a, [sent_b, sent_c]).
myRule(sent_b, [b]).
myRule(sent_c, [c]).
myRule(C(a), []).