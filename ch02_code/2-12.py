# Columns:
# 'Sepal.Length', 'Sepal.Width',
# 'Petal.Length', 'Petal.Width', 'Species'

# Visualize 4 dimensions
# Sepal.Length, Sepal.Width, 'Petal.Length',
# and scale the object by a factor of 'Petal.Width'

# Clear scene
ut.delete_all()

# Place data
for i in range(0, len(iris_data)):
    ut.create.sphere('row-' + str(i))
    v = iris_data[i]
    scale_factor = 0.2
    ut.act.scale((v[3] * scale_factor,) * 3)
    ut.act.location((v[0], v[1], v[2]))