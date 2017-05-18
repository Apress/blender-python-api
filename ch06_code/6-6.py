# Draws the distance between the origins of each object supplied
def draw_distance_matrix(context, obs, rgb_line, rgb_label, fsize):

    N = len(obs)
    for j in range(0, N):
        for i in range(j + 1, N):
            a = obs[i].location
            b = obs[j].location
            d = dist(a, b)
            mp = midpoint(a, b)

            a_2d = gl_pts(context, a)
            b_2d = gl_pts(context, b)
            mp_2d = gl_pts(context, mp)

            bgl.glColor4f(*rgb_line)
            draw_line(a_2d, b_2d)

            bgl.glColor4f(*rgb_label)
            draw_text(mp_2d, '%.3f' % d, fsize)

            
# Add this to draw_main() to draw between all selected objects:
# obs = context.selected_objects
# draw_distance_matrix(context, obs, rgb_line, rgb_label, fsize)

# Add this to draw_main() to draw between all objects in scene:
# obs = context.scene.objects
# draw_distance_matrix(context, obs, rgb_line, rgb_label, fsize)