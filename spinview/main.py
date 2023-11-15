"""
In this file, we will create a web app using Trame and Dash.plotly

Author: Qichen Xu mxjk851@gmail.com/qichenx@kth.se

2023-7-10

Wish you have 'sommartid'(summer time) everyday!


ToDO:
Add defect visualization 
workflow:
1. use clip_scalar to clip the magnetic atom and non-magnetic atom
2. sepearate visualization.
"""

# import packages
from trame.app import get_server
from trame.widgets import vuetify, html
from trame.ui.vuetify import SinglePageWithDrawerLayout
import pyvista as pv
from pyvista.plotting import colors
from pyvista.trame.ui import plotter_ui

from pyvista.trame.ui import get_or_create_viewer

# from pyvista.trame.ui import Vue2Viewer
from pyvista.demos import logo
import os
import pathlib

# Data processing
from pyvista.trame.ui import plotter_ui
from .spinview_utilities.vis_pyvista import pyvista_local_rendering, local_state_class
from .spinview_parsers.parsers import (
    parse_moment_and_coord_file,
    parse_moment_and_coord_file1,
    parse_moment_and_coord_file2,
    parse_moment_and_coord_file3,
    system_size_reader,
)
from trame.assets.local import LocalFileManager
from rich import print
from .spinview_ui.toolbar import toolbar_initialize
from .spinview_ui.data import data_initialize
from .spinview_ui.object import object_initialize
from .spinview_ui.denoise import denoise_initialize
from .spinview_ui.projection import projection_initialize
from .spinview_ui.glyph import glyph_initialize
from .spinview_ui.rmesh import rmesh_initialize
from .spinview_ui.tmesh import tmesh_initialize
from .spinview_ui.toolbar_drawer import toolbar_drawer_initialize
from .spinview_callbacks.activation_callbacks import activation_callbacks_initialize
from .spinview_callbacks.utilities_callbacks import utilities_callbacks_initialize
from .spinview_callbacks.rmesh_callbacks import rmesh_callbacks_initialize
from .spinview_callbacks.tmesh_callbacks import tmesh_callbacks_initialize
from .spinview_callbacks.glyphs_callbacks import glyphs_callbacks_initialize
from .spinview_utilities.utils import (
    spinview_checkbox,
    initial_plotter,
    plot_multiple_meshes,
)
from .spinview_utilities.profile_DB import check_profile

spinview_logo = LocalFileManager(__file__)
filepath = pathlib.Path(__file__).resolve().parent
logo_path = os.path.join(filepath, "spinview_icon")
logo_path = os.path.join(logo_path, "SpinView_logo.svg")

spinview_logo.url("svlogo", logo_path)

pv.OFF_SCREEN = True


