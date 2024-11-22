class t:
    def __init__(self, a, b):
        self.c = a
        self.d = b

a, b = input().split()
x = t('codetree','10')
print(f"user {x.c} lv {x.d}")
x.c = a
x.d = b

print(f"user {x.c} lv {x.d}")