def rmesh_callbacks_initialize(
    local_state, pyvista_LR, state, ctrl, plot_multiple_meshes, plotter, viewer
):
    @state.change("do_clip_component_recmesh")
    def do_clip_component_recmesh(
        do_clip_component_recmesh=pyvista_LR.do_rectangle_mesh_clip_scalar, **kwargs
    ):
        if local_state.do_clip_component_recmesh_indicator == 0:
            local_state.do_clip_component_recmesh_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                pyvista_LR.do_rectangle_mesh_clip_scalar = do_clip_component_recmesh
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("rectangle_mesh_rescale")
    def rectangle_mesh_rescale(
        rectangle_mesh_rescale=pyvista_LR.do_rectangle_mesh_rescale, **kwargs
    ):
        if local_state.rectangle_mesh_rescale_indicator == 0:
            local_state.rectangle_mesh_rescale_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                pyvista_LR.do_rectangle_mesh_rescale = rectangle_mesh_rescale
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("rescale_rectangle_mesh_factor")
    def rescale_rectangle_mesh_factor(
        rescale_rectangle_mesh_factor=pyvista_LR.rescale_rectangle_mesh_factor, **kwargs
    ):
        if local_state.rescale_rectangle_mesh_factor_indicator == 0:
            local_state.rescale_rectangle_mesh_factor_indicator = 1
            pass
        else:
            if pyvista_LR.do_rectangle_mesh_rescale:
                pyvista_LR.rescale_rectangle_mesh_factor = rescale_rectangle_mesh_factor
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("metallic_rmesh")
    def metallic_rmesh(metallic_rmesh=local_state.metallic_rmesh, **kwargs):
        if local_state.metallic_rmesh_indicator == 0:
            local_state.metallic_rmesh_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                local_state.metallic_rmesh = metallic_rmesh
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("pbr_rectangle")
    def pbr_rectangle(pbr_rectangle=pyvista_LR.pbr_rectangle, **kwargs):
        if local_state.pbr_rectangle_indicator == 0:
            local_state.pbr_rectangle_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                pyvista_LR.pbr_rectangle = pbr_rectangle
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("do_rectangle_mesh_contour")
    def do_rectangle_mesh_contour(
        do_rectangle_mesh_contour=pyvista_LR.do_rectangle_mesh_contour, **kwargs
    ):
        if local_state.do_rectangle_mesh_contour_indicator == 0:
            local_state.do_rectangle_mesh_contour_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                pyvista_LR.do_rectangle_mesh_contour = do_rectangle_mesh_contour
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("rectangle_mesh_interpolate_before_map")
    def rectangle_mesh_interpolate_before_map(
        rectangle_mesh_interpolate_before_map=pyvista_LR.rectangle_mesh_interpolate_before_map,
        **kwargs
    ):
        if local_state.rectangle_mesh_interpolate_before_map_indicator == 0:
            local_state.rectangle_mesh_interpolate_before_map_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                pyvista_LR.rectangle_mesh_interpolate_before_map = (
                    rectangle_mesh_interpolate_before_map
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("do_multi_rectangle_surface_contour")
    def do_multi_rectangle_surface_contour(
        do_multi_rectangle_surface_contour=pyvista_LR.do_multi_rectangle_surface_contour,
        **kwargs
    ):
        if local_state.do_multi_rectangle_surface_contour_indicator == 0:
            local_state.do_multi_rectangle_surface_contour_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                pyvista_LR.do_multi_rectangle_surface_contour = (
                    do_multi_rectangle_surface_contour
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("opacity_record_rectangle_mesh")
    def opacity_record_rectangle_mesh(
        opacity_record_rectangle_mesh=local_state.opacity_record_rectangle_mesh,
        **kwargs
    ):
        if local_state.opacity_record_rectangle_mesh_indicator == 0:
            local_state.opacity_record_rectangle_mesh_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                local_state.opacity_record_rectangle_mesh = (
                    opacity_record_rectangle_mesh
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("roughness_rmesh")
    def roughness_rmesh(roughness_rmesh=local_state.roughness_rmesh, **kwargs):
        if local_state.roughness_rmesh_indicator == 0:
            local_state.roughness_rmesh_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                local_state.roughness_rmesh = roughness_rmesh
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("rectangle_mesh_contour_isosurface_number")
    def rectangle_mesh_contour_isosurface_number(
        rectangle_mesh_contour_isosurface_number=pyvista_LR.rectangle_mesh_contour_isosurface_number,
        **kwargs
    ):
        if local_state.rectangle_mesh_contour_isosurface_number_indicator == 0:
            local_state.rectangle_mesh_contour_isosurface_number_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                pyvista_LR.rectangle_mesh_contour_isosurface_number = (
                    rectangle_mesh_contour_isosurface_number
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("rectangle_mesh_contour_isosurface_value_t")
    def rectangle_mesh_contour_isosurface_value_t(
        rectangle_mesh_contour_isosurface_value_t=local_state.rectangle_mesh_contour_isosurface_value_t,
        **kwargs
    ):
        if local_state.rectangle_mesh_contour_isosurface_value_t_indicator == 0:
            local_state.rectangle_mesh_contour_isosurface_value_t_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                local_state.rectangle_mesh_contour_isosurface_value_t = (
                    rectangle_mesh_contour_isosurface_value_t
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("rectangle_mesh_contour_isosurface_value_p")
    def rectangle_mesh_contour_isosurface_value_p(
        rectangle_mesh_contour_isosurface_value_p=local_state.rectangle_mesh_contour_isosurface_value_p,
        **kwargs
    ):
        if local_state.rectangle_mesh_contour_isosurface_value_p_indicator == 0:
            local_state.rectangle_mesh_contour_isosurface_value_p_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                local_state.rectangle_mesh_contour_isosurface_value_p = (
                    rectangle_mesh_contour_isosurface_value_p
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("rectangle_mesh_contour_isosurface_value_x")
    def rectangle_mesh_contour_isosurface_value_x(
        rectangle_mesh_contour_isosurface_value_x=local_state.rectangle_mesh_contour_isosurface_value_x,
        **kwargs
    ):
        if local_state.rectangle_mesh_contour_isosurface_value_x_indicator == 0:
            local_state.rectangle_mesh_contour_isosurface_value_x_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                local_state.rectangle_mesh_contour_isosurface_value_x = (
                    rectangle_mesh_contour_isosurface_value_x
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("rectangle_mesh_contour_isosurface_value_y")
    def rectangle_mesh_contour_isosurface_value_y(
        rectangle_mesh_contour_isosurface_value_y=local_state.rectangle_mesh_contour_isosurface_value_y,
        **kwargs
    ):
        if local_state.rectangle_mesh_contour_isosurface_value_y_indicator == 0:
            local_state.rectangle_mesh_contour_isosurface_value_y_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                local_state.rectangle_mesh_contour_isosurface_value_y = (
                    rectangle_mesh_contour_isosurface_value_y
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("rectangle_mesh_contour_isosurface_value_z")
    def rectangle_mesh_contour_isosurface_value_z(
        rectangle_mesh_contour_isosurface_value_z=local_state.rectangle_mesh_contour_isosurface_value_z,
        **kwargs
    ):
        if local_state.rectangle_mesh_contour_isosurface_value_z_indicator == 0:
            local_state.rectangle_mesh_contour_isosurface_value_z_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                local_state.rectangle_mesh_contour_isosurface_value_z = (
                    rectangle_mesh_contour_isosurface_value_z
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("rectangle_mesh_rescale_norm_x")
    def rectangle_mesh_rescale_norm_x(
        rectangle_mesh_rescale_norm_x=pyvista_LR.rescale_rectangle_mesh_norm[0],
        **kwargs
    ):
        try:
            pyvista_LR.rescale_rectangle_mesh_norm = (
                float(rectangle_mesh_rescale_norm_x),
                pyvista_LR.rescale_rectangle_mesh_norm[1],
                pyvista_LR.rescale_rectangle_mesh_norm[2],
            )
        except:
            pass

    @state.change("rectangle_mesh_rescale_norm_y")
    def rectangle_mesh_rescale_norm_y(
        rectangle_mesh_rescale_norm_y=pyvista_LR.rescale_rectangle_mesh_norm[1],
        **kwargs
    ):
        try:
            pyvista_LR.rescale_rectangle_mesh_norm = (
                pyvista_LR.rescale_rectangle_mesh_norm[0],
                float(rectangle_mesh_rescale_norm_y),
                pyvista_LR.rescale_rectangle_mesh_norm[2],
            )
        except:
            pass

    @state.change("rectangle_mesh_rescale_norm_z")
    def rectangle_mesh_rescale_norm_z(
        rectangle_mesh_rescale_norm_z=pyvista_LR.rescale_rectangle_mesh_norm[2],
        **kwargs
    ):
        try:
            pyvista_LR.rescale_rectangle_mesh_norm = (
                pyvista_LR.rescale_rectangle_mesh_norm[0],
                pyvista_LR.rescale_rectangle_mesh_norm[1],
                float(rectangle_mesh_rescale_norm_z),
            )
        except:
            pass

    @state.change("rectangle_mesh_clip_plane_free_normal_1_x")
    def rectangle_mesh_clip_plane_free_normal_1_x(
        rectangle_mesh_clip_plane_free_normal_1_x=pyvista_LR.rectangle_mesh_clip_plane_free_normal_1[
            0
        ],
        **kwargs
    ):
        try:
            pyvista_LR.rectangle_mesh_clip_plane_free_normal_1 = (
                float(rectangle_mesh_clip_plane_free_normal_1_x),
                pyvista_LR.rectangle_mesh_clip_plane_free_normal_1_1[1],
                pyvista_LR.rectangle_mesh_clip_plane_free_normal_1_1[2],
            )
        except:
            pass

    @state.change("rectangle_mesh_clip_plane_free_normal_1_y")
    def rectangle_mesh_clip_plane_free_normal_1_y(
        rectangle_mesh_clip_plane_free_normal_1_y=pyvista_LR.rectangle_mesh_clip_plane_free_normal_1[
            0
        ],
        **kwargs
    ):
        try:
            pyvista_LR.rectangle_mesh_clip_plane_free_normal_1 = (
                pyvista_LR.rectangle_mesh_clip_plane_free_normal_1[0],
                float(rectangle_mesh_clip_plane_free_normal_1_y),
                pyvista_LR.rectangle_mesh_clip_plane_free_normal_1[2],
            )
        except:
            pass

    @state.change("rectangle_mesh_clip_plane_free_normal_1_z")
    def rectangle_mesh_clip_plane_free_normal_1_z(
        rectangle_mesh_clip_plane_free_normal_1_z=pyvista_LR.rectangle_mesh_clip_plane_free_normal_1[
            0
        ],
        **kwargs
    ):
        try:
            pyvista_LR.rectangle_mesh_clip_plane_free_normal_1 = (
                pyvista_LR.rectangle_mesh_clip_plane_free_normal_1[0],
                pyvista_LR.rectangle_mesh_clip_plane_free_normal_1[1],
                float(rectangle_mesh_clip_plane_free_normal_1_z),
            )
        except:
            pass

    @state.change("rectangle_mesh_clip_plane_free_normal_2_x")
    def rectangle_mesh_clip_plane_free_normal_2_x(
        rectangle_mesh_clip_plane_free_normal_2_x=pyvista_LR.rectangle_mesh_clip_plane_free_normal_2[
            0
        ],
        **kwargs
    ):
        try:
            pyvista_LR.rectangle_mesh_clip_plane_free_normal_2 = (
                float(rectangle_mesh_clip_plane_free_normal_2_x),
                pyvista_LR.rectangle_mesh_clip_plane_free_normal_2[1],
                pyvista_LR.rectangle_mesh_clip_plane_free_normal_2[2],
            )
        except:
            pass

    @state.change("rectangle_mesh_clip_plane_free_normal_2_y")
    def rectangle_mesh_clip_plane_free_normal_2_y(
        rectangle_mesh_clip_plane_free_normal_2_y=pyvista_LR.rectangle_mesh_clip_plane_free_normal_2[
            0
        ],
        **kwargs
    ):
        try:
            pyvista_LR.rectangle_mesh_clip_plane_free_normal_2 = (
                pyvista_LR.rectangle_mesh_clip_plane_free_normal_2[0],
                float(rectangle_mesh_clip_plane_free_normal_2_y),
                pyvista_LR.rectangle_mesh_clip_plane_free_normal_2[2],
            )
        except:
            pass

    @state.change("rectangle_mesh_clip_plane_free_normal_2_z")
    def rectangle_mesh_clip_plane_free_normal_2_z(
        rectangle_mesh_clip_plane_free_normal_2_z=pyvista_LR.rectangle_mesh_clip_plane_free_normal_2[
            0
        ],
        **kwargs
    ):
        try:
            pyvista_LR.rectangle_mesh_clip_plane_free_normal_2 = (
                pyvista_LR.rectangle_mesh_clip_plane_free_normal_2[0],
                pyvista_LR.rectangle_mesh_clip_plane_free_normal_2[1],
                float(rectangle_mesh_clip_plane_free_normal_2_z),
            )
        except:
            pass

    @state.change("Cut_X_rmesh")
    def Cut_X_rmesh(
        Cut_X_rmesh=[
            local_state.rectangle_mesh_clip_scalar_max_x,
            local_state.rectangle_mesh_clip_scalar_min_x,
        ],
        **kwargs
    ):
        if local_state.Cut_X_indicator == 0:
            local_state.Cut_X_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                if (
                    pyvista_LR.add_rectangle_mesh
                    and pyvista_LR.do_rectangle_mesh_clip_scalar
                ):
                    max = Cut_X_rmesh[1]
                    min = Cut_X_rmesh[0]
                    local_state.rectangle_mesh_clip_scalar_max_x = max
                    local_state.rectangle_mesh_clip_scalar_min_x = min
                    plot_multiple_meshes(pyvista_LR, plotter, local_state)
                    ctrl.view_update()

    @state.change("Cut_Y_rmesh")
    def Cut_Y_rmesh(
        Cut_Y_rmesh=[
            local_state.rectangle_mesh_clip_scalar_max_y,
            local_state.rectangle_mesh_clip_scalar_min_y,
        ],
        **kwargs
    ):
        if local_state.Cut_Y_indicator == 0:
            local_state.Cut_Y_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                if (
                    pyvista_LR.add_rectangle_mesh
                    and pyvista_LR.do_rectangle_mesh_clip_scalar
                ):
                    max = Cut_Y_rmesh[1]
                    min = Cut_Y_rmesh[0]
                    local_state.rectangle_mesh_clip_scalar_max_y = max
                    local_state.rectangle_mesh_clip_scalar_min_y = min
                    plot_multiple_meshes(pyvista_LR, plotter, local_state)
                    ctrl.view_update()

    @state.change("Cut_Z_rmesh")
    def Cut_Z_rmesh(
        Cut_Z_rmesh=[
            local_state.rectangle_mesh_clip_scalar_max_z,
            local_state.rectangle_mesh_clip_scalar_min_z,
        ],
        **kwargs
    ):
        if local_state.Cut_Z_indicator == 0:
            local_state.Cut_Z_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                if (
                    pyvista_LR.add_rectangle_mesh
                    and pyvista_LR.do_rectangle_mesh_clip_scalar
                ):
                    max = Cut_Z_rmesh[1]
                    min = Cut_Z_rmesh[0]
                    local_state.rectangle_mesh_clip_scalar_max_z = max
                    local_state.rectangle_mesh_clip_scalar_min_z = min
                    plot_multiple_meshes(pyvista_LR, plotter, local_state)
                    ctrl.view_update()

    @state.change("Cut_theta_rmesh")
    def Cut_theta_rmesh(
        Cut_theta_rmesh=[
            pyvista_LR.rectangle_mesh_clip_scalar_min_theta,
            pyvista_LR.rectangle_mesh_clip_scalar_max_theta,
        ],
        **kwargs
    ):
        if local_state.Cut_theta_indicator == 0:
            local_state.Cut_theta_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                if (
                    pyvista_LR.add_rectangle_mesh
                    and pyvista_LR.do_rectangle_mesh_clip_scalar
                ):
                    max = Cut_theta_rmesh[1]
                    min = Cut_theta_rmesh[0]
                    pyvista_LR.rectangle_mesh_clip_scalar_max_theta = max
                    pyvista_LR.rectangle_mesh_clip_scalar_min_theta = min
                    plot_multiple_meshes(pyvista_LR, plotter, local_state)
                    ctrl.view_update()

    @state.change("Cut_phi_rmesh")
    def Cut_phi_rmesh(
        Cut_phi_rmesh=[
            pyvista_LR.rectangle_mesh_clip_scalar_min_phi,
            pyvista_LR.rectangle_mesh_clip_scalar_max_phi,
        ],
        **kwargs
    ):
        if local_state.Cut_phi_indicator == 0:
            local_state.Cut_phi_indicator = 1
            pass
        else:
            if pyvista_LR.add_rectangle_mesh:
                if (
                    pyvista_LR.add_rectangle_mesh
                    and pyvista_LR.do_rectangle_mesh_clip_scalar
                ):
                    max = Cut_phi_rmesh[1]
                    min = Cut_phi_rmesh[0]
                    pyvista_LR.rectangle_mesh_clip_scalar_max_phi = max
                    pyvista_LR.rectangle_mesh_clip_scalar_min_phi = min
                    plot_multiple_meshes(pyvista_LR, plotter, local_state)
                    ctrl.view_update()

    @state.change("rectangle_mesh_clip_plane_x_min")
    def rectangle_mesh_clip_plane_x_min(
        rectangle_mesh_clip_plane_x_min=pyvista_LR.rectangle_mesh_clip_plane_x_min,
        **kwargs
    ):
        if local_state.rectangle_mesh_clip_plane_x_min_indicator == 0:
            local_state.rectangle_mesh_clip_plane_x_min_indicator = 1
            pass
        else:
            if pyvista_LR.do_rectangle_mesh_clip:
                pyvista_LR.rectangle_mesh_clip_plane_x_min = (
                    rectangle_mesh_clip_plane_x_min
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("rectangle_mesh_clip_plane_x_max")
    def rectangle_mesh_clip_plane_x_max(
        rectangle_mesh_clip_plane_x_max=pyvista_LR.rectangle_mesh_clip_plane_x_max,
        **kwargs
    ):
        if local_state.rectangle_mesh_clip_plane_x_max_indicator == 0:
            local_state.rectangle_mesh_clip_plane_x_max_indicator = 1
            pass
        else:
            if pyvista_LR.do_rectangle_mesh_clip:
                pyvista_LR.rectangle_mesh_clip_plane_x_max = (
                    rectangle_mesh_clip_plane_x_max
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("rectangle_mesh_clip_plane_y_max")
    def rectangle_mesh_clip_plane_y_max(
        rectangle_mesh_clip_plane_y_max=pyvista_LR.rectangle_mesh_clip_plane_y_max,
        **kwargs
    ):
        if local_state.rectangle_mesh_clip_plane_y_max_indicator == 0:
            local_state.rectangle_mesh_clip_plane_y_max_indicator = 1
            pass
        else:
            if pyvista_LR.do_rectangle_mesh_clip:
                pyvista_LR.rectangle_mesh_clip_plane_y_max = (
                    rectangle_mesh_clip_plane_y_max
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("rectangle_mesh_clip_plane_y_min")
    def rectangle_mesh_clip_plane_y_min(
        rectangle_mesh_clip_plane_y_min=pyvista_LR.rectangle_mesh_clip_plane_y_min,
        **kwargs
    ):
        if local_state.rectangle_mesh_clip_plane_y_min_indicator == 0:
            local_state.rectangle_mesh_clip_plane_y_min_indicator = 1
            pass
        else:
            if pyvista_LR.do_rectangle_mesh_clip:
                pyvista_LR.rectangle_mesh_clip_plane_y_min = (
                    rectangle_mesh_clip_plane_y_min
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("rectangle_mesh_clip_plane_z_min")
    def rectangle_mesh_clip_plane_z_min(
        rectangle_mesh_clip_plane_z_min=pyvista_LR.rectangle_mesh_clip_plane_z_min,
        **kwargs
    ):
        if local_state.rectangle_mesh_clip_plane_z_min_indicator == 0:
            local_state.rectangle_mesh_clip_plane_z_min_indicator = 1
            pass
        else:
            if pyvista_LR.do_rectangle_mesh_clip:
                pyvista_LR.rectangle_mesh_clip_plane_z_min = (
                    rectangle_mesh_clip_plane_z_min
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("rectangle_mesh_clip_plane_z_max")
    def rectangle_mesh_clip_plane_z_max(
        rectangle_mesh_clip_plane_z_max=pyvista_LR.rectangle_mesh_clip_plane_z_max,
        **kwargs
    ):
        if local_state.rectangle_mesh_clip_plane_z_max_indicator == 0:
            local_state.rectangle_mesh_clip_plane_z_max_indicator = 1
            pass
        else:
            if pyvista_LR.do_rectangle_mesh_clip:
                pyvista_LR.rectangle_mesh_clip_plane_z_max = (
                    rectangle_mesh_clip_plane_z_max
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("clip_rectangle_mesh_free_1")
    def clip_rectangle_mesh_free_1(
        clip_rectangle_mesh_free_1=pyvista_LR.clip_rectangle_mesh_free_1, **kwargs
    ):
        if local_state.clip_rectangle_mesh_free_1_indicator == 0:
            local_state.clip_rectangle_mesh_free_1_indicator = 1
            pass
        else:
            if pyvista_LR.do_clip_rectangle_mesh_free_normal:
                pyvista_LR.clip_rectangle_mesh_free_1 = clip_rectangle_mesh_free_1
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("clip_rectangle_mesh_free_2")
    def clip_rectangle_mesh_free_2(
        clip_rectangle_mesh_free_2=pyvista_LR.clip_rectangle_mesh_free_2, **kwargs
    ):
        if local_state.clip_rectangle_mesh_free_2_indicator == 0:
            local_state.clip_rectangle_mesh_free_2_indicator = 1
            pass
        else:
            if pyvista_LR.do_clip_rectangle_mesh_free_normal:
                pyvista_LR.clip_rectangle_mesh_free_2 = clip_rectangle_mesh_free_2
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    def change_rectangle_cmap_vbtn_value_0():
        local_state.rectangle_cmap_vbtn = 0
        pyvista_LR.rectrangle_color_index = local_state.rectangle_cmap_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_rectangle_cmap_vbtn_value_1():
        local_state.rectangle_cmap_vbtn = 1
        pyvista_LR.rectrangle_color_index = local_state.rectangle_cmap_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_rectangle_cmap_vbtn_value_2():
        local_state.rectangle_cmap_vbtn = 2
        pyvista_LR.rectrangle_color_index = local_state.rectangle_cmap_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_rectangle_cmap_vbtn_value_3():
        local_state.rectangle_cmap_vbtn = 3
        pyvista_LR.rectrangle_color_index = local_state.rectangle_cmap_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_rectangle_cmap_vbtn_value_4():
        local_state.rectangle_cmap_vbtn = 4
        pyvista_LR.rectrangle_color_index = local_state.rectangle_cmap_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_rectangle_opacity_index_vbtn_value_0():
        local_state.rectangle_opaciy_vbtn = 0
        pyvista_LR.rectrangle_opacity_index = local_state.rectangle_opaciy_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_rectangle_opacity_index_vbtn_value_1():
        local_state.rectangle_opaciy_vbtn = 1
        pyvista_LR.rectrangle_opacity_index = local_state.rectangle_opaciy_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_rectangle_opacity_index_vbtn_value_2():
        local_state.rectangle_opaciy_vbtn = 2
        pyvista_LR.rectrangle_opacity_index = local_state.rectangle_opaciy_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_rectangle_opacity_index_vbtn_value_3():
        local_state.rectangle_opaciy_vbtn = 3
        pyvista_LR.rectrangle_opacity_index = local_state.rectangle_opaciy_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_rectangle_opacity_index_vbtn_value_4():
        local_state.rectangle_opaciy_vbtn = 4
        pyvista_LR.rectrangle_opacity_index = local_state.rectangle_opaciy_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_rectangle_opacity_index_vbtn_value_5():
        local_state.rectangle_opaciy_vbtn = 5
        pyvista_LR.rectrangle_opacity_index = local_state.rectangle_opaciy_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_rectangle_opacity_index_vbtn_value_6():
        local_state.rectangle_opaciy_vbtn = 6
        pyvista_LR.rectrangle_opacity_index = local_state.rectangle_opaciy_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def do_r_mesh_clip():
        if pyvista_LR.add_rectangle_mesh:
            pyvista_LR.do_rectangle_mesh_clip = not (pyvista_LR.do_rectangle_mesh_clip)
            if pyvista_LR.do_rectangle_mesh_clip:
                local_state.face_clip_index_r.append("face_clip_r_0")
            else:
                if "face_clip_r_0" in local_state.face_clip_index_r:
                    local_state.face_clip_index_r.remove("face_clip_r_0")

            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    def do_clip_r_mesh_free_normal():
        if pyvista_LR.add_rectangle_mesh:
            pyvista_LR.do_clip_rectangle_mesh_free_normal = not (
                pyvista_LR.do_clip_rectangle_mesh_free_normal
            )
            if pyvista_LR.do_clip_plane_free_normal:
                local_state.face_clip_index_r.append("face_clip_r_1")
            else:
                if "face_clip_r_1" in local_state.face_clip_index_r:
                    local_state.face_clip_index_r.remove("face_clip_r_1")
            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    def Contour_0():
        pyvista_LR.rectangle_mesh_contour_method_indicator = 0
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def Contour_1():
        pyvista_LR.rectangle_mesh_contour_method_indicator = 1
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def Contour_2():
        pyvista_LR.rectangle_mesh_contour_method_indicator = 2
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def Contour_3():
        pyvista_LR.rectangle_mesh_contour_method_indicator = 3
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def Contour_4():
        pyvista_LR.rectangle_mesh_contour_method_indicator = 4
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    return (
        Contour_0,
        Contour_1,
        Contour_2,
        Contour_3,
        Contour_4,
        change_rectangle_cmap_vbtn_value_0,
        change_rectangle_cmap_vbtn_value_1,
        change_rectangle_cmap_vbtn_value_2,
        change_rectangle_cmap_vbtn_value_3,
        change_rectangle_cmap_vbtn_value_4,
        change_rectangle_opacity_index_vbtn_value_0,
        change_rectangle_opacity_index_vbtn_value_1,
        change_rectangle_opacity_index_vbtn_value_2,
        change_rectangle_opacity_index_vbtn_value_3,
        change_rectangle_opacity_index_vbtn_value_4,
        change_rectangle_opacity_index_vbtn_value_5,
        change_rectangle_opacity_index_vbtn_value_6,
        do_r_mesh_clip,
        do_clip_r_mesh_free_normal,
    )