def webui_realspace(
    db_name="default.db",
    table_name="Initial_profile",
    subframes=4,
    file_type="auto",
    port_number=9000,
    trame_host="localhost",
    ui_control_model="trame",
    trame_exec_mode="main",
    trame_open_browser=False,
    pywebview_windows_size_x=1920,
    pywebview_windows_size_y=1080,
    path_from_user=None,
    pyvista_still_ratio=1,
    pyvista_interactive_ratio=1,
):  # Here we use 'Initial_profile' as default profile, to avoid our user to use 'initial' as their profile name
    """
    Trame with pyvista initialization
    """
    filepath = pathlib.Path(__file__).resolve().parent
    db_path = os.path.join(filepath, "DB")
    db_path = os.path.join(db_path, db_name)

    pyvista_LR = pyvista_local_rendering(
        db_path, table_name
    )  # the main class for pyvista rendering

    pyvista_LR.sub_frame_number = subframes
    pyvista_LR.outputfile_type = file_type

    global local_state  # I find this class needs to be global, when writing the database function, the name will refactor in the future. now... we have a global 'local'.
    local_state = local_state_class(pyvista_LR)

    local_state.ui_control_model = (
        ui_control_model  # it can be client, trame, or server
    )
    # load_own_glyphs
    own_g_path = os.path.join(filepath, "own_glyph")
    own_g_path = os.path.join(own_g_path, "own_glyph.ply")
    local_state.user_input_glyph = pv.read(os.path.expanduser(own_g_path))
    ##############
    # create panels
    # for the reason of performance we support 4 panels now
    ##############
    if local_state.sub_frame_number == 1:
        plotter = pv.Plotter(shape=(1, 1))
    elif local_state.sub_frame_number == 2:
        plotter = pv.Plotter(shape=(1, 2))
    elif local_state.sub_frame_number == 3:
        plotter = pv.Plotter(shape=(1, 3))
    elif local_state.sub_frame_number == 4:
        plotter = pv.Plotter(shape=(2, 2))

    initial_plotter(pyvista_LR, plotter)

    server = get_server()
    state, ctrl = server.state, server.controller
    server.client_type = "vue2"
    state.trame__title = "SpinView"
    state.trame__favicon = spinview_logo.svlogo
    ctrl.on_server_ready.add(ctrl.view_update)

    ####################
    # Try to find cubemap
    ####################
    local_state.cubemap_folder_names_list = []
    cubemap_in_selector = []

    ####################
    # Welcome image glyphs
    ####################
    local_state.texts = logo.text_3d("S", depth=0.3)
    local_state.texts.points *= 8.0
    local_state.texts.translate([-17.0, 20.0, 0.0], inplace=True)
    local_state.textp = logo.text_3d("p", depth=0.3)
    local_state.textp.points *= 8.0
    local_state.textp.translate([-8.0, 20.0, -0.0], inplace=True)
    local_state.texti1 = logo.text_3d("i", depth=0.3)
    local_state.texti1.points *= 8.0
    local_state.texti1.translate([-0.0, 20.0, 0.0], inplace=True)
    local_state.textn = logo.text_3d("n", depth=0.3)
    local_state.textn.points *= 8.0
    local_state.textn.translate([4.0, 20.0, -0.0], inplace=True)
    local_state.textv = logo.text_3d("V", depth=0.3)
    local_state.textv.points *= 8.0
    local_state.textv.translate([12.0, 20.0, 0.0], inplace=True)
    local_state.texti = logo.text_3d("i", depth=0.3)
    local_state.texti.points *= 8.0
    local_state.texti.translate([22.0, 20.0, -0.0], inplace=True)
    local_state.texte = logo.text_3d("e", depth=0.3)
    local_state.texte.points *= 8.0
    local_state.texte.translate([26.0, 20.0, 0.0], inplace=True)
    local_state.textw = logo.text_3d("w", depth=0.3)
    local_state.textw.points *= 8.0
    local_state.textw.translate([34.0, 20.0, -0.0], inplace=True)
    local_state.text = logo.text_3d("Welcome to", depth=0.1)
    local_state.text.points *= 4.0
    local_state.text.translate([-20.0, 35.0, 0.0], inplace=True)
    local_state.text1 = logo.text_3d("@Qichen Xu", depth=0.1)
    local_state.text1.points *= 1.5
    local_state.text1.translate([40.0, 10.0, -0.0], inplace=True)
    local_state.text2 = logo.text_3d(
        "Suggestion: Executing from the simulation folder", depth=0.1
    )
    local_state.text2.points *= 2.0
    local_state.text2.translate([-17.0, -10.0, 0.0], inplace=True)

    # -----------------------------------------------------------------------------
    # Working path
    # -----------------------------------------------------------------------------
    if path_from_user == None:
        state.selected_dir = os.getcwd()
    else:
        state.selected_dir = os.path.abspath(os.path.expanduser(path_from_user))

    # Automatically select the first support file in the folder
    if pyvista_LR.outputfile_type == "auto":
        for i in os.listdir(state.selected_dir):
            if ".out" in i:
                pyvista_LR.outputfile_type = "uppasd"
                break
            elif ".ovf" in i:
                pyvista_LR.outputfile_type = "ovf"
                break
            elif ".data" in i:
                pyvista_LR.outputfile_type = "vampire"
                break
            elif ".bin" in i:
                pyvista_LR.outputfile_type = "Excalibur"
    if pyvista_LR.outputfile_type == "uppasd":
        try:
            foler_items_for_select = [
                a
                for a in os.listdir(state.selected_dir)
                if (
                    (".out" in a)
                    and ("coord" not in a)
                    and (("moment" in a) or ("restart" in a))
                )
            ]
            foler_items_for_select.sort()

            local_state.file_select_1 = foler_items_for_select[0]

            for i in foler_items_for_select:
                if (
                    foler_items_for_select[0][0] != i[0]
                    and local_state.file_select_1[0] != i[0]
                ):
                    local_state.file_select_2 = i
                    break
            if local_state.file_select_2 == None:
                for i in foler_items_for_select:
                    if local_state.file_select_1 != i:
                        local_state.file_select_2 = i
                        break
            if local_state.file_select_2 == None:
                local_state.file_select_2 = local_state.file_select_1

            for i in foler_items_for_select:
                if (
                    foler_items_for_select[0][0] != i[0]
                    and local_state.file_select_1[0] != i[0]
                    and local_state.file_select_2[0] != i[0]
                ):
                    local_state.file_select_3 = i
                    break
            if local_state.file_select_3 == None:
                for i in foler_items_for_select:
                    if (
                        local_state.file_select_1 != i
                        and local_state.file_select_2 != i
                    ):
                        local_state.file_select_3 = i
                        break
            if local_state.file_select_3 == None:
                local_state.file_select_3 = local_state.file_select_1

            for i in foler_items_for_select:
                if (
                    foler_items_for_select[0][0] != i[0]
                    and local_state.file_select_1[0] != i[0]
                    and local_state.file_select_2[0] != i[0]
                    and local_state.file_select_3[0] != i[0]
                ):
                    local_state.file_select_4 = i
                    break
            if local_state.file_select_4 == None:
                for i in foler_items_for_select:
                    if (
                        local_state.file_select_1 != i
                        and local_state.file_select_2 != i
                        and local_state.file_select_3 != i
                    ):
                        local_state.file_select_4 = i
                        break
            if local_state.file_select_4 == None:
                local_state.file_select_4 = local_state.file_select_1
        except:
            print("Please make sure in UppASD simulation folder.")

    elif pyvista_LR.outputfile_type == "ovf":
        try:
            foler_items_for_select = [
                a for a in os.listdir(state.selected_dir) if ".ovf" in a
            ]
            foler_items_for_select.sort()
            ovf_cleanname_list = []
            for filenames_ovf in foler_items_for_select:
                filenames_ovf = filenames_ovf[:-4]
                for i in range(len(filenames_ovf)):
                    i = i + 1
                    if filenames_ovf[-i].isdigit() == False:
                        ovf_cleanname_list.append(filenames_ovf[0 : -(i - 1)])
                        break

            # remove the duplicate name
            ovf_cleanname_list = list(set(ovf_cleanname_list))
            # print(ovf_cleanname_list)
            local_state.file_select_1 = ovf_cleanname_list[0]
            if len(ovf_cleanname_list) > 1:
                local_state.file_select_2 = ovf_cleanname_list[1]
            if len(ovf_cleanname_list) > 2:
                local_state.file_select_3 = ovf_cleanname_list[2]
            if len(ovf_cleanname_list) > 3:
                local_state.file_select_4 = ovf_cleanname_list[3]
            foler_items_for_select = ovf_cleanname_list
        except:
            print("No ovf file in current directory, please check if .ovf file exists")
            pass
    elif pyvista_LR.outputfile_type == "vampire":
        try:
            foler_items_for_select = [
                a
                for a in os.listdir(state.selected_dir)
                if ((".data" in a) and ("coord" not in a))
            ]
            foler_items_for_select.sort()
            vampire_cleanname_list = []
            for filenames_vampire in foler_items_for_select:
                filenames_vampire = filenames_vampire[:-5]
                for i in range(len(filenames_vampire)):
                    i = i + 1
                    if filenames_vampire[-i].isdigit() == False:
                        vampire_cleanname_list.append(filenames_vampire[0 : -(i - 1)])
                        break

            # remove the duplicate name
            vampire_cleanname_list = list(set(vampire_cleanname_list))
            # print(ovf_cleanname_list)
            local_state.file_select_1 = vampire_cleanname_list[0]
            if len(vampire_cleanname_list) > 1:
                local_state.file_select_2 = vampire_cleanname_list[1]
            if len(vampire_cleanname_list) > 2:
                local_state.file_select_3 = vampire_cleanname_list[2]
            if len(vampire_cleanname_list) > 3:
                local_state.file_select_4 = vampire_cleanname_list[3]
            foler_items_for_select = vampire_cleanname_list
        except:
            print(
                "No vampire file in current directory, please check if .ovf file exists"
            )
            pass
    elif pyvista_LR.outputfile_type == "Excalibur":
        try:
            foler_items_for_select = [
                a for a in os.listdir(state.selected_dir) if ".bin" in a
            ]
            foler_items_for_select.sort()
            bin_cleanname_list = []
            for filenames_bin in foler_items_for_select:
                filenames_bin = filenames_bin[:-4]
                for i in range(len(filenames_bin)):
                    i = i + 1
                    if filenames_bin[-i].isdigit() == False:
                        bin_cleanname_list.append(filenames_bin[0 : -(i - 1)])
                        break

            # remove the duplicate name
            bin_cleanname_list = list(set(bin_cleanname_list))
            # print(bin_cleanname_list)
            local_state.file_select_1 = bin_cleanname_list[0]
            if len(bin_cleanname_list) > 1:
                local_state.file_select_2 = bin_cleanname_list[1]
            if len(bin_cleanname_list) > 2:
                local_state.file_select_3 = bin_cleanname_list[2]
            if len(bin_cleanname_list) > 3:
                local_state.file_select_4 = bin_cleanname_list[3]
            foler_items_for_select = bin_cleanname_list
        except:
            print("No bin file in current directory, please check if .bin file exists")
            pass
    # if True:
    try:
        # Coord and magintude of atom will not change since we assume it is the same system.
        # the first subframe

        system_size_reader(pyvista_LR, working_dir=state.selected_dir)
        pyvista_LR.mom_name = local_state.file_select_1
        (
            local_state.coord,
            local_state.mom_states_x,
            local_state.mom_states_y,
            local_state.mom_states_z,
            local_state.moment_magintude_all,
        ) = parse_moment_and_coord_file(pyvista_LR, working_dir=state.selected_dir)
        # give the initial max frame number
        local_state.max_frame = (
            int(
                len(local_state.mom_states_x)
                / (
                    pyvista_LR.system_size[0]
                    * pyvista_LR.system_size[1]
                    * pyvista_LR.system_size[2]
                )
            )
            - 1
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

        if (
            local_state.sub_frame_number == 2
            or local_state.sub_frame_number == 3
            or local_state.sub_frame_number == 4
        ):
            pyvista_LR.mom_name1 = local_state.file_select_2
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

        if local_state.sub_frame_number == 3 or local_state.sub_frame_number == 4:
            # the third subframe
            pyvista_LR.mom_name2 = local_state.file_select_3
            (
                local_state.coord,
                local_state.mom_states_x2,
                local_state.mom_states_y2,
                local_state.mom_states_z2,
                local_state.moment_magintude_all,
            ) = parse_moment_and_coord_file2(pyvista_LR, working_dir=state.selected_dir)

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
            pyvista_LR.mom_name3 = local_state.file_select_4
            (
                local_state.coord,
                local_state.mom_states_x3,
                local_state.mom_states_y3,
                local_state.mom_states_z3,
                local_state.moment_magintude_all,
            ) = parse_moment_and_coord_file3(pyvista_LR, working_dir=state.selected_dir)

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

        local_state.point_cloud_arrow_for_face_cut = pv.PolyData(
            local_state.coord.copy()
        )
        plot_multiple_meshes(pyvista_LR, plotter, local_state)

    except Exception as e:
        print(
            "No input file in current directory is find, please upload your input file or change your working directory"
        )

        print("Here is the error information: ")
        print(e)
        raise

    viewer = get_or_create_viewer(plotter)
    viewer.view_isometric()
    viewer.reset_camera()
    # -----------------------------------------------------------------------------
    # Callbacks
    # -----------------------------------------------------------------------------

    # activations
    activation_callbacks_initialize(
        local_state, pyvista_LR, state, ctrl, plot_multiple_meshes, plotter, viewer
    )
    # tmesh
    (
        change_tmesh_cmap_vbtn_value_0,
        change_tmesh_cmap_vbtn_value_1,
        change_tmesh_cmap_vbtn_value_2,
        change_tmesh_cmap_vbtn_value_3,
        change_tmesh_cmap_vbtn_value_4,
        change_tmesh_opacity_index_vbtn_value_0,
        change_tmesh_opacity_index_vbtn_value_1,
        change_tmesh_opacity_index_vbtn_value_2,
        change_tmesh_opacity_index_vbtn_value_3,
        change_tmesh_opacity_index_vbtn_value_4,
        change_tmesh_opacity_index_vbtn_value_5,
        change_tmesh_opacity_index_vbtn_value_6,
        recalculate_tmesh,
        do_t_mesh_clip,
        do_clip_t_mesh_free_normal,
        Contour_0_tmesh,
        Contour_1_tmesh,
        Contour_2_tmesh,
        Contour_3_tmesh,
        Contour_4_tmesh,
    ) = tmesh_callbacks_initialize(
        local_state, pyvista_LR, state, ctrl, plot_multiple_meshes, plotter, viewer
    )
    # glyph
    (
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
    ) = glyphs_callbacks_initialize(
        local_state, pyvista_LR, state, ctrl, plot_multiple_meshes, plotter, viewer
    )
    # rmesh
    (
        Contour_0,
        Contour_1,
        Contour_2,
        Contour_3,
        Contour_4,
        change_rectangle_cmap_vbtn_value_0,
        change_rectangle_cmap_vbtn_value_1,
        change_rectangle_cmap_vbtn_value_2,
        change_rectangle_cmap_vbtn_value_3,
        change_rectangle_cmap_vbtn_value_4,
        change_rectangle_opacity_index_vbtn_value_0,
        change_rectangle_opacity_index_vbtn_value_1,
        change_rectangle_opacity_index_vbtn_value_2,
        change_rectangle_opacity_index_vbtn_value_3,
        change_rectangle_opacity_index_vbtn_value_4,
        change_rectangle_opacity_index_vbtn_value_5,
        change_rectangle_opacity_index_vbtn_value_6,
        do_r_mesh_clip,
        do_clip_r_mesh_free_normal,
    ) = rmesh_callbacks_initialize(
        local_state, pyvista_LR, state, ctrl, plot_multiple_meshes, plotter, viewer
    )
    # utils
    (
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
    ) = utilities_callbacks_initialize(
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
    )

    # -----------------------------------------------------------------------------
    # GUI
    # -----------------------------------------------------------------------------

    with SinglePageWithDrawerLayout(server, width=390) as layout:
        layout.title.set_text("SpinView V1.0.0")
        with layout.icon as icon:
            html.Img(src=spinview_logo.svlogo, height=50, width=125)

        toolbar_initialize(
            layout, viewer, local_state, pyvista_LR, cubemap_in_selector, ctrl
        )
        ################
        # The Drawer
        ################

        with layout.drawer as drawer:
            vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
            ######
            ##data
            ######
            exist_table_in_db = check_profile(db_path=db_path)
            data_initialize(
                local_state,
                pyvista_LR,
                state,
                ctrl,
                foler_items_for_select,
                exist_table_in_db,
            )

            vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
            ######
            ##objects
            ######
            object_initialize(local_state, pyvista_LR, state, spinview_checkbox)

            vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
            ######
            ##denoise
            ######
            denoise_initialize(local_state, pyvista_LR, state, ctrl)

            vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
            ######
            ##add projections
            ######
            projection_initialize(local_state, pyvista_LR, state, ctrl)

            vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))

            ######
            ##glyphs
            ######
            glyph_initialize(
                local_state, pyvista_LR, state, ctrl, spinview_checkbox, colors
            )

            vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
            ######
            ##r mesh
            ######
            rmesh_initialize(
                local_state, pyvista_LR, state, ctrl, spinview_checkbox, colors
            )

            vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
            vuetify.VDivider(vertical=False, inset=False)
            vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
            ######
            ##T mesh
            ######
            tmesh_initialize(
                local_state, pyvista_LR, state, ctrl, spinview_checkbox, colors
            )

            vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
            vuetify.VDivider(
                vertical=False,
                inset=False,
                style=("max-width: 390; min-height: 390;max-height: 20px"),
            )
            vuetify.VSpacer(style=("max-height: 40px; min-height: 40px"))
            ######
            ##Toolbar in drawer
            ######
            toolbar_drawer_initialize(
                layout, viewer, local_state, pyvista_LR, cubemap_in_selector, ctrl
            )

        with layout.content:
            with vuetify.VContainer(
                fluid=True,
                classes="pa-0 fill-height",
                id=1,
            ):
                view = plotter_ui(
                    plotter,
                    add_menu=False,
                    still_ratio=pyvista_still_ratio,
                    interactive_ratio=pyvista_interactive_ratio,
                    default_server_rendering=True,
                )
                ctrl.store_new_profile = store_new_profile
                ctrl.view_update = view.update
                ctrl.local_rendering_basic = run_local_rendering_basic
                ctrl.local_moive_rendering_basic = run_local_moive_rendering_basic
                # ctrl.loading_upload_file = loading_upload_file
                ctrl.download_transparent_screenshot = download_transparent_screenshot
                ctrl.download_normal_screenshot = download_normal_screenshot
                ctrl.change_glyph_cmap_vbtn_value_0 = change_glyph_cmap_vbtn_value_0
                ctrl.change_glyph_cmap_vbtn_value_1 = change_glyph_cmap_vbtn_value_1
                ctrl.change_glyph_cmap_vbtn_value_2 = change_glyph_cmap_vbtn_value_2
                ctrl.change_glyph_cmap_vbtn_value_3 = change_glyph_cmap_vbtn_value_3
                ctrl.change_glyph_cmap_vbtn_value_4 = change_glyph_cmap_vbtn_value_4
                ctrl.change_glyph_opacity_index_vbtn_value_0 = (
                    change_glyph_opacity_index_vbtn_value_0
                )
                ctrl.change_glyph_opacity_index_vbtn_value_1 = (
                    change_glyph_opacity_index_vbtn_value_1
                )
                ctrl.change_glyph_opacity_index_vbtn_value_2 = (
                    change_glyph_opacity_index_vbtn_value_2
                )
                ctrl.change_glyph_opacity_index_vbtn_value_3 = (
                    change_glyph_opacity_index_vbtn_value_3
                )
                ctrl.change_glyph_opacity_index_vbtn_value_4 = (
                    change_glyph_opacity_index_vbtn_value_4
                )
                ctrl.change_glyph_opacity_index_vbtn_value_5 = (
                    change_glyph_opacity_index_vbtn_value_5
                )
                ctrl.change_glyph_opacity_index_vbtn_value_6 = (
                    change_glyph_opacity_index_vbtn_value_6
                )
                ctrl.change_point_rescale_vbtn_value_0 = (
                    change_point_rescale_vbtn_value_0
                )
                ctrl.change_point_rescale_vbtn_value_1 = (
                    change_point_rescale_vbtn_value_1
                )
                ctrl.change_point_rescale_vbtn_value_2 = (
                    change_point_rescale_vbtn_value_2
                )
                ctrl.change_point_rescale_vbtn_value_3 = (
                    change_point_rescale_vbtn_value_3
                )
                ctrl.change_point_rescale_vbtn_value_4 = (
                    change_point_rescale_vbtn_value_4
                )
                ctrl.applied_point_rescale_norm = applied_point_rescale_norm
                ctrl.do_sp_warp = do_sp_warp
                ctrl.sp_warp_kernel = sp_warp_kernel
                ctrl.denoising_N = denoising_N
                ctrl.denoising_low_pass = denoising_low_pass
                ctrl.denoising_low_pass_fft_rec = denoising_low_pass_fft_rec
                ctrl.do_clip_plane_fix_origin_and_normal = (
                    do_clip_plane_fix_origin_and_normal
                )
                ctrl.do_clip_plane_free_normal = do_clip_plane_free_normal
                ctrl.add_projection_plane_1 = add_projection_plane_1
                ctrl.add_projection_plane_2 = add_projection_plane_2
                ctrl.add_projection_plane_3 = add_projection_plane_3
                ctrl.add_projection_plane_4 = add_projection_plane_4
                ctrl.add_projection_plane_5 = add_projection_plane_5
                ctrl.add_projection_plane_6 = add_projection_plane_6
                ctrl.Contour_0 = Contour_0
                ctrl.Contour_1 = Contour_1
                ctrl.Contour_2 = Contour_2
                ctrl.Contour_3 = Contour_3
                ctrl.Contour_4 = Contour_4
                ctrl.change_rectangle_cmap_vbtn_value_0 = (
                    change_rectangle_cmap_vbtn_value_0
                )
                ctrl.change_rectangle_cmap_vbtn_value_1 = (
                    change_rectangle_cmap_vbtn_value_1
                )
                ctrl.change_rectangle_cmap_vbtn_value_2 = (
                    change_rectangle_cmap_vbtn_value_2
                )
                ctrl.change_rectangle_cmap_vbtn_value_3 = (
                    change_rectangle_cmap_vbtn_value_3
                )
                ctrl.change_rectangle_cmap_vbtn_value_4 = (
                    change_rectangle_cmap_vbtn_value_4
                )
                ctrl.change_rectangle_opacity_index_vbtn_value_0 = (
                    change_rectangle_opacity_index_vbtn_value_0
                )
                ctrl.change_rectangle_opacity_index_vbtn_value_1 = (
                    change_rectangle_opacity_index_vbtn_value_1
                )
                ctrl.change_rectangle_opacity_index_vbtn_value_2 = (
                    change_rectangle_opacity_index_vbtn_value_2
                )
                ctrl.change_rectangle_opacity_index_vbtn_value_3 = (
                    change_rectangle_opacity_index_vbtn_value_3
                )
                ctrl.change_rectangle_opacity_index_vbtn_value_4 = (
                    change_rectangle_opacity_index_vbtn_value_4
                )
                ctrl.change_rectangle_opacity_index_vbtn_value_5 = (
                    change_rectangle_opacity_index_vbtn_value_5
                )
                ctrl.change_rectangle_opacity_index_vbtn_value_6 = (
                    change_rectangle_opacity_index_vbtn_value_6
                )
                ctrl.do_r_mesh_clip = do_r_mesh_clip
                ctrl.do_clip_r_mesh_free_normal = do_clip_r_mesh_free_normal
                ctrl.change_tmesh_cmap_vbtn_value_0 = change_tmesh_cmap_vbtn_value_0
                ctrl.change_tmesh_cmap_vbtn_value_1 = change_tmesh_cmap_vbtn_value_1
                ctrl.change_tmesh_cmap_vbtn_value_2 = change_tmesh_cmap_vbtn_value_2
                ctrl.change_tmesh_cmap_vbtn_value_3 = change_tmesh_cmap_vbtn_value_3
                ctrl.change_tmesh_cmap_vbtn_value_4 = change_tmesh_cmap_vbtn_value_4
                ctrl.change_tmesh_opacity_index_vbtn_value_0 = (
                    change_tmesh_opacity_index_vbtn_value_0
                )
                ctrl.change_tmesh_opacity_index_vbtn_value_1 = (
                    change_tmesh_opacity_index_vbtn_value_1
                )
                ctrl.change_tmesh_opacity_index_vbtn_value_2 = (
                    change_tmesh_opacity_index_vbtn_value_2
                )
                ctrl.change_tmesh_opacity_index_vbtn_value_3 = (
                    change_tmesh_opacity_index_vbtn_value_3
                )
                ctrl.change_tmesh_opacity_index_vbtn_value_4 = (
                    change_tmesh_opacity_index_vbtn_value_4
                )
                ctrl.change_tmesh_opacity_index_vbtn_value_5 = (
                    change_tmesh_opacity_index_vbtn_value_5
                )
                ctrl.change_tmesh_opacity_index_vbtn_value_6 = (
                    change_tmesh_opacity_index_vbtn_value_6
                )
                ctrl.recalculate_tmesh = recalculate_tmesh
                ctrl.do_t_mesh_clip = do_t_mesh_clip
                ctrl.do_clip_t_mesh_free_normal = do_clip_t_mesh_free_normal
                ctrl.Contour_0_tmesh = Contour_0_tmesh
                ctrl.Contour_1_tmesh = Contour_1_tmesh
                ctrl.Contour_2_tmesh = Contour_2_tmesh
                ctrl.Contour_3_tmesh = Contour_3_tmesh
                ctrl.Contour_4_tmesh = Contour_4_tmesh

        # clean the trame footer
        with layout.footer as footer:
            footer.clear()

        layout.footer.set_text(
            ":::::::::SpinView V1.0.0 ::::::::: qichenx@kth.se:::::::::::::::"
        )

    if trame_exec_mode == "main":
        print(
            "[bold red]S[/bold red][#FFA500]p[/#FFA500][bold Yellow]i[/bold Yellow][bold green]n[/bold green][bold Blue]V[/bold Blue][bold green]i[/bold green][#FF1493]e[/#FF1493][bold Purple]w [/bold Purple] running on [link]http://{}:{}/[/link]".format(
                trame_host, port_number
            )
        )
        server.start(
            exec_mode=trame_exec_mode,
            host=trame_host,
            open_browser=trame_open_browser,
            port=port_number,
            show_connection_info=False,
            timeout=0,
        )
    elif trame_exec_mode == "desktop":
        print(
            "[bold red]S[/bold red][#FFA500]p[/#FFA500][bold Yellow]i[/bold Yellow][bold green]n[/bold green][bold Blue]V[/bold Blue][bold green]i[/bold green][#FF1493]e[/#FF1493][bold Purple]w [/bold Purple] start with pywebview windows size: {} X {}".format(
                pywebview_windows_size_x, pywebview_windows_size_y
            )
        )
        server.start(
            exec_mode=trame_exec_mode,
            host=trame_host,
            open_browser=trame_open_browser,
            port=port_number,
            show_connection_info=False,
            timeout=0,
            width=pywebview_windows_size_x,
            height=pywebview_windows_size_y,
        )


if __name__ == "__main__":
    webui_realspace()
