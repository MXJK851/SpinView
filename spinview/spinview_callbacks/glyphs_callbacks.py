def glyphs_callbacks_initialize(
    local_state, pyvista_LR, state, ctrl, plot_multiple_meshes, plotter, viewer
):
    @state.change("do_clip_component")
    def do_clip_component(do_clip_component=pyvista_LR.do_clip_component, **kwargs):
        if local_state.do_clip_component_indicator == 0:
            local_state.do_clip_component_indicator = 1
            pass
        else:
            pyvista_LR.do_clip_component = do_clip_component
            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    @state.change("point_rescale")
    def point_rescale(point_rescale=pyvista_LR.do_glyph_simple_point_rescale, **kwargs):
        if local_state.point_rescale_indicator == 0:
            local_state.point_rescale_indicator = 1
            pass
        else:
            if pyvista_LR.add_simple_point:
                pyvista_LR.do_glyph_simple_point_rescale = point_rescale
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("point_size")
    def point_size(point_size=pyvista_LR.simple_point_size, **kwargs):
        if local_state.point_size_indicator == 0:
            local_state.point_size_indicator = 1
            pass
        else:
            if pyvista_LR.add_simple_point:
                pyvista_LR.simple_point_size = point_size
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("metallic")
    def update_metallic(metallic=pyvista_LR.metallic_record, **kwargs):
        if pyvista_LR.code_init_indicator_metallic == 0:
            pyvista_LR.code_init_indicator_metallic = 1
            pass
        else:
            if pyvista_LR.add_cone:
                pyvista_LR.metallic_record = metallic
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("metallic_arrow")
    def metallic_arrow(metallic_arrow=pyvista_LR.metallic_arrow, **kwargs):
        if local_state.metallic_arrow_indicator == 0:
            local_state.metallic_arrow_indicator = 1
            pass
        else:
            if pyvista_LR.add_arrow:
                pyvista_LR.metallic_arrow = metallic_arrow
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("metallic_sphere")
    def metallic_sphere(metallic_sphere=pyvista_LR.metallic_sphere, **kwargs):
        if local_state.metallic_sphere_indicator == 0:
            local_state.metallic_sphere_indicator = 1
            pass
        else:
            if pyvista_LR.add_sphere:
                pyvista_LR.metallic_sphere = metallic_sphere
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("metallic_box")
    def metallic_box(metallic_box=pyvista_LR.metallic_box, **kwargs):
        if local_state.metallic_box_indicator == 0:
            local_state.metallic_box_indicator = 1
            pass
        else:
            if pyvista_LR.add_box:
                pyvista_LR.metallic_box = metallic_box
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("metallic_own")
    def metallic_own(metallic_own=pyvista_LR.metallic_own, **kwargs):
        if local_state.metallic_own_indicator == 0:
            local_state.metallic_own_indicator = 1
            pass
        else:
            if pyvista_LR.add_own_glyphs:
                pyvista_LR.metallic_own = metallic_own
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("metallic_plane")
    def metallic_plane(metallic_plane=pyvista_LR.metallic_plane, **kwargs):
        if local_state.metallic_plane_indicator == 0:
            local_state.metallic_plane_indicator = 1
            pass
        else:
            if pyvista_LR.add_plane:
                pyvista_LR.metallic_plane = metallic_plane
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("pbr")
    def update_bgc(pbr=pyvista_LR.pbr, **kwargs):
        if pyvista_LR.pbr_indicator == 0:
            pyvista_LR.pbr_indicator = 1
            pass
        else:
            if pyvista_LR.add_cone:
                pyvista_LR.pbr = pbr
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("pbr_arrow")
    def update_bgc(pbr_arrow=pyvista_LR.pbr_arrow, **kwargs):
        if local_state.pbr_arrow_indicator == 0:
            local_state.pbr_arrow_indicator = 1
            pass
        else:
            if pyvista_LR.add_arrow:
                pyvista_LR.pbr_arrow = pbr_arrow
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("pbr_sphere")
    def update_bgc(pbr_sphere=pyvista_LR.pbr_sphere, **kwargs):
        if local_state.pbr_sphere_indicator == 0:
            local_state.pbr_sphere_indicator = 1
            pass
        else:
            if pyvista_LR.add_sphere:
                pyvista_LR.pbr_sphere = pbr_sphere
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("pbr_plane")
    def update_bgc(pbr_plane=pyvista_LR.pbr_plane, **kwargs):
        if local_state.pbr_plane_indicator == 0:
            local_state.pbr_plane_indicator = 1
            pass
        else:
            if pyvista_LR.add_plane:
                pyvista_LR.pbr_plane = pbr_plane
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("do_interpolated_projection")
    def do_interpolated_projection(
        do_interpolated_projection=local_state.do_interpolated_projection, **kwargs
    ):
        if local_state.do_interpolated_projection_indicator == 0:
            local_state.do_interpolated_projection_indicator = 1
            pass
        else:
            if pyvista_LR.add_glyphs:
                local_state.do_interpolated_projection = do_interpolated_projection
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("pbr_box")
    def update_bgc(pbr_box=pyvista_LR.pbr_box, **kwargs):
        if local_state.pbr_box_indicator == 0:
            local_state.pbr_box_indicator = 1
            pass
        else:
            if pyvista_LR.add_box:
                pyvista_LR.pbr_box = pbr_box
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("pbr_own")
    def pbr_own(pbr_own=pyvista_LR.pbr_own, **kwargs):
        if local_state.pbr_own_indicator == 0:
            local_state.pbr_own_indicator = 1
            pass
        else:
            if pyvista_LR.add_own_glyphs:
                pyvista_LR.pbr_own = pbr_own
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("do_scale_cone")
    def do_scale_cone(do_scale_cone=pyvista_LR.do_scale_cone, **kwargs):
        if local_state.do_scale_cone_indicator == 0:
            local_state.do_scale_cone_indicator = 1
            pass
        else:
            if pyvista_LR.add_cone:
                pyvista_LR.do_scale_cone = do_scale_cone
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("do_scale_arrow")
    def do_scale_arrow(do_scale_arrow=pyvista_LR.do_scale_arrow, **kwargs):
        if local_state.do_scale_arrow_indicator == 0:
            local_state.do_scale_arrow_indicator = 1
            pass
        else:
            if pyvista_LR.add_arrow:
                pyvista_LR.do_scale_arrow = do_scale_arrow
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("do_scale_box")
    def do_scale_box(do_scale_box=pyvista_LR.do_scale_box, **kwargs):
        if local_state.do_scale_box_indicator == 0:
            local_state.do_scale_box_indicator = 1
            pass
        else:
            if pyvista_LR.add_box:
                pyvista_LR.do_scale_box = do_scale_box
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("do_scale_sphere")
    def do_scale_sphere(do_scale_sphere=pyvista_LR.do_scale_sphere, **kwargs):
        if local_state.do_scale_sphere_indicator == 0:
            local_state.do_scale_sphere_indicator = 1
            pass
        else:
            if pyvista_LR.add_sphere:
                pyvista_LR.do_scale_sphere = do_scale_sphere
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("do_scale_plane")
    def do_scale_plane(do_scale_plane=pyvista_LR.do_scale_plane, **kwargs):
        if local_state.do_scale_plane_indicator == 0:
            local_state.do_scale_plane_indicator = 1
            pass
        else:
            if pyvista_LR.add_plane:
                pyvista_LR.do_scale_plane = do_scale_plane
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("do_scale_own")
    def do_scale_own(do_scale_own=pyvista_LR.do_scale_own, **kwargs):
        if local_state.do_scale_own_indicator == 0:
            local_state.do_scale_own_indicator = 1
            pass
        else:
            if pyvista_LR.add_own_glyphs:
                pyvista_LR.do_scale_own = do_scale_own
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("opacity")
    def update_opacity(opacity=pyvista_LR.code_init_indicator_opacity, **kwargs):
        if pyvista_LR.code_init_indicator_opacity == 0:
            pyvista_LR.code_init_indicator_opacity = 1
            pass
        else:
            if pyvista_LR.add_glyphs:
                pyvista_LR.opacity_record = opacity
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("roughness_sphere")
    def roughness_sphere(roughness_sphere=pyvista_LR.roughness_sphere, **kwargs):
        if local_state.roughness_sphere_indicator == 0:
            local_state.roughness_sphere_indicator = 1
            pass
        else:
            if pyvista_LR.add_sphere:
                pyvista_LR.roughness_sphere = roughness_sphere
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("roughness_arrow")
    def roughness_sphere(roughness_arrow=pyvista_LR.roughness_arrow, **kwargs):
        if local_state.roughness_arrow_indicator == 0:
            local_state.roughness_arrow_indicator = 1
            pass
        else:
            if pyvista_LR.add_arrow:
                pyvista_LR.roughness_arrow = roughness_arrow
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("roughness_box")
    def roughness_box(roughness_box=pyvista_LR.roughness_box, **kwargs):
        if local_state.roughness_box_indicator == 0:
            local_state.roughness_box_indicator = 1
            pass
        else:
            if pyvista_LR.add_box:
                pyvista_LR.roughness_box = roughness_box
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("metallic_arrow")
    def metallic_arrow(metallic_arrow=pyvista_LR.metallic_arrow, **kwargs):
        if local_state.metallic_arrow_indicator == 0:
            local_state.metallic_arrow_indicator = 1
            pass
        else:
            if pyvista_LR.add_arrow:
                pyvista_LR.metallic_arrow = metallic_arrow
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("roughness_plane")
    def roughness_plane(roughness_plane=pyvista_LR.roughness_plane, **kwargs):
        if local_state.roughness_plane_indicator == 0:
            local_state.roughness_plane_indicator = 1
            pass
        else:
            if pyvista_LR.add_plane:
                pyvista_LR.roughness_plane = roughness_plane
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("roughness_own")
    def roughness_own(roughness_own=pyvista_LR.roughness_own, **kwargs):
        if local_state.roughness_own_indicator == 0:
            local_state.roughness_own_indicator = 1
            pass
        else:
            if pyvista_LR.add_own:
                pyvista_LR.roughness_own = roughness_own
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("resolutions")
    def update_cone_resolution(resolutions=pyvista_LR.resolutions, **kwargs):
        if pyvista_LR.code_init_indicator_resolutions == 0:
            pyvista_LR.code_init_indicator_resolutions = 1
            pass
        else:
            if pyvista_LR.add_cone:
                pyvista_LR.resolutions = int(resolutions)
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("Ratio")
    def update_Ratio(Ratio=pyvista_LR.Ratio_record, **kwargs):
        if pyvista_LR.code_init_indicator_Ratio == 0:
            pyvista_LR.code_init_indicator_Ratio = 1
            pass
        else:
            if pyvista_LR.add_cone:
                pyvista_LR.Ratio_record = Ratio
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("Ratio_record_arrow")
    def Ratio_record_arrow(Ratio_record_arrow=pyvista_LR.Ratio_record_arrow, **kwargs):
        if local_state.Ratio_record_arrow_indicator == 0:
            local_state.Ratio_record_arrow_indicator = 1
            pass
        else:
            if pyvista_LR.add_arrow:
                pyvista_LR.Ratio_record_arrow = Ratio_record_arrow
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("tip_length_arrow")
    def tip_length_arrow(tip_length_arrow=pyvista_LR.tip_length_arrow, **kwargs):
        if local_state.tip_length_arrow_indicator == 0:
            local_state.tip_length_arrow_indicator = 1
            pass
        else:
            if pyvista_LR.add_arrow:
                pyvista_LR.tip_length_arrow = tip_length_arrow
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("tip_radius_arrow")
    def tip_radius_arrow(tip_radius_arrow=pyvista_LR.tip_radius_arrow, **kwargs):
        if local_state.tip_radius_arrow_indicator == 0:
            local_state.tip_radius_arrow_indicator = 1
            pass
        else:
            if pyvista_LR.add_arrow:
                pyvista_LR.tip_radius_arrow = tip_radius_arrow
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("tip_resolution_arrow")
    def tip_resolution_arrow(
        tip_resolution_arrow=pyvista_LR.tip_resolution_arrow, **kwargs
    ):
        if local_state.tip_resolution_arrow_indicator == 0:
            local_state.tip_resolution_arrow_indicator = 1
            pass
        else:
            if pyvista_LR.add_arrow:
                pyvista_LR.tip_resolution_arrow = tip_resolution_arrow
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("shaft_radius_arrow")
    def shaft_radius_arrow(shaft_radius_arrow=pyvista_LR.shaft_radius_arrow, **kwargs):
        if local_state.shaft_radius_arrow_indicator == 0:
            local_state.shaft_radius_arrow_indicator = 1
            pass
        else:
            if pyvista_LR.add_arrow:
                pyvista_LR.shaft_radius_arrow = shaft_radius_arrow
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("shaft_resolution_arrow")
    def shaft_resolution_arrow(
        shaft_resolution_arrow=pyvista_LR.shaft_resolution_arrow, **kwargs
    ):
        if local_state.shaft_resolution_arrow_indicator == 0:
            local_state.shaft_resolution_arrow_indicator = 1
            pass
        else:
            if pyvista_LR.add_arrow:
                pyvista_LR.shaft_resolution_arrow = shaft_resolution_arrow
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("Ratio_record_box")
    def Ratio_record_box(Ratio_record_box=pyvista_LR.Ratio_record_box, **kwargs):
        if local_state.Ratio_record_box_indicator == 0:
            local_state.Ratio_record_box_indicator = 1
            pass
        else:
            if pyvista_LR.add_box:
                pyvista_LR.Ratio_record_box = Ratio_record_box
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("Ratio_record_sphere")
    def Ratio_record_sphere(
        Ratio_record_sphere=pyvista_LR.Ratio_record_sphere, **kwargs
    ):
        if local_state.Ratio_record_sphere_indicator == 0:
            local_state.Ratio_record_sphere_indicator = 1
            pass
        else:
            if pyvista_LR.add_sphere:
                pyvista_LR.Ratio_record_sphere = Ratio_record_sphere
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("radius_sphere")
    def radius_sphere(radius_sphere=pyvista_LR.radius_sphere, **kwargs):
        if local_state.radius_sphere_indicator == 0:
            local_state.radius_sphere_indicator = 1
            pass
        else:
            if pyvista_LR.add_sphere:
                pyvista_LR.radius_sphere = radius_sphere
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("theta_resolution_sphere")
    def theta_resolution_sphere(
        theta_resolution_sphere=pyvista_LR.theta_resolution_sphere, **kwargs
    ):
        if local_state.theta_resolution_sphere_indicator == 0:
            local_state.theta_resolution_sphere_indicator = 1
            pass
        else:
            if pyvista_LR.add_sphere:
                pyvista_LR.theta_resolution_sphere = theta_resolution_sphere
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("phi_resolution_sphere")
    def phi_resolution_sphere(
        phi_resolution_sphere=pyvista_LR.phi_resolution_sphere, **kwargs
    ):
        if local_state.phi_resolution_sphere_indicator == 0:
            local_state.phi_resolution_sphere_indicator = 1
            pass
        else:
            if pyvista_LR.add_sphere:
                pyvista_LR.phi_resolution_sphere = phi_resolution_sphere
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("Ratio_record_plane")
    def Ratio_record_plane(Ratio_record_plane=pyvista_LR.Ratio_record_plane, **kwargs):
        if local_state.Ratio_record_plane_indicator == 0:
            local_state.Ratio_record_plane_indicator = 1
            pass
        else:
            if pyvista_LR.add_plane:
                pyvista_LR.Ratio_record_plane = Ratio_record_plane
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("Ratio_record_own")
    def Ratio_record_own(Ratio_record_own=pyvista_LR.Ratio_record_own, **kwargs):
        if local_state.Ratio_record_own_indicator == 0:
            local_state.Ratio_record_own_indicator = 1
            pass
        else:
            if pyvista_LR.add_own_glyphs:
                pyvista_LR.Ratio_record_own = Ratio_record_own
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("cone_highth")
    def update_cone_highth(cone_highth=pyvista_LR.cone_highth_record, **kwargs):
        if pyvista_LR.code_init_indicator_cone_highth == 0:
            pyvista_LR.code_init_indicator_cone_highth = 1
            pass
        else:
            if pyvista_LR.add_cone:
                pyvista_LR.cone_highth_record = cone_highth
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("cone_Radius")
    def update_cone_Radius(cone_Radius=pyvista_LR.cone_Radius_record, **kwargs):
        if pyvista_LR.code_init_indicator_cone_Radius == 0:
            pyvista_LR.code_init_indicator_cone_Radius = 1
            pass
        else:
            if pyvista_LR.add_cone:
                pyvista_LR.cone_Radius_record = cone_Radius
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("point_rescale_norm_x")
    def point_rescale_norm_x(
        point_rescale_norm_x=pyvista_LR.rescale_simple_point_norm[0], **kwargs
    ):
        try:
            pyvista_LR.rescale_simple_point_norm = (
                float(point_rescale_norm_x),
                pyvista_LR.rescale_simple_point_norm[1],
                pyvista_LR.rescale_simple_point_norm[2],
            )
        except:
            pass

    @state.change("point_rescale_norm_y")
    def point_rescale_norm_y(
        point_rescale_norm_y=pyvista_LR.rescale_simple_point_norm[1], **kwargs
    ):
        try:
            pyvista_LR.rescale_simple_point_norm = (
                pyvista_LR.rescale_simple_point_norm[0],
                float(point_rescale_norm_y),
                pyvista_LR.rescale_simple_point_norm[2],
            )
        except:
            pass

    @state.change("point_rescale_norm_z")
    def point_rescale_norm_z(
        point_rescale_norm_z=pyvista_LR.rescale_simple_point_norm[2], **kwargs
    ):
        try:
            pyvista_LR.rescale_simple_point_norm = (
                pyvista_LR.rescale_simple_point_norm[0],
                pyvista_LR.rescale_simple_point_norm[1],
                float(point_rescale_norm_z),
            )
        except:
            pass

    # cone center shift
    @state.change("cone_center_x")
    def cone_center_x(cone_center_x=pyvista_LR.Cone_center[0], **kwargs):
        try:
            pyvista_LR.Cone_center = (
                float(cone_center_x),
                pyvista_LR.Cone_center[1],
                pyvista_LR.Cone_center[2],
            )
        except:
            pass

    @state.change("cone_center_y")
    def cone_center_y(cone_center_y=pyvista_LR.Cone_center[1], **kwargs):
        try:
            pyvista_LR.Cone_center = (
                pyvista_LR.Cone_center[0],
                float(cone_center_y),
                pyvista_LR.Cone_center[2],
            )
        except:
            pass

    @state.change("cone_center_z")
    def cone_center_z(cone_center_z=pyvista_LR.Cone_center[2], **kwargs):
        try:
            pyvista_LR.Cone_center = (
                pyvista_LR.Cone_center[0],
                pyvista_LR.Cone_center[1],
                float(cone_center_z),
            )
        except:
            pass

    # arrow start shift
    @state.change("arrow_start_x")
    def arrow_start_x(arrow_start_x=pyvista_LR.start_arrow[0], **kwargs):
        try:
            pyvista_LR.start_arrow = (
                float(arrow_start_x),
                pyvista_LR.start_arrow[1],
                pyvista_LR.start_arrow[2],
            )
        except:
            pass

    @state.change("arrow_start_y")
    def arrow_start_y(arrow_start_y=pyvista_LR.start_arrow[1], **kwargs):
        try:
            pyvista_LR.start_arrow = (
                pyvista_LR.start_arrow[0],
                float(arrow_start_y),
                pyvista_LR.start_arrow[2],
            )
        except:
            pass

    @state.change("arrow_start_z")
    def arrow_start_z(arrow_start_z=pyvista_LR.start_arrow[2], **kwargs):
        try:
            pyvista_LR.start_arrow = (
                pyvista_LR.start_arrow[0],
                pyvista_LR.start_arrow[1],
                float(arrow_start_z),
            )
        except:
            pass

    @state.change("dataset_clip_plane_free_normal_1_x")
    def dataset_clip_plane_free_normal_1_x(
        dataset_clip_plane_free_normal_1_x=pyvista_LR.dataset_clip_plane_free_normal_1[
            0
        ],
        **kwargs
    ):
        try:
            pyvista_LR.dataset_clip_plane_free_normal_1 = (
                float(dataset_clip_plane_free_normal_1_x),
                pyvista_LR.dataset_clip_plane_free_normal_1[1],
                pyvista_LR.dataset_clip_plane_free_normal_1[2],
            )
        except:
            pass

    @state.change("dataset_clip_plane_free_normal_1_y")
    def dataset_clip_plane_free_normal_1_y(
        dataset_clip_plane_free_normal_1_y=pyvista_LR.dataset_clip_plane_free_normal_1[
            0
        ],
        **kwargs
    ):
        try:
            pyvista_LR.dataset_clip_plane_free_normal_1 = (
                pyvista_LR.dataset_clip_plane_free_normal_1[0],
                float(dataset_clip_plane_free_normal_1_y),
                pyvista_LR.dataset_clip_plane_free_normal_1[2],
            )
        except:
            pass

    @state.change("dataset_clip_plane_free_normal_1_z")
    def dataset_clip_plane_free_normal_1_z(
        dataset_clip_plane_free_normal_1_z=pyvista_LR.dataset_clip_plane_free_normal_1[
            0
        ],
        **kwargs
    ):
        try:
            pyvista_LR.dataset_clip_plane_free_normal_1 = (
                pyvista_LR.dataset_clip_plane_free_normal_1[0],
                pyvista_LR.dataset_clip_plane_free_normal_1[1],
                float(dataset_clip_plane_free_normal_1_z),
            )
        except:
            pass

    @state.change("dataset_clip_plane_free_normal_2_x")
    def dataset_clip_plane_free_normal_2_x(
        dataset_clip_plane_free_normal_2_x=pyvista_LR.dataset_clip_plane_free_normal_2[
            0
        ],
        **kwargs
    ):
        try:
            pyvista_LR.dataset_clip_plane_free_normal_2 = (
                float(dataset_clip_plane_free_normal_2_x),
                pyvista_LR.dataset_clip_plane_free_normal_2[1],
                pyvista_LR.dataset_clip_plane_free_normal_2[2],
            )
        except:
            pass

    @state.change("dataset_clip_plane_free_normal_2_y")
    def dataset_clip_plane_free_normal_2_y(
        dataset_clip_plane_free_normal_2_y=pyvista_LR.dataset_clip_plane_free_normal_2[
            0
        ],
        **kwargs
    ):
        try:
            pyvista_LR.dataset_clip_plane_free_normal_2 = (
                pyvista_LR.dataset_clip_plane_free_normal_2[0],
                float(dataset_clip_plane_free_normal_2_y),
                pyvista_LR.dataset_clip_plane_free_normal_2[2],
            )
        except:
            pass

    @state.change("dataset_clip_plane_free_normal_2_z")
    def dataset_clip_plane_free_normal_2_z(
        dataset_clip_plane_free_normal_2_z=pyvista_LR.dataset_clip_plane_free_normal_2[
            0
        ],
        **kwargs
    ):
        try:
            pyvista_LR.dataset_clip_plane_free_normal_2 = (
                pyvista_LR.dataset_clip_plane_free_normal_2[0],
                pyvista_LR.dataset_clip_plane_free_normal_2[1],
                float(dataset_clip_plane_free_normal_2_z),
            )
        except:
            pass

    @state.change("Cut_X")
    def Cut_X(
        Cut_X=[pyvista_LR.x_compoment_filter_min, pyvista_LR.x_compoment_filter_max],
        **kwargs
    ):
        if pyvista_LR.code_init_indicator_Cut_X == 0:
            pyvista_LR.code_init_indicator_Cut_X = 1
            pass
        else:
            if pyvista_LR.add_glyphs and pyvista_LR.do_clip_component:
                max = Cut_X[1]
                min = Cut_X[0]
                pyvista_LR.x_compoment_filter_max = max
                pyvista_LR.x_compoment_filter_min = min
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("Cut_Y")
    def Cut_Y(
        Cut_Y=[pyvista_LR.y_compoment_filter_min, pyvista_LR.y_compoment_filter_max],
        **kwargs
    ):
        if pyvista_LR.code_init_indicator_Cut_Y == 0:
            pyvista_LR.code_init_indicator_Cut_Y = 1
            pass
        else:
            if pyvista_LR.add_glyphs and pyvista_LR.do_clip_component:
                max = Cut_Y[1]
                min = Cut_Y[0]
                pyvista_LR.y_compoment_filter_max = max
                pyvista_LR.y_compoment_filter_min = min
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("Cut_Z")
    def Cut_Z(
        Cut_Z=[pyvista_LR.z_compoment_filter_min, pyvista_LR.z_compoment_filter_max],
        **kwargs
    ):
        if pyvista_LR.code_init_indicator_Cut_Z == 0:
            pyvista_LR.code_init_indicator_Cut_Z = 1
            pass
        else:
            if pyvista_LR.add_glyphs and pyvista_LR.do_clip_component:
                max = Cut_Z[1]
                min = Cut_Z[0]
                pyvista_LR.z_compoment_filter_max = max
                pyvista_LR.z_compoment_filter_min = min
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("Cut_phi_glyph")
    def Cut_phi_glyph(
        Cut_phi_glyph=[
            pyvista_LR.phi_compoment_filter_min,
            pyvista_LR.phi_compoment_filter_max,
        ],
        **kwargs
    ):
        if local_state.cut_phi_indicator == 0:
            local_state.cut_phi_indicator = 1
            pass
        else:
            if pyvista_LR.add_glyphs and pyvista_LR.do_clip_component:
                max = Cut_phi_glyph[1]
                min = Cut_phi_glyph[0]
                pyvista_LR.phi_compoment_filter_max = max
                pyvista_LR.phi_compoment_filter_min = min
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("Cut_theta_glyph")
    def Cut_theta_glyph(
        Cut_theta_glyph=[
            pyvista_LR.theta_compoment_filter_min,
            pyvista_LR.theta_compoment_filter_max,
        ],
        **kwargs
    ):
        if local_state.cut_theta_indicator == 0:
            local_state.cut_theta_indicator = 1
            pass
        else:
            if pyvista_LR.add_glyphs and pyvista_LR.do_clip_component:
                max = Cut_theta_glyph[1]
                min = Cut_theta_glyph[0]
                pyvista_LR.theta_compoment_filter_max = max
                pyvista_LR.theta_compoment_filter_min = min
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("clip_plane_x_min")
    def clip_plane_x_min(clip_plane_x_min=pyvista_LR.clip_plane_x_min, **kwargs):
        if local_state.clip_plane_x_min_indicator == 0:
            local_state.clip_plane_x_min_indicator = 1
            pass
        else:
            if pyvista_LR.do_clip_plane_fix_origin_and_normal:
                pyvista_LR.clip_plane_x_min = clip_plane_x_min
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("clip_plane_x_max")
    def clip_plane_x_max(clip_plane_x_max=pyvista_LR.clip_plane_x_max, **kwargs):
        if local_state.clip_plane_x_max_indicator == 0:
            local_state.clip_plane_x_max_indicator = 1
            pass
        else:
            if pyvista_LR.do_clip_plane_fix_origin_and_normal:
                pyvista_LR.clip_plane_x_max = clip_plane_x_max
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("clip_plane_y_min")
    def clip_plane_y_min(clip_plane_y_min=pyvista_LR.clip_plane_y_min, **kwargs):
        if local_state.clip_plane_y_min_indicator == 0:
            local_state.clip_plane_y_min_indicator = 1
            pass
        else:
            if pyvista_LR.do_clip_plane_fix_origin_and_normal:
                pyvista_LR.clip_plane_y_min = clip_plane_y_min
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("clip_plane_y_max")
    def clip_plane_y_max(clip_plane_y_max=pyvista_LR.clip_plane_y_max, **kwargs):
        if local_state.clip_plane_y_max_indicator == 0:
            local_state.clip_plane_y_max_indicator = 1
            pass
        else:
            if pyvista_LR.do_clip_plane_fix_origin_and_normal:
                pyvista_LR.clip_plane_y_max = clip_plane_y_max
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("clip_plane_z_min")
    def clip_plane_z_min(clip_plane_z_min=pyvista_LR.clip_plane_z_min, **kwargs):
        if local_state.clip_plane_z_min_indicator == 0:
            local_state.clip_plane_z_min_indicator = 1
            pass
        else:
            if pyvista_LR.do_clip_plane_fix_origin_and_normal:
                pyvista_LR.clip_plane_z_min = clip_plane_z_min
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("clip_plane_z_max")
    def clip_plane_z_max(clip_plane_z_max=pyvista_LR.clip_plane_z_max, **kwargs):
        if local_state.clip_plane_z_max_indicator == 0:
            local_state.clip_plane_z_max_indicator = 1
            pass
        else:
            if pyvista_LR.do_clip_plane_fix_origin_and_normal:
                pyvista_LR.clip_plane_z_max = clip_plane_z_max
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("clip_plane_free_min")
    def clip_plane_free_min(clip_plane_free_min=pyvista_LR.clip_plane_free_1, **kwargs):
        if local_state.clip_plane_free_min_indicator == 0:
            local_state.clip_plane_free_min_indicator = 1
            pass
        else:
            if pyvista_LR.do_clip_plane_free_normal:
                pyvista_LR.clip_plane_free_1 = clip_plane_free_min
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("clip_plane_free_max")
    def clip_plane_free_max(clip_plane_free_max=pyvista_LR.clip_plane_free_2, **kwargs):
        if local_state.clip_plane_free_max_indicator == 0:
            local_state.clip_plane_free_max_indicator = 1
            pass
        else:
            if pyvista_LR.do_clip_plane_free_normal:
                pyvista_LR.clip_plane_free_2 = clip_plane_free_max
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    def change_glyph_cmap_vbtn_value_0():
        local_state.glyph_cmap_vbtn = 0
        pyvista_LR.color_map_index = local_state.glyph_cmap_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_glyph_cmap_vbtn_value_1():
        local_state.glyph_cmap_vbtn = 1
        pyvista_LR.color_map_index = local_state.glyph_cmap_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_glyph_cmap_vbtn_value_2():
        local_state.glyph_cmap_vbtn = 2
        pyvista_LR.color_map_index = local_state.glyph_cmap_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_glyph_cmap_vbtn_value_3():
        local_state.glyph_cmap_vbtn = 3
        pyvista_LR.color_map_index = local_state.glyph_cmap_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_glyph_cmap_vbtn_value_4():
        local_state.glyph_cmap_vbtn = 4
        pyvista_LR.color_map_index = local_state.glyph_cmap_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_glyph_opacity_index_vbtn_value_0():
        local_state.glyph_opaciy_vbtn = 0
        pyvista_LR.opacity_index = local_state.glyph_opaciy_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_glyph_opacity_index_vbtn_value_1():
        local_state.glyph_opaciy_vbtn = 1
        pyvista_LR.opacity_index = local_state.glyph_opaciy_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_glyph_opacity_index_vbtn_value_2():
        local_state.glyph_opaciy_vbtn = 2
        pyvista_LR.opacity_index = local_state.glyph_opaciy_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_glyph_opacity_index_vbtn_value_3():
        local_state.glyph_opaciy_vbtn = 3
        pyvista_LR.opacity_index = local_state.glyph_opaciy_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_glyph_opacity_index_vbtn_value_4():
        local_state.glyph_opaciy_vbtn = 4
        pyvista_LR.opacity_index = local_state.glyph_opaciy_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_glyph_opacity_index_vbtn_value_5():
        local_state.glyph_opaciy_vbtn = 5
        pyvista_LR.opacity_index = local_state.glyph_opaciy_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_glyph_opacity_index_vbtn_value_6():
        local_state.glyph_opaciy_vbtn = 6
        pyvista_LR.opacity_index = local_state.glyph_opaciy_vbtn
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_point_rescale_vbtn_value_0():
        if pyvista_LR.do_glyph_simple_point_rescale:
            pyvista_LR.rescale_simple_point_index = 0
            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()
            viewer.update()
            viewer.push_camera()

    def change_point_rescale_vbtn_value_1():
        if pyvista_LR.do_glyph_simple_point_rescale:
            pyvista_LR.rescale_simple_point_index = 1
            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    def change_point_rescale_vbtn_value_2():
        if pyvista_LR.do_glyph_simple_point_rescale:
            pyvista_LR.rescale_simple_point_index = 2
            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()
            viewer.update()
            viewer.push_camera()

    def change_point_rescale_vbtn_value_3():
        if pyvista_LR.do_glyph_simple_point_rescale:
            pyvista_LR.rescale_simple_point_index = 3
            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()
            viewer.update()
            viewer.push_camera()

    @state.change("point_rescale_factor")
    def point_rescale_factor(
        point_rescale_factor=pyvista_LR.rescale_simple_point_factor, **kwargs
    ):
        if local_state.point_rescale_factor_indicator == 0:
            local_state.point_rescale_factor_indicator = 1
            pass
        else:
            if pyvista_LR.do_glyph_simple_point_rescale:
                pyvista_LR.rescale_simple_point_factor = point_rescale_factor
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    def change_point_rescale_vbtn_value_4():
        if pyvista_LR.do_glyph_simple_point_rescale:
            pyvista_LR.rescale_simple_point_index = 4
            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()
            viewer.update()
            viewer.push_camera()

    def applied_point_rescale_norm():
        # this is universe function, the name of the function should be refacored
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def do_clip_plane_fix_origin_and_normal():
        if pyvista_LR.add_glyphs:
            pyvista_LR.do_clip_plane_fix_origin_and_normal = not (
                pyvista_LR.do_clip_plane_fix_origin_and_normal
            )
            if pyvista_LR.do_clip_plane_fix_origin_and_normal:
                local_state.face_clip_index.append("face_clip_0")
            else:
                if "face_clip_0" in local_state.face_clip_index:
                    local_state.face_clip_index.remove("face_clip_0")

            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    def do_clip_plane_free_normal():
        if pyvista_LR.add_glyphs:
            pyvista_LR.do_clip_plane_free_normal = not (
                pyvista_LR.do_clip_plane_free_normal
            )
            if pyvista_LR.do_clip_plane_free_normal:
                local_state.face_clip_index.append("face_clip_1")
            else:
                if "face_clip_1" in local_state.face_clip_index:
                    local_state.face_clip_index.remove("face_clip_1")
            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    return (
        change_glyph_cmap_vbtn_value_0,
        change_glyph_cmap_vbtn_value_1,
        change_glyph_cmap_vbtn_value_2,
        change_glyph_cmap_vbtn_value_3,
        change_glyph_cmap_vbtn_value_4,
        change_glyph_opacity_index_vbtn_value_0,
        change_glyph_opacity_index_vbtn_value_1,
        change_glyph_opacity_index_vbtn_value_2,
        change_glyph_opacity_index_vbtn_value_3,
        change_glyph_opacity_index_vbtn_value_4,
        change_glyph_opacity_index_vbtn_value_5,
        change_glyph_opacity_index_vbtn_value_6,
        change_point_rescale_vbtn_value_0,
        change_point_rescale_vbtn_value_1,
        change_point_rescale_vbtn_value_2,
        change_point_rescale_vbtn_value_3,
        change_point_rescale_vbtn_value_4,
        applied_point_rescale_norm,
        do_clip_plane_fix_origin_and_normal,
        do_clip_plane_free_normal,
    )
