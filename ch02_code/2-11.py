# Columns:
# 'Sepal.Length', 'Sepal.Width',
# 'Petal.Length', 'Petal.Width', 'Species'

# Visualize 3 dimensions
# Sepal.Length, Sepal.Width, and 'Petal.Length'

# Clear scene
ut.delete_all()

# Place data
for i in range(0, len(iris_data)):
    ut.create.sphere('row-' + str(i))
    v = iris_data[i]
    ut.act.scale((0.25, 0.25, 0.25))
    ut.act.location((v[0], v[1], v[2]))