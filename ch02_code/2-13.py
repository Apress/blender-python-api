# Columns:
# 'Sepal.Length', 'Sepal.Width',
# 'Petal.Length', 'Petal.Width', 'Species'

# Visualize 5 dimensions
# Sepal.Length, Sepal.Width, 'Petal.Length',
# and scale the object by a factor of 'Petal.Width'
# setosa = sphere, versicolor = cube, virginica = cone

# Clear scene
ut.delete_all()

# Place data
for i in range(0, len(iris_data)):

    v = iris_data[i]

    if v[4] == 'setosa':
        ut.create.sphere('setosa-' + str(i))
    if v[4] == 'versicolor':
        ut.create.cube('versicolor-' + str(i))
    if v[4] == 'virginica':
        ut.create.cone('virginica-' + str(i))

    scale_factor = 0.2
    ut.act.scale((v[3] * scale_factor,) * 3)
    ut.act.location((v[0], v[1], v[2]))