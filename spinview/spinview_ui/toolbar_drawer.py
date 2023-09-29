from trame.widgets import vuetify
from pyvista.plotting import colors


def toolbar_drawer_initialize(
    layout, viewer, local_state, pyvista_LR, cubemap_in_selector, ctrl
):
    with vuetify.VListGroup(
        color="blue-grey darken-2", prepend_icon="mdi-hammer-wrench"
    ):
        with vuetify.Template(
            v_slot_activator=True,
        ):
            vuetify.VListItemTitle(
                "Toolbar",
                style="display: flex; align-items: center; justify-content: center",
            )

        vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))

        with vuetify.VCardText("Quick control: "):
            viewer.ui_controls(mode=local_state.ui_control_model)
        ################
        # Choose scalar bar to show
        ################

        vuetify.VSpacer(style=("max-height: 40px; min-height: 30px"))
        with vuetify.VCardText("Scalar bar: "):
            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="2"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="6"):
                    vuetify.VSelect(
                        v_model=("choose_scalar_bar", pyvista_LR.antialiasing),
                        items=("scalar_bar_choose", ["Deactivate", "Activate"]),
                        prepend_inner_icon="mdi-ruler",
                        hide_details=True,
                        dense=True,
                        solo=True,
                    )

        ################
        # Antialiasing
        ################
        vuetify.VSpacer(style=("max-height: 40px; min-height: 30px"))
        with vuetify.VCardText("Antialiasing: "):
            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="2"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="6"):
                    vuetify.VSelect(
                        v_model=("antialiasing", pyvista_LR.antialiasing),
                        items=("list_antialiasing", ["ssaa", "msaa", "fxaa"]),
                        prepend_inner_icon="mdi-quality-high",
                        hide_details=True,
                        dense=True,
                        # outlined=True,
                        solo=True,
                        # classes="pt-1 ml-2",
                    )

        ################
        # BGC selector
        ################
        vuetify.VSpacer(style=("max-height: 40px; min-height: 30px"))
        with vuetify.VCardText("Background"):
            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="2"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="6"):
                    vuetify.VSelect(
                        v_model=("bgc", pyvista_LR.bgc),
                        items=(
                            "list_bgc",
                            (list(colors.hexcolors.keys()) + cubemap_in_selector),
                        ),
                        prepend_inner_icon="mdi-border-color",
                        hide_details=True,
                        dense=True,
                        # outlined=True,
                        solo=True,
                        prefix="Background:",
                        # classes="pt-1 ml-2",
                    )

        vuetify.VSpacer(style=("max-height: 40px; min-height: 30px"))
        with vuetify.VCardText("Colormap"):
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="2"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="7"):
                    vuetify.VSelect(
                        v_model=("cmap", pyvista_LR.cmap_record),
                        items=(
                            "list_Colormaps",
                            [
                                "Accent",
                                "Accent_r",
                                "Blues",
                                "Blues_r",
                                "BrBG",
                                "BrBG_r",
                                "BuGn",
                                "BuGn_r",
                                "BuPu",
                                "BuPu_r",
                                "CMRmap",
                                "CMRmap_r",
                                "Dark2",
                                "Dark2_r",
                                "GnBu",
                                "GnBu_r",
                                "Greens",
                                "Greens_r",
                                "Greys",
                                "Greys_r",
                                "OrRd",
                                "OrRd_r",
                                "Oranges",
                                "Oranges_r",
                                "PRGn",
                                "PRGn_r",
                                "Paired",
                                "Paired_r",
                                "Pastel1",
                                "Pastel1_r",
                                "Pastel2",
                                "Pastel2_r",
                                "PiYG",
                                "PiYG_r",
                                "PuBu",
                                "PuBuGn",
                                "PuBuGn_r",
                                "PuBu_r",
                                "PuOr",
                                "PuOr_r",
                                "PuRd",
                                "PuRd_r",
                                "Purples",
                                "Purples_r",
                                "RdBu",
                                "RdBu_r",
                                "RdGy",
                                "RdGy_r",
                                "RdPu",
                                "RdPu_r",
                                "RdYlBu",
                                "RdYlBu_r",
                                "RdYlGn",
                                "RdYlGn_r",
                                "Reds",
                                "Reds_r",
                                "Set1",
                                "Set1_r",
                                "Set2",
                                "Set2_r",
                                "Set3",
                                "Set3_r",
                                "Spectral",
                                "Spectral_r",
                                "Wistia",
                                "Wistia_r",
                                "YlGn",
                                "YlGnBu",
                                "YlGnBu_r",
                                "YlGn_r",
                                "YlOrBr",
                                "YlOrBr_r",
                                "YlOrRd",
                                "YlOrRd_r",
                                "afmhot",
                                "afmhot_r",
                                "autumn",
                                "autumn_r",
                                "binary",
                                "binary_r",
                                "bone",
                                "bone_r",
                                "brg",
                                "brg_r",
                                "bwr",
                                "bwr_r",
                                "cividis",
                                "cividis_r",
                                "cool",
                                "cool_r",
                                "coolwarm",
                                "coolwarm_r",
                                "copper",
                                "copper_r",
                                "cubehelix",
                                "cubehelix_r",
                                "flag",
                                "flag_r",
                                "gist_earth",
                                "gist_earth_r",
                                "gist_gray",
                                "gist_gray_r",
                                "gist_heat",
                                "gist_heat_r",
                                "gist_ncar",
                                "gist_ncar_r",
                                "gist_rainbow",
                                "gist_rainbow_r",
                                "gist_stern",
                                "gist_stern_r",
                                "gist_yarg",
                                "gist_yarg_r",
                                "gnuplot",
                                "gnuplot2",
                                "gnuplot2_r",
                                "gnuplot_r",
                                "gray",
                                "gray_r",
                                "hot",
                                "hot_r",
                                "hsv",
                                "hsv_r",
                                "inferno",
                                "inferno_r",
                                "jet",
                                "jet_r",
                                "magma",
                                "magma_r",
                                "nipy_spectral",
                                "nipy_spectral_r",
                                "ocean",
                                "ocean_r",
                                "pink",
                                "pink_r",
                                "plasma",
                                "plasma_r",
                                "prism",
                                "prism_r",
                                "rainbow",
                                "rainbow_r",
                                "seismic",
                                "seismic_r",
                                "spring",
                                "spring_r",
                                "summer",
                                "summer_r",
                                "tab10",
                                "tab10_r",
                                "tab20",
                                "tab20_r",
                                "tab20b",
                                "tab20b_r",
                                "tab20c",
                                "tab20c_r",
                                "terrain",
                                "terrain_r",
                                "turbo",
                                "turbo_r",
                                "twilight",
                                "twilight_r",
                                "twilight_shifted",
                                "twilight_shifted_r",
                                "viridis",
                                "viridis_r",
                                "winter",
                                "winter_r",
                            ],
                        ),
                        hide_details=True,
                        dense=True,
                        # outlined=True,
                        prepend_inner_icon="mdi-format-color-fill",
                        solo=True,
                        prefix="Colormap:",
                        # hint="Select a colormap",
                        # classes="pt-1 ml-2",
                        color="orange darken-2",
                        style=("max-width: 350px; min-width: 150px"),
                    )

        ################
        # Image download
        ################
        vuetify.VSpacer(style=("max-height: 40px; min-height: 30px"))
        with vuetify.VCardText("Image resolution: "):
            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="2"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="6"):
                    vuetify.VSelect(
                        label="Screenshot",
                        v_model=(
                            "downloadscreenshot",
                            local_state.download_screenshot_resolution,
                        ),
                        items=(
                            "list_sr",
                            [
                                1,
                                2,
                                3,
                                4,
                                5,
                                6,
                                7,
                                8,
                                9,
                                10,
                            ],
                        ),
                        hide_details=True,
                        dense=True,
                        # outlined=True,
                        solo=True,
                        prefix="Res:",
                        # classes="pt-1 ml-2",
                    )
        vuetify.VSpacer(style=("max-height: 40px; min-height: 30px"))
        with vuetify.VRow(
            classes="pt-3",
            dense=False,
        ):
            with vuetify.VCol(cols="4"):
                vuetify.VSpacer()
            with vuetify.VCol(cols="4"):
                with vuetify.VBtn(
                    click=ctrl.download_normal_screenshot,
                    elevation=2,
                    rounded=True,
                    color="yellow lighten-5",
                ):
                    vuetify.VIcon("mdi-image-area", color="blue-grey lighten-2")
        vuetify.VSpacer(style=("max-height: 40px; min-height: 30px"))
        with vuetify.VRow(
            classes="pt-3",
            dense=False,
        ):
            with vuetify.VCol(cols="4"):
                vuetify.VSpacer()
            with vuetify.VCol(cols="4"):
                with vuetify.VBtn(
                    click=ctrl.download_transparent_screenshot,
                    elevation=2,
                    rounded=True,
                    color="yellow lighten-5",
                ):
                    vuetify.VIcon("mdi-image-filter-hdr", color="blue-grey lighten-2")
        ################
        # Moive download
        ################
        vuetify.VSpacer(style=("max-height: 40px; min-height: 30px"))
        with vuetify.VCardText("Moive resolution: "):
            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="2"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="6"):
                    vuetify.VSelect(
                        label="downloadmovie",
                        v_model=("downloadmovie", local_state.moive_size_x),
                        items=(
                            "list_mr",
                            [
                                500,
                                1000,
                                1500,
                                2000,
                                2500,
                                3000,
                                3500,
                                4000,
                                4500,
                                5000,
                                5500,
                                6000,
                                6500,
                                7000,
                                7500,
                                8000,
                                8500,
                                9000,
                                9500,
                                10000,
                            ],
                        ),
                        hide_details=True,
                        dense=True,
                        # outlined=True,
                        solo=True,
                        prefix="Res:",
                        # classes="pt-1 ml-2",
                    )
        vuetify.VSpacer(style=("max-height: 40px; min-height: 30px"))
        with vuetify.VCardText("Moive fps: "):
            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="2"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="6"):
                    vuetify.VSelect(
                        label="moivefps",
                        v_model=("moivefps", local_state.moive_fps),
                        items=(
                            "list_fps",
                            [
                                1,
                                2,
                                3,
                                5,
                                10,
                                15,
                                20,
                                25,
                                30,
                                35,
                                40,
                                45,
                                50,
                                55,
                                60,
                                65,
                                70,
                                75,
                                80,
                                85,
                                90,
                                95,
                                100,
                            ],
                        ),
                        hide_details=True,
                        dense=True,
                        # outlined=True,
                        solo=True,
                        prefix="Res:",
                        # classes="pt-1 ml-2",
                    )
        vuetify.VSpacer(style=("max-height: 40px; min-height: 30px"))
        with vuetify.VRow(
            classes="pt-3",
            dense=False,
        ):
            with vuetify.VCol(cols="4"):
                vuetify.VSpacer()
            with vuetify.VCol(cols="4"):
                # vuetify.VBtn("Moive Rendering", click=ctrl.local_moive_rendering_basic)
                with vuetify.VBtn(
                    click=ctrl.local_moive_rendering_basic,
                    elevation=2,
                    rounded=True,
                    color="yellow lighten-5",
                ):
                    vuetify.VIcon(
                        "mdi-video-vintage",
                        color="blue-grey darken-2",
                    )

        ################
        # Local rendering
        ################
        vuetify.VSpacer(style=("max-height: 40px; min-height: 30px"))
        with vuetify.VRow(
            classes="pt-3",
            dense=False,
        ):
            with vuetify.VCol(cols="3"):
                vuetify.VSpacer()
            with vuetify.VCol(cols="4"):
                vuetify.VBtn(
                    "Local View",
                    click=ctrl.local_rendering_basic,
                    elevation=2,
                    rounded=True,
                    color="blue lighten-5",
                    classes="grey--text text--darken-3",
                )
        ################
        # Bright/Dark mode
        ################
        vuetify.VSpacer(style=("max-height: 40px; min-height: 30px"))
        with vuetify.VRow(
            classes="pt-3",
            dense=False,
        ):
            with vuetify.VCol(cols="3"):
                vuetify.VSpacer()
            with vuetify.VCol(cols="4"):
                vuetify.VSwitch(
                    hide_details=True,
                    v_model=("$vuetify.theme.dark"),
                    append_icon="mdi-lightbulb-on",
                    prepend_icon="mdi-lightbulb-on-outline",
                )
