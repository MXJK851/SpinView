from trame.widgets import vuetify


def tmesh_initialize(local_state, pyvista_LR, state, ctrl, spinview_checkbox, colors):
    with vuetify.VListGroup(
        color="green accent-3", prepend_icon="mdi-triangle-outline"
    ):
        with vuetify.Template(v_slot_activator=True):
            vuetify.VListItemTitle(
                "Delaunay triangulation mesh",
                style="display: flex; align-items: center; justify-content: center",
            )
        with vuetify.VRow(
            classes="pt-3",
            dense=False,
        ):
            with vuetify.VCol(cols="2"):
                vuetify.VSpacer()
            with vuetify.VCol(cols="7"):
                spinview_checkbox(
                    model=("activate_unstructured_mesh", False),
                    on_icon="mdi-cube-outline",
                    off_icon="mdi-cube-off-outline",
                    label="Triangulation mesh",
                    tooltip="Time consuming \n Delaunay triangulation needed for each frame",
                )
        vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
        with vuetify.VCardText("Recalculate triangulation mesh:"):
            with vuetify.VRow(dense=False):
                # Cone C_x
                with vuetify.VCol(cols="3"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="3"):
                    vuetify.VBtn(
                        "ReCalc",
                        color="green accent-3",
                        rounded=True,
                        large=True,
                        click=ctrl.recalculate_tmesh,
                    )

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        with vuetify.VRow(classes="pt-3", dense=False):
            with vuetify.VCol(cols="1"):
                vuetify.VSpacer()
            with vuetify.VCol(cols="9"):
                with vuetify.VCardText("   Triangulation mesh cmap component:"):
                    with vuetify.VBtnToggle(
                        color="green accent-3",
                        multiple=False,
                        split=True,
                        mandatory=True,
                        value=local_state.Tmesh_cmap_vbtn,
                        rounded=True,
                        v_model=(
                            "view_mode_tmesh",
                            "tmesh_cmap{}".format(pyvista_LR.rectrangle_color_index),
                        ),
                    ):
                        with vuetify.VBtn(
                            click=ctrl.change_tmesh_cmap_vbtn_value_0,
                            value="tmesh_cmap0",
                        ):
                            vuetify.VIcon("mdi-alpha-x")
                        with vuetify.VBtn(
                            click=ctrl.change_tmesh_cmap_vbtn_value_1,
                            value="tmesh_cmap1",
                        ):
                            vuetify.VIcon("mdi-alpha-y")
                        with vuetify.VBtn(
                            click=ctrl.change_tmesh_cmap_vbtn_value_2,
                            value="tmesh_cmap2",
                        ):
                            vuetify.VIcon("mdi-alpha-z")
                        with vuetify.VBtn(
                            click=ctrl.change_tmesh_cmap_vbtn_value_3,
                            value="tmesh_cmap3",
                        ):
                            vuetify.VIcon("mdi-alpha-t")
                        with vuetify.VBtn(
                            click=ctrl.change_tmesh_cmap_vbtn_value_4,
                            value="tmesh_cmap4",
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
                with vuetify.VCardText("    Triangulation mesh opacity component:"):
                    with vuetify.VBtnToggle(
                        tag="sss",
                        color="green accent-3",
                        multiple=False,
                        split=True,
                        mandatory=True,
                        value=local_state.Tmesh_opaciy_vbtn,
                        rounded=True,
                        dense=True,
                        v_model=(
                            "view_mode_tmesh_op",
                            "tmesh_opacity{}".format(
                                pyvista_LR.unstructured_mesh_color_map_opacity_index
                            ),
                        ),
                    ):
                        with vuetify.VBtn(
                            click=ctrl.change_tmesh_opacity_index_vbtn_value_0,
                            value="tmesh_opacity0",
                        ):
                            vuetify.VIcon("mdi-alpha-x")
                        with vuetify.VBtn(
                            click=ctrl.change_tmesh_opacity_index_vbtn_value_1,
                            value="tmesh_opacity1",
                        ):
                            vuetify.VIcon("mdi-alpha-y")
                        with vuetify.VBtn(
                            click=ctrl.change_tmesh_opacity_index_vbtn_value_2,
                            value="tmesh_opacity2",
                        ):
                            vuetify.VIcon("mdi-alpha-z")
                        with vuetify.VBtn(
                            click=ctrl.change_tmesh_opacity_index_vbtn_value_3,
                            value="tmesh_opacity3",
                        ):
                            vuetify.VIcon("mdi-alpha-t")
                        with vuetify.VBtn(
                            click=ctrl.change_tmesh_opacity_index_vbtn_value_4,
                            value="tmesh_opacity4",
                        ):
                            vuetify.VIcon("mdi-alpha-t-box")
                        with vuetify.VBtn(
                            click=ctrl.change_tmesh_opacity_index_vbtn_value_5,
                            value="tmesh_opacity5",
                        ):
                            vuetify.VIcon("mdi-alpha-p")
                        with vuetify.VBtn(
                            click=ctrl.change_tmesh_opacity_index_vbtn_value_6,
                            value="tmesh_opacity6",
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
                            "opacity_record_tmesh",
                            local_state.opacity_record_tmesh,
                        ),
                        min=0,
                        max=1,
                        step=0.01,
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        dense=False,
                        append_icon="mdi-water-opacity",
                        track_color="green accent-3",
                        color="green accent-3",
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
                            "unstructured_mesh_interpolate_before_map",
                            pyvista_LR.unstructured_mesh_interpolate_before_map,
                        ),
                        items=(
                            "list_unstructured_mesh_interpolate_before_map",
                            [True, False],
                        ),
                        hide_details=True,
                        dense=False,
                        outlined=True,
                        classes="pt-1 ml-2",
                        style=("max-width: 140px"),
                        color="green accent-3",
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
                        v_model=("pbr_unstructured", pyvista_LR.pbr_unstructured),
                        items=("list_pbr_unstructured", [True, False]),
                        hide_details=True,
                        dense=False,
                        outlined=True,
                        classes="pt-1 ml-2",
                        style=("max-width: 140px"),
                        color="green accent-3",
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
                        v_model=("metallic_tmesh", local_state.metallic_tmesh),
                        min=0,
                        max=1,
                        step=0.01,
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        append_icon="mdi-gold",
                        color="green accent-3",
                        dense=False,
                    )
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        with vuetify.VCardText("Roughness:"):
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=("roughness_tmesh", local_state.roughness_tmesh),
                        min=0,
                        max=1,
                        step=0.01,
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        dense=False,
                        append_icon="mdi-square-opacity",
                        color="green accent-3",
                    )
        vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
        vuetify.VDivider(
            vertical=False,
            inset=False,
            style=("max-width: 390; min-height: 390;max-height: 20px"),
        )
        vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
        with vuetify.VListGroup(
            color="green accent-3", prepend_icon="mdi-alpha-c-circle-outline"
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
                                "do_unstructured_mesh_contour",
                                pyvista_LR.do_unstructured_mesh_contour,
                            ),
                            items=(
                                "list_do_do_unstructured_mesh_contour",
                                [True, False],
                            ),
                            hide_details=True,
                            dense=False,
                            outlined=True,
                            classes="pt-1 ml-2",
                            style=("max-width: 140px"),
                            color="green accent-3",
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
                                "do_multi_unstructured_surface_contour",
                                pyvista_LR.do_multi_unstructured_surface_contour,
                            ),
                            items=(
                                "list_do_multi_unstructured_surface_contour",
                                [True, False],
                            ),
                            hide_details=True,
                            dense=False,
                            outlined=True,
                            classes="pt-1 ml-2",
                            style=("max-width: 140px"),
                            color="green accent-3",
                        )
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Contour numbers:"):
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=(
                                "unstructured_mesh_contour_isosurface_number",
                                pyvista_LR.unstructured_mesh_contour_isosurface_number,
                            ),
                            min=0,
                            max=40,
                            step=1,
                            label="Contour number",
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-magnify-plus",
                            color="green accent-3",
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
                    with vuetify.VCol(cols="10"):
                        with vuetify.VBtnToggle(
                            color="green accent-3",
                            multiple=False,
                            split=True,
                            mandatory=False,
                            v_model=(
                                "Contour_i_tmesh",
                                "Contour_tmesh_{}".format(
                                    pyvista_LR.rectangle_mesh_contour_method_indicator
                                ),
                            ),
                        ):
                            with vuetify.VBtn(
                                click=ctrl.Contour_0_tmesh,
                                value="Contour_tmesh_0",
                                large=False,
                            ):
                                vuetify.VIcon("mdi-alpha-x")
                            vuetify.VSpacer(style=("max-width: 20px; min-width: 20px"))
                            with vuetify.VBtn(
                                click=ctrl.Contour_1_tmesh,
                                value="Contour_tmesh_1",
                                large=False,
                            ):
                                vuetify.VIcon("mdi-alpha-y")
                            vuetify.VSpacer(style=("max-width: 20px; min-width: 20px"))
                            with vuetify.VBtn(
                                click=ctrl.Contour_2_tmesh,
                                value="Contour_tmesh_2",
                                large=False,
                            ):
                                vuetify.VIcon("mdi-alpha-z")
                            vuetify.VSpacer(style=("max-width: 20px; min-width: 20px"))
                            with vuetify.VBtn(
                                click=ctrl.Contour_3_tmesh,
                                value="Contour_tmesh_3",
                                large=False,
                            ):
                                vuetify.VIcon("mdi-alpha-t")
                            vuetify.VSpacer(style=("max-width: 20px; min-width: 20px"))
                            with vuetify.VBtn(
                                click=ctrl.Contour_4_tmesh,
                                value="Contour_tmesh_4",
                                large=False,
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
                                "t_mesh_contour_isosurface_value_x",
                                local_state.t_mesh_contour_isosurface_value_x,
                            ),
                            min=-1,
                            max=1,
                            step=0.01,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-magnify-plus",
                            color="green accent-3",
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
                                "t_mesh_contour_isosurface_value_y",
                                local_state.t_mesh_contour_isosurface_value_y,
                            ),
                            min=-1,
                            max=1,
                            step=0.01,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-alpha-y",
                            color="green accent-3",
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
                                "t_mesh_contour_isosurface_value_z",
                                local_state.t_mesh_contour_isosurface_value_z,
                            ),
                            min=-1,
                            max=1,
                            step=0.01,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-alpha-z",
                            color="green accent-3",
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
                                "unstructured_mesh_contour_isosurface_value_t",
                                local_state.unstructured_mesh_contour_isosurface_value_t,
                            ),
                            min=1,
                            max=179,
                            step=1,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-magnify-plus",
                            color="green accent-3",
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
                                "unstructured_mesh_contour_isosurface_value_p",
                                local_state.unstructured_mesh_contour_isosurface_value_p,
                            ),
                            min=-179,
                            max=179,
                            step=1,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-magnify-plus",
                            color="green accent-3",
                            dense=True,
                        )
            vuetify.VSpacer(style=("max-height: 40px; min-height: 30px"))

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        with vuetify.VListGroup(
            color="green accent-3", prepend_icon="mdi-alpha-r-circle-outline"
        ):
            with vuetify.Template(
                v_slot_activator=True,
            ):
                vuetify.VListItemTitle(
                    "Rescale",
                    style="display: flex; align-items: center; justify-content: center",
                )

            ##############
            # Rescale Tmesh
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
                            "unstructured_mesh_rescale",
                            pyvista_LR.do_unstructured_mesh_rescale,
                        ),
                        items=("list_point_rescale", [True, False]),
                        hide_details=True,
                        dense=False,
                        outlined=True,
                        classes="pt-1 ml-2",
                        append_icon="mdi-alphabet-piqad",
                        style=("max-width: 140px"),
                        color="green accent-3",
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
                                "rescale_unstructured_mesh_factor",
                                pyvista_LR.rescale_unstructured_mesh_factor,
                            ),
                            min=0.05,
                            max=30,
                            step=0.05,
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-cosine-wave",
                            color="green accent-3",
                            dense=False,
                        )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VCardText("Rescale norm:"):
                with vuetify.VRow(dense=True):
                    # ___________________________
                    # unstructured_mesh rescale norm x
                    # ___________________________
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=(
                                "unstructured_mesh_rescale_norm_x",
                                pyvista_LR.rescale_unstructured_mesh_norm[0],
                            ),
                            solo=True,
                            # rounded =True,
                        )

                    # ___________________________
                    # unstructured_mesh rescale norm x
                    # ___________________________
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=(
                                "unstructured_mesh_rescale_norm_y",
                                pyvista_LR.rescale_unstructured_mesh_norm[1],
                            ),
                            solo=True,
                            # rounded =True,
                        )

                    # ___________________________
                    # unstructured_mesh rescale norm x
                    # ___________________________
                    with vuetify.VCol(cols="3"):
                        vuetify.VTextField(
                            v_model=(
                                "unstructured_mesh_rescale_norm_z",
                                pyvista_LR.rescale_unstructured_mesh_norm[2],
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
                            color="green accent-3",
                            rounded=True,
                            large=True,
                            click=ctrl.applied_point_rescale_norm,
                        )
                vuetify.VDivider(
                    vertical=False,
                    inset=False,
                    style=("max-width: 390; min-height: 390;max-height: 20px"),
                )
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        with vuetify.VListGroup(
            color="green accent-3", prepend_icon="mdi-alpha-c-circle-outline"
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
                                "do_clip_component_Tmesh",
                                pyvista_LR.do_unstructured_mesh_clip_scalar,
                            ),
                            items=("list_do_clip_component_Tmesh", [True, False]),
                            hide_details=True,
                            dense=False,
                            outlined=True,
                            classes="pt-1 ml-2",
                            append_icon="mdi-content-cut",
                            style=("max-width: 250px"),
                            color="green accent-3",
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
                                    "Cut_X_tmesh",
                                    [
                                        local_state.t_mesh_clip_scalar_min_x,
                                        local_state.t_mesh_clip_scalar_max_x,
                                    ],
                                ),
                                min=-1,
                                max=1,
                                step=0.01,
                                thumb_label=True,
                                hide_details=False,
                                dense=True,
                                color="green accent-3",
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
                                    "Cut_Y_tmesh",
                                    [
                                        local_state.t_mesh_clip_scalar_min_y,
                                        local_state.t_mesh_clip_scalar_max_y,
                                    ],
                                ),
                                min=-1,
                                max=1,
                                step=0.01,
                                thumb_label=True,
                                hide_details=False,
                                dense=True,
                                color="green accent-3",
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
                                    "Cut_Z_tmesh",
                                    [
                                        local_state.t_mesh_clip_scalar_min_z,
                                        local_state.t_mesh_clip_scalar_max_z,
                                    ],
                                ),
                                min=-1,
                                max=1,
                                step=0.01,
                                thumb_label=True,
                                hide_details=False,
                                dense=True,
                                color="green accent-3",
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
                                    "Cut_theta_tmesh",
                                    [
                                        pyvista_LR.unstructured_mesh_clip_scalar_min_theta,
                                        pyvista_LR.unstructured_mesh_clip_scalar_max_theta,
                                    ],
                                ),
                                min=0,
                                max=180,
                                step=1,
                                thumb_label=True,
                                hide_details=False,
                                color="green accent-3",
                                dense=True,
                            )

                vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
                with vuetify.VCardText("Clip phi: "):
                    with vuetify.VRow(classes="pt-3", dense=False):
                        with vuetify.VCol(cols="1"):
                            vuetify.VSpacer()
                        with vuetify.VCol(cols="9"):
                            vuetify.VRangeSlider(
                                v_model=(
                                    "Cut_phi_Tmesh",
                                    [
                                        pyvista_LR.unstructured_mesh_clip_scalar_min_phi,
                                        pyvista_LR.unstructured_mesh_clip_scalar_max_phi,
                                    ],
                                ),
                                min=-180,
                                max=180,
                                step=0.01,
                                thumb_label=True,
                                hide_details=False,
                                dense=True,
                                color="green accent-3",
                            )

                ##############
                # Face clip T mesh
                ##############
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="2"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="6"):
                        with vuetify.VCardText(f"Face clip rectangle mesh XYZ/Free:"):
                            with vuetify.VBtnToggle(
                                color="green accent-3",
                                multiple=True,
                                split=True,
                                mandatory=False,
                                v_model=(
                                    "view_mode_face_clip_tmesh",
                                    local_state.face_clip_index_t,
                                ),
                            ):
                                with vuetify.VBtn(
                                    click=ctrl.do_t_mesh_clip,
                                    value="face_clip_t_0",
                                    large=True,
                                ):
                                    vuetify.VIcon("mdi-axis-arrow")
                                vuetify.VSpacer(
                                    style=("max-width: 20px; min-width: 20px")
                                )
                                with vuetify.VBtn(
                                    click=ctrl.do_clip_t_mesh_free_normal,
                                    value="face_clip_t_1",
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
                                "unstructured_mesh_clip_plane_x_min",
                                pyvista_LR.unstructured_mesh_clip_plane_x_min,
                            ),
                            min=local_state.point_cloud_arrow_for_face_cut.bounds[0],
                            max=local_state.point_cloud_arrow_for_face_cut.bounds[1],
                            step=0.1,
                            label="X min->max",
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-alpha-x-circle-outline",
                            color="green accent-3",
                            dense=False,
                        )

                # X_max
                pyvista_LR.unstructured_mesh_clip_plane_x_max = (
                    local_state.point_cloud_arrow_for_face_cut.bounds[1]
                )
                vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=(
                                "unstructured_mesh_clip_plane_x_max",
                                pyvista_LR.unstructured_mesh_clip_plane_x_max,
                            ),
                            min=local_state.point_cloud_arrow_for_face_cut.bounds[0],
                            max=local_state.point_cloud_arrow_for_face_cut.bounds[1],
                            step=0.1,
                            label="X max->min",
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-alpha-x-circle",
                            color="green accent-3",
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
                                "unstructured_mesh_clip_plane_y_min",
                                pyvista_LR.unstructured_mesh_clip_plane_y_min,
                            ),
                            min=local_state.point_cloud_arrow_for_face_cut.bounds[2],
                            max=local_state.point_cloud_arrow_for_face_cut.bounds[3],
                            step=0.1,
                            label="Y min->max",
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-alpha-y-circle-outline",
                            color="green accent-3",
                            dense=False,
                        )

                # y_max
                pyvista_LR.unstructured_mesh_clip_plane_y_max = (
                    local_state.point_cloud_arrow_for_face_cut.bounds[3]
                )
                vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=(
                                "unstructured_mesh_clip_plane_y_max",
                                pyvista_LR.unstructured_mesh_clip_plane_y_max,
                            ),
                            min=local_state.point_cloud_arrow_for_face_cut.bounds[2],
                            max=local_state.point_cloud_arrow_for_face_cut.bounds[3],
                            step=0.1,
                            label="Y max->min",
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-alpha-y-circle",
                            color="green accent-3",
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
                                "unstructured_mesh_clip_plane_z_min",
                                pyvista_LR.unstructured_mesh_clip_plane_z_min,
                            ),
                            min=local_state.point_cloud_arrow_for_face_cut.bounds[4],
                            max=local_state.point_cloud_arrow_for_face_cut.bounds[5],
                            step=0.1,
                            label="Z min->max",
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-alpha-z-circle-outline",
                            color="green accent-3",
                            dense=False,
                        )

                # z_max
                pyvista_LR.unstructured_mesh_clip_plane_z_max = (
                    local_state.point_cloud_arrow_for_face_cut.bounds[5]
                )
                vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
                with vuetify.VRow(classes="pt-3", dense=False):
                    with vuetify.VCol(cols="1"):
                        vuetify.VSpacer()
                    with vuetify.VCol(cols="9"):
                        vuetify.VSlider(
                            v_model=(
                                "unstructured_mesh_clip_plane_z_max",
                                pyvista_LR.unstructured_mesh_clip_plane_z_max,
                            ),
                            min=local_state.point_cloud_arrow_for_face_cut.bounds[4],
                            max=local_state.point_cloud_arrow_for_face_cut.bounds[5],
                            step=0.1,
                            label="Z max->min",
                            # classes="mt-1",
                            thumb_label=True,
                            hide_details=False,
                            append_icon="mdi-alpha-z-circle",
                            color="green accent-3",
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
                                    "unstructured_mesh_clip_plane_free_normal_1_x",
                                    pyvista_LR.unstructured_mesh_clip_plane_free_normal_1[
                                        0
                                    ],
                                ),
                                solo=True,
                                # rounded =True,
                            )
                        with vuetify.VCol(cols="3"):
                            vuetify.VTextField(
                                v_model=(
                                    "unstructured_mesh_clip_plane_free_normal_1_y",
                                    pyvista_LR.unstructured_mesh_clip_plane_free_normal_1[
                                        1
                                    ],
                                ),
                                solo=True,
                                # rounded =True,
                            )

                        with vuetify.VCol(cols="3"):
                            vuetify.VTextField(
                                v_model=(
                                    "unstructured_mesh_clip_plane_free_normal_1_z",
                                    pyvista_LR.unstructured_mesh_clip_plane_free_normal_1[
                                        2
                                    ],
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
                                v_model=("clip_unstructured_mesh_free_1", 0),
                                min=0,
                                max=1000,
                                step=0.1,
                                label="User's min->max",
                                # classes="mt-1",
                                thumb_label=True,
                                hide_details=False,
                                append_icon="mdi-alpha-u-circle-outline",
                                color="green accent-3",
                                dense=False,
                            )

                # free normal clip min
                vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
                with vuetify.VCardText("Free clip 2: "):
                    with vuetify.VRow(dense=True):
                        with vuetify.VCol(cols="1"):
                            vuetify.VSpacer()
                        with vuetify.VCol(cols="3"):
                            vuetify.VTextField(
                                v_model=(
                                    "unstructured_mesh_clip_plane_free_normal_2_x",
                                    pyvista_LR.unstructured_mesh_clip_plane_free_normal_2[
                                        0
                                    ],
                                ),
                                solo=True,
                                # rounded =True,
                            )
                        with vuetify.VCol(cols="3"):
                            vuetify.VTextField(
                                v_model=(
                                    "unstructured_mesh_clip_plane_free_normal_2_y",
                                    pyvista_LR.unstructured_mesh_clip_plane_free_normal_2[
                                        1
                                    ],
                                ),
                                solo=True,
                                # rounded =True,
                            )

                        with vuetify.VCol(cols="3"):
                            vuetify.VTextField(
                                v_model=(
                                    "unstructured_mesh_clip_plane_free_normal_2_z",
                                    pyvista_LR.unstructured_mesh_clip_plane_free_normal_2[
                                        2
                                    ],
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
                                v_model=("clip_unstructured_mesh_free_2", 0),
                                min=0,
                                max=1000,
                                step=0.1,
                                label="User's max->min",
                                # classes="mt-1",
                                thumb_label=True,
                                hide_details=False,
                                append_icon="mdi-alpha-u-circle",
                                color="green accent-3",
                                dense=False,
                            )
