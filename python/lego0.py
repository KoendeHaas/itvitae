block_amount = 70
block_wishlist = [8, 12, 4, 2 , 120]

total = 0

for block in block_wishlist:
    total += (block_amount * block)

print(f"Total amount = €{total / 100}")