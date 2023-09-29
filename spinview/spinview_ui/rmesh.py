from trame.widgets import vuetify


def rmesh_initialize(local_state, pyvista_LR, state, ctrl, spinview_checkbox, colors):
    with vuetify.VListGroup(color="lime darken-2", prepend_icon="mdi-square-outline"):
        vuetify.VCardText(
            "Rectangle mesh mainly works (for others try Tmesh) for homogeneous data, i.e., rectangular mesh in micromagnetic data, atomistic data with simple cubic lattice."
        )
        with vuetify.Template(v_slot_activator=True):
            vuetify.VListItemTitle(
                "Rectangle mesh",
                style="display: flex; align-items: center; justify-content: center",
            )

        with vuetify.VRow(
            classes="pt-3",
            dense=False,
        ):
            with vuetify.VCol(cols="3"):
                vuetify.VSpacer()
            with vuetify.VCol(cols="7"):
                spinview_checkbox(
                    model=("activate_rectangle_mesh", False),
                    on_icon="mdi-vector-square",
                    off_icon="mdi-vector-square-remove",
                    label="Rectangle mesh",
                    tooltip="Activate/Deactivate rectangle mesh",
                )
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        vuetify.VDivider(
            vertical=False,
            inset=False,
            style=("max-width: 390; min-height: 390;max-height: 20px"),
        )

        with vuetify.VRow(classes="pt-3", dense=False):
            with vuetify.VCol(cols="1"):
                vuetify.VSpacer()
            with vuetify.VCol(cols="9"):
                with vuetify.VCardText("    Rectangle mesh cmap component:"):
                    with vuetify.VBtnToggle(
                        color="lime darken-2",
                        multiple=False,
                        split=True,
                        mandatory=True,
                        value=local_state.rectangle_cmap_vbtn,
                        rounded=True,
                        v_model=(
                            "view_mode_rectang",
                            "rectangle_cmap{}".format(
                                pyvista_LR.rectrangle_color_index
                            ),
                        ),
                    ):
                        with vuetify.VBtn(
                            click=ctrl.change_rectangle_cmap_vbtn_value_0,
                            value="rectangle_cmap0",
                        ):
                            vuetify.VIcon("mdi-alpha-x")
                        with vuetify.VBtn(
                            click=ctrl.change_rectangle_cmap_vbtn_value_1,
                            value="rectangle_cmap1",
                        ):
                            vuetify.VIcon("mdi-alpha-y")
                        with vuetify.VBtn(
                            click=ctrl.change_rectangle_cmap_vbtn_value_2,
                            value="rectangle_cmap2",
                        ):
                            vuetify.VIcon("mdi-alpha-z")
                        with vuetify.VBtn(
                            click=ctrl.change_rectangle_cmap_vbtn_value_3,
                            value="rectangle_cmap3",
                        ):
                            vuetify.VIcon("mdi-alpha-t")
                        with vuetify.VBtn(
                            click=ctrl.change_rectangle_cmap_vbtn_value_4,
                            value="rectangle_cmap4",
                        ):
                            vuetify.VIcon("mdi-alpha-p")
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        vuetify.VDivider(
            vertical=False,
            inset=False,
            style=("max-width: 390; min-height: 390;max-height: 20px"),
        )
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

        with vuetify.VRow(classes="pt-3", dense=False):
            with vuetify.VCol(cols="10"):
                with vuetify.VCardText("    Rectangle mesh opacity component:"):
                    with vuetify.VBtnToggle(
                        tag="sss",
                        color="lime darken-2",
                        multiple=False,
                        split=True,
                        mandatory=True,
                        value=local_state.rectangle_opaciy_vbtn,
                        rounded=True,
                        dense=True,
                        v_model=(
                            "view_mode_Rectangle_op",
                            "Rectangle_opacity{}".format(pyvista_LR.opacity_index),
                        ),
                    ):
                        with vuetify.VBtn(
                            click=ctrl.change_rectangle_opacity_index_vbtn_value_0,
                            value="Rectangle_opacity0",
                        ):
                            vuetify.VIcon("mdi-alpha-x")
                        with vuetify.VBtn(
                            click=ctrl.change_rectangle_opacity_index_vbtn_value_1,
                            value="Rectangle_opacity1",
                        ):
                            vuetify.VIcon("mdi-alpha-y")
                        with vuetify.VBtn(
                            click=ctrl.change_rectangle_opacity_index_vbtn_value_2,
                            value="Rectangle_opacity2",
                        ):
                            vuetify.VIcon("mdi-alpha-z")
                        with vuetify.VBtn(
                            click=ctrl.change_rectangle_opacity_index_vbtn_value_3,
                            value="Rectangle_opacity3",
                        ):
                            vuetify.VIcon("mdi-alpha-t")
                        with vuetify.VBtn(
                            click=ctrl.change_rectangle_opacity_index_vbtn_value_4,
                            value="Rectangle_opacity4",
                        ):
                            vuetify.VIcon("mdi-alpha-t-box")
                        with vuetify.VBtn(
                            click=ctrl.change_rectangle_opacity_index_vbtn_value_5,
                            value="Rectangle_opacity5",
                        ):
                            vuetify.VIcon("mdi-alpha-p")
                        with vuetify.VBtn(
                            click=ctrl.change_rectangle_opacity_index_vbtn_value_6,
                            value="Rectangle_opacity6",
                        ):
                            vuetify.VIcon(" mdi-account-details")

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        with vuetify.VCardText("Opacity:"):
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=(
                            "opacity_record_rectangle_mesh",
                            local_state.opacity_record_rectangle_mesh,
                        ),
                        min=0,
                        max=1,
                        step=0.01,
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        dense=False,
                        append_icon="mdi-water-opacity",
                        track_color="lime darken-2",
                        color="lime darken-2",
                    )

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

        with vuetify.VCardText("OpenGL interpolate:"):
            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="4"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="6"):
                    vuetify.VSwitch(
                        v_model=(
                            "rectangle_mesh_interpolate_before_map",
                            pyvista_LR.rectangle_mesh_interpolate_before_map,
                        ),
                        items=(
                            "list_rectangle_mesh_interpolate_before_map",
                            [True, False],
                        ),
                        hide_details=True,
                        dense=False,
                        outlined=True,
                        classes="pt-1 ml-2",
                        style=("max-width: 140px"),
                        color="lime darken-2",
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

        with vuetify.VCardText("Physically Based Rendering:"):
            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="4"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="6"):
                    vuetify.VSwitch(
                        v_model=("pbr_rectangle", pyvista_LR.pbr_rectangle),
                        items=("list_pbr_rectangle", [True, False]),
                        hide_details=True,
                        dense=False,
                        outlined=True,
                        classes="pt-1 ml-2",
                        style=("max-width: 140px"),
                        color="lime darken-2",
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
                        v_model=("metallic_rmesh", local_state.metallic_rmesh),
                        min=0,
                        max=1,
                        step=0.01,
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        append_icon="mdi-gold",
                        color="lime darken-2",
                        dense=False,
                    )
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        with vuetify.VCardText("Roughness:"):
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=("roughness_rmesh", local_state.roughness_rmesh),
                        min=0,
                        max=1,
                        step=0.01,
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        dense=False,
                        append_icon="mdi-square-opacity",
                        color="lime darken-2",
                    )

        vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
        vuetify.VDivider(
            vertical=False,
            inset=False,
            style=("max-width: 390; min-height: 390;max-height: 20px"),
        )
        vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
        with vuetify.VListGroup(
            color="lime darken-2", prepend_icon="mdi-alpha-c-circle-outline"
        ):
            with vuetify.Template(
                v_slot_activator=True,
            ):
                vuetify.VListItemTitle(
                    "Contour filters",
                    style="display: flex; align-items: center; justify-content: center",
                )
            with vuetify.VCardText("Contour:"):
                with vuetify.VRow(
                    classes="pt-3",
                    dense=False,
                ):
                    with vuetify.VCol(cols="4"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="6"):
                        vuetify.VSwitch(
                            v_model=(
                                "do_rectangle_mesh_contour",
                                pyvista_LR.do_rectangle_mesh_contour,
                            ),
                            items=("list_do_rectangle_mesh_contour", [True, False]),
                            hide_details=True,
                            dense=False,
                            outlined=True,
                            classes="pt-1 ml-2",
                            style=("max-width: 140px"),
                            color="lime darken-2",
                        )
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

            with vuetify.VCardText("Multi contour:"):
                with vuetify.VRow(
                    classes="pt-3",
                    dense=False,
                ):
                    with vuetify.VCol(cols="4"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="6"):
                        vuetify.VSwitch(
                            v_model=(
                                "do_multi_rectangle_surface_contour",
                                pyvista_LR.do_multi_rectangle_surface_contour,
                            ),
                            items=("list_do_scale_own", [True, False]),
                            hide_details=True,
                            dense=False,
                            outlined=True,
                            classes="pt-1 ml-2",
                            style=("max-width: 140px"),
                            color="lime darken-2",
                        )
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()

            with vuetify.VCardText("Contour numbers:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=(
                                "rectangle_mesh_contour_isosurface_number",
                                pyvista_LR.rectangle_mesh_contour_isosurface_number,
                            ),
                            min=0,
                            max=40,
                            step=1,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-nativescript",
                            color="lime darken-2",
                            dense=True,
                        )
                vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            with vuetify.VCardText("Contour component:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="7"):
                        with vuetify.VBtnToggle(
                            color="lime darken-2",
                            multiple=False,
                            split=True,
                            dense=True,
                            mandatory=False,
                            v_model=(
                                "Contour_i",
                                "Contour_{}".format(
                                    pyvista_LR.rectangle_mesh_contour_method_indicator
                                ),
                            ),
                        ):
                            with vuetify.VBtn(
                                click=ctrl.Contour_0, value="Contour_0", large=False
                            ):
                                vuetify.VIcon("mdi-alpha-x")
                            vuetify.VSpacer(style=("max-width: 20px; min-width: 20px"))
                            with vuetify.VBtn(
                                click=ctrl.Contour_1, value="Contour_1", large=False
                            ):
                                vuetify.VIcon("mdi-alpha-y")
                            vuetify.VSpacer(style=("max-width: 20px; min-width: 20px"))
                            with vuetify.VBtn(
                                click=ctrl.Contour_2, value="Contour_2", large=False
                            ):
                                vuetify.VIcon("mdi-alpha-z")
                            vuetify.VSpacer(style=("max-width: 20px; min-width: 20px"))
                            with vuetify.VBtn(
                                click=ctrl.Contour_3, value="Contour_3", large=False
                            ):
                                vuetify.VIcon("mdi-alpha-t")
                            vuetify.VSpacer(style=("max-width: 20px; min-width: 20px"))
                            with vuetify.VBtn(
                                click=ctrl.Contour_4, value="Contour_4", large=False
                            ):
                                vuetify.VIcon("mdi-alpha-p")

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Contour X value:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=(
                                "rectangle_mesh_contour_isosurface_value_x",
                                local_state.rectangle_mesh_contour_isosurface_value_x,
                            ),
                            min=-1,
                            max=1,
                            step=0.01,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-alpha-x",
                            color="lime darken-2",
                            dense=True,
                        )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Contour Y value:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=(
                                "rectangle_mesh_contour_isosurface_value_y",
                                local_state.rectangle_mesh_contour_isosurface_value_y,
                            ),
                            min=-1,
                            max=1,
                            step=0.01,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-alpha-y",
                            color="lime darken-2",
                            dense=True,
                        )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Contour Z value:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=(
                                "rectangle_mesh_contour_isosurface_value_z",
                                local_state.rectangle_mesh_contour_isosurface_value_z,
                            ),
                            min=-1,
                            max=1,
                            step=0.01,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-alpha-z",
                            color="lime darken-2",
                            dense=True,
                        )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Contour theta value:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=(
                                "rectangle_mesh_contour_isosurface_value_t",
                                local_state.rectangle_mesh_contour_isosurface_value_t,
                            ),
                            min=1,
                            max=179,
                            step=1,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-alpha-t",
                            color="lime darken-2",
                            dense=True,
                        )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

            with vuetify.VCardText("Contour phi value:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=(
                                "rectangle_mesh_contour_isosurface_value_p",
                                local_state.rectangle_mesh_contour_isosurface_value_p,
                            ),
                            min=-179,
                            max=179,
                            step=1,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-alpha-p",
                            color="lime darken-2",
                            dense=True,
                        )

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        with vuetify.VListGroup(
            color="lime darken-2", prepend_icon="mdi-alpha-r-circle-outline"
        ):
            with vuetify.Template(
                v_slot_activator=True,
            ):
                vuetify.VListItemTitle(
                    "Rescale",
                    style="display: flex; align-items: center; justify-content: center",
                )
            ##############
            # Rescale Recmesh
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
                            "rectangle_mesh_rescale",
                            pyvista_LR.do_rectangle_mesh_rescale,
                        ),
                        items=("list_point_rescale", [True, False]),
                        hide_details=True,
                        dense=False,
                        outlined=True,
                        classes="pt-1 ml-2",
                        append_icon="mdi-alphabet-piqad",
                        style=("max-width: 140px"),
                        color="lime darken-2",
                    )
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Rescale Factor:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=(
                                "rescale_rectangle_mesh_factor",
                                pyvista_LR.rescale_rectangle_mesh_factor,
                            ),
                            min=0.05,
                            max=30,
                            step=0.05,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-cosine-wave",
                            color="lime darken-2",
                            dense=False,
                        )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Rescale norm:"):
                with vuetify.VRow(dense=True):
                    # ___________________________
                    # rectangle_mesh rescale norm x
                    # ___________________________
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=(
                                "rectangle_mesh_rescale_norm_x",
                                pyvista_LR.rescale_simple_point_norm[0],
                            ),
                            solo=True,
                            # rounded =True,
                        )

                    # ___________________________
                    # rectangle_mesh rescale norm x
                    # ___________________________
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=(
                                "rectangle_mesh_rescale_norm_y",
                                pyvista_LR.rescale_simple_point_norm[1],
                            ),
                            solo=True,
                            # rounded =True,
                        )

                    # ___________________________
                    # rectangle_mesh rescale norm x
                    # ___________________________
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=(
                                "rectangle_mesh_rescale_norm_z",
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
                            color="lime darken-2",
                            rounded=True,
                            large=True,
                            click=ctrl.applied_point_rescale_norm,
                        )

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        with vuetify.VListGroup(
            color="lime darken-2", prepend_icon="mdi-alpha-c-circle-outline"
        ):
            with vuetify.Template(
                v_slot_activator=True,
            ):
                vuetify.VListItemTitle(
                    "Clip",
                    style="display: flex; align-items: center; justify-content: center",
                )
            with vuetify.VCardText("Clip component rectangle mesh:"):
                with vuetify.VRow(
                    classes="pt-3",
                    dense=False,
                ):
                    with vuetify.VCol(cols="4"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="4"):
                        vuetify.VSwitch(
                            v_model=(
                                "do_clip_component_recmesh",
                                pyvista_LR.do_rectangle_mesh_clip_scalar,
                            ),
                            items=("list_do_clip_component_recmesh", [True, False]),
                            hide_details=True,
                            dense=False,
                            outlined=True,
                            classes="pt-1 ml-2",
                            append_icon="mdi-content-cut",
                            style=("max-width: 250px"),
                            color="lime darken-2",
                        )
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Clip X: "):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VRangeSlider(
                            v_model=(
                                "Cut_X_rmesh",
                                [
                                    local_state.rectangle_mesh_clip_scalar_min_x,
                                    local_state.rectangle_mesh_clip_scalar_max_x,
                                ],
                            ),
                            min=-1,
                            max=1,
                            step=0.01,
                            thumb_label=True,
                            hide_details=False,
                            dense=True,
                            color="lime darken-2",
                            append_icon="mdi-alpha-x-box-outline",
                        )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Clip Y: "):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VRangeSlider(
                            v_model=(
                                "Cut_Y_rmesh",
                                [
                                    local_state.rectangle_mesh_clip_scalar_min_y,
                                    local_state.rectangle_mesh_clip_scalar_max_y,
                                ],
                            ),
                            min=-1,
                            max=1,
                            step=0.01,
                            thumb_label=True,
                            hide_details=False,
                            dense=True,
                            color="lime darken-2",
                            append_icon="mdi-alpha-y-box-outline",
                        )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Clip Z: "):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VRangeSlider(
                            v_model=(
                                "Cut_Z_rmesh",
                                [
                                    local_state.rectangle_mesh_clip_scalar_min_z,
                                    local_state.rectangle_mesh_clip_scalar_max_z,
                                ],
                            ),
                            min=-1,
                            max=1,
                            step=0.01,
                            thumb_label=True,
                            hide_details=False,
                            dense=True,
                            color="lime darken-2",
                            append_icon="mdi-alpha-z-box-outline",
                        )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

            with vuetify.VCardText("Clip theta: "):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VRangeSlider(
                            v_model=(
                                "Cut_theta_rmesh",
                                [
                                    pyvista_LR.rectangle_mesh_clip_scalar_min_theta,
                                    pyvista_LR.rectangle_mesh_clip_scalar_max_theta,
                                ],
                            ),
                            min=0,
                            max=180,
                            step=1,
                            thumb_label=True,
                            hide_details=False,
                            color="lime darken-2",
                            dense=True,
                            append_icon="mdi-alpha-t-box-outline",
                        )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Clip phi: "):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VRangeSlider(
                            v_model=(
                                "Cut_phi_rmesh",
                                [
                                    pyvista_LR.rectangle_mesh_clip_scalar_min_phi,
                                    pyvista_LR.rectangle_mesh_clip_scalar_max_phi,
                                ],
                            ),
                            min=-180,
                            max=180,
                            step=1,
                            thumb_label=True,
                            hide_details=False,
                            dense=True,
                            color="lime darken-2",
                            append_icon="mdi-alpha-p-box-outline",
                        )

                vuetify.VDivider(
                    vertical=False,
                    inset=False,
                    style=("max-width: 390; min-height: 390;max-height: 20px"),
                )

            ##############
            # Face clip rectangle mesh
            ##############
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="2"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="6"):
                    with vuetify.VCardText(f"Face clip rectangle mesh XYZ/Free:"):
                        with vuetify.VBtnToggle(
                            color="lime darken-2",
                            multiple=True,
                            split=True,
                            mandatory=False,
                            v_model=(
                                "view_mode_face_clip_rmesh",
                                local_state.face_clip_index_r,
                            ),
                        ):
                            with vuetify.VBtn(
                                click=ctrl.do_r_mesh_clip,
                                value="face_clip_r_0",
                                large=True,
                            ):
                                vuetify.VIcon("mdi-axis-arrow")
                            vuetify.VSpacer(style=("max-width: 20px; min-width: 20px"))
                            with vuetify.VBtn(
                                click=ctrl.do_clip_r_mesh_free_normal,
                                value="face_clip_r_1",
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
                            "rectangle_mesh_clip_plane_x_min",
                            pyvista_LR.rectangle_mesh_clip_plane_x_min,
                        ),
                        min=local_state.point_cloud_arrow_for_face_cut.bounds[0],
                        max=local_state.point_cloud_arrow_for_face_cut.bounds[1],
                        step=0.1,
                        label="X min->max",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        append_icon="mdi-alpha-x-circle-outline",
                        color="lime darken-2",
                        dense=False,
                    )

            # X_max
            pyvista_LR.rectangle_mesh_clip_plane_x_max = (
                local_state.point_cloud_arrow_for_face_cut.bounds[1]
            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=(
                            "rectangle_mesh_clip_plane_x_max",
                            pyvista_LR.rectangle_mesh_clip_plane_x_max,
                        ),
                        min=local_state.point_cloud_arrow_for_face_cut.bounds[0],
                        max=local_state.point_cloud_arrow_for_face_cut.bounds[1],
                        step=0.1,
                        label="X max->min",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        append_icon="mdi-alpha-x-circle",
                        color="lime darken-2",
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
                            "rectangle_mesh_clip_plane_y_min",
                            pyvista_LR.rectangle_mesh_clip_plane_y_min,
                        ),
                        min=local_state.point_cloud_arrow_for_face_cut.bounds[2],
                        max=local_state.point_cloud_arrow_for_face_cut.bounds[3],
                        step=0.1,
                        label="Y min->max",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        append_icon="mdi-alpha-y-circle-outline",
                        color="lime darken-2",
                        dense=False,
                    )

            # y_max
            pyvista_LR.rectangle_mesh_clip_plane_y_max = (
                local_state.point_cloud_arrow_for_face_cut.bounds[3]
            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=(
                            "rectangle_mesh_clip_plane_y_max",
                            pyvista_LR.rectangle_mesh_clip_plane_y_max,
                        ),
                        min=local_state.point_cloud_arrow_for_face_cut.bounds[2],
                        max=local_state.point_cloud_arrow_for_face_cut.bounds[3],
                        step=0.1,
                        label="Y max->min",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        append_icon="mdi-alpha-y-circle",
                        color="lime darken-2",
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
                            "rectangle_mesh_clip_plane_z_min",
                            pyvista_LR.rectangle_mesh_clip_plane_z_min,
                        ),
                        min=local_state.point_cloud_arrow_for_face_cut.bounds[4],
                        max=local_state.point_cloud_arrow_for_face_cut.bounds[5],
                        step=0.1,
                        label="Z min->max",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        append_icon="mdi-alpha-z-circle-outline",
                        color="lime darken-2",
                        dense=False,
                    )

            # z_max
            pyvista_LR.rectangle_mesh_clip_plane_z_max = (
                local_state.point_cloud_arrow_for_face_cut.bounds[5]
            )
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=(
                            "rectangle_mesh_clip_plane_z_max",
                            pyvista_LR.rectangle_mesh_clip_plane_z_max,
                        ),
                        min=local_state.point_cloud_arrow_for_face_cut.bounds[4],
                        max=local_state.point_cloud_arrow_for_face_cut.bounds[5],
                        step=0.1,
                        label="Z max->min",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        append_icon="mdi-alpha-z-circle",
                        color="lime darken-2",
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
                                "rectangle_mesh_clip_plane_free_normal_1_x",
                                pyvista_LR.rectangle_mesh_clip_plane_free_normal_1[0],
                            ),
                            solo=True,
                            # rounded =True,
                        )
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=(
                                "rectangle_mesh_clip_plane_free_normal_1_y",
                                pyvista_LR.rectangle_mesh_clip_plane_free_normal_1[1],
                            ),
                            solo=True,
                            # rounded =True,
                        )

                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=(
                                "rectangle_mesh_clip_plane_free_normal_1_z",
                                pyvista_LR.rectangle_mesh_clip_plane_free_normal_1[2],
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
                            v_model=("clip_rectangle_mesh_free_1", 0),
                            min=0,
                            max=1000,
                            step=0.1,
                            label="User's min->max",
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-alpha-u-circle-outline",
                            color="lime darken-2",
                            dense=False,
                        )

            # free normal clip max
            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Free clip 1: "):
                with vuetify.VRow(dense=True):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=(
                                "rectangle_mesh_clip_plane_free_normal_2_x",
                                pyvista_LR.rectangle_mesh_clip_plane_free_normal_2[0],
                            ),
                            solo=True,
                            # rounded =True,
                        )
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=(
                                "rectangle_mesh_clip_plane_free_normal_2_z",
                                pyvista_LR.rectangle_mesh_clip_plane_free_normal_2[1],
                            ),
                            solo=True,
                            # rounded =True,
                        )

                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=(
                                "dataset_clip_plane_free_normal_2_z",
                                pyvista_LR.rectangle_mesh_clip_plane_free_normal_2[2],
                            ),
                            solo=True,
                            # rounded =True,
                            min_height=50,
                        )
                # free_max
                # z_max
                pyvista_LR.clip_rectangle_mesh_free_2 = (
                    local_state.point_cloud_arrow_for_face_cut.bounds[5]
                )
                vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=("clip_rectangle_mesh_free_2", 0),
                            min=0,
                            max=1000,
                            step=0.1,
                            label="User's max->min",
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-alpha-u-circle",
                            color="lime darken-2",
                            dense=False,
                        )
