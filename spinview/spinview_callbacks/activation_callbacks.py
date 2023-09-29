def activation_callbacks_initialize(
    local_state, pyvista_LR, state, ctrl, plot_multiple_meshes, plotter,viewer
):
    @state.change("activate_glyphs")
    def activate_glyphs(activate_glyphs=pyvista_LR.add_glyphs, **kwargs):
        if local_state.activate_glyphs_indicator == 0:
            local_state.activate_glyphs_indicator = 1
            pass
        else:
            pyvista_LR.add_glyphs = activate_glyphs
            try:
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()
            except:
                print("Can not activate glyphs, check if the data is loaded")
                pass

    # ___________________________
    # Point activation
    # ___________________________
    @state.change("activate_point")
    def activate_point(activate_point=pyvista_LR.add_simple_point, **kwargs):
        if local_state.activate_point_indicator == 0:
            local_state.activate_point_indicator = 1
            pass
        else:
            pyvista_LR.add_simple_point = activate_point
            try:
                plot_multiple_meshes(pyvista_LR, plotter, local_state)

                ctrl.view_update()
            except:
                print("Can not activate cone, check if the data is loaded")
                pass

    # ___________________________
    # Cones activation
    # ___________________________
    @state.change("activate_cone")
    def activate_cone(activate_cone=pyvista_LR.add_cone, **kwargs):
        if local_state.activate_cone_indicator == 0:
            local_state.activate_cone_indicator = 1
            pass
        else:
            pyvista_LR.add_cone = activate_cone
            try:
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()
            except:
                print("Can not activate cone, check if the data is loaded")
                pass

    # ___________________________
    # Arrows activation
    # ___________________________
    @state.change("activate_arrow")
    def activate_arrow(activate_arrow=pyvista_LR.add_arrow, **kwargs):
        if local_state.activate_arrow_indicator == 0:
            local_state.activate_arrow_indicator = 1
            pass
        else:
            pyvista_LR.add_arrow = activate_arrow
            try:
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()
            except:
                print("Can not activate Arrow, check if the data is loaded")
                pass

    # ___________________________
    # Sphere activation
    # ___________________________
    @state.change("activate_sphere")
    def activate_sphere(activate_sphere=pyvista_LR.add_sphere, **kwargs):
        if local_state.activate_sphere_indicator == 0:
            local_state.activate_sphere_indicator = 1
            pass
        else:
            pyvista_LR.add_sphere = activate_sphere
            try:
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()
            except:
                print("Can not activate sphere, check if the data is loaded")
                pass

    # ___________________________
    # plane activation
    # ___________________________
    @state.change("activate_plane")
    def activate_plane(activate_plane=pyvista_LR.add_plane, **kwargs):
        if local_state.activate_plane_indicator == 0:
            local_state.activate_plane_indicator = 1
            pass
        else:
            pyvista_LR.add_plane = activate_plane
            try:
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()
            except:
                print("Can not activate plane, check if the data is loaded")
                pass

    # ___________________________
    # box  activation
    # ___________________________
    @state.change("activate_box")
    def activate_box(activate_box=pyvista_LR.add_box, **kwargs):
        if local_state.activate_box_indicator == 0:
            local_state.activate_box_indicator = 1
            pass
        else:
            pyvista_LR.add_box = activate_box
            try:
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()
            except:
                print("Can not activate box, check if the data is loaded")
                pass

    # ___________________________
    # own_glyphs  activation
    # ___________________________

    @state.change("activate_own_glyphs")
    def activate_own_glyphs(activate_own_glyphs=pyvista_LR.add_own_glyphs, **kwargs):
        if local_state.activate_own_glyphs_indicator == 0:
            local_state.activate_own_glyphs_indicator = 1
            pass
        else:
            pyvista_LR.add_own_glyphs = activate_own_glyphs
            # plot_multiple_meshes(pyvista_LR, plotter, local_state)
            # ctrl.view_update()
            try:
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()
            except:
                print("Can not activate own_glyphs, check if the data is loaded")
                pass

    @state.change("activate_unstructured_mesh")
    def activate_glyphs(
        activate_unstructured_mesh=pyvista_LR.add_unstructured_mesh, **kwargs
    ):
        if local_state.activate_unstructured_mesh_indicator == 0:
            local_state.activate_unstructured_mesh_indicator = 1
            pass
        else:
            pyvista_LR.add_unstructured_mesh = activate_unstructured_mesh
            ctrl.view_update()

            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()
            # try:
            #     plot_multiple_meshes(pyvista_LR,plotter,local_state)
            #     ctrl.view_update()
            # except:
            #     print('Can not activate unstructured mesh, check if the data is loaded')
            #     pass

    @state.change("activate_rectangle_mesh")
    def activate_glyphs(
        activate_rectangle_mesh=pyvista_LR.add_rectangle_mesh, **kwargs
    ):
        if local_state.activate_rectangle_mesh_indicator == 0:
            local_state.activate_rectangle_mesh_indicator = 1
            pass
        else:
            pyvista_LR.add_rectangle_mesh = activate_rectangle_mesh
            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()
