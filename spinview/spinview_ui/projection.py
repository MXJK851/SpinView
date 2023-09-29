from trame.widgets import vuetify


def projection_initialize(local_state, pyvista_LR, state, ctrl):
    with vuetify.VListGroup(
        color="purple darken-2", prepend_icon="mdi-alpha-p-circle-outline"
    ):
        with vuetify.Template(
            v_slot_activator=True,
        ):
            vuetify.VListItemTitle(
                "Projections",
                style="display: flex; align-items: center; justify-content: center",
            )
        # buttons for the projections (glyphs)

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

        with vuetify.VRow(classes="pt-3", dense=False):
            with vuetify.VCol(cols="1"):
                vuetify.VSpacer()
            with vuetify.VCol(cols="9"):
                with vuetify.VCardText("Add projection planes:"):
                    with vuetify.VBtnToggle(
                        tag="ss",
                        color="purple darken-2",
                        multiple=True,
                        split=True,
                        mandatory=False,
                        rounded=True,
                        dense=True,
                        v_model=(
                            "view_mode_glyph_projection",
                            list(local_state.glyph_projection_plane),
                        ),
                    ):
                        with vuetify.VBtn(
                            click=ctrl.add_projection_plane_1,
                            value="Glyph_projection_0",
                        ):
                            vuetify.VIcon("mdi-alpha-f")
                        with vuetify.VBtn(
                            click=ctrl.add_projection_plane_2,
                            value="Glyph_projection_1",
                        ):
                            vuetify.VIcon("mdi-alpha-b")
                        with vuetify.VBtn(
                            click=ctrl.add_projection_plane_3,
                            value="Glyph_projection_2",
                        ):
                            vuetify.VIcon("mdi-alpha-l")
                        with vuetify.VBtn(
                            click=ctrl.add_projection_plane_4,
                            value="Glyph_projection_3",
                        ):
                            vuetify.VIcon("mdi-alpha-r")
                        with vuetify.VBtn(
                            click=ctrl.add_projection_plane_5,
                            value="Glyph_projection_4",
                        ):
                            vuetify.VIcon("mdi-alpha-u")
                        with vuetify.VBtn(
                            click=ctrl.add_projection_plane_6,
                            value="Glyph_projection_5",
                        ):
                            vuetify.VIcon("mdi-alpha-d")
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))

        with vuetify.VCardText("Apply fft on projections:"):
            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="4"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="7"):
                    vuetify.VSwitch(
                        v_model=(
                            "do_glyph_projection_fft",
                            local_state.do_glyph_projection_fft,
                        ),
                        items=("list_fft_proj", [True, False]),
                        hide_details=True,
                        dense=False,
                        outlined=True,
                        classes="pt-1 ml-2",
                        style=("max-width: 140px"),
                        color="purple darken-2",
                    )
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()

        with vuetify.VCardText("OpenGL interpolate:"):
            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="4"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="7"):
                    vuetify.VSwitch(
                        v_model=(
                            "do_interpolated_projection",
                            local_state.do_interpolated_projection,
                        ),
                        items=("list_do_interpolated_projection", [True, False]),
                        hide_details=True,
                        dense=False,
                        outlined=True,
                        classes="pt-1 ml-2",
                        style=("max-width: 140px"),
                        color="purple darken-2",
                    )
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
