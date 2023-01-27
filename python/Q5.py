frozenset1={'C', 'A', 'B', 'D'}
print("frozen_set_1: frozenset(",frozenset1,")")
frozenset2={2, 'A', 'C', 4}
print("frozen_set_2: frozenset(",frozenset2,")")
frozenset_union=frozenset1.union(frozenset2)
print("frozen_union: frozenset(",frozenset_union,")")
frozenset_common=frozenset1.intersection(frozenset2)
print("frozenset_common: frozenset(",frozenset_common,")")
frozenset_difference=frozenset1.difference(frozenset2)
print("frozenset_difference: frozenset(",frozenset_difference,")")
frozenset_distinct=frozenset1.symmetric_difference(frozenset2)
print("frozenset_distinct: frozenset(",frozenset_distinct,")")
