myAsm(asm1).
myAsm(asm2).
contrary(asm1, C(asm1)).
contrary(asm2, C(asm2)).
myRule(sent1, [asm1]).
myRule(sent2, [asm1, asm2]).
myRule(sent3, [C(asm1)]).
myRule(sent4, []).
myRule(C(asm1), [sent1, sent4]).