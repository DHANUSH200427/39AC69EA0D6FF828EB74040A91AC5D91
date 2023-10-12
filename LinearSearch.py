def linear_search_product(productlist, targetproduct):
  indices = []
  for index, product in enumerate(productlist):
    if product == targetproduct:
      indices.append(index)
  return indices


products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
result = linear_search_product(products, target)
print(result)
