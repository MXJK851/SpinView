import pyvista as pv
import numpy as np


def utilities_callbacks_initialize(
    local_state,
    pyvista_LR,
    state,
    ctrl,
    plot_multiple_meshes,
    plotter,
    db_path,
    parse_moment_and_coord_file,
    parse_moment_and_coord_file1,
    parse_moment_and_coord_file2,
    parse_moment_and_coord_file3,
    viewer,
):
    # ___________________________
    # Choose scalar bar
    # ___________________________
    @state.change("choose_scalar_bar")
    def choose_scalar_bar(choose_scalar_bar="None", **kwargs):
        if local_state.scalar_bar_indicator == 0:
            local_state.scalar_bar_indicator = 1
            pass
        else:
            if choose_scalar_bar == "Deactivate":
                pyvista_LR.show_unstructured_mesh_scalar_bar = False
                pyvista_LR.show_scalar_bar = False
                pyvista_LR.show_rectangle_mesh_scalar_bar = False
                try:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_00")
                except:
                    pass
                try:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_01")
                except:
                    pass
                try:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_10")
                except:
                    pass
                try:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_02")
                except:
                    pass
                try:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_11")
                except:
                    pass

                try:
                    plotter.remove_scalar_bar(
                        local_state.rectangle_mesh_scalar_bar_name + "_00"
                    )
                except:
                    pass
                try:
                    plotter.remove_scalar_bar(
                        local_state.rectangle_mesh_scalar_bar_name + "_01"
                    )
                except:
                    pass
                try:
                    plotter.remove_scalar_bar(
                        local_state.rectangle_mesh_scalar_bar_name + "_10"
                    )
                except:
                    pass
                try:
                    plotter.remove_scalar_bar(
                        local_state.rectangle_mesh_scalar_bar_name + "_02"
                    )
                except:
                    pass
                try:
                    plotter.remove_scalar_bar(
                        local_state.rectangle_mesh_scalar_bar_name + "_11"
                    )
                except:
                    pass

                try:
                    plotter.remove_scalar_bar(
                        local_state.unstructured_mesh_scalar_bar_name + "_00"
                    )
                except:
                    pass
                try:
                    plotter.remove_scalar_bar(
                        local_state.unstructured_mesh_scalar_bar_name + "_01"
                    )
                except:
                    pass
                try:
                    plotter.remove_scalar_bar(
                        local_state.unstructured_mesh_scalar_bar_name + "_10"
                    )
                except:
                    pass
                try:
                    plotter.remove_scalar_bar(
                        local_state.unstructured_mesh_scalar_bar_name + "_02"
                    )
                except:
                    pass
                try:
                    plotter.remove_scalar_bar(
                        local_state.unstructured_mesh_scalar_bar_name + "_11"
                    )
                except:
                    pass

            elif choose_scalar_bar == "Activate":
                pyvista_LR.show_unstructured_mesh_scalar_bar = True
                pyvista_LR.show_scalar_bar = True
                pyvista_LR.show_rectangle_mesh_scalar_bar = True
            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    @state.change("bgc")
    def update_bgc(bgc=pyvista_LR.bgc, **kwargs):
        if pyvista_LR.bgc_indicator == 0:
            pyvista_LR.bgc_indicator = 1
            pass
        else:
            pyvista_LR.bgc = bgc
            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    @state.change("replace_table")
    def replace_table(replace_table=None, **kwargs):
        local_state.new_profile_name = str(replace_table)
        ctrl.view_update()

    @state.change("downloadscreenshot")
    def update_bgc(
        downloadscreenshot=local_state.download_screenshot_resolution, **kwargs
    ):
        if local_state.download_screenshot_indicator == 0:
            local_state.download_screenshot_indicator = 1
            pass
        else:
            local_state.download_screenshot_resolution = downloadscreenshot

    @state.change("downloadmovie")
    def downloadmovie(downloadmovie=local_state.moive_size_x, **kwargs):
        local_state.moive_size_x = downloadmovie
        local_state.moive_size_y = downloadmovie

    @state.change("moivefps")
    def moivefps(moivefps=local_state.moive_fps, **kwargs):
        local_state.moive_fps = moivefps

    @state.change("mom_name")
    def mom_name(mom_name=local_state.file_select_1, **kwargs):
        pyvista_LR.mom_name = mom_name
        if local_state.change_mom1 == 0:
            local_state.change_mom1 = 1
            pass
        else:
            try:
                # print(pyvista_LR.mom_name)
                (
                    local_state.coord,
                    local_state.mom_states_x,
                    local_state.mom_states_y,
                    local_state.mom_states_z,
                    local_state.moment_magintude_all,
                ) = parse_moment_and_coord_file(
                    pyvista_LR, working_dir=state.selected_dir
                )

                local_state.mom_states_x_one_frame = local_state.mom_states_x[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]  # we only need one frame.

                local_state.mom_states_y_one_frame = local_state.mom_states_y[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]

                local_state.mom_states_z_one_frame = local_state.mom_states_z[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]

                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                print("moment file 1 {}  loaded".format(pyvista_LR.mom_name))
            except:
                print("moment file 1 is not loaded")
                print("moment file 1 may need check")
        ctrl.view_update()

    @state.change("mom_name1")
    def mom_name1(mom_name1=local_state.file_select_2, **kwargs):
        pyvista_LR.mom_name1 = mom_name1
        if local_state.change_mom2 == 0:
            local_state.change_mom2 = 1
            pass
        else:
            try:
                pyvista_LR.mom_name1 = mom_name1
                (
                    local_state.coord,
                    local_state.mom_states_x1,
                    local_state.mom_states_y1,
                    local_state.mom_states_z1,
                    local_state.moment_magintude_all,
                ) = parse_moment_and_coord_file1(
                    pyvista_LR, working_dir=state.selected_dir
                )

                local_state.mom_states_x_one_frame1 = local_state.mom_states_x1[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]  # we only need one frame.

                local_state.mom_states_y_one_frame1 = local_state.mom_states_y1[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]

                local_state.mom_states_z_one_frame1 = local_state.mom_states_z1[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                print("moment file 2 {}  loaded".format(pyvista_LR.mom_name1))
            except:
                print("moment file 2 is not loaded")
                print("moment file 2 may need check")
        ctrl.view_update()

    @state.change("mom_name2")
    def mom_name2(mom_name2=local_state.file_select_3, **kwargs):
        pyvista_LR.mom_name2 = mom_name2
        if local_state.change_mom3 == 0:
            local_state.change_mom3 = 1
            pass
        else:
            try:
                (
                    local_state.coord,
                    local_state.mom_states_x2,
                    local_state.mom_states_y2,
                    local_state.mom_states_z2,
                    local_state.moment_magintude_all,
                ) = parse_moment_and_coord_file2(
                    pyvista_LR, working_dir=state.selected_dir
                )

                local_state.mom_states_x_one_frame2 = local_state.mom_states_x2[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]  # we only need one frame.

                local_state.mom_states_y_one_frame2 = local_state.mom_states_y2[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]

                local_state.mom_states_z_one_frame2 = local_state.mom_states_z2[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                print("moment file 3 {}  loaded".format(pyvista_LR.mom_name2))
            except:
                print("moment file 3 is not loaded")
                print("moment file 3 may need check")

        ctrl.view_update()

    @state.change("mom_name3")
    def mom_name3(mom_name3=local_state.file_select_4, **kwargs):
        pyvista_LR.mom_name3 = mom_name3
        if local_state.change_mom4 == 0:
            local_state.change_mom4 = 1
            pass
        else:
            try:
                (
                    local_state.coord,
                    local_state.mom_states_x3,
                    local_state.mom_states_y3,
                    local_state.mom_states_z3,
                    local_state.moment_magintude_all,
                ) = parse_moment_and_coord_file3(
                    pyvista_LR, working_dir=state.selected_dir
                )

                local_state.mom_states_x_one_frame3 = local_state.mom_states_x3[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]  # we only need one frame.

                local_state.mom_states_y_one_frame3 = local_state.mom_states_y3[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]

                local_state.mom_states_z_one_frame3 = local_state.mom_states_z3[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                print("moment file 4 {}  loaded".format(pyvista_LR.mom_name3))
            except:
                print("moment file 4 is not loaded")
                print("moment file 4 may need check")

        ctrl.view_update()

    @state.change("coord_name")
    def update_coord_name(coord_name=pyvista_LR.coord_name, **kwargs):
        if pyvista_LR.coord_file_indicator == 0:
            pyvista_LR.coord_file_indicator = 1
            pass
        else:
            try:
                pyvista_LR.coord_name = coord_name
                (
                    local_state.coord,
                    local_state.mom_states_x,
                    local_state.mom_states_y,
                    local_state.mom_states_z,
                    local_state.moment_magintude_all,
                ) = parse_moment_and_coord_file(
                    pyvista_LR, working_dir=state.selected_dir
                )
                local_state.mom_states_x_one_frame = local_state.mom_states_x[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]  # we only need one frame.
                local_state.mom_states_y_one_frame = local_state.mom_states_y[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]
                local_state.mom_states_z_one_frame = local_state.mom_states_z[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]
                local_state.moment_magintude = local_state.moment_magintude_all[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]
                local_state.frame_change = True
                local_state.max_frame = (
                    int(len(local_state.mom_states_x) / len(local_state.coord)) - 1
                )

                # plotter_add_mesh(pyvista_LR,local_state.coord,local_state.mom_states_x_one_frame,local_state.mom_states_y_one_frame,local_state.mom_states_z_one_frame,plotter)
            except:
                print("not a valid UppASD coord file")

        ctrl.view_update()

    @state.change("ovf_name")
    def update_ovf_name(ovf_name=pyvista_LR.ovf_name, **kwargs):
        if pyvista_LR.ovf_file_indicator == 0:
            pyvista_LR.ovf_file_indicator = 1
            pass
        else:
            pyvista_LR.ovf_name = ovf_name
            (
                local_state.coord,
                local_state.mom_states_x,
                local_state.mom_states_y,
                local_state.mom_states_z,
                local_state.moment_magintude,
            ) = parse_moment_and_coord_file(pyvista_LR, working_dir=state.selected_dir)
            local_state.mom_states_x_one_frame = local_state.mom_states_x[
                ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                    (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                )
            ]  # we only need one frame.
            local_state.mom_states_y_one_frame = local_state.mom_states_y[
                ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                    (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                )
            ]
            local_state.mom_states_z_one_frame = local_state.mom_states_z[
                ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                    (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                )
            ]
            local_state.max_frame = (
                int(len(local_state.mom_states_x) / len(local_state.coord)) - 1
            )

            plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    @state.change("antialiasing")
    def update_antialiasing(antialiasing=pyvista_LR.antialiasing, **kwargs):
        if local_state.antialiasing_indicator == 0:
            local_state.antialiasing_indicator = 1
            pass
        else:
            pyvista_LR.antialiasing = antialiasing
            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    @state.change("cmap")
    def update_cmap(cmap=pyvista_LR.cmap_record, **kwargs):
        # Cmap should be universial
        if pyvista_LR.code_init_indicator_cmap == 0:
            pyvista_LR.code_init_indicator_cmap = 1
            pass
        else:
            pyvista_LR.cmap_record = cmap
            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    @state.change("frame")
    def update_frame(frame=pyvista_LR.frame_number, **kwargs):
        if pyvista_LR.code_init_indicator_frame == 0:
            pyvista_LR.code_init_indicator_frame = 1
            pass
        else:
            # if int(frame)>local_state.max_frame-1:
            #     print('Exceed the maximum frame number. We will show the last frame now.')
            # else:
            pyvista_LR.frame_number = int(frame)
            local_state.mom_states_x_one_frame = local_state.mom_states_x[
                ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                    (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                )
            ]  # we only need one frame.

            local_state.mom_states_y_one_frame = local_state.mom_states_y[
                ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                    (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                )
            ]

            local_state.mom_states_z_one_frame = local_state.mom_states_z[
                ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                    (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                )
            ]

            # local_state.moment_magintude = local_state.moment_magintude_all[((pyvista_LR.frame_number)*(len(local_state.coord))):((pyvista_LR.frame_number+1)*(len(local_state.coord)))]

            if (
                local_state.sub_frame_number == 2
                or local_state.sub_frame_number == 3
                or local_state.sub_frame_number == 4
            ):
                local_state.mom_states_x_one_frame1 = local_state.mom_states_x1[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]  # we only need one frame.

                local_state.mom_states_y_one_frame1 = local_state.mom_states_y1[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]

                local_state.mom_states_z_one_frame1 = local_state.mom_states_z1[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]

            # local_state.moment_magintude = local_state.moment_magintude_all[((pyvista_LR.frame_number)*(len(local_state.coord))):((pyvista_LR.frame_number+1)*(len(local_state.coord)))]

            if local_state.sub_frame_number == 3 or local_state.sub_frame_number == 4:
                local_state.mom_states_x_one_frame2 = local_state.mom_states_x2[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]  # we only need one frame.

                local_state.mom_states_y_one_frame2 = local_state.mom_states_y2[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]

                local_state.mom_states_z_one_frame2 = local_state.mom_states_z2[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]

            # local_state.moment_magintude = local_state.moment_magintude_all[((pyvista_LR.frame_number)*(len(local_state.coord))):((pyvista_LR.frame_number+1)*(len(local_state.coord)))]

            if local_state.sub_frame_number == 4:
                local_state.mom_states_x_one_frame3 = local_state.mom_states_x3[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]  # we only need one frame.

                local_state.mom_states_y_one_frame3 = local_state.mom_states_y3[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]

                local_state.mom_states_z_one_frame3 = local_state.mom_states_z3[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]

            # local_state.moment_magintude = local_state.moment_magintude_all[((pyvista_LR.frame_number)*(len(local_state.coord))):((pyvista_LR.frame_number+1)*(len(local_state.coord)))]
            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            local_state.frame_change = True
            ctrl.view_update()

    @state.change("do_glyph_projection_fft")
    def do_glyph_projection_fft(
        do_glyph_projection_fft=local_state.do_glyph_projection_fft, **kwargs
    ):
        if local_state.do_glyph_projection_fft_indicator == 0:
            local_state.do_glyph_projection_fft_indicator = 1
            pass
        else:
            local_state.do_glyph_projection_fft = do_glyph_projection_fft
            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    @state.change("swk_c")
    def swk_c(swk_c=local_state.warp_kernel_color, **kwargs):
        if local_state.swk_c_indicator == 0:
            local_state.swk_c_indicator = 1
            pass
        else:
            if (
                local_state.add_warpped_sphere_kernel
                and local_state.do_warp_sphere
                and pyvista_LR.add_glyphs
            ):
                local_state.warp_kernel_color = swk_c
                local_state.warp_kernel_color_changed = True
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("skw_ratio")
    def skw_ratio(skw_ratio=local_state.warpped_sphere_kernel, **kwargs):
        if local_state.skw_ratio_indicator == 0:
            local_state.skw_ratio_indicator = 1
            pass
        else:
            if pyvista_LR.add_glyphs and local_state.add_warpped_sphere_kernel:
                local_state.warpped_sphere_kernel = skw_ratio
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("warp_sphere_radius")
    def warp_sphere_radius(warp_sphere_radius=local_state.warp_sphere_radius, **kwargs):
        if local_state.warp_sphere_radius_indicator == 0:
            local_state.warp_sphere_radius_indicator = 1
            pass
        else:
            if pyvista_LR.add_glyphs and local_state.do_warp_sphere:
                local_state.warp_sphere_radius = warp_sphere_radius
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("low_pass_filter_order")
    def low_pass_filter_order(
        low_pass_filter_order=local_state.low_pass_filter_order, **kwargs
    ):
        if local_state.low_pass_filter_order_indicator == 0:
            local_state.low_pass_filter_order_indicator = 1
            pass
        else:
            if local_state.start_desoning_filter_index == 1:
                local_state.low_pass_filter_order = low_pass_filter_order
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("low_pass_normalized_freq")
    def low_pass_normalized_freq(
        low_pass_normalized_freq=local_state.low_pass_normalized_freq, **kwargs
    ):
        if local_state.low_pass_normalized_freq_indicator == 0:
            local_state.low_pass_normalized_freq_indicator = 1
            pass
        else:
            if local_state.start_desoning_filter_index == 1:
                local_state.low_pass_normalized_freq = low_pass_normalized_freq
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("fft_rec_windows_X")
    def fft_rec_windows_X(fft_rec_windows_X=local_state.fft_rec_windows_X, **kwargs):
        if local_state.fft_rec_windows_X_indicator == 0:
            local_state.fft_rec_windows_X_indicator = 1
            pass
        else:
            if local_state.start_desoning_filter_index == 2:
                local_state.fft_rec_windows_X = fft_rec_windows_X
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("fft_rec_windows_Y")
    def fft_rec_windows_Y(fft_rec_windows_Y=local_state.fft_rec_windows_Y, **kwargs):
        if local_state.fft_rec_windows_Y_indicator == 0:
            local_state.fft_rec_windows_Y_indicator = 1
            pass
        else:
            if local_state.start_desoning_filter_index == 2:
                local_state.fft_rec_windows_Y = fft_rec_windows_Y
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("fft_rec_windows_Z")
    def fft_rec_windows_Z(fft_rec_windows_Z=local_state.fft_rec_windows_Z, **kwargs):
        if local_state.fft_rec_windows_Z_indicator == 0:
            local_state.fft_rec_windows_Z_indicator = 1
            pass
        else:
            if local_state.start_desoning_filter_index == 2:
                local_state.fft_rec_windows_Z = fft_rec_windows_Z
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    @state.change("roughness")
    def update_roughness(roughness=pyvista_LR.roughness_record, **kwargs):
        if pyvista_LR.code_init_indicator_roughness == 0:
            pyvista_LR.code_init_indicator_roughness = 1
            pass
        else:
            if pyvista_LR.add_cone:
                pyvista_LR.roughness_record = roughness
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    def run_local_rendering_basic():
        if local_state.sub_frame_number == 1:
            current_plotter = pv.Plotter(
                shape=(1, 1), off_screen=False, title="SpinView Local View"
            )
            current_plotter.camera.position = plotter.camera.position
            current_plotter.camera.focal_point = plotter.camera.focal_point
            current_plotter.camera.up = plotter.camera.up
            current_plotter.background_color = plotter.background_color
            current_plotter.enable_anti_aliasing(pyvista_LR.antialiasing)
            current_plotter.add_axes()
        elif local_state.sub_frame_number == 2:
            current_plotter = pv.Plotter(
                shape=(1, 2), off_screen=False, title="SpinView Local View"
            )
            current_plotter.camera.position = plotter.camera.position
            current_plotter.camera.focal_point = plotter.camera.focal_point
            current_plotter.camera.up = plotter.camera.up
            current_plotter.background_color = plotter.background_color
            current_plotter.enable_anti_aliasing(pyvista_LR.antialiasing)
            current_plotter.add_axes()
        elif local_state.sub_frame_number == 3:
            current_plotter = pv.Plotter(
                shape=(1, 3), off_screen=False, title="SpinView Local View"
            )
            current_plotter.camera.position = plotter.camera.position
            current_plotter.camera.focal_point = plotter.camera.focal_point
            current_plotter.camera.up = plotter.camera.up
            current_plotter.background_color = plotter.background_color
            current_plotter.enable_anti_aliasing(pyvista_LR.antialiasing)
            current_plotter.add_axes()
        elif local_state.sub_frame_number == 4:
            current_plotter = pv.Plotter(
                shape=(2, 2), off_screen=False, title="SpinView Local View"
            )
            current_plotter.camera.position = plotter.camera.position
            current_plotter.camera.focal_point = plotter.camera.focal_point
            current_plotter.camera.up = plotter.camera.up
            current_plotter.background_color = plotter.background_color
            current_plotter.enable_anti_aliasing(pyvista_LR.antialiasing)
            current_plotter.add_axes()
        current_plotter.enable_anti_aliasing(pyvista_LR.antialiasing)
        plot_multiple_meshes(pyvista_LR, current_plotter, local_state)
        current_plotter.show()

        # map it back

        plotter.camera.position = current_plotter.camera.position
        plotter.camera.focal_point = current_plotter.camera.focal_point
        plotter.camera.up = current_plotter.camera.up
        plotter.background_color = current_plotter.background_color
        ctrl.view_update()
        viewer.update()
        viewer.push_camera()

        # current_plotter.enable_anti_aliasing(pyvista_LR.antialiasing)
        # current_plotter.add_axes()

    def change_subframe_to_1():
        local_state.sub_frame_number = 1
        if local_state.sub_frame_number == 1:
            plotter = pv.Plotter(shape=(1, 1))
        elif local_state.sub_frame_number == 2:
            plotter = pv.Plotter(shape=(1, 2))
        elif local_state.sub_frame_number == 3:
            plotter = pv.Plotter(shape=(1, 3))
        elif local_state.sub_frame_number == 4:
            plotter = pv.Plotter(shape=(2, 2))
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_subframe_to_2():
        local_state.sub_frame_number = 2
        # local_state.coord,local_state.mom_states_x,local_state.mom_states_y,local_state.mom_states_z,local_state.moment_magintude_all = parse_moment_and_coord_file(pyvista_LR,working_dir = state.selected_dir)
        # the second subframe
        local_state.sub_frame_number = 2
        if local_state.sub_frame_number == 1:
            plotter = pv.Plotter(shape=(1, 1))
        elif local_state.sub_frame_number == 2:
            plotter = pv.Plotter(shape=(1, 2))
        elif local_state.sub_frame_number == 3:
            plotter = pv.Plotter(shape=(1, 3))
        elif local_state.sub_frame_number == 4:
            plotter = pv.Plotter(shape=(2, 2))
        (
            local_state.coord,
            local_state.mom_states_x1,
            local_state.mom_states_y1,
            local_state.mom_states_z1,
            local_state.moment_magintude_all,
        ) = parse_moment_and_coord_file1(pyvista_LR, working_dir=state.selected_dir)

        local_state.mom_states_x_one_frame1 = local_state.mom_states_x1[
            ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                (pyvista_LR.frame_number + 1) * (len(local_state.coord))
            )
        ]  # we only need one frame.

        local_state.mom_states_y_one_frame1 = local_state.mom_states_y1[
            ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                (pyvista_LR.frame_number + 1) * (len(local_state.coord))
            )
        ]

        local_state.mom_states_z_one_frame1 = local_state.mom_states_z1[
            ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                (pyvista_LR.frame_number + 1) * (len(local_state.coord))
            )
        ]

        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    @state.change("unified_control")
    def unified_control(unified_control=local_state.unified_control, **kwargs):
        if local_state.unified_control_indicator == 0:
            local_state.unified_control_indicator = 1
            pass
        else:
            if local_state.sub_frame_number > 1:
                local_state.unified_control = unified_control
                plot_multiple_meshes(pyvista_LR, plotter, local_state)
                ctrl.view_update()

    def change_subframe_to_3():
        # the second subframe
        # local_state.coord,local_state.mom_states_x2,local_state.mom_states_y2,local_state.mom_states_z2,local_state.moment_magintude_all = parse_moment_and_coord_file1(pyvista_LR,working_dir = state.selected_dir)
        # the third subframe
        local_state.sub_frame_number = 3
        if local_state.sub_frame_number == 1:
            plotter = pv.Plotter(shape=(1, 1))
        elif local_state.sub_frame_number == 2:
            plotter = pv.Plotter(shape=(1, 2))
        elif local_state.sub_frame_number == 3:
            plotter = pv.Plotter(shape=(1, 3))
        elif local_state.sub_frame_number == 4:
            plotter = pv.Plotter(shape=(2, 2))
        (
            local_state.coord,
            local_state.mom_states_x1,
            local_state.mom_states_y1,
            local_state.mom_states_z1,
            local_state.moment_magintude_all,
        ) = parse_moment_and_coord_file2(pyvista_LR, working_dir=state.selected_dir)

        local_state.mom_states_x_one_frame1 = local_state.mom_states_x1[
            ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                (pyvista_LR.frame_number + 1) * (len(local_state.coord))
            )
        ]  # we only need one frame.

        local_state.mom_states_y_one_frame1 = local_state.mom_states_y1[
            ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                (pyvista_LR.frame_number + 1) * (len(local_state.coord))
            )
        ]

        local_state.mom_states_z_one_frame1 = local_state.mom_states_z1[
            ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                (pyvista_LR.frame_number + 1) * (len(local_state.coord))
            )
        ]

        local_state.mom_states_x_one_frame2 = local_state.mom_states_x2[
            ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                (pyvista_LR.frame_number + 1) * (len(local_state.coord))
            )
        ]  # we only need one frame.

        local_state.mom_states_y_one_frame2 = local_state.mom_states_y2[
            ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                (pyvista_LR.frame_number + 1) * (len(local_state.coord))
            )
        ]

        local_state.mom_states_z_one_frame2 = local_state.mom_states_z2[
            ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                (pyvista_LR.frame_number + 1) * (len(local_state.coord))
            )
        ]

        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def change_subframe_to_4():
        local_state.sub_frame_number = 4
        if local_state.sub_frame_number == 1:
            plotter = pv.Plotter(shape=(1, 1))
        elif local_state.sub_frame_number == 2:
            plotter = pv.Plotter(shape=(1, 2))
        elif local_state.sub_frame_number == 3:
            plotter = pv.Plotter(shape=(1, 3))
        elif local_state.sub_frame_number == 4:
            plotter = pv.Plotter(shape=(2, 2))
            # the second subframe
        # local_state.coord,local_state.mom_states_x2,local_state.mom_states_y2,local_state.mom_states_z2,local_state.moment_magintude_all = parse_moment_and_coord_file1(pyvista_LR,working_dir = state.selected_dir)
        # the third subframe
        (
            local_state.coord,
            local_state.mom_states_x1,
            local_state.mom_states_y1,
            local_state.mom_states_z1,
            local_state.moment_magintude_all,
        ) = parse_moment_and_coord_file2(pyvista_LR, working_dir=state.selected_dir)
        (
            local_state.coord,
            local_state.mom_states_x3,
            local_state.mom_states_y3,
            local_state.mom_states_z3,
            local_state.moment_magintude_all,
        ) = parse_moment_and_coord_file3(pyvista_LR, working_dir=state.selected_dir)

        local_state.mom_states_x_one_frame1 = local_state.mom_states_x1[
            ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                (pyvista_LR.frame_number + 1) * (len(local_state.coord))
            )
        ]  # we only need one frame.

        local_state.mom_states_y_one_frame1 = local_state.mom_states_y1[
            ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                (pyvista_LR.frame_number + 1) * (len(local_state.coord))
            )
        ]

        local_state.mom_states_z_one_frame1 = local_state.mom_states_z1[
            ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                (pyvista_LR.frame_number + 1) * (len(local_state.coord))
            )
        ]

        local_state.mom_states_x_one_frame2 = local_state.mom_states_x2[
            ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                (pyvista_LR.frame_number + 1) * (len(local_state.coord))
            )
        ]  # we only need one frame.

        local_state.mom_states_y_one_frame2 = local_state.mom_states_y2[
            ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                (pyvista_LR.frame_number + 1) * (len(local_state.coord))
            )
        ]

        local_state.mom_states_z_one_frame2 = local_state.mom_states_z2[
            ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                (pyvista_LR.frame_number + 1) * (len(local_state.coord))
            )
        ]

        local_state.mom_states_x_one_frame3 = local_state.mom_states_x3[
            ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                (pyvista_LR.frame_number + 1) * (len(local_state.coord))
            )
        ]  # we only need one frame.

        local_state.mom_states_y_one_frame3 = local_state.mom_states_y3[
            ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                (pyvista_LR.frame_number + 1) * (len(local_state.coord))
            )
        ]

        local_state.mom_states_z_one_frame3 = local_state.mom_states_z3[
            ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                (pyvista_LR.frame_number + 1) * (len(local_state.coord))
            )
        ]

        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def do_sp_warp():
        if pyvista_LR.add_glyphs:
            local_state.do_warp_sphere = not (local_state.do_warp_sphere)
            if local_state.do_warp_sphere:
                local_state.do_warp_sphere_vbtn_light.append("sp_warp_0")
            else:
                if "sp_warp_0" in local_state.do_warp_sphere_vbtn_light:
                    local_state.do_warp_sphere_vbtn_light.remove("sp_warp_0")
            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            viewer.view_isometric()
            viewer.reset_camera()

    def sp_warp_kernel():
        if pyvista_LR.add_glyphs:
            local_state.add_warpped_sphere_kernel = not (
                local_state.add_warpped_sphere_kernel
            )
            if local_state.add_warpped_sphere_kernel:
                local_state.do_warp_sphere_vbtn_light.append("sp_warp_1")
            else:
                if "sp_warp_1" in local_state.do_warp_sphere_vbtn_light:
                    local_state.do_warp_sphere_vbtn_light.remove("sp_warp_1")

            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            viewer.view_isometric()
            viewer.reset_camera()

    def add_projection_plane_1():
        if pyvista_LR.add_glyphs:
            pyvista_LR.add_projection_plane_1 = not (pyvista_LR.add_projection_plane_1)
            if "Glyph_projection_0" not in local_state.glyph_projection_plane:
                local_state.glyph_projection_plane.append("Glyph_projection_0")
            else:
                local_state.glyph_projection_plane.remove("Glyph_projection_0")

            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    def add_projection_plane_2():
        if pyvista_LR.add_glyphs:
            pyvista_LR.add_projection_plane_2 = not (pyvista_LR.add_projection_plane_2)
            if "Glyph_projection_1" not in local_state.glyph_projection_plane:
                local_state.glyph_projection_plane.append("Glyph_projection_1")
            else:
                local_state.glyph_projection_plane.remove("Glyph_projection_1")

            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    def add_projection_plane_3():
        if pyvista_LR.add_glyphs:
            pyvista_LR.add_projection_plane_3 = not (pyvista_LR.add_projection_plane_3)
            if "Glyph_projection_2" not in local_state.glyph_projection_plane:
                local_state.glyph_projection_plane.append("Glyph_projection_2")
            else:
                local_state.glyph_projection_plane.remove("Glyph_projection_2")

            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    def add_projection_plane_4():
        if pyvista_LR.add_glyphs:
            pyvista_LR.add_projection_plane_4 = not (pyvista_LR.add_projection_plane_4)
            if "Glyph_projection_3" not in local_state.glyph_projection_plane:
                local_state.glyph_projection_plane.append("Glyph_projection_3")
            else:
                local_state.glyph_projection_plane.remove("Glyph_projection_3")

            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    def add_projection_plane_5():
        if pyvista_LR.add_glyphs:
            pyvista_LR.add_projection_plane_5 = not (pyvista_LR.add_projection_plane_5)
            if "Glyph_projection_4" not in local_state.glyph_projection_plane:
                local_state.glyph_projection_plane.append("Glyph_projection_4")
            else:
                local_state.glyph_projection_plane.remove("Glyph_projection_4")

            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    def add_projection_plane_6():
        if pyvista_LR.add_glyphs:
            pyvista_LR.add_projection_plane_6 = not (pyvista_LR.add_projection_plane_6)
            if "Glyph_projection_5" not in local_state.glyph_projection_plane:
                local_state.glyph_projection_plane.append("Glyph_projection_5")
            else:
                local_state.glyph_projection_plane.remove("Glyph_projection_5")

            plot_multiple_meshes(pyvista_LR, plotter, local_state)
            ctrl.view_update()

    def denoising_low_pass():
        local_state.start_desoning_filter_index = 1
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def denoising_low_pass_fft_rec():
        local_state.start_desoning_filter_index = 2
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def denoising_N():
        local_state.start_desoning_filter_index = 0
        plot_multiple_meshes(pyvista_LR, plotter, local_state)
        ctrl.view_update()

    def run_local_moive_rendering_basic():
        if local_state.sub_frame_number == 1:
            current_plotter = pv.Plotter(
                shape=(1, 1),
                window_size=([local_state.moive_size_x, local_state.moive_size_y]),
                off_screen=True,
            )
            current_plotter.camera.position = plotter.camera.position
            current_plotter.camera.focal_point = plotter.camera.focal_point
            current_plotter.camera.up = plotter.camera.up
            current_plotter.background_color = plotter.background_color
            current_plotter.enable_anti_aliasing(pyvista_LR.antialiasing)
            current_plotter.add_axes()
        elif local_state.sub_frame_number == 2:
            current_plotter = pv.Plotter(
                shape=(1, 2),
                window_size=([local_state.moive_size_x, local_state.moive_size_y]),
                off_screen=True,
            )
            current_plotter.camera.position = plotter.camera.position
            current_plotter.camera.focal_point = plotter.camera.focal_point
            current_plotter.camera.up = plotter.camera.up
            current_plotter.background_color = plotter.background_color
            current_plotter.enable_anti_aliasing(pyvista_LR.antialiasing)
            current_plotter.add_axes()
        elif local_state.sub_frame_number == 3:
            current_plotter = pv.Plotter(
                shape=(1, 3),
                window_size=([local_state.moive_size_x, local_state.moive_size_y]),
                off_screen=True,
            )
            current_plotter.camera.position = plotter.camera.position
            current_plotter.camera.focal_point = plotter.camera.focal_point
            current_plotter.camera.up = plotter.camera.up
            current_plotter.background_color = plotter.background_color
            current_plotter.enable_anti_aliasing(pyvista_LR.antialiasing)
            current_plotter.add_axes()
        elif local_state.sub_frame_number == 4:
            current_plotter = pv.Plotter(
                shape=(2, 2),
                window_size=([local_state.moive_size_x, local_state.moive_size_y]),
                off_screen=True,
            )
            current_plotter.camera.position = plotter.camera.position
            current_plotter.camera.focal_point = plotter.camera.focal_point
            current_plotter.camera.up = plotter.camera.up
            current_plotter.background_color = plotter.background_color
            current_plotter.enable_anti_aliasing(pyvista_LR.antialiasing)
            current_plotter.add_axes()
        current_plotter.enable_anti_aliasing(pyvista_LR.antialiasing)
        movie_length = int(len(local_state.mom_states_x) / len(local_state.coord))
        current_plotter.open_movie(
            (state.selected_dir + "/SpinView_trajectory.mp4"),
            framerate=local_state.moive_fps,
            quality=7,
        )

        for frame_number in range(movie_length):
            print(
                "SpinView: Rendering frame "
                + str(frame_number)
                + "/"
                + str(movie_length)
            )
            _temp = pyvista_LR.frame_number

            pyvista_LR.frame_number = int(frame_number)

            local_state.mom_states_x_one_frame = local_state.mom_states_x[
                ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                    (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                )
            ]  # we only need one frame.

            local_state.mom_states_y_one_frame = local_state.mom_states_y[
                ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                    (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                )
            ]

            local_state.mom_states_z_one_frame = local_state.mom_states_z[
                ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                    (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                )
            ]

            if (
                local_state.sub_frame_number == 2
                or local_state.sub_frame_number == 3
                or local_state.sub_frame_number == 4
            ):
                local_state.mom_states_x_one_frame1 = local_state.mom_states_x1[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]  # we only need one frame.

                local_state.mom_states_y_one_frame1 = local_state.mom_states_y1[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]

                local_state.mom_states_z_one_frame1 = local_state.mom_states_z1[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]

            if local_state.sub_frame_number == 3 or local_state.sub_frame_number == 4:
                local_state.mom_states_x_one_frame2 = local_state.mom_states_x2[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]  # we only need one frame.

                local_state.mom_states_y_one_frame2 = local_state.mom_states_y2[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]

                local_state.mom_states_z_one_frame2 = local_state.mom_states_z2[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]

            if local_state.sub_frame_number == 4:
                # the fourth subframe

                local_state.mom_states_x_one_frame3 = local_state.mom_states_x3[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]  # we only need one frame.

                local_state.mom_states_y_one_frame3 = local_state.mom_states_y3[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]

                local_state.mom_states_z_one_frame3 = local_state.mom_states_z3[
                    ((pyvista_LR.frame_number) * (len(local_state.coord))) : (
                        (pyvista_LR.frame_number + 1) * (len(local_state.coord))
                    )
                ]

            plot_multiple_meshes(pyvista_LR, current_plotter, local_state)
            pyvista_LR.frame_number = _temp
            current_plotter.add_text(
                "Frame:{}".format(np.round(frame_number * 1, 1)),
                name="time",
                position="upper_right",
                color="Black",
                shadow=True,
                font_size=20,
            )
            current_plotter.write_frame()
            local_state.frame_change = True
        # Closes and finalizes movie

        current_plotter.close()

    @state.change("new_profile_name")
    def new_profile_name(new_profile_name=local_state.new_profile_name, **kwargs):
        try:
            local_state.new_profile_name = str(new_profile_name)
        except:
            pass

    @state.change("download_transparent_screenshot")
    def download_transparent_screenshot():
        plotter.screenshot(
            "{}/SpinView_transparent_screenshot.png".format(state.selected_dir),
            transparent_background=True,
            scale=local_state.download_screenshot_resolution,
            # window_size=(
            #     int(local_state.download_screenshot_resolution),
            #     int(local_state.download_screenshot_resolution),
            # ),
        )
        print(
            "Transparent screenshot is downloaded at {}/SpinView_transparent_screenshot.png".format(
                state.selected_dir
            )
        )
        # ctrl.view_update()

    @state.change("download_normal_screenshot")
    def download_normal_screenshot():
        plotter.screenshot(
            "{}/SpinView_normal_screenshot.png".format(state.selected_dir),
            transparent_background=False,
            scale=local_state.download_screenshot_resolution,
            # window_size=(
            #     int(local_state.download_screenshot_resolution),
            #     int(local_state.download_screenshot_resolution),
            # ),
        )
        plotter.save_graphic(
            "{}/SpinView_normal_vector_graph.svg".format(state.selected_dir)
        )
        print(local_state.download_screenshot_resolution)
        print(
            "Normal screenshot is downloaded at {}/SpinView_normal_screenshot.png  and {}/SpinView_normal_vector_graph.svg".format(
                state.selected_dir, state.selected_dir
            )
        )
        # ctrl.view_update()

    def exchange_parameter_from_pyvista_LR_to_local_state(pyvista_LR, local_state):
        pyvista_LR.do_delaunay = local_state.do_delaunay

        pyvista_LR.antialiasing_indicator = 0
        pyvista_LR.download_screenshot_resolution = (
            local_state.download_screenshot_resolution
        )
        pyvista_LR.download_screenshot_indicator = 0
        pyvista_LR.activate_glyphs_indicator = 0
        pyvista_LR.activate_rectangle_mesh_indicator = 0
        pyvista_LR.activate_unstructured_mesh_indicator = 0
        pyvista_LR.code_init_indicator_cmap = 0
        pyvista_LR.code_init_indicator_frame = 0
        pyvista_LR.code_init_indicator_metallic = 0
        pyvista_LR.code_init_indicator_opacity = 0
        pyvista_LR.code_init_indicator_roughness = 0
        pyvista_LR.code_init_indicator_resolutions = 0
        pyvista_LR.code_init_indicator_Ratio = 0
        pyvista_LR.code_init_indicator_cone_highth = 0
        pyvista_LR.code_init_indicator_cone_Radius = 0
        pyvista_LR.code_init_indicator_cs = 0
        pyvista_LR.code_init_indicator_Cut_X = 0
        pyvista_LR.code_init_indicator_Cut_Y = 0
        pyvista_LR.code_init_indicator_Cut_Z = 0
        pyvista_LR.code_init_indicator_fxyzc = 0
        pyvista_LR.download_screenshot_indicator = 0
        pyvista_LR.activate_glyphs_indicator = 0
        pyvista_LR.activate_rectangle_mesh_indicator = 0
        pyvista_LR.activate_unstructured_mesh_indicator = 0
        pyvista_LR.moment_file_indicator = 0
        pyvista_LR.coord_file_indicator = 0
        pyvista_LR.ovf_file_indicator = 0
        pyvista_LR.bgc_indicator = 0
        pyvista_LR.pbr_indicator = 0
        pyvista_LR.rectangle_mesh_contour_method_indicator = 0
        pyvista_LR.unstructured_mesh_contour_method_indicator = 0
        pyvista_LR.antialiasing_indicator = 0
        pyvista_LR.tmesh_op_indicator = 0
        pyvista_LR.activate_cone_indicator = 0
        pyvista_LR.activate_arrow_indicator = 0
        pyvista_LR.activate_sphere_indicator = 0
        pyvista_LR.activate_box_indicator = 0
        pyvista_LR.activate_own_glyphs_indicator = 0
        pyvista_LR.activate_plane_indicator = 0
        pyvista_LR.scalar_bar_indicator = 0
        pyvista_LR.cone_cmap_index_indicator = 0
        pyvista_LR.do_clip_component_indicator = 0
        pyvista_LR.activate_point_indicator = 0
        pyvista_LR.point_rescale_indicator = 0
        pyvista_LR.point_size_indicator = 0
        pyvista_LR.point_rescale_factor_indicator = 0
        pyvista_LR.swk_c_indicator = 0
        pyvista_LR.warp_sphere_radius_indicator = 0
        pyvista_LR.skw_ratio_indicator = 0
        pyvista_LR.do_glyph_projection_fft_indicator = 0
        pyvista_LR.cut_phi_indicator = 0
        pyvista_LR.cut_theta_indicator = 0

        pyvista_LR.excu_from_other_place = local_state.excu_from_other_place
        pyvista_LR.nothing_show = local_state.nothing_show
        pyvista_LR.frame_change = local_state.frame_change
        pyvista_LR.projection_plane_1_added = local_state.projection_plane_1_added
        pyvista_LR.projection_plane_2_added = local_state.projection_plane_2_added
        pyvista_LR.projection_plane_3_added = local_state.projection_plane_3_added
        pyvista_LR.projection_plane_4_added = local_state.projection_plane_4_added
        pyvista_LR.projection_plane_5_added = local_state.projection_plane_5_added
        pyvista_LR.projection_plane_6_added = local_state.projection_plane_6_added
        pyvista_LR.cone_added_1 = local_state.cone_added_1
        pyvista_LR.cone_added_2 = local_state.cone_added_2
        pyvista_LR.cone_added_3 = local_state.cone_added_3
        pyvista_LR.cone_added_4 = local_state.cone_added_4
        pyvista_LR.arrow_added_1 = local_state.arrow_added_1
        pyvista_LR.arrow_added_2 = local_state.arrow_added_2
        pyvista_LR.arrow_added_3 = local_state.arrow_added_3
        pyvista_LR.arrow_added_4 = local_state.arrow_added_4
        pyvista_LR.sphere_added_1 = local_state.sphere_added_1
        pyvista_LR.sphere_added_2 = local_state.sphere_added_2
        pyvista_LR.sphere_added_3 = local_state.sphere_added_3
        pyvista_LR.sphere_added_4 = local_state.sphere_added_4
        pyvista_LR.box_added_1 = local_state.box_added_1
        pyvista_LR.box_added_2 = local_state.box_added_2
        pyvista_LR.box_added_3 = local_state.box_added_3
        pyvista_LR.box_added_4 = local_state.box_added_4
        pyvista_LR.own_glyphs_added_1 = local_state.own_glyphs_added_1
        pyvista_LR.own_glyphs_added_2 = local_state.own_glyphs_added_2
        pyvista_LR.own_glyphs_added_3 = local_state.own_glyphs_added_3
        pyvista_LR.own_glyphs_added_4 = local_state.own_glyphs_added_4
        pyvista_LR.plane_added_1 = local_state.plane_added_1
        pyvista_LR.plane_added_2 = local_state.plane_added_2
        pyvista_LR.plane_added_3 = local_state.plane_added_3
        pyvista_LR.plane_added_4 = local_state.plane_added_4
        pyvista_LR.tmesh_op_indicator = 0
        pyvista_LR.unstructured_mesh_added_1 = local_state.unstructured_mesh_added_1
        pyvista_LR.unstructured_mesh_added_2 = local_state.unstructured_mesh_added_2
        pyvista_LR.unstructured_mesh_added_3 = local_state.unstructured_mesh_added_3
        pyvista_LR.unstructured_mesh_added_4 = local_state.unstructured_mesh_added_4
        pyvista_LR.rectangle_mesh_added_1 = local_state.rectangle_mesh_added_1
        pyvista_LR.rectangle_mesh_added_2 = local_state.rectangle_mesh_added_2
        pyvista_LR.rectangle_mesh_added_3 = local_state.rectangle_mesh_added_3
        pyvista_LR.rectangle_mesh_added_4 = local_state.rectangle_mesh_added_4
        pyvista_LR.rectangle_mesh_contour_isosurface_value_x = (
            local_state.rectangle_mesh_contour_isosurface_value_x
        )
        pyvista_LR.rectangle_mesh_contour_isosurface_value_y = (
            local_state.rectangle_mesh_contour_isosurface_value_y
        )
        pyvista_LR.rectangle_mesh_contour_isosurface_value_z = (
            local_state.rectangle_mesh_contour_isosurface_value_z
        )
        pyvista_LR.simple_point_added_1 = local_state.simple_point_added_1
        pyvista_LR.simple_point_added_2 = local_state.simple_point_added_2
        pyvista_LR.simple_point_added_3 = local_state.simple_point_added_3
        pyvista_LR.simple_point_added_4 = local_state.simple_point_added_4
        pyvista_LR.excu_from_other_place_welcome_image = (
            local_state.excu_from_other_place_welcome_image
        )
        pyvista_LR.nothing_show_welcome_image = local_state.nothing_show_welcome_image
        pyvista_LR.first_time_nothing_show = local_state.first_time_nothing_show
        pyvista_LR.cubemap_exist = local_state.cubemap_exist
        pyvista_LR.activate_cone_indicator = 0
        pyvista_LR.activate_arrow_indicator = 0
        pyvista_LR.activate_sphere_indicator = 0
        pyvista_LR.activate_box_indicator = 0
        pyvista_LR.activate_own_glyphs_indicator = 0
        pyvista_LR.activate_plane_indicator = 0
        pyvista_LR.sub_frame_number = local_state.sub_frame_number

        pyvista_LR.scalar_bar_indicator = 0
        pyvista_LR.moive_size_x = local_state.moive_size_x
        pyvista_LR.moive_size_y = local_state.moive_size_y
        pyvista_LR.welcome_image_not_created = local_state.welcome_image_not_created
        pyvista_LR.cone_cmap_index_indicator = 0
        pyvista_LR.glyph_cmap_vbtn = local_state.glyph_cmap_vbtn
        pyvista_LR.glyph_opaciy_vbtn = local_state.glyph_opaciy_vbtn
        pyvista_LR.do_clip_component_indicator = 0
        pyvista_LR.activate_point_indicator = 0
        pyvista_LR.point_rescale_indicator = 0
        pyvista_LR.point_size_indicator = 0
        pyvista_LR.point_rescale_factor_indicator = 0
        pyvista_LR.warp_sphere_radius = local_state.warp_sphere_radius
        pyvista_LR.do_warp_sphere = local_state.do_warp_sphere
        pyvista_LR.add_warpped_sphere_kernel = local_state.add_warpped_sphere_kernel
        pyvista_LR.warpped_sphere_kernel = local_state.warpped_sphere_kernel
        pyvista_LR.warp_kernel_color = local_state.warp_kernel_color
        pyvista_LR.swk_c_indicator = 0
        pyvista_LR.swk_added = local_state.swk_added
        pyvista_LR.warp_sphere_radius_indicator = 0
        pyvista_LR.skw_ratio_indicator = 0
        pyvista_LR.warp_kernel_color_changed = local_state.warp_kernel_color_changed
        pyvista_LR.start_desoning_filter_index = local_state.start_desoning_filter_index
        pyvista_LR.low_pass_filter_order = local_state.low_pass_filter_order
        pyvista_LR.low_pass_normalized_freq = local_state.low_pass_normalized_freq
        pyvista_LR.fft_rec_windows_X = local_state.fft_rec_windows_X
        pyvista_LR.fft_rec_windows_Y = local_state.fft_rec_windows_Y
        pyvista_LR.fft_rec_windows_Z = local_state.fft_rec_windows_Z
        pyvista_LR.projection_plane_added_1_1 = local_state.projection_plane_added_1_1
        pyvista_LR.projection_plane_added_1_2 = local_state.projection_plane_added_1_2
        pyvista_LR.projection_plane_added_1_3 = local_state.projection_plane_added_1_3
        pyvista_LR.projection_plane_added_1_4 = local_state.projection_plane_added_1_4
        pyvista_LR.projection_plane_added_2_1 = local_state.projection_plane_added_2_1
        pyvista_LR.projection_plane_added_2_2 = local_state.projection_plane_added_2_2
        pyvista_LR.projection_plane_added_2_3 = local_state.projection_plane_added_2_3
        pyvista_LR.projection_plane_added_2_4 = local_state.projection_plane_added_2_4
        pyvista_LR.projection_plane_added_3_1 = local_state.projection_plane_added_3_1
        pyvista_LR.projection_plane_added_3_2 = local_state.projection_plane_added_3_2
        pyvista_LR.projection_plane_added_3_3 = local_state.projection_plane_added_3_3
        pyvista_LR.projection_plane_added_3_4 = local_state.projection_plane_added_3_4
        pyvista_LR.projection_plane_added_4_1 = local_state.projection_plane_added_4_1
        pyvista_LR.projection_plane_added_4_2 = local_state.projection_plane_added_4_2
        pyvista_LR.projection_plane_added_4_3 = local_state.projection_plane_added_4_3
        pyvista_LR.projection_plane_added_4_4 = local_state.projection_plane_added_4_4
        pyvista_LR.projection_plane_added_5_1 = local_state.projection_plane_added_5_1
        pyvista_LR.projection_plane_added_5_2 = local_state.projection_plane_added_5_2
        pyvista_LR.projection_plane_added_5_3 = local_state.projection_plane_added_5_3
        pyvista_LR.projection_plane_added_5_4 = local_state.projection_plane_added_5_4
        pyvista_LR.projection_plane_added_6_1 = local_state.projection_plane_added_6_1
        pyvista_LR.projection_plane_added_6_2 = local_state.projection_plane_added_6_2
        pyvista_LR.projection_plane_added_6_3 = local_state.projection_plane_added_6_3
        pyvista_LR.projection_plane_added_6_4 = local_state.projection_plane_added_6_4
        pyvista_LR.do_glyph_projection_fft = local_state.do_glyph_projection_fft
        pyvista_LR.do_glyph_projection_fft_indicator = 0
        pyvista_LR.cut_phi_indicator = 0
        pyvista_LR.cut_theta_indicator = 0
        pyvista_LR.rectangle_cmap_vbtn = local_state.rectangle_cmap_vbtn
        pyvista_LR.rectangle_opaciy_vbtn = local_state.rectangle_opaciy_vbtn
        pyvista_LR.Tmesh_cmap_vbtn = local_state.Tmesh_cmap_vbtn
        pyvista_LR.Tmesh_opaciy_vbtn = local_state.Tmesh_opaciy_vbtn
        pyvista_LR.rectangle_mesh_contour_isosurface_value_t = (
            local_state.rectangle_mesh_contour_isosurface_value_t
        )
        pyvista_LR.rectangle_mesh_contour_isosurface_value_p = (
            local_state.rectangle_mesh_contour_isosurface_value_p
        )
        pyvista_LR.unstructured_mesh_contour_isosurface_value_t = (
            local_state.unstructured_mesh_contour_isosurface_value_t
        )
        pyvista_LR.unstructured_mesh_contour_isosurface_value_p = (
            local_state.unstructured_mesh_contour_isosurface_value_p
        )
        pyvista_LR.opacity_record_tmesh = local_state.opacity_record_tmesh
        pyvista_LR.opacity_record_rectangle_mesh = (
            local_state.opacity_record_rectangle_mesh
        )

        pyvista_LR.change_mom1 = 0
        pyvista_LR.change_mom2 = 0
        pyvista_LR.change_mom3 = 0
        pyvista_LR.change_mom4 = 0

        pyvista_LR.rec_mesh_color_scalar = local_state.rec_mesh_color_scalar
        pyvista_LR.rectangle_mesh_clip_scalar_max_x = (
            local_state.rectangle_mesh_clip_scalar_max_x
        )
        pyvista_LR.rectangle_mesh_clip_scalar_min_x = (
            local_state.rectangle_mesh_clip_scalar_min_x
        )
        pyvista_LR.rectangle_mesh_clip_scalar_max_y = (
            local_state.rectangle_mesh_clip_scalar_max_y
        )
        pyvista_LR.rectangle_mesh_clip_scalar_min_y = (
            local_state.rectangle_mesh_clip_scalar_min_y
        )
        pyvista_LR.rectangle_mesh_clip_scalar_max_z = (
            local_state.rectangle_mesh_clip_scalar_max_z
        )
        pyvista_LR.rectangle_mesh_clip_scalar_min_z = (
            local_state.rectangle_mesh_clip_scalar_min_z
        )
        pyvista_LR.roughness_rmesh = local_state.roughness_rmesh
        pyvista_LR.metallic_rmesh = local_state.metallic_rmesh
        pyvista_LR.metallic_tmesh = local_state.metallic_tmesh
        pyvista_LR.roughness_tmesh = local_state.roughness_tmesh
        pyvista_LR.pyvista_backend_interactive_ratio = (
            local_state.pyvista_backend_interactive_ratio
        )
        pyvista_LR.pyvista_backend_still_ratio = local_state.pyvista_backend_still_ratio
        pyvista_LR.do_interpolated_projection = local_state.do_interpolated_projection
        pyvista_LR.t_mesh_contour_isosurface_value_x = (
            local_state.t_mesh_contour_isosurface_value_x
        )
        pyvista_LR.t_mesh_contour_isosurface_value_y = (
            local_state.t_mesh_contour_isosurface_value_y
        )
        pyvista_LR.t_mesh_contour_isosurface_value_z = (
            local_state.t_mesh_contour_isosurface_value_z
        )
        pyvista_LR.t_mesh_clip_scalar_max_x = local_state.t_mesh_clip_scalar_max_x
        pyvista_LR.t_mesh_clip_scalar_min_x = local_state.t_mesh_clip_scalar_min_x
        pyvista_LR.t_mesh_clip_scalar_max_y = local_state.t_mesh_clip_scalar_max_y
        pyvista_LR.t_mesh_clip_scalar_min_y = local_state.t_mesh_clip_scalar_min_y
        pyvista_LR.t_mesh_clip_scalar_max_z = local_state.t_mesh_clip_scalar_max_z
        pyvista_LR.t_mesh_clip_scalar_min_z = local_state.t_mesh_clip_scalar_min_z

    def store_new_profile():
        exchange_parameter_from_pyvista_LR_to_local_state(pyvista_LR, local_state)
        print("Table : {} is stored".format(str(local_state.new_profile_name)))
        pyvista_LR.store_profile(
            table_name_store=str(local_state.new_profile_name), db_path=db_path
        )

    return (
        store_new_profile,
        run_local_rendering_basic,
        run_local_moive_rendering_basic,
        download_transparent_screenshot,
        download_normal_screenshot,
        do_sp_warp,
        sp_warp_kernel,
        denoising_N,
        denoising_low_pass,
        denoising_low_pass_fft_rec,
        add_projection_plane_1,
        add_projection_plane_2,
        add_projection_plane_3,
        add_projection_plane_4,
        add_projection_plane_5,
        add_projection_plane_6,
    )
