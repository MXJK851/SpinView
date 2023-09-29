from trame.widgets import vuetify


def denoise_initialize(local_state, pyvista_LR, state, ctrl):
    with vuetify.VListGroup(
        color="light-green darken-2", prepend_icon="mdi-monitor-shimmer"
    ):
        with vuetify.Template(
            v_slot_activator=True,
        ):
            vuetify.VListItemTitle(
                "Denoise",
                style="display: flex; align-items: center; justify-content: center",
            )
        #! here it should be a selector for ovf files in the folder
        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        with vuetify.VCardText("Low pass denoising:"):
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    with vuetify.VBtnToggle(
                        color="light-green darken-2",
                        multiple=False,
                        split=True,
                        mandatory=True,
                        v_model=(
                            "view_mode_denosing",
                            "denoising_{}".format(
                                local_state.start_desoning_filter_index
                            ),
                        ),
                    ):
                        with vuetify.VBtn(
                            click=ctrl.denoising_N, value="denoising_0", large=True
                        ):
                            vuetify.VIcon("mdi-alpha-n")
                        vuetify.VSpacer(style=("max-width: 20px; min-width: 20px"))
                        with vuetify.VBtn(
                            click=ctrl.denoising_low_pass,
                            value="denoising_1",
                            large=True,
                        ):
                            vuetify.VIcon("mdi-alpha-b")
                        vuetify.VSpacer(style=("max-width: 20px; min-width: 20px"))
                        with vuetify.VBtn(
                            click=ctrl.denoising_low_pass_fft_rec,
                            value="denoising_2",
                            large=True,
                        ):
                            vuetify.VIcon("mdi-alpha-r")

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        with vuetify.VCardText("Butterworth low pass denoising:"):
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=(
                            "low_pass_filter_order",
                            local_state.low_pass_filter_order,
                        ),
                        min=1,
                        max=50,
                        step=1,
                        label="Filter order",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        dense=False,
                        append_icon=" mdi-counter",
                        track_color="light-green darken-2",
                        color="light-green darken-2",
                    )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=(
                            "low_pass_normalized_freq",
                            local_state.low_pass_normalized_freq,
                        ),
                        min=0.01,
                        max=0.99,
                        step=0.01,
                        label="Threshold ",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        dense=False,
                        append_icon=" mdi-sine-wave",
                        track_color="light-green darken-2",
                        color="light-green darken-2",
                    )

        vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
        with vuetify.VCardText("FFT with rectangle windows filter:"):
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=("fft_rec_windows_X", local_state.fft_rec_windows_X),
                        min=1,
                        max=int(pyvista_LR.system_size[0] / 2),
                        step=1,
                        label="Threshold",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        dense=False,
                        append_icon=" mdi-alpha-x-circle",
                        track_color="light-green darken-2",
                        color="light-green darken-2",
                    )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=("fft_rec_windows_Y", local_state.fft_rec_windows_Y),
                        min=1,
                        max=int(pyvista_LR.system_size[1] / 2),
                        step=1,
                        label="Threshold",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        dense=False,
                        append_icon="mdi-alpha-y-circle",
                        track_color="light-green darken-2",
                        color="light-green darken-2",
                    )

            vuetify.VSpacer(style=("max-height: 20px; min-height: 20px"))
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=("fft_rec_windows_Z", local_state.fft_rec_windows_Z),
                        min=1,
                        max=int(pyvista_LR.system_size[2] / 2),
                        step=1,
                        label="Threshold",
                        # classes="mt-1",
                        thumb_label=True,
                        hide_details=False,
                        dense=False,
                        append_icon=" mdi-alpha-z-circle",
                        track_color="light-green darken-2",
                        color="light-green darken-2",
                    )
