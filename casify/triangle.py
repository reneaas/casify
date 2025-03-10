def _draw_angle_arc(
    vertex,
    *other_points,
    radius=0.4,
    show_angle_value=False,
    vertex_label=None,
    side_label=False,
    fontsize=20,
):
    """
    Draw an arc to show the angle between two points relative to a vertex.
    For right angles (90 degrees), draws a small square instead.

    Parameters:
    -----------
    ax : matplotlib.axes.Axes
        The axes to draw on
    vertex : tuple
        The vertex point (x, y)
    p1, p2 : tuple
        The two points forming the angle with the vertex
    radius : float
        Radius of the arc or size of the square for right angles
    """
    import numpy as np
    import plotmath

    ax = plotmath.gca()

    # Convert points to numpy arrays with float values
    vertex = np.array(vertex, dtype=float)
    p1, p2 = other_points
    p1 = np.array(p1, dtype=float)
    p2 = np.array(p2, dtype=float)

    # Calculate vectors from vertex to points
    v1 = p1 - vertex
    v2 = p2 - vertex

    # Calculate angles
    angle1 = np.arctan2(v1[1], v1[0])
    angle2 = np.arctan2(v2[1], v2[0])

    # Calculate the angle between vectors
    dot_product = np.dot(v1, v2)
    norms = np.linalg.norm(v1) * np.linalg.norm(v2)
    angle = np.arccos(np.clip(dot_product / norms, -1.0, 1.0))

    # Check if it's approximately a right angle (90 degrees = π/2 radians)
    if np.abs(angle - np.pi / 2) < 1e-10:
        # Draw a square for right angle
        # Get unit vectors

        katet_len = radius / np.sqrt(2)

        u1 = v1 / np.linalg.norm(v1)
        u2 = v2 / np.linalg.norm(v2)

        u1 = u1 * katet_len
        u2 = u2 * katet_len

        # Calculate square corners
        square_points = [
            vertex + u1,
            vertex + (u1 + u2),
            vertex + u2,
            vertex,
        ]

        # Convert to separate x and y arrays
        x = [p[0] for p in square_points]
        y = [p[1] for p in square_points]

        # Plot the square
        ax.plot(x, y, "k-", linewidth=1)

        unit_vector = np.array(
            [
                2 * radius * 0.5 * (np.cos(angle1) + np.cos(angle2)),
                2 * radius * 0.5 * (np.sin(angle1) + np.sin(angle2)),
            ]
        )

        if vertex_label:
            ax.text(
                x=vertex[0] - 0.5 * unit_vector[0],
                y=vertex[1] - 0.5 * unit_vector[1],
                s=f"${vertex_label}$",
                fontsize=fontsize,
                ha="center",
                va="center",
            )

    else:
        # Ensure proper angle range for drawing the smaller angle
        if abs(angle2 - angle1) > np.pi:
            if angle2 > angle1:
                angle2 -= 2 * np.pi
            else:
                angle1 -= 2 * np.pi

        # Create arc points
        theta = np.linspace(angle1, angle2, 100)
        x = vertex[0] + radius * np.cos(theta)
        y = vertex[1] + radius * np.sin(theta)

        # Draw the arc
        ax.plot(x, y, "k-", linewidth=1)

        # Calculate text position
        unit_vector = np.array(
            [
                2 * radius * 0.5 * (np.cos(angle1) + np.cos(angle2)),
                2 * radius * 0.5 * (np.sin(angle1) + np.sin(angle2)),
            ]
        )
        x = vertex[0] + unit_vector[0]
        y = vertex[1] + unit_vector[1]

        angle_deg = np.degrees(angle)
        if np.abs(angle_deg - round(angle_deg)) < 1e-8:
            angle_str = f"${int(round(angle_deg))}^\\circ$"
        else:
            angle_str = f"${angle_deg:.2f}^\\circ$"

        # Plot the angle value
        # Determine text alignment based on position relative to vertex
        dx = x - vertex[0]
        dy = y - vertex[1]

        # Set horizontal alignment
        if abs(dx) < 0.1:  # Near vertical
            ha = "center"
        elif dx > 0:
            ha = "left"
        else:
            ha = "right"

        # Set vertical alignment
        if abs(dy) < 0.1:  # Near horizontal
            va = "center"
        elif dy > 0:
            va = "bottom"
        else:
            va = "top"

        if show_angle_value:
            ax.text(x, y, angle_str, fontsize=fontsize, ha="center", va="center")

        if vertex_label:
            ax.text(
                x=vertex[0] - 0.5 * unit_vector[0],
                y=vertex[1] - 0.5 * unit_vector[1],
                s=f"${vertex_label}$",
                fontsize=fontsize,
                ha=ha,
                va=va,
            )

    if side_label:
        # Get the two points that form the side opposite to vertex
        p1, p2 = other_points

        # Calculate midpoint of the side
        midpoint = np.array([(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2])

        # Calculate side vector and its length
        side_vector = np.array(p2) - np.array(p1)
        side_length = np.linalg.norm(side_vector)

        # Create perpendicular vector (rotate 90 degrees counterclockwise)
        perp_vector = np.array([-side_vector[1], side_vector[0]])
        perp_vector = perp_vector / np.linalg.norm(perp_vector)  # Normalize

        # Determine if vertex is above or below the side
        vertex_to_mid = midpoint - vertex
        dot_product = np.dot(vertex_to_mid, perp_vector)

        # Offset in the opposite direction of the vertex
        offset = -np.sign(dot_product) * perp_vector * 0.3

        # Position the label
        label_pos = midpoint + offset

        # Format the side length
        if np.abs(side_length - round(side_length)) < 1e-10:
            side_str = f"${int(round(side_length))}$"
        else:
            side_str = f"${side_length:.2f}$"

        # Add the label with automatic alignment
        ax.text(
            label_pos[0],
            label_pos[1],
            side_str,
            fontsize=fontsize,
            ha="center",
            va="center",
        )


# def _label_vertices(points, labels=["A", "B", "C"]):

#     for point, label in zip(points, labels):


def draw_triangle(
    *points,
    sss=None,
    asa=None,
    sas=None,
    show_vertices=True,
    radius=0.4,
    alpha=0.1,
    show=True,
    color=(0, 100 / 255, 140 / 255),
    fontsize=20,
    label_angles=(True, True, True),
    vertex_labels=("A", "B", "C"),
    label_sides=(True, True, True),
):
    import sympy
    import plotmath

    if sss:
        triangle = sympy.Triangle(sss=sss)
    elif asa:
        triangle = sympy.Triangle(asa=asa)
    elif sas:
        triangle = sympy.Triangle(sas=sas)
    else:
        triangle = sympy.Triangle(*points)

    side_lengths = [side.length for side in triangle.sides]

    points = [(point.x.evalf(), point.y.evalf()) for point in triangle.vertices]

    plotmath.plot_polygon(
        *points,
        show_vertices=show_vertices,
        alpha=alpha,
        color=color,
    )

    for vertex, label_angle, vertex_label, label_side in zip(
        points, label_angles, vertex_labels, label_sides
    ):
        other_points = [point for point in points if point != vertex]

        _draw_angle_arc(
            vertex,
            *other_points,
            radius=radius,
            show_angle_value=label_angle,
            fontsize=fontsize,
            vertex_label=vertex_label,
            side_label=label_side,
        )

    ax = plotmath.gca()
    ax.axis("equal")
    ax.axis("off")

    if show:
        plotmath.show()
    else:
        return plotmath.gca()
