from trame.widgets import vuetify
import matplotlib.colors as mcolors


def glyph_initialize(local_state, pyvista_LR, state, ctrl, spinview_checkbox, colors):
    with vuetify.VListGroup(
        color="orange darken-2", prepend_icon="mdi-alpha-g-box-outline"
    ):
        with vuetify.Template(
            v_slot_activator=True,
        ):
            vuetify.VListItemTitle(
                "Glyphs",
                style="display: flex; align-items: center; justify-content: center",
            )

        ##########
        # Glyphs Global properties
        ##########
        # ---------------------------
        # Activate glyphs
        # ---------------------------
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        with vuetify.VRow(
            classes="pt-3",
            dense=False,
        ):
            with vuetify.VCol(cols="4"):
                vuetify.VSpacer()
            with vuetify.VCol(cols="3"):
                spinview_checkbox(
                    model=("activate_glyphs", pyvista_LR.add_glyphs),
                    on_icon="mdi-alpha-g-circle",
                    off_icon="mdi-alpha-g-circle-outline",
                    label="Glyphs:",
                    tooltip="Activate/Deactivate all glyphs",
                    color_in="orange darken-2",
                )
            with vuetify.VCol(cols="3"):
                vuetify.VSpacer()
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        vuetify.VDivider(
            vertical=False,
            inset=False,
            style=("max-width: 390; min-height: 390;max-height: 20px"),
        )

        ################
        # Cmap selector
        ################

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        with vuetify.VRow(classes="pt-3", dense=False):
            with vuetify.VCol(cols="1"):
                vuetify.VSpacer()
            with vuetify.VCol(cols="8"):
                with vuetify.VCardText("    Glyph cmap component:"):
                    with vuetify.VBtnToggle(
                        color="orange darken-2",
                        multiple=False,
                        split=True,
                        mandatory=True,
                        value=local_state.glyph_cmap_vbtn,
                        rounded=True,
                        v_model=(
                            "view_mode",
                            "Glyph_cmap{}".format(pyvista_LR.color_map_index),
                        ),
                    ):
                        with vuetify.VBtn(
                            click=ctrl.change_glyph_cmap_vbtn_value_0,
                            value="Glyph_cmap0",
                        ):
                            vuetify.VIcon("mdi-alpha-x")
                        with vuetify.VBtn(
                            click=ctrl.change_glyph_cmap_vbtn_value_1,
                            value="Glyph_cmap1",
                        ):
                            vuetify.VIcon("mdi-alpha-y")
                        with vuetify.VBtn(
                            click=ctrl.change_glyph_cmap_vbtn_value_2,
                            value="Glyph_cmap2",
                        ):
                            vuetify.VIcon("mdi-alpha-z")
                        with vuetify.VBtn(
                            click=ctrl.change_glyph_cmap_vbtn_value_3,
                            value="Glyph_cmap3",
                        ):
                            vuetify.VIcon("mdi-alpha-t")
                        with vuetify.VBtn(
                            click=ctrl.change_glyph_cmap_vbtn_value_4,
                            value="Glyph_cmap4",
                        ):
                            vuetify.VIcon("mdi-alpha-p")

        vuetify.VSpacer(style=("max-height: 30px; min-height: 30px"))
        vuetify.VDivider(
            vertical=False,
            inset=False,
            style=("max-width: 390; min-height: 390;max-height: 20px"),
        )
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

        with vuetify.VRow(classes="pt-3", dense=False):
            with vuetify.VCol(cols="10"):
                with vuetify.VCardText("    Glyph opacity component:"):
                    with vuetify.VBtnToggle(
                        tag="ss",
                        color="orange darken-2",
                        multiple=False,
                        split=True,
                        mandatory=True,
                        value=local_state.glyph_opaciy_vbtn,
                        rounded=True,
                        dense=True,
                        v_model=(
                            "view_mode1",
                            "Glyph_opacity{}".format(pyvista_LR.opacity_index),
                        ),
                    ):
                        with vuetify.VBtn(
                            click=ctrl.change_glyph_opacity_index_vbtn_value_0,
                            value="Glyph_opacity0",
                        ):
                            vuetify.VIcon("mdi-alpha-x")
                        with vuetify.VBtn(
                            click=ctrl.change_glyph_opacity_index_vbtn_value_1,
                            value="Glyph_opacity1",
                        ):
                            vuetify.VIcon("mdi-alpha-y")
                        with vuetify.VBtn(
                            click=ctrl.change_glyph_opacity_index_vbtn_value_2,
                            value="Glyph_opacity2",
                        ):
                            vuetify.VIcon("mdi-alpha-z")
                        with vuetify.VBtn(
                            click=ctrl.change_glyph_opacity_index_vbtn_value_3,
                            value="Glyph_opacity3",
                        ):
                            vuetify.VIcon("mdi-alpha-t")
                        with vuetify.VBtn(
                            click=ctrl.change_glyph_opacity_index_vbtn_value_4,
                            value="Glyph_opacity4",
                        ):
                            vuetify.VIcon("mdi-alpha-t-box")
                        with vuetify.VBtn(
                            click=ctrl.change_glyph_opacity_index_vbtn_value_5,
                            value="Glyph_opacity5",
                        ):
                            vuetify.VIcon("mdi-alpha-p")
                        with vuetify.VBtn(
                            click=ctrl.change_glyph_opacity_index_vbtn_value_6,
                            value="Glyph_opacity6",
                        ):
                            vuetify.VIcon(" mdi-account-details")

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        with vuetify.VRow(classes="pt-3", dense=False):
            with vuetify.VCol(cols="1"):
                vuetify.VSpacer()
            with vuetify.VCol(cols="9"):
                vuetify.VSlider(
                    v_model=("opacity", 1),
                    min=0,
                    max=1,
                    step=0.01,
                    label="Opacity",
                    # classes="mt-1",
                    thumb_label=True,
                    hide_details=False,
                    dense=False,
                    append_icon="mdi-water-opacity",
                    track_color="orange darken-2",
                    color="orange darken-2",
                )

        vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
        vuetify.VDivider(
            vertical=False,
            inset=False,
            style=("max-width: 390; min-height: 390;max-height: 20px"),
        )
        vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
        with vuetify.VListGroup(
            color="orange darken-2", prepend_icon="mdi-alpha-c-circle-outline"
        ):
            with vuetify.Template(
                v_slot_activator=True,
            ):
                vuetify.VListItemTitle(
                    "Clip filters",
                    style="display: flex; align-items: center; justify-content: center",
                )

            ##############
            # Face clip
            ##############
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="2"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="6"):
                    with vuetify.VCardText(f"Face clip XYZ/Free:"):
                        with vuetify.VBtnToggle(
                            color="orange darken-2",
                            multiple=True,
                            split=True,
                            mandatory=False,
                            v_model=(
                                "view_mode_face_clip",
                                local_state.face_clip_index,
                            ),
                        ):
                            with vuetify.VBtn(
                                click=ctrl.do_clip_plane_fix_origin_and_normal,
                                value="face_clip_0",
                                large=True,
                            ):
                                vuetify.VIcon("mdi-axis-arrow")
                            vuetify.VSpacer(style=("max-width: 20px; min-width: 20px"))
                            with vuetify.VBtn(
                                click=ctrl.do_clip_plane_free_normal,
                                value="face_clip_1",
                                large=True,
                            ):
                                vuetify.VIcon("mdi-axis-x-arrow")

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

            # X_min
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=(
                            "clip_plane_x_min",
                            local_state.point_cloud_arrow_for_face_cut.bounds[0],
                        ),
                        min=local_state.point_cloud_arrow_for_face_cut.bounds[0],
                        max=local_state.point_cloud_arrow_for_face_cut.bounds[1],
                        step=0.1,
                        label="X min->max",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        append_icon="mdi-alpha-x-circle-outline",
                        color="orange darken-2",
                        dense=False,
                    )

            # X_max
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=(
                            "clip_plane_x_max",
                            local_state.point_cloud_arrow_for_face_cut.bounds[1],
                        ),
                        min=local_state.point_cloud_arrow_for_face_cut.bounds[0],
                        max=local_state.point_cloud_arrow_for_face_cut.bounds[1],
                        step=0.1,
                        label="X max->min",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        append_icon="mdi-alpha-x-circle",
                        color="orange darken-2",
                        dense=False,
                    )

            # y_min
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=(
                            "clip_plane_y_min",
                            local_state.point_cloud_arrow_for_face_cut.bounds[2],
                        ),
                        min=local_state.point_cloud_arrow_for_face_cut.bounds[2],
                        max=local_state.point_cloud_arrow_for_face_cut.bounds[3],
                        step=0.1,
                        label="Y min->max",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        append_icon="mdi-alpha-y-circle-outline",
                        color="orange darken-2",
                        dense=False,
                    )

            # y_max
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=(
                            "clip_plane_y_max",
                            local_state.point_cloud_arrow_for_face_cut.bounds[3],
                        ),
                        min=local_state.point_cloud_arrow_for_face_cut.bounds[2],
                        max=local_state.point_cloud_arrow_for_face_cut.bounds[3],
                        step=0.1,
                        label="Y max->min",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        append_icon="mdi-alpha-y-circle",
                        color="orange darken-2",
                        dense=False,
                    )

            # z_min
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=(
                            "clip_plane_z_min",
                            local_state.point_cloud_arrow_for_face_cut.bounds[4],
                        ),
                        min=local_state.point_cloud_arrow_for_face_cut.bounds[4],
                        max=local_state.point_cloud_arrow_for_face_cut.bounds[5],
                        step=0.1,
                        label="Z min->max",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        append_icon="mdi-alpha-z-circle-outline",
                        color="orange darken-2",
                        dense=False,
                    )

            # z_max
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=(
                            "clip_plane_z_max",
                            local_state.point_cloud_arrow_for_face_cut.bounds[5],
                        ),
                        min=local_state.point_cloud_arrow_for_face_cut.bounds[4],
                        max=local_state.point_cloud_arrow_for_face_cut.bounds[5],
                        step=0.1,
                        label="Z max->min",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        append_icon="mdi-alpha-z-circle",
                        color="orange darken-2",
                        dense=False,
                    )

            # free normal clip min
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Free clip 1: "):
                with vuetify.VRow(dense=True):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=(
                                "dataset_clip_plane_free_normal_1_x",
                                pyvista_LR.dataset_clip_plane_free_normal_1[0],
                            ),
                            solo=True,
                            # rounded =True,
                        )
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=(
                                "dataset_clip_plane_free_normal_1_y",
                                pyvista_LR.dataset_clip_plane_free_normal_1[1],
                            ),
                            solo=True,
                            # rounded =True,
                        )

                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=(
                                "dataset_clip_plane_free_normal_1_z",
                                pyvista_LR.dataset_clip_plane_free_normal_1[2],
                            ),
                            solo=True,
                            # rounded =True,
                            min_height=50,
                        )
                # free_min
                vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=("clip_plane_free_min", 0),
                            min=0,
                            max=1000,
                            step=0.1,
                            label="User's min->max",
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-alpha-u-circle-outline",
                            color="orange darken-2",
                            dense=False,
                        )

            # free normal clip max
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Free clip 2: "):
                with vuetify.VRow(dense=True):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=(
                                "dataset_clip_plane_free_normal_2_x",
                                pyvista_LR.dataset_clip_plane_free_normal_2[0],
                            ),
                            solo=True,
                            # rounded =True,
                        )
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=(
                                "dataset_clip_plane_free_normal_2_y",
                                pyvista_LR.dataset_clip_plane_free_normal_2[1],
                            ),
                            solo=True,
                            # rounded =True,
                        )

                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=(
                                "dataset_clip_plane_free_normal_2_z",
                                pyvista_LR.dataset_clip_plane_free_normal_2[2],
                            ),
                            solo=True,
                            # rounded =True,
                            min_height=50,
                        )
                # free_max
                # z_max
                vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=("clip_plane_free_max", 0),
                            min=0,
                            max=1000,
                            step=0.1,
                            label="User's max->min",
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-alpha-u-circle",
                            color="orange darken-2",
                            dense=False,
                        )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )

            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="2"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="7"):
                    vuetify.VSwitch(
                        label="Clip component",
                        v_model=("do_clip_component", pyvista_LR.do_clip_component),
                        items=("list_do_clip_component", [True, False]),
                        hide_details=True,
                        dense=False,
                        outlined=True,
                        classes="pt-1 ml-2",
                        append_icon="mdi-content-cut",
                        style=("max-width: 250px"),
                        color="orange darken-2",
                    )
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VRangeSlider(
                        v_model=(
                            "Cut_X",
                            [
                                pyvista_LR.x_compoment_filter_min,
                                pyvista_LR.x_compoment_filter_max,
                            ],
                        ),
                        min=-1,
                        max=1,
                        step=0.01,
                        thumb_label=True,
                        label="Clip X",
                        hide_details=False,
                        dense=True,
                        color="orange darken-2",
                    )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VRangeSlider(
                        v_model=(
                            "Cut_Y",
                            [
                                pyvista_LR.y_compoment_filter_min,
                                pyvista_LR.y_compoment_filter_max,
                            ],
                        ),
                        min=-1,
                        max=1,
                        step=0.01,
                        thumb_label=True,
                        label="Clip Y",
                        hide_details=False,
                        color="orange darken-2",
                        dense=True,
                    )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VRangeSlider(
                        v_model=(
                            "Cut_Z",
                            [
                                pyvista_LR.z_compoment_filter_min,
                                pyvista_LR.z_compoment_filter_max,
                            ],
                        ),
                        min=-1,
                        max=1,
                        step=0.01,
                        thumb_label=True,
                        label="Clip Z",
                        hide_details=False,
                        dense=True,
                        color="orange darken-2",
                    )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VRangeSlider(
                        v_model=(
                            "Cut_phi_glyph",
                            [
                                pyvista_LR.phi_compoment_filter_min,
                                pyvista_LR.phi_compoment_filter_max,
                            ],
                        ),
                        min=-180,
                        max=180,
                        step=1,
                        thumb_label=True,
                        label="Clip phi",
                        hide_details=False,
                        dense=True,
                        color="orange darken-2",
                    )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VRangeSlider(
                        v_model=(
                            "Cut_theta_glyph",
                            [
                                pyvista_LR.theta_compoment_filter_min,
                                pyvista_LR.theta_compoment_filter_max,
                            ],
                        ),
                        min=0,
                        max=180,
                        step=1,
                        thumb_label=True,
                        label="Clip theta",
                        hide_details=False,
                        dense=True,
                        color="orange darken-2",
                    )

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        with vuetify.VListGroup(
            color="orange darken-2", prepend_icon="mdi-alpha-w-circle-outline"
        ):
            with vuetify.Template(
                v_slot_activator=True,
            ):
                vuetify.VListItemTitle(
                    "Wrapper",
                    style="display: flex; align-items: center; justify-content: center",
                )

            ################
            # Shpere warpper
            ################
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="2"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="6"):
                    with vuetify.VCardText(f"Sphere wrapping:"):
                        with vuetify.VBtnToggle(
                            color="orange darken-2",
                            multiple=True,
                            split=True,
                            mandatory=False,
                            v_model=(
                                "view_mode_sp_warp",
                                local_state.do_warp_sphere_vbtn_light,
                            ),
                        ):
                            with vuetify.VBtn(
                                click=ctrl.do_sp_warp, value="sp_warp_0", large=True
                            ):
                                vuetify.VIcon("mdi-panorama-sphere-outline")
                            vuetify.VSpacer(style=("max-width: 20px; min-width: 20px"))
                            with vuetify.VBtn(
                                click=ctrl.sp_warp_kernel, value="sp_warp_1", large=True
                            ):
                                vuetify.VIcon("mdi-alpha-k")

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

            with vuetify.VCardText(f"Sphere wrapping kernel color:"):
                vuetify.VSelect(
                    v_model=("swk_c", "Gray"),
                    items=(
                        "list_swk_c",
                        [
                            "White",
                            "Yellow",
                            "Blue",
                            "Red",
                            "Green",
                            "Black",
                            "Brown",
                            "Azure",
                            "Ivory",
                            "Teal",
                            "Silver",
                            "Purple",
                            "Navy blue",
                            "Pea green",
                            "Gray",
                            "Orange",
                            "Maroon",
                            "Charcoal",
                            "Aquamarine",
                            "Coral",
                            "Fuchsia",
                            "Wheat",
                            "Lime",
                            "Crimson",
                            "Khaki",
                            "Hot pink",
                            "Magenta",
                            "Olden",
                            "Plum",
                            "Olive",
                            "Cyan",
                        ],
                    ),
                    prepend_icon=" mdi-palette",
                    hide_details=True,
                    dense=True,
                    # outlined=True,
                    color="orange darken-2",
                    solo=True,
                    # classes="pt-1 ml-2",
                )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=("warp_sphere_radius", local_state.warp_sphere_radius),
                        min=1,
                        max=50,
                        step=1,
                        label="Sphere radius",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        dense=False,
                        append_icon=" mdi-radius",
                        track_color="orange darken-2",
                        color="orange darken-2",
                    )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=("skw_ratio", local_state.warpped_sphere_kernel),
                        min=0.01,
                        max=1,
                        step=0.01,
                        label="Kernel ratio",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        dense=False,
                        append_icon=" mdi-diameter",
                        track_color="orange darken-2",
                        color="orange darken-2",
                    )
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )

            ##############
            # Rescale
            ##############
            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="3"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="7"):
                    vuetify.VSwitch(
                        label="Rescale",
                        v_model=(
                            "point_rescale",
                            pyvista_LR.do_glyph_simple_point_rescale,
                        ),
                        items=("list_point_rescale", [True, False]),
                        hide_details=True,
                        dense=False,
                        outlined=True,
                        classes="pt-1 ml-2",
                        append_icon="mdi-alphabet-piqad",
                        style=("max-width: 140px"),
                        color="orange darken-2",
                    )
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    with vuetify.VCardText(f"    Point rescale component:"):
                        with vuetify.VBtnToggle(
                            color="orange darken-2",
                            multiple=False,
                            split=True,
                            mandatory=True,
                            rounded=True,
                            v_model=(
                                "view_mode2",
                                "point_rescale_{}".format(
                                    pyvista_LR.rescale_simple_point_index
                                ),
                            ),
                        ):
                            with vuetify.VBtn(
                                click=ctrl.change_point_rescale_vbtn_value_0,
                                value="point_rescale_0",
                            ):
                                vuetify.VIcon("mdi-alpha-x")
                            with vuetify.VBtn(
                                click=ctrl.change_point_rescale_vbtn_value_1,
                                value="point_rescale_1",
                            ):
                                vuetify.VIcon("mdi-alpha-y")
                            with vuetify.VBtn(
                                click=ctrl.change_point_rescale_vbtn_value_2,
                                value="point_rescale_2",
                            ):
                                vuetify.VIcon("mdi-alpha-z")
                            with vuetify.VBtn(
                                click=ctrl.change_point_rescale_vbtn_value_3,
                                value="point_rescale_3",
                            ):
                                vuetify.VIcon("mdi-alpha-t")
                            with vuetify.VBtn(
                                click=ctrl.change_point_rescale_vbtn_value_4,
                                value="point_rescale_4",
                            ):
                                vuetify.VIcon("mdi-alpha-p")

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=(
                            "point_rescale_factor",
                            pyvista_LR.rescale_simple_point_factor,
                        ),
                        min=0.1,
                        max=30,
                        step=0.1,
                        label="Rescale Factor",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        append_icon="mdi-cosine-wave",
                        color="orange darken-2",
                        dense=False,
                    )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

            with vuetify.VRow(dense=True):
                # ___________________________
                # point rescale norm x
                # ___________________________
                with vuetify.VCol(cols="3"):
                    vuetify.VTextField(
                        v_model=(
                            "point_rescale_norm_x",
                            pyvista_LR.rescale_simple_point_norm[0],
                        ),
                        solo=True,
                        # rounded =True,
                    )

                # ___________________________
                # point rescale norm x
                # ___________________________
                with vuetify.VCol(cols="3"):
                    vuetify.VTextField(
                        v_model=(
                            "point_rescale_norm_y",
                            pyvista_LR.rescale_simple_point_norm[1],
                        ),
                        solo=True,
                        # rounded =True,
                    )

                # ___________________________
                # point rescale norm x
                # ___________________________
                with vuetify.VCol(cols="3"):
                    vuetify.VTextField(
                        v_model=(
                            "point_rescale_norm_z",
                            pyvista_LR.rescale_simple_point_norm[2],
                        ),
                        solo=True,
                        # rounded =True,
                        min_height=50,
                    )

                # ___________________________
                # Applied button
                # ___________________________
                with vuetify.VCol(cols="3"):
                    vuetify.VBtn(
                        "Apply",
                        color="orange darken-2",
                        rounded=True,
                        large=True,
                        click=ctrl.applied_point_rescale_norm,
                    )
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        vuetify.VDivider(
            vertical=False,
            inset=False,
            style=("max-width: 390; min-height: 390;max-height: 20px"),
        )
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

        # ___________________________
        # Point List Group
        # ___________________________
        with vuetify.VListGroup(color="orange darken-2"):
            with vuetify.Template(
                v_slot_activator=True,
            ):
                vuetify.VListItemTitle("Point", classes="")
                # ___________________________
                # point activation
                # ___________________________
            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                vuetify.VSpacer(style=("max-width: 20px; min-width: 20px"))
                with vuetify.VRow(
                    classes="pt-3",
                    dense=False,
                ):
                    with vuetify.VCol(cols="4"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="3"):
                        spinview_checkbox(
                            model=("activate_point", pyvista_LR.add_simple_point),
                            on_icon=" mdi-square-medium",
                            off_icon=" mdi-square-medium-outline",
                            label="Point",
                            color_in="orange darken-2",
                            # tooltip='Activate/Deactivate Cones',
                        )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Point Size:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=("point_size", pyvista_LR.simple_point_size),
                            min=1,
                            max=50,
                            step=1,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-magnify-plus",
                            color="orange darken-2",
                            dense=False,
                        )

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        vuetify.VDivider(
            vertical=False,
            inset=False,
            style=("max-width: 390; min-height: 390;max-height: 20px"),
        )
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        # ___________________________
        # Cone List Group
        # ___________________________

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        with vuetify.VListGroup(color="orange darken-2"):
            with vuetify.Template(v_slot_activator=True):
                vuetify.VListItemTitle("Cone", classes="")
                # ___________________________
                # Cones activation
                # ___________________________

            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="4"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="3"):
                    spinview_checkbox(
                        model=("activate_cone", True),
                        on_icon="mdi-cone",
                        off_icon="mdi-cone-off",
                        label="Cone",
                        color_in="orange darken-2",
                        # tooltip='Activate/Deactivate Cones',
                    )
                with vuetify.VCol(cols="3"):
                    vuetify.VSpacer()

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

            with vuetify.VCardText("Cone center shift:"):
                with vuetify.VRow(dense=True):
                    # Cone C_x
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=("cone_center_x", pyvista_LR.Cone_center[0]),
                            solo=True,
                            # rounded =True,
                        )
                    # Cone C_y
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=("cone_center_y", pyvista_LR.Cone_center[1]),
                            solo=True,
                            # rounded =True,
                        )

                    # Cone C_z
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=("cone_center_z", pyvista_LR.Cone_center[2]),
                            solo=True,
                            # rounded =True,
                            min_height=50,
                        )
                    # Applied button
                    with vuetify.VCol(cols="3"):
                        vuetify.VBtn(
                            "Apply",
                            color="orange darken-2",
                            rounded=True,
                            large=True,
                            click=ctrl.applied_point_rescale_norm,
                        )

                vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
                vuetify.VDivider(
                    vertical=False,
                    inset=False,
                    style=("max-width: 390; min-height: 390;max-height: 20px"),
                )
                vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

                with vuetify.VCardText("Physically Based Rendering:"):
                    with vuetify.VRow(
                        classes="pt-3",
                        dense=False,
                    ):
                        with vuetify.VCol(cols="4"):
                            vuetify.VSpacer()
                        with vuetify.VCol(cols="6"):
                            vuetify.VSwitch(
                                v_model=("pbr", pyvista_LR.pbr),
                                items=("list_pbr", [True, False]),
                                hide_details=True,
                                dense=False,
                                outlined=True,
                                classes="pt-1 ml-2",
                                style=("max-width: 140px"),
                                color="orange darken-2",
                            )
                        with vuetify.VCol(cols="1"):
                            vuetify.VSpacer()
                with vuetify.VCardText("Metallic:"):
                    with vuetify.VRow(classes="pt-3", dense=False):
                        with vuetify.VCol(cols="1"):
                            vuetify.VSpacer()
                        with vuetify.VCol(cols="9"):
                            vuetify.VSlider(
                                v_model=("metallic", pyvista_LR.metallic_record),
                                min=0,
                                max=1,
                                step=0.01,
                                # classes="mt-1",
                                thumb_label=True,
                                hide_details=False,
                                append_icon="mdi-gold",
                                color="orange darken-2",
                                dense=False,
                            )
                with vuetify.VCardText("Roughness:"):
                    with vuetify.VRow(classes="pt-3", dense=False):
                        with vuetify.VCol(cols="1"):
                            vuetify.VSpacer()
                        with vuetify.VCol(cols="9"):
                            vuetify.VSlider(
                                v_model=("roughness", pyvista_LR.roughness_record),
                                min=0,
                                max=1,
                                step=0.01,
                                # classes="mt-1",
                                thumb_label=True,
                                hide_details=False,
                                dense=False,
                                append_icon="mdi-square-opacity",
                                color="orange darken-2",
                            )
                vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
                vuetify.VDivider(
                    vertical=False,
                    inset=False,
                    style=("max-width: 390; min-height: 390;max-height: 20px"),
                )
                vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

                with vuetify.VCardText("Properties:"):
                    with vuetify.VCardText("Ratio:"):
                        with vuetify.VRow(classes="pt-3", dense=False):
                            with vuetify.VCol(cols="1"):
                                vuetify.VSpacer()
                            with vuetify.VCol(cols="9"):
                                vuetify.VSlider(
                                    v_model=("Ratio", pyvista_LR.Ratio_record),
                                    min=0.01,
                                    max=10,
                                    step=0.01,
                                    # classes="mt-1",
                                    thumb_label=True,
                                    hide_details=False,
                                    append_icon="mdi-magnify-plus",
                                    color="orange darken-2",
                                    dense=True,
                                )
                    vuetify.VDivider(
                        vertical=False,
                        inset=False,
                        style=("max-width: 390; min-height: 390;max-height: 20px"),
                    )
                    with vuetify.VCardText("Resolutions:"):
                        with vuetify.VRow(classes="pt-3", dense=False):
                            with vuetify.VCol(cols="1"):
                                vuetify.VSpacer()
                            with vuetify.VCol(cols="9"):
                                vuetify.VSlider(
                                    v_model=("resolutions", pyvista_LR.resolutions),
                                    min=1,
                                    max=40,
                                    step=1,
                                    # classes="mt-1",
                                    thumb_label=True,
                                    hide_details=False,
                                    append_icon="mdi-dots-grid",
                                    color="orange darken-2",
                                    dense=True,
                                )

                    vuetify.VDivider(
                        vertical=False,
                        inset=False,
                        style=("max-width: 390; min-height: 390;max-height: 20px"),
                    )
                    with vuetify.VCardText("Cone highth:"):
                        with vuetify.VRow(classes="pt-3", dense=False):
                            with vuetify.VCol(cols="1"):
                                vuetify.VSpacer()
                            with vuetify.VCol(cols="9"):
                                vuetify.VSlider(
                                    v_model=(
                                        "cone_highth",
                                        pyvista_LR.cone_highth_record,
                                    ),
                                    min=0,
                                    max=5,
                                    step=0.01,
                                    # classes="mt-1",
                                    thumb_label=True,
                                    hide_details=False,
                                    append_icon="mdi-pencil-ruler",
                                    color="orange darken-2",
                                    dense=True,
                                )

                    vuetify.VDivider(
                        vertical=False,
                        inset=False,
                        style=("max-width: 390; min-height: 390;max-height: 20px"),
                    )
                    with vuetify.VCardText("Cone radius:"):
                        with vuetify.VRow(classes="pt-3", dense=False):
                            with vuetify.VCol(cols="1"):
                                vuetify.VSpacer()
                            with vuetify.VCol(cols="9"):
                                vuetify.VSlider(
                                    # Opacity
                                    v_model=(
                                        "cone_Radius",
                                        pyvista_LR.cone_Radius_record,
                                    ),
                                    min=0,
                                    max=5,
                                    step=0.01,
                                    # classes="mt-1",
                                    thumb_label=True,
                                    hide_details=False,
                                    append_icon=" mdi-ruler-square-compass",
                                    color="orange darken-2",
                                    dense=True,
                                )
                vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
                vuetify.VDivider(
                    vertical=False,
                    inset=False,
                    style=("max-width: 390; min-height: 390;max-height: 20px"),
                )
                vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
                with vuetify.VCardText("Alloy rendering:"):
                    with vuetify.VRow(
                        classes="pt-3",
                        dense=False,
                    ):
                        with vuetify.VCol(cols="4"):
                            vuetify.VSpacer()
                        with vuetify.VCol(cols="6"):
                            vuetify.VSwitch(
                                v_model=("do_scale_cone", pyvista_LR.do_scale_cone),
                                items=("list_do_scale_cone", [True, False]),
                                hide_details=True,
                                dense=False,
                                outlined=True,
                                classes="pt-1 ml-2",
                                style=("max-width: 140px"),
                                color="orange darken-2",
                            )
                        with vuetify.VCol(cols="1"):
                            vuetify.VSpacer()

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        vuetify.VDivider(
            vertical=False,
            inset=False,
            style=("max-width: 390; min-height: 390;max-height: 20px"),
        )
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

        # ___________________________
        # Arrows activation
        # ___________________________
        with vuetify.VListGroup(color="orange darken-2"):
            with vuetify.Template(
                v_slot_activator=True,
            ):
                vuetify.VListItemTitle("Arrow", classes="")
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="4"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="3"):
                    spinview_checkbox(
                        model=("activate_arrow", pyvista_LR.add_arrow),
                        on_icon="mdi-arrow-up-bold",
                        off_icon="mdi-arrow-up-bold-outline",
                        label="Arrow",
                        color_in="orange darken-2",
                        # tooltip='Activate/Deactivate Arrows'
                    )
                with vuetify.VCol(cols="3"):
                    vuetify.VSpacer()
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Cone center shift:"):
                with vuetify.VRow(dense=True):
                    # arrow a_x
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=("arrow_start_x", pyvista_LR.start_arrow[0]),
                            solo=True,
                            # rounded =True,
                        )
                    # arrow a_y
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=("arrow_start_y", pyvista_LR.start_arrow[1]),
                            solo=True,
                            # rounded =True,
                        )

                    # arrow a_z
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=("arrow_start_z", pyvista_LR.start_arrow[2]),
                            solo=True,
                            # rounded =True,
                            min_height=50,
                        )
                    # Applied button
                    with vuetify.VCol(cols="3"):
                        vuetify.VBtn(
                            "Apply",
                            color="orange darken-2",
                            rounded=True,
                            large=True,
                            click=ctrl.applied_point_rescale_norm,
                        )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

            with vuetify.VCardText("Physically Based Rendering:"):
                with vuetify.VRow(
                    classes="pt-3",
                    dense=False,
                ):
                    with vuetify.VCol(cols="4"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="6"):
                        vuetify.VSwitch(
                            v_model=("pbr_arrow", pyvista_LR.pbr_arrow),
                            items=("list_pbr_arrow", [True, False]),
                            hide_details=True,
                            dense=False,
                            outlined=True,
                            classes="pt-1 ml-2",
                            style=("max-width: 140px"),
                            color="orange darken-2",
                        )
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Metallic:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=("metallic_arrow", pyvista_LR.metallic_arrow),
                            min=0,
                            max=1,
                            step=0.01,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-gold",
                            color="orange darken-2",
                            dense=False,
                        )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Roughness:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=("roughness_arrow", pyvista_LR.roughness_arrow),
                            min=0,
                            max=1,
                            step=0.01,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            dense=False,
                            append_icon="mdi-square-opacity",
                            color="orange darken-2",
                        )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Properties:"):
                with vuetify.VCardText("Ratio:"):
                    with vuetify.VRow(classes="pt-3", dense=False):
                        with vuetify.VCol(cols="1"):
                            vuetify.VSpacer()
                        with vuetify.VCol(cols="9"):
                            vuetify.VSlider(
                                v_model=(
                                    "Ratio_record_arrow",
                                    pyvista_LR.Ratio_record_arrow,
                                ),
                                min=0.01,
                                max=10,
                                step=0.01,
                                # classes="mt-1",
                                thumb_label=True,
                                hide_details=False,
                                append_icon="mdi-magnify-plus",
                                color="orange darken-2",
                                dense=True,
                            )

                vuetify.VDivider(
                    vertical=False,
                    inset=False,
                    style=("max-width: 390; min-height: 390;max-height: 20px"),
                )
                # with vuetify.VCardText("Tip lenth:"):
                #     with vuetify.VRow(classes="pt-3", dense=False):
                #         with vuetify.VCol(cols="1"):
                #             vuetify.VSpacer()
                #         with vuetify.VCol(cols="9"):
                #             vuetify.VSlider(
                #                 v_model=(
                #                     "tip_length_arrow",
                #                     pyvista_LR.tip_length_arrow,
                #                 ),
                #                 min=0,
                #                 max=10,
                #                 step=0.01,
                #                 # classes="mt-1",
                #                 thumb_label=True,
                #                 hide_details=False,
                #                 append_icon="mdi-pencil-ruler",
                #                 color="orange darken-2",
                #                 dense=True,
                #             )

                # vuetify.VDivider(
                #     vertical=False,
                #     inset=False,
                #     style=("max-width: 390; min-height: 390;max-height: 20px"),
                # )
                with vuetify.VCardText("Tip radius:"):
                    with vuetify.VRow(classes="pt-3", dense=False):
                        with vuetify.VCol(cols="1"):
                            vuetify.VSpacer()
                        with vuetify.VCol(cols="9"):
                            vuetify.VSlider(
                                v_model=(
                                    "tip_radius_arrow",
                                    pyvista_LR.tip_radius_arrow,
                                ),
                                min=0,
                                max=4,
                                step=0.01,
                                # classes="mt-1",
                                thumb_label=True,
                                hide_details=False,
                                append_icon="mdi-math-compass",
                                color="orange darken-2",
                                dense=True,
                            )
                vuetify.VDivider(
                    vertical=False,
                    inset=False,
                    style=("max-width: 390; min-height: 390;max-height: 20px"),
                )
                with vuetify.VCardText("Tip resolution:"):
                    with vuetify.VRow(classes="pt-3", dense=False):
                        with vuetify.VCol(cols="1"):
                            vuetify.VSpacer()
                        with vuetify.VCol(cols="9"):
                            vuetify.VSlider(
                                v_model=(
                                    "tip_resolution_arrow",
                                    pyvista_LR.tip_resolution_arrow,
                                ),
                                min=0,
                                max=40,
                                step=1,
                                # classes="mt-1",
                                thumb_label=True,
                                hide_details=False,
                                append_icon="mdi-dots-grid",
                                color="orange darken-2",
                                dense=True,
                            )

                vuetify.VDivider(
                    vertical=False,
                    inset=False,
                    style=("max-width: 390; min-height: 390;max-height: 20px"),
                )
                with vuetify.VCardText("Shaft radius:"):
                    with vuetify.VRow(classes="pt-3", dense=False):
                        with vuetify.VCol(cols="1"):
                            vuetify.VSpacer()
                        with vuetify.VCol(cols="9"):
                            vuetify.VSlider(
                                v_model=(
                                    "shaft_radius_arrow",
                                    pyvista_LR.shaft_radius_arrow,
                                ),
                                min=0,
                                max=4,
                                step=0.01,
                                # classes="mt-1",
                                thumb_label=True,
                                hide_details=False,
                                append_icon="mdi-ruler-square-compass",
                                color="orange darken-2",
                                dense=True,
                            )

                vuetify.VDivider(
                    vertical=False,
                    inset=False,
                    style=("max-width: 390; min-height: 390;max-height: 20px"),
                )
                with vuetify.VCardText("Shaft resolution:"):
                    with vuetify.VRow(classes="pt-3", dense=False):
                        with vuetify.VCol(cols="1"):
                            vuetify.VSpacer()
                        with vuetify.VCol(cols="9"):
                            vuetify.VSlider(
                                v_model=(
                                    "shaft_resolution_arrow",
                                    pyvista_LR.shaft_resolution_arrow,
                                ),
                                min=0,
                                max=40,
                                step=1,
                                # classes="mt-1",
                                thumb_label=True,
                                hide_details=False,
                                append_icon="mdi-dots-circle",
                                color="orange darken-2",
                                dense=True,
                            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Alloy rendering:"):
                with vuetify.VRow(
                    classes="pt-3",
                    dense=False,
                ):
                    with vuetify.VCol(cols="4"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="6"):
                        vuetify.VSwitch(
                            v_model=("do_scale_arrow", pyvista_LR.do_scale_arrow),
                            items=("list_do_scale_arrow", [True, False]),
                            hide_details=True,
                            dense=False,
                            outlined=True,
                            classes="pt-1 ml-2",
                            validate_on_blur=True,
                            style=("max-width: 140px"),
                            color="orange darken-2",
                        )
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        vuetify.VDivider(
            vertical=False,
            inset=False,
            style=("max-width: 390; min-height: 390;max-height: 20px"),
        )
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

        # ___________________________
        # box  activation
        # ___________________________
        with vuetify.VListGroup(color="orange darken-2"):
            with vuetify.Template(
                v_slot_activator=True,
            ):
                vuetify.VListItemTitle("Box", classes="")

            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="4"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="3"):
                    spinview_checkbox(
                        model=("activate_box", pyvista_LR.add_box),
                        on_icon="mdi-cube",
                        off_icon="mdi-cube-off",
                        label="Box",
                        color_in="orange darken-2",
                    )
                with vuetify.VCol(cols="3"):
                    vuetify.VSpacer()

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

            with vuetify.VCardText("Physically Based Rendering:"):
                with vuetify.VRow(
                    classes="pt-3",
                    dense=False,
                ):
                    with vuetify.VCol(cols="3"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="6"):
                        vuetify.VSwitch(
                            v_model=("pbr_box", pyvista_LR.pbr_box),
                            items=("list_pbr_box", [True, False]),
                            hide_details=True,
                            dense=False,
                            outlined=True,
                            classes="pt-1 ml-2",
                            style=("max-width: 140px"),
                            color="orange darken-2",
                        )
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()

            with vuetify.VCardText("Metallic:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=("metallic_box", pyvista_LR.metallic_box),
                            min=0,
                            max=1,
                            step=0.01,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-gold",
                            color="orange darken-2",
                            dense=False,
                        )
            with vuetify.VCardText("Roughness:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=("roughness_box", pyvista_LR.roughness_box),
                            min=0,
                            max=1,
                            step=0.01,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            dense=False,
                            append_icon="mdi-square-opacity",
                            color="orange darken-2",
                        )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Properties:"):
                with vuetify.VCardText("Ratio:"):
                    with vuetify.VRow(classes="pt-3", dense=False):
                        with vuetify.VCol(cols="1"):
                            vuetify.VSpacer()
                        with vuetify.VCol(cols="9"):
                            vuetify.VSlider(
                                v_model=(
                                    "Ratio_record_box",
                                    pyvista_LR.Ratio_record_box,
                                ),
                                min=0.01,
                                max=10,
                                step=0.01,
                                label="Ratio",
                                # classes="mt-1",
                                thumb_label=True,
                                hide_details=False,
                                append_icon="mdi-magnify-plus",
                                color="orange darken-2",
                                dense=True,
                            )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Alloy rendering:"):
                with vuetify.VRow(
                    classes="pt-3",
                    dense=False,
                ):
                    with vuetify.VCol(cols="3"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="6"):
                        vuetify.VSwitch(
                            v_model=("do_scale_box", pyvista_LR.do_scale_box),
                            items=("list_do_scale_box", [True, False]),
                            hide_details=True,
                            dense=False,
                            outlined=True,
                            style=("max-width: 140px"),
                            color="orange darken-2",
                        )
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        vuetify.VDivider(
            vertical=False,
            inset=False,
            style=("max-width: 390; min-height: 390;max-height: 20px"),
        )
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

        # ___________________________
        # Sphere activation
        # ___________________________

        with vuetify.VListGroup(color="orange darken-2"):
            with vuetify.Template(
                v_slot_activator=True,
            ):
                vuetify.VListItemTitle("Sphere", classes="")

            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="4"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="3"):
                    spinview_checkbox(
                        model=("activate_sphere", pyvista_LR.add_sphere),
                        on_icon="mdi-sphere",
                        off_icon="mdi-sphere-off",
                        label="Sphere",
                        color_in="orange darken-2",
                        tooltip="Time consiming",
                    )
                with vuetify.VCol(cols="3"):
                    vuetify.VSpacer()
            vuetify.VSpacer(style=("max-height: 30px; min-height: 30px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )

            with vuetify.VCardText("Physically Based Rendering:"):
                with vuetify.VRow(
                    classes="pt-3",
                    dense=False,
                ):
                    with vuetify.VCol(cols="4"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="6"):
                        vuetify.VSwitch(
                            v_model=("pbr_sphere", pyvista_LR.pbr_sphere),
                            items=("list_pbr_sphere", [True, False]),
                            hide_details=True,
                            dense=False,
                            outlined=True,
                            classes="pt-1 ml-2",
                            style=("max-width: 140px"),
                            color="orange darken-2",
                        )
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()

            with vuetify.VCardText("Metallic:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=("metallic_sphere", pyvista_LR.metallic_sphere),
                            min=0,
                            max=1,
                            step=0.01,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-gold",
                            color="orange darken-2",
                            dense=False,
                        )
            with vuetify.VCardText("Roughness:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=("roughness_sphere", pyvista_LR.roughness_sphere),
                            min=0,
                            max=1,
                            step=0.01,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            dense=False,
                            append_icon="mdi-square-opacity",
                            color="orange darken-2",
                        )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Properties:"):
                with vuetify.VCardText("Ratio:"):
                    with vuetify.VRow(classes="pt-3", dense=False):
                        with vuetify.VCol(cols="1"):
                            vuetify.VSpacer()
                        with vuetify.VCol(cols="9"):
                            vuetify.VSlider(
                                v_model=(
                                    "Ratio_record_sphere",
                                    pyvista_LR.Ratio_record_sphere,
                                ),
                                min=0.01,
                                max=10,
                                step=0.01,
                                # classes="mt-1",
                                thumb_label=True,
                                hide_details=False,
                                append_icon="mdi-magnify-plus",
                                color="orange darken-2",
                                dense=True,
                            )

            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            with vuetify.VCardText("Radius:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=("radius_sphere", pyvista_LR.radius_sphere),
                            min=0,
                            max=10,
                            step=0.01,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-math-compass",
                            color="orange darken-2",
                            dense=True,
                        )
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            with vuetify.VCardText("Theta resolution:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=(
                                "theta_resolution_sphere",
                                pyvista_LR.theta_resolution_sphere,
                            ),
                            min=0,
                            max=40,
                            step=1,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-dots-circle",
                            color="orange darken-2",
                            dense=True,
                        )
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            with vuetify.VCardText("Phi resolution:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=(
                                "phi_resolution_sphere",
                                pyvista_LR.phi_resolution_sphere,
                            ),
                            min=0,
                            max=40,
                            step=1,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-dots-hexagon",
                            color="orange darken-2",
                            dense=True,
                        )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Alloy rendering:"):
                with vuetify.VRow(
                    classes="pt-3",
                    dense=False,
                ):
                    with vuetify.VCol(cols="4"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="6"):
                        vuetify.VSwitch(
                            v_model=("do_scale_sphere", pyvista_LR.do_scale_sphere),
                            items=("list_do_scale_sphere", [True, False]),
                            hide_details=True,
                            dense=False,
                            outlined=True,
                            classes="pt-1 ml-2",
                            style=("max-width: 140px"),
                            color="orange darken-2",
                        )
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        vuetify.VDivider(
            vertical=False,
            inset=False,
            style=("max-width: 390; min-height: 390;max-height: 20px"),
        )
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

        # ___________________________
        # plane activation
        # ___________________________
        with vuetify.VListGroup(color="orange darken-2"):
            with vuetify.Template(
                v_slot_activator=True,
            ):
                vuetify.VListItemTitle("Plane", classes="")

            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="4"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="3"):
                    spinview_checkbox(
                        model=("activate_plane", pyvista_LR.add_plane),
                        on_icon="mdi-square",
                        off_icon="mdi-square-off-outline",
                        label="Plane",
                        color_in="orange darken-2",
                        # tooltip='Activate/Deactivate Plane'
                    )
                with vuetify.VCol(cols="3"):
                    vuetify.VSpacer()

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="4"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="6"):
                    vuetify.VSwitch(
                        v_model=("pbr_plane", pyvista_LR.pbr_plane),
                        items=("list_pbr_plane", [True, False]),
                        hide_details=True,
                        dense=False,
                        outlined=True,
                        classes="pt-1 ml-2",
                        style=("max-width: 140px"),
                        color="orange darken-2",
                    )
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Metallic:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=("metallic_plane", pyvista_LR.metallic_plane),
                            min=0,
                            max=1,
                            step=0.01,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-gold",
                            color="orange darken-2",
                            dense=False,
                        )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Roughness:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=("roughness_plane", pyvista_LR.roughness_plane),
                            min=0,
                            max=1,
                            step=0.01,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            dense=False,
                            append_icon="mdi-square-opacity",
                            color="orange darken-2",
                        )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Properties:"):
                with vuetify.VCardText("Ratio:"):
                    with vuetify.VRow(classes="pt-3", dense=False):
                        with vuetify.VCol(cols="1"):
                            vuetify.VSpacer()
                        with vuetify.VCol(cols="9"):
                            vuetify.VSlider(
                                v_model=(
                                    "Ratio_record_plane",
                                    pyvista_LR.Ratio_record_plane,
                                ),
                                min=0.01,
                                max=10,
                                step=0.01,
                                # classes="mt-1",
                                thumb_label=True,
                                hide_details=False,
                                append_icon="mdi-magnify-plus",
                                color="orange darken-2",
                                dense=True,
                            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Alloy rendering:"):
                with vuetify.VRow(
                    classes="pt-3",
                    dense=False,
                ):
                    with vuetify.VCol(cols="4"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="6"):
                        vuetify.VSwitch(
                            v_model=("do_scale_plane", pyvista_LR.do_scale_plane),
                            items=("list_do_scale_plane", [True, False]),
                            hide_details=True,
                            dense=False,
                            outlined=True,
                            classes="pt-1 ml-2",
                            style=("max-width: 140px"),
                            color="orange darken-2",
                        )
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        vuetify.VDivider(
            vertical=False,
            inset=False,
            style=("max-width: 390; min-height: 390;max-height: 20px"),
        )
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

        # ___________________________
        # own_glyphs   activation
        # ___________________________
        with vuetify.VListGroup(color="orange darken-2"):
            with vuetify.Template(
                v_slot_activator=True,
            ):
                vuetify.VListItemTitle("User's glyph", classes="")
            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="4"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="3"):
                    spinview_checkbox(
                        model=("activate_own_glyphs", pyvista_LR.add_own_glyphs),
                        on_icon="mdi-emoticon-wink",
                        off_icon="mdi-emoticon-cool",
                        label="User's",
                        color_in="orange darken-2",
                        # tooltip='Validate your own glyphs'
                    )
                with vuetify.VCol(cols="3"):
                    vuetify.VSpacer()
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

            with vuetify.VCardText("Physically Based Rendering:"):
                with vuetify.VRow(
                    classes="pt-3",
                    dense=False,
                ):
                    with vuetify.VCol(cols="4"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="6"):
                        vuetify.VSwitch(
                            v_model=("pbr_own", pyvista_LR.pbr_own),
                            items=("list_pbr_own", [True, False]),
                            hide_details=True,
                            dense=False,
                            outlined=True,
                            classes="pt-1 ml-2",
                            style=("max-width: 140px"),
                            color="orange darken-2",
                        )
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Metallic:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=("metallic_own", pyvista_LR.metallic_own),
                            min=0,
                            max=1,
                            step=0.01,
                            label="Metallic_O",
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-gold",
                            color="orange darken-2",
                            dense=False,
                        )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Roughness:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=("roughness", pyvista_LR.roughness_own),
                            min=0,
                            max=1,
                            step=0.01,
                            label="Roughness",
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            dense=False,
                            append_icon="mdi-square-opacity",
                            color="orange darken-2",
                        )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            pyvista_LR.Ratio_record_own = 0.05
            with vuetify.VCardText("Properties:"):
                with vuetify.VCardText("Ratio:"):
                    with vuetify.VRow(classes="pt-3", dense=False):
                        with vuetify.VCol(cols="1"):
                            vuetify.VSpacer()
                        with vuetify.VCol(cols="9"):
                            vuetify.VSlider(
                                v_model=(
                                    "Ratio_record_own",
                                    pyvista_LR.Ratio_record_own,
                                ),
                                min=0.01,
                                max=10,
                                step=0.01,
                                label="Ratio",
                                # classes="mt-1",
                                thumb_label=True,
                                hide_details=False,
                                append_icon="mdi-magnify-plus",
                                color="orange darken-2",
                                dense=True,
                            )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Alloy rendering:"):
                with vuetify.VRow(
                    classes="pt-3",
                    dense=False,
                ):
                    with vuetify.VCol(cols="4"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="6"):
                        vuetify.VSwitch(
                            label="Alloy",
                            v_model=("do_scale_own", pyvista_LR.do_scale_own),
                            items=("list_do_scale_own", [True, False]),
                            hide_details=True,
                            dense=False,
                            outlined=True,
                            classes="pt-1 ml-2",
                            prepend_icon=" mdi-eye-off-outline",
                            append_icon="mdi-eye-outline",
                            style=("max-width: 140px"),
                            color="orange darken-2",
                        )
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
