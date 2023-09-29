def tmesh_callbacks_initialize(
    local_state, pyvista_LR, state, ctrl, plot_multiple_meshes, plotter, viewer
):
    @state.change("do_clip_component_Tmesh")
    def do_clip_component_Tmesh(
        do_clip_component_Tmesh=pyvista_LR.do_unstructured_mesh_clip_scalar, **kwargs
    ):
        if local_state.do_clip_component_Tmesh_indicator == 0:
            local_state.do_clip_component_Tmesh_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                pyvista_LR.do_unstructured_mesh_clip_scalar = do_clip_component_Tmesh
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("unstructured_mesh_rescale")
    def unstructured_mesh_rescale(
        unstructured_mesh_rescale=pyvista_LR.do_unstructured_mesh_rescale, **kwargs
    ):
        if local_state.unstructured_mesh_rescale_indicator == 0:
            local_state.unstructured_mesh_rescale_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                pyvista_LR.do_unstructured_mesh_rescale = unstructured_mesh_rescale
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("rescale_unstructured_mesh_factor")
    def rescale_unstructured_mesh_factor(
        rescale_unstructured_mesh_factor=pyvista_LR.rescale_unstructured_mesh_factor,
        **kwargs
    ):
        if local_state.rescale_unstructured_mesh_factor_indicator == 0:
            local_state.rescale_unstructured_mesh_factor_indicator = 1
            pass
        else:
            if pyvista_LR.do_unstructured_mesh_rescale:
                pyvista_LR.rescale_unstructured_mesh_factor = (
                    rescale_unstructured_mesh_factor
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("metallic_tmesh")
    def metallic_tmesh(metallic_tmesh=local_state.metallic_tmesh, **kwargs):
        if local_state.metallic_tmesh_indicator == 0:
            local_state.metallic_tmesh_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                local_state.metallic_tmesh = metallic_tmesh
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("roughness_tmesh")
    def roughness_tmesh(roughness_tmesh=local_state.roughness_tmesh, **kwargs):
        if local_state.roughness_tmesh_indicator == 0:
            local_state.roughness_tmesh_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                local_state.roughness_tmesh = roughness_tmesh
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("pbr_unstructured")
    def pbr_unstructured(pbr_unstructured=pyvista_LR.pbr_unstructured, **kwargs):
        if local_state.pbr_unstructured_indicator == 0:
            local_state.pbr_unstructured_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                pyvista_LR.pbr_unstructured = pbr_unstructured
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("do_multi_unstructured_surface_contour")
    def do_multi_unstructured_surface_contour(
        do_multi_unstructured_surface_contour=pyvista_LR.do_multi_unstructured_surface_contour,
        **kwargs
    ):
        if local_state.do_multi_unstructured_surface_contour_indicator == 0:
            local_state.do_multi_unstructured_surface_contour_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                pyvista_LR.do_multi_unstructured_surface_contour = (
                    do_multi_unstructured_surface_contour
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("unstructured_mesh_interpolate_before_map")
    def unstructured_mesh_interpolate_before_map(
        unstructured_mesh_interpolate_before_map=pyvista_LR.unstructured_mesh_interpolate_before_map,
        **kwargs
    ):
        if local_state.unstructured_mesh_interpolate_before_map_indicator == 0:
            local_state.unstructured_mesh_interpolate_before_map_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                pyvista_LR.unstructured_mesh_interpolate_before_map = (
                    unstructured_mesh_interpolate_before_map
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("do_unstructured_mesh_contour")
    def do_unstructured_mesh_contour(
        do_unstructured_mesh_contour=pyvista_LR.do_unstructured_mesh_contour, **kwargs
    ):
        if local_state.do_unstructured_mesh_contour_indicator == 0:
            local_state.do_unstructured_mesh_contour_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                pyvista_LR.do_unstructured_mesh_contour = do_unstructured_mesh_contour
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("opacity_record_tmesh")
    def opacity_record_tmesh(
        opacity_record_tmesh=local_state.opacity_record_tmesh, **kwargs
    ):
        if local_state.opacity_record_tmesh_indicator == 0:
            local_state.opacity_record_tmesh_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                local_state.opacity_record_tmesh = opacity_record_tmesh
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("roughness_tmesh")
    def roughness_tmesh(roughness_tmesh=local_state.roughness_tmesh, **kwargs):
        if local_state.roughness_tmesh_indicator == 0:
            local_state.roughness_tmesh_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                local_state.roughness_tmesh = roughness_tmesh
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("unstructured_mesh_contour_isosurface_number")
    def unstructured_mesh_contour_isosurface_number(
        unstructured_mesh_contour_isosurface_number=pyvista_LR.unstructured_mesh_contour_isosurface_number,
        **kwargs
    ):
        if local_state.unstructured_mesh_contour_isosurface_number_indicator == 0:
            local_state.unstructured_mesh_contour_isosurface_number_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                pyvista_LR.unstructured_mesh_contour_isosurface_number = int(
                    unstructured_mesh_contour_isosurface_number
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("t_mesh_contour_isosurface_value_x")
    def t_mesh_contour_isosurface_value_x(
        t_mesh_contour_isosurface_value_x=local_state.t_mesh_contour_isosurface_value_x,
        **kwargs
    ):
        if local_state.t_mesh_contour_isosurface_value_x_indicator == 0:
            local_state.t_mesh_contour_isosurface_value_x_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                local_state.t_mesh_contour_isosurface_value_x = (
                    t_mesh_contour_isosurface_value_x
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("t_mesh_contour_isosurface_value_y")
    def t_mesh_contour_isosurface_value_y(
        t_mesh_contour_isosurface_value_y=local_state.t_mesh_contour_isosurface_value_y,
        **kwargs
    ):
        if local_state.t_mesh_contour_isosurface_value_y_indicator == 0:
            local_state.t_mesh_contour_isosurface_value_y_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                local_state.t_mesh_contour_isosurface_value_y = (
                    t_mesh_contour_isosurface_value_y
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("t_mesh_contour_isosurface_value_z")
    def t_mesh_contour_isosurface_value_z(
        t_mesh_contour_isosurface_value_z=local_state.t_mesh_contour_isosurface_value_z,
        **kwargs
    ):
        if local_state.t_mesh_contour_isosurface_value_z_indicator == 0:
            local_state.t_mesh_contour_isosurface_value_z_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                local_state.t_mesh_contour_isosurface_value_z = (
                    t_mesh_contour_isosurface_value_z
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("unstructured_mesh_contour_isosurface_value")
    def unstructured_mesh_contour_isosurface_value(
        unstructured_mesh_contour_isosurface_value=pyvista_LR.unstructured_mesh_contour_isosurface_value,
        **kwargs
    ):
        if local_state.unstructured_mesh_contour_isosurface_value_indicator == 0:
            local_state.unstructured_mesh_contour_isosurface_value_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                pyvista_LR.unstructured_mesh_contour_isosurface_value = (
                    unstructured_mesh_contour_isosurface_value
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("unstructured_mesh_contour_isosurface_value_t")
    def unstructured_mesh_contour_isosurface_value_t(
        unstructured_mesh_contour_isosurface_value_t=local_state.unstructured_mesh_contour_isosurface_value_t,
        **kwargs
    ):
        if local_state.unstructured_mesh_contour_isosurface_value_t_indicator == 0:
            local_state.unstructured_mesh_contour_isosurface_value_t_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                local_state.unstructured_mesh_contour_isosurface_value_t = (
                    unstructured_mesh_contour_isosurface_value_t
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("unstructured_mesh_contour_isosurface_value_p")
    def unstructured_mesh_contour_isosurface_value_p(
        unstructured_mesh_contour_isosurface_value_p=local_state.unstructured_mesh_contour_isosurface_value_p,
        **kwargs
    ):
        if local_state.unstructured_mesh_contour_isosurface_value_p_indicator == 0:
            local_state.unstructured_mesh_contour_isosurface_value_p_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                local_state.unstructured_mesh_contour_isosurface_value_p = (
                    unstructured_mesh_contour_isosurface_value_p
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("unstructured_mesh_rescale_norm_y")
    def unstructured_mesh_rescale_norm_y(
        unstructured_mesh_rescale_norm_y=pyvista_LR.rescale_unstructured_mesh_norm[1],
        **kwargs
    ):
        try:
            pyvista_LR.rescale_unstructured_mesh_norm = (
                pyvista_LR.rescale_unstructured_mesh_norm[0],
                float(unstructured_mesh_rescale_norm_y),
                pyvista_LR.rescale_unstructured_mesh_norm[2],
            )
        except:
            pass

    @state.change("unstructured_mesh_rescale_norm_z")
    def unstructured_mesh_rescale_norm_z(
        unstructured_mesh_rescale_norm_z=pyvista_LR.rescale_unstructured_mesh_norm[2],
        **kwargs
    ):
        try:
            pyvista_LR.rescale_unstructured_mesh_norm = (
                pyvista_LR.rescale_unstructured_mesh_norm[0],
                pyvista_LR.rescale_unstructured_mesh_norm[1],
                float(unstructured_mesh_rescale_norm_z),
            )
        except:
            pass

    @state.change("unstructured_mesh_clip_plane_free_normal_1_x")
    def unstructured_mesh_clip_plane_free_normal_1_x(
        unstructured_mesh_clip_plane_free_normal_1_x=pyvista_LR.unstructured_mesh_clip_plane_free_normal_1[
            0
        ],
        **kwargs
    ):
        try:
            pyvista_LR.unstructured_mesh_clip_plane_free_normal_1 = (
                float(unstructured_mesh_clip_plane_free_normal_1_x),
                pyvista_LR.unstructured_mesh_clip_plane_free_normal_1[1],
                pyvista_LR.unstructured_mesh_clip_plane_free_normal_1[2],
            )
        except:
            pass

    @state.change("unstructured_mesh_clip_plane_free_normal_1_y")
    def unstructured_mesh_clip_plane_free_normal_1_y(
        unstructured_mesh_clip_plane_free_normal_1_y=pyvista_LR.unstructured_mesh_clip_plane_free_normal_1[
            0
        ],
        **kwargs
    ):
        try:
            pyvista_LR.unstructured_mesh_clip_plane_free_normal_1 = (
                pyvista_LR.unstructured_mesh_clip_plane_free_normal_1[0],
                float(unstructured_mesh_clip_plane_free_normal_1_y),
                pyvista_LR.unstructured_mesh_clip_plane_free_normal_1[2],
            )
        except:
            pass

    @state.change("unstructured_mesh_clip_plane_free_normal_1_z")
    def unstructured_mesh_clip_plane_free_normal_1_z(
        unstructured_mesh_clip_plane_free_normal_1_z=pyvista_LR.unstructured_mesh_clip_plane_free_normal_1[
            0
        ],
        **kwargs
    ):
        try:
            pyvista_LR.unstructured_mesh_clip_plane_free_normal_1 = (
                pyvista_LR.unstructured_mesh_clip_plane_free_normal_1[0],
                pyvista_LR.unstructured_mesh_clip_plane_free_normal_1[1],
                float(unstructured_mesh_clip_plane_free_normal_1_z),
            )
        except:
            pass

    @state.change("unstructured_mesh_clip_plane_free_normal_2_x")
    def unstructured_mesh_clip_plane_free_normal_2_x(
        unstructured_mesh_clip_plane_free_normal_2_x=pyvista_LR.unstructured_mesh_clip_plane_free_normal_2[
            0
        ],
        **kwargs
    ):
        try:
            pyvista_LR.unstructured_mesh_clip_plane_free_normal_2 = (
                float(unstructured_mesh_clip_plane_free_normal_2[0]),
                float(pyvista_LR.unstructured_mesh_clip_plane_free_normal_2[1]),
                float(pyvista_LR.unstructured_mesh_clip_plane_free_normal_2[2]),
            )
        except:
            pass

    @state.change("unstructured_mesh_clip_plane_free_normal_2_y")
    def unstructured_mesh_clip_plane_free_normal_2_y(
        unstructured_mesh_clip_plane_free_normal_2_y=pyvista_LR.unstructured_mesh_clip_plane_free_normal_2[
            1
        ],
        **kwargs
    ):
        try:
            pyvista_LR.unstructured_mesh_clip_plane_free_normal_2 = (
                pyvista_LR.unstructured_mesh_clip_plane_free_normal_2[0],
                float(unstructured_mesh_clip_plane_free_normal_2_y),
                pyvista_LR.unstructured_mesh_clip_plane_free_normal_2[2],
            )
        except:
            pass

    @state.change("unstructured_mesh_clip_plane_free_normal_2_z")
    def unstructured_mesh_clip_plane_free_normal_2_z(
        unstructured_mesh_clip_plane_free_normal_2_z=pyvista_LR.unstructured_mesh_clip_plane_free_normal_2[
            2
        ],
        **kwargs
    ):
        try:
            pyvista_LR.unstructured_mesh_clip_plane_free_normal_2 = (
                pyvista_LR.unstructured_mesh_clip_plane_free_normal_2[0],
                pyvista_LR.unstructured_mesh_clip_plane_free_normal_2[1],
                float(unstructured_mesh_clip_plane_free_normal_2_z),
            )
        except:
            pass

    @state.change("Cut_X_tmesh")
    def Cut_X_tmesh(
        Cut_X_tmesh=[
            local_state.t_mesh_clip_scalar_max_x,
            local_state.t_mesh_clip_scalar_min_x,
        ],
        **kwargs
    ):
        if local_state.Cut_X_tmesh_indicator == 0:
            local_state.Cut_X_tmesh_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                if (
                    pyvista_LR.add_unstructured_mesh
                    and pyvista_LR.do_unstructured_mesh_clip_scalar
                ):
                    max = Cut_X_tmesh[1]
                    min = Cut_X_tmesh[0]
                    local_state.t_mesh_clip_scalar_max_x = max
                    local_state.t_mesh_clip_scalar_min_x = min
                    plot_multiple_meshes(pyvista_LR, plotter, local_state)
                    ctrl.view_update()

    @state.change("Cut_Y_tmesh")
    def Cut_Y_tmesh(
        Cut_Y_tmesh=[
            local_state.t_mesh_clip_scalar_max_y,
            local_state.t_mesh_clip_scalar_min_y,
        ],
        **kwargs
    ):
        if local_state.Cut_Y_tmesh_indicator == 0:
            local_state.Cut_Y_tmesh_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                if (
                    pyvista_LR.add_unstructured_mesh
                    and pyvista_LR.do_unstructured_mesh_clip_scalar
                ):
                    max = Cut_Y_tmesh[1]
                    min = Cut_Y_tmesh[0]
                    local_state.t_mesh_clip_scalar_max_y = max
                    local_state.t_mesh_clip_scalar_min_y = min
                    plot_multiple_meshes(pyvista_LR, plotter, local_state)
                    ctrl.view_update()

    @state.change("Cut_Z_tmesh")
    def Cut_Z_tmesh(
        Cut_Z_tmesh=[
            local_state.t_mesh_clip_scalar_max_z,
            local_state.t_mesh_clip_scalar_min_z,
        ],
        **kwargs
    ):
        if local_state.Cut_Z_tmesh_indicator == 0:
            local_state.Cut_Z_tmesh_indicator = 1
            pass
        else:
            if pyvista_LR.add_unstructured_mesh:
                if (
                    pyvista_LR.add_unstructured_mesh
                    and pyvista_LR.do_unstructured_mesh_clip_scalar
                ):
                    max = Cut_Z_tmesh[1]
                    min = Cut_Z_tmesh[0]
                    local_state.t_mesh_clip_scalar_max_z = max
                    local_state.t_mesh_clip_scalar_min_z = min
                    plot_multiple_meshes(pyvista_LR, plotter, local_state)
                    ctrl.view_update()

    @state.change("Cut_theta_tmesh")
    def Cut_theta_tmesh(
        Cut_theta_tmesh=[
            pyvista_LR.unstructured_mesh_clip_scalar_min_theta,
            pyvista_LR.unstructured_mesh_clip_scalar_max_theta,
        ],
        **kwargs
    ):
        if local_state.Cut_theta_tmesh_indicator == 0:
            local_state.Cut_theta_tmesh_indicator = 1
            pass
        else:
            if pyvista_LR.do_unstructured_mesh_clip_scalar:
                max = Cut_theta_tmesh[1]
                min = Cut_theta_tmesh[0]
                pyvista_LR.unstructured_mesh_clip_scalar_max_theta = max
                pyvista_LR.unstructured_mesh_clip_scalar_min_theta = min
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("Cut_phi_Tmesh")
    def Cut_phi_Tmesh(
        Cut_phi_Tmesh=[
            pyvista_LR.unstructured_mesh_clip_scalar_min_phi,
            pyvista_LR.unstructured_mesh_clip_scalar_max_phi,
        ],
        **kwargs
    ):
        if local_state.Cut_phi_Tmesh_indicator == 0:
            local_state.Cut_phi_Tmesh_indicator = 1
            pass
        else:
            if pyvista_LR.do_unstructured_mesh_clip_scalar:
                max = Cut_phi_Tmesh[1]
                min = Cut_phi_Tmesh[0]
                pyvista_LR.unstructured_mesh_clip_scalar_max_phi = max
                pyvista_LR.unstructured_mesh_clip_scalar_min_phi = min
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("unstructured_mesh_clip_plane_x_min")
    def unstructured_mesh_clip_plane_x_min(
        unstructured_mesh_clip_plane_x_min=pyvista_LR.unstructured_mesh_clip_plane_x_min,
        **kwargs
    ):
        if local_state.unstructured_mesh_clip_plane_x_min_indicator == 0:
            local_state.unstructured_mesh_clip_plane_x_min_indicator = 1
            pass
        else:
            if pyvista_LR.do_unstructured_mesh_clip:
                pyvista_LR.unstructured_mesh_clip_plane_x_min = (
                    unstructured_mesh_clip_plane_x_min
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("unstructured_mesh_clip_plane_x_max")
    def unstructured_mesh_clip_plane_x_max(
        unstructured_mesh_clip_plane_x_max=pyvista_LR.unstructured_mesh_clip_plane_x_max,
        **kwargs
    ):
        if local_state.unstructured_mesh_clip_plane_x_max_indicator == 0:
            local_state.unstructured_mesh_clip_plane_x_max_indicator = 1
            pass
        else:
            if pyvista_LR.do_unstructured_mesh_clip:
                pyvista_LR.unstructured_mesh_clip_plane_x_max = (
                    unstructured_mesh_clip_plane_x_max
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("unstructured_mesh_clip_plane_y_max")
    def unstructured_mesh_clip_plane_y_max(
        unstructured_mesh_clip_plane_y_max=pyvista_LR.unstructured_mesh_clip_plane_y_max,
        **kwargs
    ):
        if local_state.unstructured_mesh_clip_plane_y_max_indicator == 0:
            local_state.unstructured_mesh_clip_plane_y_max_indicator = 1
            pass
        else:
            if pyvista_LR.do_unstructured_mesh_clip:
                pyvista_LR.unstructured_mesh_clip_plane_y_max = (
                    unstructured_mesh_clip_plane_y_max
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("unstructured_mesh_clip_plane_y_min")
    def unstructured_mesh_clip_plane_y_min(
        unstructured_mesh_clip_plane_y_min=pyvista_LR.unstructured_mesh_clip_plane_y_min,
        **kwargs
    ):
        if local_state.unstructured_mesh_clip_plane_y_min_indicator == 0:
            local_state.unstructured_mesh_clip_plane_y_min_indicator = 1
            pass
        else:
            if pyvista_LR.do_unstructured_mesh_clip:
                pyvista_LR.unstructured_mesh_clip_plane_y_min = (
                    unstructured_mesh_clip_plane_y_min
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("unstructured_mesh_clip_plane_z_min")
    def unstructured_mesh_clip_plane_z_min(
        unstructured_mesh_clip_plane_z_min=pyvista_LR.unstructured_mesh_clip_plane_z_min,
        **kwargs
    ):
        if local_state.unstructured_mesh_clip_plane_z_min_indicator == 0:
            local_state.unstructured_mesh_clip_plane_z_min_indicator = 1
            pass
        else:
            if pyvista_LR.do_unstructured_mesh_clip:
                pyvista_LR.unstructured_mesh_clip_plane_z_min = (
                    unstructured_mesh_clip_plane_z_min
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("unstructured_mesh_clip_plane_z_max")
    def unstructured_mesh_clip_plane_z_max(
        unstructured_mesh_clip_plane_z_max=pyvista_LR.unstructured_mesh_clip_plane_z_max,
        **kwargs
    ):
        if local_state.unstructured_mesh_clip_plane_z_max_indicator == 0:
            local_state.unstructured_mesh_clip_plane_z_max_indicator = 1
            pass
        else:
            if pyvista_LR.do_unstructured_mesh_clip:
                pyvista_LR.unstructured_mesh_clip_plane_z_max = (
                    unstructured_mesh_clip_plane_z_max
                )
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("clip_unstructured_mesh_free_1")
    def clip_unstructured_mesh_free_1(
        clip_unstructured_mesh_free_1=pyvista_LR.clip_unstructured_mesh_free_1, **kwargs
    ):
        if local_state.clip_unstructured_mesh_free_1_indicator == 0:
            local_state.clip_unstructured_mesh_free_1_indicator = 1
            pass
        else:
            if pyvista_LR.do_clip_unstructured_mesh_free_normal:
                pyvista_LR.clip_unstructured_mesh_free_1 = clip_unstructured_mesh_free_1
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("clip_unstructured_mesh_free_2")
    def clip_unstructured_mesh_free_2(
        clip_unstructured_mesh_free_2=pyvista_LR.clip_unstructured_mesh_free_2, **kwargs
    ):
        if local_state.clip_unstructured_mesh_free_2_indicator == 0:
            local_state.clip_unstructured_mesh_free_2_indicator = 1
            pass
        else:
            if pyvista_LR.do_clip_unstructured_mesh_free_normal:
                pyvista_LR.clip_unstructured_mesh_free_2 = clip_unstructured_mesh_free_2
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    def change_tmesh_cmap_vbtn_value_0():
        local_state.Tmesh_cmap_vbtn = 0
        pyvista_LR.unstructured_mesh_color_map_index = local_state.Tmesh_cmap_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)

    def change_tmesh_cmap_vbtn_value_1():
        local_state.Tmesh_cmap_vbtn = 1
        pyvista_LR.unstructured_mesh_color_map_index = local_state.Tmesh_cmap_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)

    def change_tmesh_cmap_vbtn_value_2():
        local_state.Tmesh_cmap_vbtn = 2
        pyvista_LR.unstructured_mesh_color_map_index = local_state.Tmesh_cmap_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)

    def change_tmesh_cmap_vbtn_value_3():
        local_state.Tmesh_cmap_vbtn = 3
        pyvista_LR.unstructured_mesh_color_map_index = local_state.Tmesh_cmap_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)

    def change_tmesh_cmap_vbtn_value_4():
        local_state.Tmesh_cmap_vbtn = 4
        pyvista_LR.unstructured_mesh_color_map_index = local_state.Tmesh_cmap_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)

    def change_tmesh_opacity_index_vbtn_value_0():
        local_state.Tmesh_opaciy_vbtn = 0
        pyvista_LR.unstructured_mesh_color_map_opacity_index = (
            local_state.Tmesh_opaciy_vbtn
        )
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_tmesh_opacity_index_vbtn_value_1():
        local_state.Tmesh_opaciy_vbtn = 1
        pyvista_LR.unstructured_mesh_color_map_opacity_index = (
            local_state.Tmesh_opaciy_vbtn
        )
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_tmesh_opacity_index_vbtn_value_2():
        local_state.Tmesh_opaciy_vbtn = 2
        pyvista_LR.unstructured_mesh_color_map_opacity_index = (
            local_state.Tmesh_opaciy_vbtn
        )
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_tmesh_opacity_index_vbtn_value_3():
        local_state.Tmesh_opaciy_vbtn = 3
        pyvista_LR.unstructured_mesh_color_map_opacity_index = (
            local_state.Tmesh_opaciy_vbtn
        )
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_tmesh_opacity_index_vbtn_value_4():
        local_state.Tmesh_opaciy_vbtn = 4
        pyvista_LR.unstructured_mesh_color_map_opacity_index = (
            local_state.Tmesh_opaciy_vbtn
        )
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_tmesh_opacity_index_vbtn_value_5():
        local_state.Tmesh_opaciy_vbtn = 5
        pyvista_LR.unstructured_mesh_color_map_opacity_index = (
            local_state.Tmesh_opaciy_vbtn
        )
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_tmesh_opacity_index_vbtn_value_6():
        local_state.Tmesh_opaciy_vbtn = 6
        pyvista_LR.unstructured_mesh_color_map_opacity_index = (
            local_state.Tmesh_opaciy_vbtn
        )
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def recalculate_tmesh():
        local_state.frame_change = True  # to recalculated tmesh
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def do_t_mesh_clip():
        if pyvista_LR.add_unstructured_mesh:
            pyvista_LR.do_unstructured_mesh_clip = not (
                pyvista_LR.do_unstructured_mesh_clip
            )
            if pyvista_LR.do_unstructured_mesh_clip:
                local_state.face_clip_index_t.append("face_clip_t_0")
            else:
                if "face_clip_t_0" in local_state.face_clip_index_t:
                    local_state.face_clip_index_t.remove("face_clip_t_0")

            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    def do_clip_t_mesh_free_normal():
        if pyvista_LR.add_unstructured_mesh:
            pyvista_LR.do_clip_unstructured_mesh_free_normal = not (
                pyvista_LR.do_clip_unstructured_mesh_free_normal
            )
            if pyvista_LR.do_clip_unstructured_mesh_free_normal:
                local_state.face_clip_index_t.append("face_clip_t_1")
            else:
                if "face_clip_t_1" in local_state.face_clip_index_t:
                    local_state.face_clip_index_t.remove("face_clip_t_1")
            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    def Contour_0_tmesh():
        pyvista_LR.unstructured_mesh_contour_method_indicator = 0
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def Contour_1_tmesh():
        pyvista_LR.unstructured_mesh_contour_method_indicator = 1
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def Contour_2_tmesh():
        pyvista_LR.unstructured_mesh_contour_method_indicator = 2
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def Contour_3_tmesh():
        pyvista_LR.unstructured_mesh_contour_method_indicator = 3
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def Contour_4_tmesh():
        pyvista_LR.unstructured_mesh_contour_method_indicator = 4
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    return (
        change_tmesh_cmap_vbtn_value_0,
        change_tmesh_cmap_vbtn_value_1,
        change_tmesh_cmap_vbtn_value_2,
        change_tmesh_cmap_vbtn_value_3,
        change_tmesh_cmap_vbtn_value_4,
        change_tmesh_opacity_index_vbtn_value_0,
        change_tmesh_opacity_index_vbtn_value_1,
        change_tmesh_opacity_index_vbtn_value_2,
        change_tmesh_opacity_index_vbtn_value_3,
        change_tmesh_opacity_index_vbtn_value_4,
        change_tmesh_opacity_index_vbtn_value_5,
        change_tmesh_opacity_index_vbtn_value_6,
        recalculate_tmesh,
        do_t_mesh_clip,
        do_clip_t_mesh_free_normal,
        Contour_0_tmesh,
        Contour_1_tmesh,
        Contour_2_tmesh,
        Contour_3_tmesh,
        Contour_4_tmesh,
    )
