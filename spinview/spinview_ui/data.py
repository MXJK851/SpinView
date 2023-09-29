from trame.widgets import vuetify
import os


def data_initialize(
    local_state, pyvista_LR, state, ctrl, foler_items_for_select, exist_table_in_db
):
    with vuetify.VListGroup(color="light-blue darken-2", prepend_icon="mdi-file-cog"):
        with vuetify.Template(
            v_slot_activator=True,
        ):
            vuetify.VListItemTitle(
                "Data",
                style="display: flex; align-items: center; justify-content: center",
            )
        # ___________________________
        # Frame slider
        # ___________________________

        vuetify.VSpacer(style=("max-height: 15px; min-height: 10px"))
        with vuetify.VCardText("Choose one frame in trajectory:"):
            with vuetify.VRow(classes="pt-3", dense=False):
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="9"):
                    vuetify.VSlider(
                        v_model=("frame", pyvista_LR.frame_number),
                        min=0,
                        max=local_state.max_frame,
                        step=1,
                        thumb_label=True,
                        thumb_size=30,
                        value=pyvista_LR.frame_number,
                        label="Frames",
                        hide_details=True,
                        dense=False,
                        thumb_color="light-blue darken-1",
                        color="light-green lighten-4",
                        # disabled= (False if (pyvista_LR.outputfile_type == 'UppASD') else True),
                        append_icon="mdi-filmstrip",
                        # disabled  = local_state.is_traj,
                    )

        vuetify.VSpacer(style=("max-height: 15px; min-height: 10px"))

        vuetify.VSpacer(style=("max-height: 15px; min-height: 10px"))

        vuetify.VSpacer(style=("max-height: 15px; min-height: 10px"))
        vuetify.VSelect(
            label="Choose File 1",
            v_model=("mom_name", local_state.file_select_1),
            items=("list_moment_file1", foler_items_for_select),
            hide_details=True,
            dense=False,
            outlined=True,
            classes="pt-1 ml-2",
            style="max-width: 350px",
            color="light-blue accent-4",
            prepend_icon="mdi-numeric-1-box-multiple-outline",
        )
        vuetify.VSpacer(style=("max-height: 15px; min-height: 10px"))

        # Not offer in here in this version
        # vuetify.VFileInput(
        #     label="Upload File 1",
        #     v_model=("upload_moment_file", None),
        # )

        vuetify.VSpacer(style=("max-height: 15px; min-height: 10px"))
        vuetify.VSelect(
            label="Choose File 2",
            v_model=("mom_name1", local_state.file_select_2),
            items=("list_moment_file1", foler_items_for_select),
            hide_details=True,
            dense=False,
            outlined=True,
            classes="pt-1 ml-2",
            style="max-width: 350px",
            color="light-blue accent-3",
            disabled=(True if local_state.sub_frame_number == 1 else False),
            prepend_icon="mdi-numeric-2-box-multiple-outline",
        )

        vuetify.VSpacer(style=("max-height: 15px; min-height: 10px"))
        vuetify.VSelect(
            label="Choose File 3",
            v_model=("mom_name2", local_state.file_select_3),
            items=("list_moment_file2", foler_items_for_select),
            hide_details=True,
            dense=False,
            outlined=True,
            classes="pt-1 ml-2",
            style="max-width: 350px",
            color="light-blue accent-3",
            prepend_icon="mdi-numeric-3-box-multiple-outline",
            disabled=(
                True
                if (
                    local_state.sub_frame_number == 1
                    or local_state.sub_frame_number == 2
                )
                else False
            ),
        )

        vuetify.VSpacer(style=("max-height: 15px; min-height: 10px"))
        vuetify.VSelect(
            label="Choose File 4",
            v_model=("mom_name3", local_state.file_select_4),
            items=("list_moment_file3", foler_items_for_select),
            hide_details=True,
            dense=False,
            outlined=True,
            classes="pt-1 ml-2",
            style="max-width: 350px",
            color="light-blue accent-1",
            prepend_icon="mdi-numeric-4-box-multiple-outline",
            disabled=(
                True
                if (
                    local_state.sub_frame_number == 1
                    or local_state.sub_frame_number == 2
                    or local_state.sub_frame_number == 3
                )
                else False
            ),
        )
        vuetify.VSpacer(style=("max-height: 55px; min-height: 55px"))

        ##############
        # Rescale
        ##############
        with vuetify.VCardText("Unified control (in local view mode):"):
            with vuetify.VRow(
                classes="pt-3",
                dense=False,
            ):
                with vuetify.VCol(cols="3"):
                    vuetify.VSpacer()
                with vuetify.VCol(cols="7"):
                    vuetify.VSwitch(
                        v_model=(
                            "unified_control",
                            local_state.unified_control,
                        ),
                        items=("list_unified_control", [True, False]),
                        hide_details=True,
                        dense=False,
                        outlined=True,
                        classes="pt-1 ml-2",
                        prepend_icon="mdi-handshake-outline",
                        disabled=(True if local_state.sub_frame_number == 1 else False),
                        style=("max-width: 140px"),
                        color="green accent-3",
                    )
                with vuetify.VCol(cols="1"):
                    vuetify.VSpacer()

        ################
        # replace old table in db
        ################
        vuetify.VSpacer(style=("max-width: 30px; min-width: 10px"))
        vuetify.VDivider(vertical=True, classes="mx-1")
        vuetify.VSpacer(style=("max-width: 30px; min-width: 10px"))
        table_name_list = []
        for i in exist_table_in_db:
            table_name_list.append(i[0])
        with vuetify.VCardText("Replace exist profile:"):
            with vuetify.VRow(dense=False):
                with vuetify.VCol(cols="6"):
                    vuetify.VSelect(
                        v_model=("replace_table", table_name_list[0]),
                        items=("list_table", table_name_list),
                        prepend_inner_icon="mdi-database-edit",
                        hide_details=True,
                        dense=True,
                        solo=True,
                    )
                with vuetify.VCol(cols="3"):
                    vuetify.VBtn(
                        "Replace",
                        color="green accent-3",
                        rounded=True,
                        large=True,
                        click=ctrl.store_new_profile,
                    )

        vuetify.VSpacer(style=("max-height: 420px; min-height: 40px"))
        with vuetify.VCardText("Create new profile:"):
            with vuetify.VRow(dense=False):
                # Cone C_x
                with vuetify.VCol(cols="6"):
                    vuetify.VTextField(
                        v_model=("new_profile_name", local_state.new_profile_name),
                        solo=True,
                        # rounded =True,
                    )
                with vuetify.VCol(cols="3"):
                    vuetify.VBtn(
                        "Store",
                        color="green accent-3",
                        rounded=True,
                        large=True,
                        click=ctrl.store_new_profile,
                    )
