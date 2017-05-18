# Add in body of script, outside any class declarations
def in_bbox(lbound, ubound, v, buffer=0.0001):
    return lbound[0] - buffer <= v[0] <= ubound[0] + buffer and \
        lbound[1] - buffer <= v[1] <= ubound[1] + buffer and \
        lbound[2] - buffer <= v[2] <= ubound[2] + buffer


class act:

    # Add to ut.act class
    def select_by_loc(lbound=(0, 0, 0), ubound=(0, 0, 0),
                      select_mode='VERT', coords='GLOBAL'):

        # Set selection mode, VERT, EDGE, or FACE
        selection_mode(select_mode)

        # Grab the transformation matrix
        world = bpy.context.object.matrix_world

        # Instantiate a bmesh object and ensure lookup table
        # Running bm.faces.ensure_lookup_table() works for all parts
        bm = bmesh.from_edit_mesh(bpy.context.object.data)
        bm.faces.ensure_lookup_table()

        # Initialize list of vertices and list of parts to be selected
        verts = []
        to_select = []

        # For VERT, EDGE, or FACE ...
        # 1. Grab list of global or local coordinates
        # 2. Test if the piece is entirely within the rectangular
        #    prism defined by lbound and ubound
        # 3. Select each piece that returned True and deselect
        #    each piece that returned False in Step 2

        if select_mode == 'VERT':
            if coords == 'GLOBAL':
                [verts.append((world * v.co).to_tuple()) for v in bm.verts]
            elif coords == 'LOCAL':
                [verts.append(v.co.to_tuple()) for v in bm.verts]

            [to_select.append(in_bbox(lbound, ubound, v)) for v in verts]
            for vertObj, select in zip(bm.verts, to_select):
                vertObj.select = select

        if select_mode == 'EDGE':
            if coords == 'GLOBAL':
                [verts.append([(world * v.co).to_tuple()
                               for v in e.verts]) for e in bm.edges]
            elif coords == 'LOCAL':
                [verts.append([v.co.to_tuple() for v in e.verts])
                 for e in bm.edges]

            [to_select.append(all(in_bbox(lbound, ubound, v)
                                  for v in e)) for e in verts]
            for edgeObj, select in zip(bm.edges, to_select):
                edgeObj.select = select

        if select_mode == 'FACE':
            if coords == 'GLOBAL':
                [verts.append([(world * v.co).to_tuple()
                               for v in f.verts]) for f in bm.faces]
            elif coords == 'LOCAL':
                [verts.append([v.co.to_tuple() for v in f.verts])
                 for f in bm.faces]

            [to_select.append(all(in_bbox(lbound, ubound, v)
                                  for v in f)) for f in verts]
            for faceObj, select in zip(bm.faces, to_select):
                faceObj.select = select