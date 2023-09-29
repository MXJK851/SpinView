from trame.widgets import vuetify


def object_initialize(local_state, pyvista_LR, state, spinview_checkbox):
    with vuetify.VListGroup(color="cyan darken-2", prepend_icon="mdi-arrow-decision"):
        with vuetify.Template(
            v_slot_activator=True,
        ):
            vuetify.VListItemTitle(
                "Objects",
                style="display: flex; align-items: center; justify-content: center",
            )
        # ---------------------------
        # Activate glyphs
        # ---------------------------
        with vuetify.VRow(
            classes="pt-3",
            dense=False,
        ):
            vuetify.VSpacer(style=("max-width: 40px; min-width: 40px"))
            with vuetify.VCol(cols="3"):
                vuetify.VSpacer()
            with vuetify.VCol(cols="3"):
                spinview_checkbox(
                    model=("activate_glyphs", pyvista_LR.add_glyphs),
                    on_icon="mdi-alpha-g-circle",
                    off_icon="mdi-alpha-g-circle-outline",
                    label="Glyphs:",
                    tooltip="Activate/Deactivate all glyphs",
                    color_in="cyan darken-2",
                )
            with vuetify.VCol(cols="3"):
                vuetify.VSpacer()

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        with vuetify.VRow(dense=True):
            # ___________________________
            # Point activation
            # ___________________________
            vuetify.VSpacer(style=("max-width: 30px; min-width: 30px"))
            with vuetify.VCol(cols="3", dense=True):
                spinview_checkbox(
                    model=("activate_point", pyvista_LR.add_simple_point),
                    on_icon=" mdi-square-medium",
                    off_icon=" mdi-square-medium-outline",
                    label="Point",
                    color_in="cyan darken-2",
                    # tooltip='Activate/Deactivate Cones',
                )
            # ___________________________
            # Cones activation
            # ___________________________
            vuetify.VSpacer(style=("max-width: 20px; min-width: 20px"))
            with vuetify.VCol(cols="3", dense=True):
                spinview_checkbox(
                    model=("activate_cone", pyvista_LR.add_cone),
                    on_icon="mdi-cone",
                    off_icon="mdi-cone-off",
                    label="Cone",
                    color_in="cyan darken-2",
                    # tooltip='Activate/Deactivate Cones',
                )
            # ___________________________
            # Arrows activation
            # ___________________________`
            vuetify.VSpacer(style=("max-width: 20px; min-width: 20px"))
            with vuetify.VCol(cols="3", dense=True):
                spinview_checkbox(
                    model=("activate_arrow", pyvista_LR.add_arrow),
                    on_icon="mdi-arrow-up-bold",
                    off_icon="mdi-arrow-up-bold-outline",
                    label="Arrow",
                    color_in="cyan darken-2",
                    # tooltip='Activate/Deactivate Arrows'
                )

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

        with vuetify.VRow(dense=True):
            # ___________________________
            # box  activation
            # ___________________________
            vuetify.VSpacer(style=("max-width: 30px; min-width: 30px"))

            with vuetify.VCol(cols="3", dense=True):
                spinview_checkbox(
                    model=("activate_box", pyvista_LR.add_box),
                    on_icon="mdi-cube",
                    off_icon="mdi-cube-off",
                    label="Box",
                    color_in="cyan darken-2",
                )
            vuetify.VSpacer(style=("max-width: 20px; min-width: 20px"))
            # ___________________________
            # Sphere activation
            # ___________________________
            with vuetify.VCol(cols="3"):
                spinview_checkbox(
                    model=("activate_sphere", pyvista_LR.add_sphere),
                    on_icon="mdi-sphere",
                    off_icon="mdi-sphere-off",
                    label="Sphere",
                    color_in="cyan darken-2",
                    tooltip="Time consiming",
                )
            vuetify.VSpacer(style=("max-width: 20px; min-width: 20px"))
            with vuetify.VCol(cols="3", dense=True):
                # ___________________________
                # plane activation
                # ___________________________
                spinview_checkbox(
                    model=("activate_plane", pyvista_LR.add_plane),
                    on_icon="mdi-square",
                    off_icon="mdi-square-off-outline",
                    label="Plane",
                    color_in="cyan darken-2",
                    # tooltip='Activate/Deactivate Plane'
                )

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        with vuetify.VRow(dense=True):
            vuetify.VSpacer(style=("max-width: 30px; min-width: 30px"))
            # ___________________________
            # own_glyphs   activation
            # ___________________________

            with vuetify.VCol(cols="3", dense=True):
                spinview_checkbox(
                    model=("activate_own_glyphs", pyvista_LR.add_own_glyphs),
                    on_icon="mdi-emoticon-wink",
                    off_icon="mdi-emoticon-cool",
                    label="User's",
                    color_in="cyan darken-2",
                    # tooltip='Validate your own glyphs'
                )

        vuetify.VSpacer(style=("max-height: 50px; min-height: 50px"))
        with vuetify.VCardText("Rectangle mesh"):
            # ---------------------------
            # Activate add_rectangle_mesh
            # ---------------------------
            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="3"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="7"):
                    spinview_checkbox(
                        model=(
                            "activate_rectangle_mesh",
                            pyvista_LR.add_rectangle_mesh,
                        ),
                        on_icon="mdi-vector-square",
                        off_icon="mdi-vector-square-remove",
                        label="Rectangle mesh",
                        tooltip="Activate/Deactivate rectangle mesh",
                        color_in="cyan darken-2",
                    )
        vuetify.VSpacer(style=("max-height: 50px; min-height: 50px"))

        with vuetify.VCardText("Delaunay triangulation mesh (time consuming)"):
            # ---------------------------
            # Activate add_unstructured_mesh
            # ---------------------------
            vuetify.VSpacer(style=("max-height: 15px; min-height: 10px"))
            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="4"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="7"):
                    spinview_checkbox(
                        model=(
                            "activate_unstructured_mesh",
                            pyvista_LR.add_unstructured_mesh,
                        ),
                        on_icon="mdi-cube-outline",
                        off_icon="mdi-cube-off-outline",
                        label="T mesh",
                        color_in="cyan darken-2",
                        tooltip='Time consuming "Delaunay triangulation operation" needed for each frame',
                    )

            vuetify.VSpacer(style=("max-height: 30px; min-height: 20px"))
