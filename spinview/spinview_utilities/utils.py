"""
In this file, we have all supporting functions for the project

Author: Qichen Xu mxjk851@gmail.com/qichenx@kth.se

2023-7-10

Wish you have 'sommartid'(summer time) everyday!

"""

from rich import print
from trame.widgets import vuetify, html
import numpy as np
import pyvista as pv
from scipy import signal
from scipy.fft import fftn, ifftn, fftshift, ifftshift


from inspect import getframeinfo, stack


def Brick_title(title, color_in="grey", size_in="small"):
    vuetify.VCardTitle(
        title,
        classes="{} py-1 grey--text text--darken-3".format(color_in),
        style="user-select: none; cursor: pointer",
        hide_details=True,
        size=size_in,
        dense=True,
    )
    content = vuetify.VCardText(classes="py-2")
    return content


def spinview_checkbox(model, on_icon, off_icon, label, tooltip=None, color_in="grey"):
    with vuetify.VTooltip(bottom=True):
        with vuetify.Template(v_slot_activator="{ on, attrs }"):
            with html.Div(v_on="on", v_bind="attrs"):
                vuetify.VCheckbox(
                    v_model=model,
                    on_icon=on_icon,
                    off_icon=off_icon,
                    label=label,
                    dense=False,
                    hide_details=True,
                    ripple=True,
                    color=color_in,
                    classes="grey--text text--darken-3",
                )
        if tooltip is not None:
            html.Span(tooltip, classes="small")


def VExpansionPanels_title(title):
    vuetify.VExpansionPanels(
        title,
        # classes="grey lighten-1 py-1 grey--text text--darken-3",
        # style="user-select: none; cursor: pointer",
        # hide_details=True,
        size="small",
        focusable=True,
        popout=True,
        # dense=True,
    )
    content = vuetify.VCardText(classes="py-2")
    return content


def normalize(v):
    norm = np.sqrt(np.einsum("ij,ij->i", v, v))
    res = np.array([v[:, 0] / norm, v[:, 1] / norm, v[:, 2] / norm]).T
    return res


def nothing_show_welcome_image_rendering(plotter, subplot_index_list=[0, 0]):
    if local_state.welcome_image_not_created:
        plotter.subplot(subplot_index_list[0], subplot_index_list[1])
        glyphs_list = [
            local_state.texts,
            local_state.textp,
            local_state.texti1,
            local_state.textn,
            local_state.textv,
            local_state.texti,
            local_state.texte,
            local_state.textw,
            local_state.text,
            local_state.text1,
        ]
        color_list = [
            "orangered",
            "gold",
            "yellow",
            "springgreen",
            "royalblue",
            "forestgreen",
            "magenta",
            "violet",
            "lavender",
            "black",
        ]
        names = globals()
        for i in range(1, 11):
            names[
                "em"
                + str(i)
                + "_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1])
            ] = plotter.add_mesh(
                glyphs_list[i - 1],
                color=color_list[i - 1],
                pbr=True,
                metallic=0.1,
                roughness=0.1,
            )
    else:
        eval(
            "em"
            + str(i)
            + "_"
            + str(subplot_index_list[0])
            + str(subplot_index_list[1])
        ).SetVisibility(True)


def nothing_show_welcome_image_removing(plotter, subplot_index_list=[0, 0]):
    try:
        # print('start removing welcome image')
        for i in range(1, 11):
            eval(
                "em"
                + str(i)
                + "_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1])
            ).SetVisibility(False)
    except:
        pass
        # print('no welcome image to remove')


def asSpherical(xyz):
    # takes list xyz (single coord)
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]
    r = np.sqrt(x * x + y * y + z * z)
    theta = np.arccos(z / r) * 180 / np.pi  # to degrees
    phi = np.arctan2(y, x) * 180 / np.pi
    return [theta, phi]


def asCartesian(sph_coords):
    # takes list rthetaphi (single coord)
    r = sph_coords[0]
    theta = sph_coords[1] * np.pi / 180  # to radian
    phi = sph_coords[2] * np.pi / 180
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return np.array([x, y, z])


def plotter_add_mesh(
    pyvista_LR,
    coord_xyz,
    mom_states_x,
    mom_states_y,
    mom_states_z,
    plotter,
    subplot_index_list=[0, 0],
    local_state=None,
):
    print(
        "[bold red]S[/bold red][#FFA500]p[/#FFA500][bold Yellow]i[/bold Yellow][bold green]n[/bold green][bold Blue]V[/bold Blue][bold green]i[/bold green][#FF1493]e[/#FF1493][bold Purple]w [/bold Purple] processing  ... ..."
    )
    actor_name_list = [
        "actor_unstructured_mesh",
        "actor_own",
        "actor_box",
        "actor_plane",
        "actor_sphere",
        "actor_arrow",
        "actor_cone",
        "actor_rectangle_mesh",
    ]
    actor_list = globals()

    ######
    # Bgc or CubeMap
    ######

    plotter.subplot(subplot_index_list[0], subplot_index_list[1])

    plotter.background_color = pyvista_LR.bgc

    #########
    # Denosing filter, dev feature now. but should works well, at least for the demo
    # only low pass offered in this version, band pass will introduced in furture version
    #########

    if local_state.start_desoning_filter_index == 0:
        vectors = np.vstack([mom_states_x, mom_states_y, mom_states_z])

    elif local_state.start_desoning_filter_index == 1:
        #########
        # Low pass butterworth filter
        #########
        b, a = signal.butter(
            local_state.low_pass_filter_order,
            local_state.low_pass_normalized_freq,
            "lowpass",
        )
        filted_mom_states_x = signal.filtfilt(b, a, mom_states_x)
        filted_mom_states_y = signal.filtfilt(b, a, mom_states_y)
        filted_mom_states_z = signal.filtfilt(b, a, mom_states_z)
        normed_mom = normalize(
            np.array([filted_mom_states_x, filted_mom_states_y, filted_mom_states_z]).T
        )
        vectors = np.vstack([normed_mom[:, 0], normed_mom[:, 1], normed_mom[:, 2]])

    elif local_state.start_desoning_filter_index == 2:
        #########
        # Low pass FFT-rec-windows filter
        #########
        # make the low-pass windows
        c_x, c_y, c_z = (
            int(pyvista_LR.system_size[0] / 2),
            int(pyvista_LR.system_size[1] / 2),
            int(pyvista_LR.system_size[2] / 2),
        )
        mask = np.zeros(
            (
                int(pyvista_LR.system_size[0]),
                int(pyvista_LR.system_size[1]),
                int(pyvista_LR.system_size[2]),
            ),
            np.uint8,
        )
        mask[
            c_x - local_state.fft_rec_windows_X : c_x + local_state.fft_rec_windows_X,
            c_y - local_state.fft_rec_windows_Y : c_y + local_state.fft_rec_windows_Y,
            c_z - local_state.fft_rec_windows_Z : c_z + local_state.fft_rec_windows_Z,
        ] = 1

        # handle the X component
        before_fft_X = mom_states_x.reshape(
            int(pyvista_LR.system_size[0]),
            int(pyvista_LR.system_size[1]),
            int(pyvista_LR.system_size[2]),
        )
        after_fft_X = fftn(before_fft_X)
        after_fft_central_X = fftshift(after_fft_X)
        f_X = after_fft_central_X * mask
        f_X = ifftshift(f_X)
        ishift_X = ifftn(f_X).reshape(
            int(
                pyvista_LR.system_size[0]
                * pyvista_LR.system_size[1]
                * pyvista_LR.system_size[2]
            ),
            1,
        )

        # handle the Y component
        before_fft_Y = mom_states_y.reshape(
            int(pyvista_LR.system_size[0]),
            int(pyvista_LR.system_size[1]),
            int(pyvista_LR.system_size[2]),
        )
        after_fft_Y = fftn(before_fft_Y)
        after_fft_central_Y = fftshift(after_fft_Y)
        f_Y = after_fft_central_Y * mask
        f_Y = ifftshift(f_Y)
        ishift_Y = ifftn(f_Y).reshape(
            int(
                pyvista_LR.system_size[0]
                * pyvista_LR.system_size[1]
                * pyvista_LR.system_size[2]
            ),
            1,
        )

        # handle the Z component
        before_fft_Z = mom_states_z.reshape(
            int(pyvista_LR.system_size[0]),
            int(pyvista_LR.system_size[1]),
            int(pyvista_LR.system_size[2]),
        )
        after_fft_Z = fftn(before_fft_Z)
        after_fft_central_Z = fftshift(after_fft_Z)
        f_Z = after_fft_central_Z * mask
        f_Z = ifftshift(f_Z)
        ishift_Z = ifftn(f_Z).reshape(
            int(
                pyvista_LR.system_size[0]
                * pyvista_LR.system_size[1]
                * pyvista_LR.system_size[2]
            ),
            1,
        )

        normed_mom = normalize(
            np.array([np.real(ishift_X), np.real(ishift_Y), np.real(ishift_Z)]).T[0]
        )
        vectors = np.vstack([normed_mom[:, 0], normed_mom[:, 1], normed_mom[:, 2]])

    vectors_PolyData_1 = vectors.copy()
    vectors_PolyData_2 = vectors.copy()
    vectors_PolyData_3 = vectors.copy()
    vectors_PolyData_4 = vectors.copy()
    # get polar angle theta and the azimuthal angle phi in spherical coordinates
    theta, phi = asSpherical(vectors)
    theta_for_sphere_warp = theta.copy()
    phi_for_sphere_warp = phi.copy()
    # works for cmap
    c_theta = theta
    c_phi = phi
    # works for opacity  in [-1,1]
    o_theta = (180 - theta) / 180
    o_theta2 = theta / 180
    o_phi = (phi + 180) / 360

    ####################################
    #
    #   Sphere warpping
    #
    # prepare point_cloud_arrow for sphere warpping
    # this should be a local variable, now it in local_state
    # maybe in furture it would be a store in pyvista_LR
    #
    ####################################
    sph_coords = [
        np.ones(np.shape(theta_for_sphere_warp)) * local_state.warp_sphere_radius,
        theta_for_sphere_warp,
        phi_for_sphere_warp,
    ]
    cart = asCartesian(sph_coords).T
    global swk

    if local_state.add_warpped_sphere_kernel and pyvista_LR.add_glyphs:
        swk = plotter.add_mesh(
            pv.Sphere(
                center=(
                    0 - local_state.warp_sphere_radius * 1.1,
                    0 - local_state.warp_sphere_radius * 1.1,
                    0 - local_state.warp_sphere_radius * 1.1,
                ),
                radius=local_state.warp_sphere_radius
                * local_state.warpped_sphere_kernel,
                theta_resolution=local_state.warp_sphere_radius * 20,
                phi_resolution=local_state.warp_sphere_radius * 20,
            ),
            color=local_state.warp_kernel_color[0],
            opacity=1,
            pbr=True,
            name="warpped_sphere_kernel",
        )
        local_state.swk_added = True
        local_state.warp_kernel_color_changed = False

    if local_state.do_warp_sphere:
        point_cloud_arrow = pv.PolyData(cart - local_state.warp_sphere_radius * 1.1)

    else:
        point_cloud_arrow = pv.PolyData(coord_xyz)

    if local_state.do_warp_sphere == False and local_state.swk_added:
        swk.SetVisibility(False)
        local_state.swk_added = False

    ####################################
    # Try to remove welcome
    ####################################
    if (
        local_state.excu_from_other_place == True
        and local_state.excu_from_other_place_welcome_image == True
    ):
        local_state.excu_from_other_place_welcome_image = False
        local_state.excu_from_other_place = False
        try:
            plotter.remove_actor(em1_w)
            plotter.remove_actor(em2_w)
            plotter.remove_actor(em3_w)
            plotter.remove_actor(em4_w)
            plotter.remove_actor(em5_w)
            plotter.remove_actor(em6_w)
            plotter.remove_actor(em7_w)
            plotter.remove_actor(em8_w)
            plotter.remove_actor(em9_w)
            plotter.remove_actor(em10_w)
            plotter.remove_actor(em11_w)
        except:
            print("Oops, welcome information seeems not removed")
            pass
    ####################################
    # prepare point_cloud_arrow for glyph
    ####################################
    if pyvista_LR.add_glyphs:
        local_state.nothing_show = False
        # record all cmap component and opacity component  We use RGBA colorspace in the project
        if int(pyvista_LR.color_map_index) in [0, 1, 2]:
            point_cloud_arrow["color_component"] = vectors_PolyData_1[
                pyvista_LR.color_map_index, :
            ]
            local_state.clim_range = [-1, 1]
            if int(pyvista_LR.color_map_index) == 0:
                local_state.glyph_scalar_bar_name = "G_x"
            elif int(pyvista_LR.color_map_index) == 1:
                local_state.glyph_scalar_bar_name = "G_y"
            elif int(pyvista_LR.color_map_index) == 2:
                local_state.glyph_scalar_bar_name = "G_z"
        elif int(pyvista_LR.color_map_index) == 3:
            point_cloud_arrow["color_component"] = c_theta
            local_state.clim_range = [0, 180]
            local_state.glyph_scalar_bar_name = "G_theta"
        elif int(pyvista_LR.color_map_index) == 4:
            local_state.clim_range = [-180, 180]
            point_cloud_arrow["color_component"] = c_phi
            local_state.glyph_scalar_bar_name = "G_phi"

        if int(pyvista_LR.opacity_index) == 3:
            point_cloud_arrow["opacity_component"] = o_theta
        elif int(pyvista_LR.opacity_index) == 4:
            point_cloud_arrow["opacity_component"] = o_theta2
        elif int(pyvista_LR.opacity_index) == 5:
            point_cloud_arrow["opacity_component"] = o_phi
        elif int(pyvista_LR.opacity_index) in [0, 1, 2]:
            point_cloud_arrow["opacity_component"] = (
                vectors_PolyData_1.copy()[pyvista_LR.opacity_index, :] + 1
            ) / 2
        elif int(pyvista_LR.opacity_index) == 6:
            point_cloud_arrow["opacity_component"] = (
                np.ones(len(o_phi)) * pyvista_LR.opacity_record
            )

        point_cloud_arrow[
            "vectors"
        ] = (
            vectors_PolyData_2.T
        )  # I remove a copy here, if something strange happens, check this line.:
        # magnitude is used for scaling the arrow when the system is a alloy system.
        point_cloud_arrow["magnitute"] = local_state.moment_magintude
        point_cloud_arrow["rescale_x"] = vectors_PolyData_1[0, :]
        point_cloud_arrow["rescale_y"] = vectors_PolyData_1[1, :]
        point_cloud_arrow["rescale_z"] = vectors_PolyData_1[2, :]
        point_cloud_arrow["rescale_phi"] = c_phi  # range [-180,180]
        point_cloud_arrow["rescale_theta"] = c_theta  # range [0,180]

        point_cloud_arrow["x_com"] = vectors_PolyData_1[0, :]
        point_cloud_arrow["y_com"] = vectors_PolyData_1[1, :]
        point_cloud_arrow["z_com"] = vectors_PolyData_1[2, :]
        point_cloud_arrow["phi_com"] = c_phi  # range [-180,180]
        point_cloud_arrow["theta_com"] = c_theta  # range [0,180]

    #################################################
    # prepare meshdata_rectangle for rectangle mesh
    #################################################
    if pyvista_LR.add_rectangle_mesh and local_state.do_warp_sphere == False:
        ########################
        # Mesh Color
        ########################
        if int(pyvista_LR.rectrangle_color_index) in [0, 1, 2]:
            local_state.rectrangle_mesh_image_data = vectors_PolyData_4[
                pyvista_LR.rectrangle_color_index, :
            ]
            local_state.rectrangle_clim_range = [-1, 1]
            if int(pyvista_LR.rectrangle_color_index) == 0:
                local_state.rectangle_mesh_scalar_bar_name = "RM_x"
                local_state.rec_mesh_color_scalar = "x_com"
            elif int(pyvista_LR.rectrangle_color_index) == 1:
                local_state.rectangle_mesh_scalar_bar_name = "RM_y"
                local_state.rec_mesh_color_scalar = "y_com"
            elif int(pyvista_LR.rectrangle_color_index) == 2:
                local_state.rectangle_mesh_scalar_bar_name = "RM_z"
                local_state.rec_mesh_color_scalar = "z_com"

        elif int(pyvista_LR.rectrangle_color_index) == 3:
            local_state.rectrangle_mesh_image_data = c_theta
            local_state.rectrangle_clim_range = [0, 180]
            local_state.rectangle_mesh_scalar_bar_name = "RM_theta"
            local_state.rec_mesh_color_scalar = "theta_com"
        elif int(pyvista_LR.rectrangle_color_index) == 4:
            local_state.rectrangle_clim_range = [-180, 180]
            local_state.rectrangle_mesh_image_data = c_phi
            local_state.rectangle_mesh_scalar_bar_name = "RM_phi"
            local_state.rec_mesh_color_scalar = "phi_com"
        ########################
        # Mesh Opacity
        ########################
        if int(pyvista_LR.rectrangle_opacity_index) == 3:
            local_state.rectrangle_mesh_opacity = o_theta
        elif int(pyvista_LR.rectrangle_opacity_index) == 4:
            local_state.rectrangle_mesh_opacity = o_theta2
        elif int(pyvista_LR.rectrangle_opacity_index) == 5:
            local_state.rectrangle_mesh_opacity = o_phi
        elif int(pyvista_LR.rectrangle_opacity_index) in [0, 1, 2]:
            local_state.rectrangle_mesh_opacity = (
                vectors_PolyData_4.copy()[pyvista_LR.rectrangle_opacity_index, :] + 1
            ) / 2
        elif (
            int(pyvista_LR.rectrangle_opacity_index) == 6
        ):  # this is use user's own opacity for whole mesh
            local_state.rectrangle_mesh_opacity = (
                np.ones(len(o_phi)) * local_state.opacity_record_rectangle_mesh
            )

    ####################################################
    # prepare meshdata_unstructured for unstructured mesh
    ####################################################
    if pyvista_LR.add_unstructured_mesh and local_state.do_warp_sphere == False:
        point_cloud_arrow_unstructured = pv.PolyData(coord_xyz)
        point_cloud_arrow_unstructured["vectors"] = vectors_PolyData_3.T

        # record all cmap component and opacity component  We use RGBA colorspace in the project
        point_cloud_arrow_unstructured["UM_x"] = vectors_PolyData_1[0, :]
        point_cloud_arrow_unstructured["UM_y"] = vectors_PolyData_1[1, :]
        point_cloud_arrow_unstructured["UM_z"] = vectors_PolyData_1[2, :]
        point_cloud_arrow_unstructured["UM_theta"] = c_theta.copy()
        point_cloud_arrow_unstructured["UM_phi"] = c_phi.copy()

        point_cloud_arrow_unstructured["opacity_UM_theta"] = o_theta
        point_cloud_arrow_unstructured["opacity_UM_theta2"] = o_theta2
        point_cloud_arrow_unstructured["opacity_UM_phi"] = o_phi
        point_cloud_arrow_unstructured["opacity_UM_x"] = (
            vectors_PolyData_1.copy()[0, :] + 1
        ) / 2
        point_cloud_arrow_unstructured["opacity_UM_y"] = (
            vectors_PolyData_1.copy()[1, :] + 1
        ) / 2
        point_cloud_arrow_unstructured["opacity_UM_z"] = (
            vectors_PolyData_1.copy()[2, :] + 1
        ) / 2
        point_cloud_arrow_unstructured["free_t_mesh_opacity_component"] = (
            np.ones(len(o_phi)) * local_state.opacity_record_tmesh
        )

        point_cloud_arrow_unstructured["rescale_x"] = vectors_PolyData_1[0, :]
        point_cloud_arrow_unstructured["rescale_y"] = vectors_PolyData_1[1, :]
        point_cloud_arrow_unstructured["rescale_z"] = vectors_PolyData_1[2, :]
        point_cloud_arrow_unstructured["rescale_phi"] = c_phi  # range [-180,180]
        point_cloud_arrow_unstructured["rescale_theta"] = c_theta  # range [0,180]

        if int(pyvista_LR.unstructured_mesh_color_map_index) in [0, 1, 2]:
            local_state.clim_range_unstructured_mesh = [-1, 1]
            if int(pyvista_LR.unstructured_mesh_color_map_index) == 0:
                local_state.unstructured_mesh_scalar_bar_name = "UM_x"
            elif int(pyvista_LR.unstructured_mesh_color_map_index) == 1:
                local_state.unstructured_mesh_scalar_bar_name = "UM_y"
            elif int(pyvista_LR.unstructured_mesh_color_map_index) == 2:
                local_state.unstructured_mesh_scalar_bar_name = "UM_z"

        elif int(pyvista_LR.unstructured_mesh_color_map_index) == 3:
            point_cloud_arrow_unstructured["color_component"] = c_theta
            local_state.clim_range_unstructured_mesh = [0, 180]
            local_state.unstructured_mesh_scalar_bar_name = "UM_theta"
        elif int(pyvista_LR.unstructured_mesh_color_map_index) == 4:
            local_state.clim_range_unstructured_mesh = [-180, 180]
            point_cloud_arrow_unstructured["color_component"] = c_phi
            local_state.unstructured_mesh_scalar_bar_name = "UM_phi"

        if int(pyvista_LR.unstructured_mesh_color_map_opacity_index) == 3:
            local_state.tmesh_op_indicator = "opacity_UM_theta"
        elif int(pyvista_LR.unstructured_mesh_color_map_opacity_index) == 4:
            local_state.tmesh_op_indicator = "opacity_UM_theta2"
        elif int(pyvista_LR.unstructured_mesh_color_map_opacity_index) == 5:
            local_state.tmesh_op_indicator = "opacity_UM_phi"
        elif int(pyvista_LR.unstructured_mesh_color_map_opacity_index) in [0]:
            local_state.tmesh_op_indicator = "opacity_UM_x"
        elif int(pyvista_LR.unstructured_mesh_color_map_opacity_index) in [0]:
            local_state.tmesh_op_indicator = "opacity_UM_y"
        elif int(pyvista_LR.unstructured_mesh_color_map_opacity_index) in [0]:
            local_state.tmesh_op_indicator = "opacity_UM_z"
        elif int(pyvista_LR.unstructured_mesh_color_map_opacity_index) == 6:
            local_state.tmesh_op_indicator = "free_t_mesh_opacity_component"

    ####################################################
    # add all glpyhs
    ####################################################
    if pyvista_LR.add_glyphs:
        ########################
        # Rescale
        # here the name is little bit confusing and should be refactored, it is for all glyphs not only for simple point
        # but now I think we the rescale operator should be a global operator for all glyphs.
        # Have chance to split it in the future.
        ########################
        if pyvista_LR.do_glyph_simple_point_rescale:
            if pyvista_LR.rescale_simple_point_index == 0:
                point_cloud_arrow = point_cloud_arrow.copy().warp_by_scalar(
                    "rescale_x",
                    factor=pyvista_LR.rescale_simple_point_factor,
                    normal=pyvista_LR.rescale_simple_point_norm,
                )
            elif pyvista_LR.rescale_simple_point_index == 1:
                point_cloud_arrow = point_cloud_arrow.copy().warp_by_scalar(
                    "rescale_y",
                    factor=pyvista_LR.rescale_simple_point_factor,
                    normal=pyvista_LR.rescale_simple_point_norm,
                )
            elif pyvista_LR.rescale_simple_point_index == 2:
                point_cloud_arrow = point_cloud_arrow.copy().warp_by_scalar(
                    "rescale_z",
                    factor=pyvista_LR.rescale_simple_point_factor,
                    normal=pyvista_LR.rescale_simple_point_norm,
                )
            elif pyvista_LR.rescale_simple_point_index == 3:
                point_cloud_arrow = point_cloud_arrow.copy().warp_by_scalar(
                    "rescale_phi",
                    factor=pyvista_LR.rescale_simple_point_factor,
                    normal=pyvista_LR.rescale_simple_point_norm,
                )
            elif pyvista_LR.rescale_simple_point_index == 4:
                point_cloud_arrow = point_cloud_arrow.copy().warp_by_scalar(
                    "rescale_theta",
                    factor=pyvista_LR.rescale_simple_point_factor,
                    normal=pyvista_LR.rescale_simple_point_norm,
                )
        else:
            point_cloud_arrow = point_cloud_arrow.copy()

        ########################
        # scalar clip
        ########################

        if pyvista_LR.do_clip_component:
            point_cloud_arrow = point_cloud_arrow.clip_scalar(
                scalars="x_com", invert=True, value=pyvista_LR.x_compoment_filter_max
            )
            point_cloud_arrow = point_cloud_arrow.clip_scalar(
                scalars="x_com", invert=False, value=pyvista_LR.x_compoment_filter_min
            )
            point_cloud_arrow = point_cloud_arrow.clip_scalar(
                scalars="y_com", invert=True, value=pyvista_LR.y_compoment_filter_max
            )
            point_cloud_arrow = point_cloud_arrow.clip_scalar(
                scalars="y_com", invert=False, value=pyvista_LR.y_compoment_filter_min
            )
            point_cloud_arrow = point_cloud_arrow.clip_scalar(
                scalars="z_com", invert=True, value=pyvista_LR.z_compoment_filter_max
            )
            point_cloud_arrow = point_cloud_arrow.clip_scalar(
                scalars="z_com", invert=False, value=pyvista_LR.z_compoment_filter_min
            )
            point_cloud_arrow = point_cloud_arrow.clip_scalar(
                scalars="phi_com",
                invert=True,
                value=pyvista_LR.phi_compoment_filter_max,
            )
            point_cloud_arrow = point_cloud_arrow.clip_scalar(
                scalars="phi_com",
                invert=False,
                value=pyvista_LR.phi_compoment_filter_min,
            )
            point_cloud_arrow = point_cloud_arrow.clip_scalar(
                scalars="theta_com",
                invert=True,
                value=pyvista_LR.theta_compoment_filter_max,
            )
            point_cloud_arrow = point_cloud_arrow.clip_scalar(
                scalars="theta_com",
                invert=False,
                value=pyvista_LR.theta_compoment_filter_min,
            )

        ########################
        # face clip
        ########################
        if (
            pyvista_LR.do_clip_plane_fix_origin_and_normal
            and local_state.do_warp_sphere == False
        ):
            # Here we first have 3 sliders for X,Y and Z axis, respectively.
            # The slider should be start from the beginning of the axis to the end (max length)of the axis.
            # This fliter start from the (x_min,y_min,z_min).
            # if needed we add pyvista_LR.do_clip_plane_variable_origin_and_normal,clip_component.do_clip_box

            # Remember to show the max and min of the axis in the slider.(prepend and append icon)
            # Here we have 6 slider start from 0 and end with point_cloud_arrow.bounds[1,3,5]

            if (
                pyvista_LR.clip_plane_x_max - pyvista_LR.clip_plane_x_min <= 1
            ):  # only max than 1 is valid for clip
                pass
            else:
                point_cloud_arrow = point_cloud_arrow.copy().clip(
                    "x",
                    invert=False,
                    origin=(
                        point_cloud_arrow.bounds[0],
                        point_cloud_arrow.bounds[2],
                        point_cloud_arrow.bounds[4],
                    ),
                    value=pyvista_LR.clip_plane_x_min,
                )
                point_cloud_arrow = point_cloud_arrow.copy().clip(
                    "x",
                    invert=True,
                    origin=(
                        point_cloud_arrow.bounds[0],
                        point_cloud_arrow.bounds[2],
                        point_cloud_arrow.bounds[4],
                    ),
                    value=pyvista_LR.clip_plane_x_max,
                )

            if (
                pyvista_LR.clip_plane_y_max - pyvista_LR.clip_plane_y_min <= 1
            ):  # only max than 1 is valid for clip
                pass
            else:
                point_cloud_arrow = point_cloud_arrow.copy().clip(
                    "y",
                    invert=False,
                    origin=(
                        point_cloud_arrow.bounds[0],
                        point_cloud_arrow.bounds[2],
                        point_cloud_arrow.bounds[4],
                    ),
                    value=pyvista_LR.clip_plane_y_min,
                )
                point_cloud_arrow = point_cloud_arrow.copy().clip(
                    "y",
                    invert=True,
                    origin=(
                        point_cloud_arrow.bounds[0],
                        point_cloud_arrow.bounds[2],
                        point_cloud_arrow.bounds[4],
                    ),
                    value=pyvista_LR.clip_plane_y_max,
                )

            if (
                pyvista_LR.clip_plane_z_max - pyvista_LR.clip_plane_z_min <= 1
            ):  # only max than 1 is valid for clip
                pass
            else:
                point_cloud_arrow = point_cloud_arrow.copy().clip(
                    "z",
                    invert=False,
                    origin=(
                        point_cloud_arrow.bounds[0],
                        point_cloud_arrow.bounds[2],
                        point_cloud_arrow.bounds[4],
                    ),
                    value=pyvista_LR.clip_plane_z_min,
                )
                point_cloud_arrow = point_cloud_arrow.copy().clip(
                    "z",
                    invert=True,
                    origin=(
                        point_cloud_arrow.bounds[0],
                        point_cloud_arrow.bounds[2],
                        point_cloud_arrow.bounds[4],
                    ),
                    value=pyvista_LR.clip_plane_z_max,
                )
        if pyvista_LR.do_clip_plane_free_normal:
            point_cloud_arrow = point_cloud_arrow.copy().clip(
                pyvista_LR.dataset_clip_plane_free_normal_1,
                invert=False,
                origin=(
                    point_cloud_arrow.bounds[0],
                    point_cloud_arrow.bounds[2],
                    point_cloud_arrow.bounds[4],
                ),
                value=pyvista_LR.clip_plane_free_1,
            )
            point_cloud_arrow = point_cloud_arrow.copy().clip(
                pyvista_LR.dataset_clip_plane_free_normal_2,
                invert=True,
                origin=(
                    point_cloud_arrow.bounds[0],
                    point_cloud_arrow.bounds[2],
                    point_cloud_arrow.bounds[5],
                ),
                value=-pyvista_LR.clip_plane_free_2,
            )

        #############################################################################################
        # Add projections
        #############################################################################################
        if pyvista_LR.add_projection_plane_1 and local_state.do_warp_sphere == False:
            projection_surface_1 = point_cloud_arrow.project_points_to_plane(
                normal=[1, 0, 0]
            )
            du_1 = projection_surface_1.delaunay_2d()

            if du_1.points.size == 0:
                pass
            else:
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.projection_plane_added_1_1 = True
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.projection_plane_added_1_2 = True
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.projection_plane_added_1_3 = True
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.projection_plane_added_1_4 = True

                if local_state.do_glyph_projection_fft == False:
                    actor_list[
                        "projection_plane_1_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    ] = plotter.add_mesh(
                        du_1,
                        name="du_1",
                        scalars="color_component",
                        show_scalar_bar=False,
                        cmap=pyvista_LR.cmap_record,
                        metallic=pyvista_LR.metallic_record,
                        roughness=pyvista_LR.roughness_record,
                        interpolate_before_map=local_state.do_interpolated_projection,
                    )
                    local_state.projection_plane_1_added = True
                else:
                    proj_fft_x = np.array([du_1.bounds[0]])
                    proj_fft_y = np.linspace(
                        *du_1.bounds[2:4], pyvista_LR.system_size[1]
                    )
                    proj_fft_z = np.linspace(
                        *du_1.bounds[4:6], pyvista_LR.system_size[2]
                    )
                    rect = pv.RectilinearGrid(
                        proj_fft_x, proj_fft_y, proj_fft_z
                    ).sample(du_1)
                    array = np.array(
                        rect["color_component"].reshape(
                            pyvista_LR.system_size[1], pyvista_LR.system_size[2]
                        )
                    )

                    proj_fft_yv, proj_fft_zv = np.meshgrid(proj_fft_y, proj_fft_z)
                    coord_fft = np.array(
                        [
                            np.ones(
                                pyvista_LR.system_size[1] * pyvista_LR.system_size[2]
                            )
                            * proj_fft_x,
                            proj_fft_yv.reshape(
                                pyvista_LR.system_size[1] * pyvista_LR.system_size[2], 1
                            ).squeeze(),
                            proj_fft_zv.reshape(
                                pyvista_LR.system_size[1] * pyvista_LR.system_size[2], 1
                            ).squeeze(),
                        ]
                    ).T

                    after_fft = fftn(array)
                    after_fft = fftshift(after_fft)
                    after_fft = np.real(after_fft)
                    point_cloud_arrow_projection_fft = pv.PolyData(coord_fft)
                    point_cloud_arrow_projection_fft["fft"] = after_fft.reshape(
                        pyvista_LR.system_size[1] * pyvista_LR.system_size[2], 1
                    )

                    du_1_fft = point_cloud_arrow_projection_fft.delaunay_2d()

                    actor_list[
                        "projection_plane_1_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    ] = plotter.add_mesh(
                        du_1_fft,
                        name="du_1",
                        scalars="fft",
                        show_scalar_bar=False,
                        cmap="gray",
                        interpolate_before_map=local_state.do_interpolated_projection,
                    )
                    local_state.projection_plane_1_added = True

        if (
            pyvista_LR.add_projection_plane_1 == False
            and (
                local_state.projection_plane_added_1_1
                or local_state.projection_plane_added_1_2
                or local_state.projection_plane_added_1_3
                or local_state.projection_plane_added_1_4
            )
            == True
        ):
            try:
                (
                    eval(
                        "projection_plane_1_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    )
                ).SetVisibility(False)
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.projection_plane_added_1_1 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.projection_plane_added_1_2 = False
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.projection_plane_added_1_3 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.projection_plane_added_1_4 = False
            except:
                print("Oops, projection plane 1 seems not removed")
                pass

        if pyvista_LR.add_projection_plane_2 and local_state.do_warp_sphere == False:
            projection_surface_2 = point_cloud_arrow.project_points_to_plane(
                normal=[-1, 0, 0]
            )
            du_2 = projection_surface_2.delaunay_2d()

            if du_2.points.size == 0:
                pass
            else:
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.projection_plane_added_2_1 = True
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.projection_plane_added_2_2 = True
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.projection_plane_added_2_3 = True
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.projection_plane_added_2_4 = True
                if local_state.do_glyph_projection_fft == False:
                    actor_list[
                        "projection_plane_2_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    ] = plotter.add_mesh(
                        du_2,
                        name="du_2",
                        scalars="color_component",
                        show_scalar_bar=False,
                        cmap=pyvista_LR.cmap_record,
                        metallic=pyvista_LR.metallic_record,
                        roughness=pyvista_LR.roughness_record,
                        interpolate_before_map=local_state.do_interpolated_projection,
                    )
                    local_state.projection_plane_2_added = True
                else:
                    proj_fft_x = np.array([du_2.bounds[0]])
                    proj_fft_y = np.linspace(
                        *du_2.bounds[2:4], pyvista_LR.system_size[1]
                    )
                    proj_fft_z = np.linspace(
                        *du_2.bounds[4:6], pyvista_LR.system_size[2]
                    )
                    rect = pv.RectilinearGrid(
                        proj_fft_x, proj_fft_y, proj_fft_z
                    ).sample(du_2)
                    array = np.array(
                        rect["color_component"].reshape(
                            pyvista_LR.system_size[1], pyvista_LR.system_size[2]
                        )
                    )

                    proj_fft_yv, proj_fft_zv = np.meshgrid(proj_fft_y, proj_fft_z)
                    coord_fft = np.array(
                        [
                            np.ones(
                                pyvista_LR.system_size[1] * pyvista_LR.system_size[2]
                            )
                            * proj_fft_x,
                            proj_fft_yv.reshape(
                                pyvista_LR.system_size[1] * pyvista_LR.system_size[2], 1
                            ).squeeze(),
                            proj_fft_zv.reshape(
                                pyvista_LR.system_size[1] * pyvista_LR.system_size[2], 1
                            ).squeeze(),
                        ]
                    ).T

                    after_fft = fftn(array)
                    after_fft = fftshift(after_fft)
                    after_fft = np.real(after_fft)
                    point_cloud_arrow_projection_fft = pv.PolyData(coord_fft)
                    point_cloud_arrow_projection_fft["fft"] = after_fft.reshape(
                        pyvista_LR.system_size[1] * pyvista_LR.system_size[2], 1
                    )

                    du_2_fft = point_cloud_arrow_projection_fft.delaunay_2d()

                    actor_list[
                        "projection_plane_2_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    ] = plotter.add_mesh(
                        du_2_fft,
                        name="du_2",
                        scalars="fft",
                        show_scalar_bar=False,
                        cmap="gray",
                        interpolate_before_map=local_state.do_interpolated_projection,
                    )
                    local_state.projection_plane_2_added = True

        if (
            pyvista_LR.add_projection_plane_2 == False
            and (
                local_state.projection_plane_added_2_1
                or local_state.projection_plane_added_2_2
                or local_state.projection_plane_added_2_3
                or local_state.projection_plane_added_2_4
            )
            == True
        ):
            try:
                (
                    eval(
                        "projection_plane_2_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    )
                ).SetVisibility(False)
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.projection_plane_added_2_1 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.projection_plane_added_2_2 = False
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.projection_plane_added_2_3 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.projection_plane_added_2_4 = False
            except:
                print("Oops, projection plane 2 seems not removed")
                pass

        if pyvista_LR.add_projection_plane_3 and local_state.do_warp_sphere == False:
            projection_surface_3 = point_cloud_arrow.project_points_to_plane(
                normal=[0, 1, 0]
            )
            du_3 = projection_surface_3.delaunay_2d()

            if du_3.points.size == 0:
                pass
            else:
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.projection_plane_added_3_1 = True
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.projection_plane_added_3_2 = True
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.projection_plane_added_3_3 = True
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.projection_plane_added_3_4 = True
                if local_state.do_glyph_projection_fft == False:
                    actor_list[
                        "projection_plane_3_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    ] = plotter.add_mesh(
                        du_3,
                        name="du_3",
                        scalars="color_component",
                        show_scalar_bar=False,
                        cmap=pyvista_LR.cmap_record,
                        metallic=pyvista_LR.metallic_record,
                        roughness=pyvista_LR.roughness_record,
                        interpolate_before_map=local_state.do_interpolated_projection,
                    )
                    local_state.projection_plane_3_added = True
                else:
                    proj_fft_y = np.array([du_3.bounds[3]])
                    proj_fft_x = np.linspace(
                        *du_3.bounds[0:2], pyvista_LR.system_size[0]
                    )
                    proj_fft_z = np.linspace(
                        *du_3.bounds[4:6], pyvista_LR.system_size[2]
                    )
                    rect = pv.RectilinearGrid(
                        proj_fft_x, proj_fft_y, proj_fft_z
                    ).sample(du_3)
                    array = np.array(
                        rect["color_component"].reshape(
                            pyvista_LR.system_size[0], pyvista_LR.system_size[2]
                        )
                    )

                    proj_fft_xv, proj_fft_zv = np.meshgrid(proj_fft_x, proj_fft_z)
                    coord_fft = np.array(
                        [
                            proj_fft_xv.reshape(
                                pyvista_LR.system_size[0] * pyvista_LR.system_size[2], 1
                            ).squeeze(),
                            np.ones(
                                pyvista_LR.system_size[0] * pyvista_LR.system_size[2]
                            )
                            * proj_fft_y,
                            proj_fft_zv.reshape(
                                pyvista_LR.system_size[0] * pyvista_LR.system_size[2], 1
                            ).squeeze(),
                        ]
                    ).T

                    after_fft = fftn(array)
                    after_fft = fftshift(after_fft)
                    after_fft = np.real(after_fft)
                    point_cloud_arrow_projection_fft = pv.PolyData(coord_fft)
                    point_cloud_arrow_projection_fft["fft"] = after_fft.reshape(
                        pyvista_LR.system_size[0] * pyvista_LR.system_size[2], 1
                    )

                    du_3_fft = point_cloud_arrow_projection_fft.delaunay_2d()

                    actor_list[
                        "projection_plane_3_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    ] = plotter.add_mesh(
                        du_3_fft,
                        name="du_3",
                        scalars="fft",
                        show_scalar_bar=False,
                        cmap="gray",
                        interpolate_before_map=local_state.do_interpolated_projection,
                    )
                    local_state.projection_plane_3_added = True

        if (
            pyvista_LR.add_projection_plane_3 == False
            and (
                local_state.projection_plane_added_3_1
                or local_state.projection_plane_added_3_2
                or local_state.projection_plane_added_3_3
                or local_state.projection_plane_added_3_4
            )
            == True
        ):
            try:
                (
                    eval(
                        "projection_plane_3_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    )
                ).SetVisibility(False)
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.projection_plane_added_3_1 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.projection_plane_added_3_2 = False
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.projection_plane_added_3_3 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.projection_plane_added_3_4 = False
            except:
                print("Oops, projection plane 3 seems not removed")
                pass

        if pyvista_LR.add_projection_plane_4 and local_state.do_warp_sphere == False:
            projection_surface_4 = point_cloud_arrow.project_points_to_plane(
                normal=[0, -1, 0]
            )
            du_4 = projection_surface_4.delaunay_2d()

            if du_4.points.size == 0:
                pass
            else:
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.projection_plane_added_4_1 = True
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.projection_plane_added_4_2 = True
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.projection_plane_added_4_3 = True
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.projection_plane_added_4_4 = True
                if local_state.do_glyph_projection_fft == False:
                    actor_list[
                        "projection_plane_4_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    ] = plotter.add_mesh(
                        du_4,
                        name="du_4",
                        scalars="color_component",
                        show_scalar_bar=False,
                        cmap=pyvista_LR.cmap_record,
                        metallic=pyvista_LR.metallic_record,
                        roughness=pyvista_LR.roughness_record,
                        interpolate_before_map=local_state.do_interpolated_projection,
                    )
                    local_state.projection_plane_4_added = True
                else:
                    proj_fft_y = np.array([du_4.bounds[3]])
                    proj_fft_x = np.linspace(
                        *du_4.bounds[0:2], pyvista_LR.system_size[0]
                    )
                    proj_fft_z = np.linspace(
                        *du_4.bounds[4:6], pyvista_LR.system_size[2]
                    )
                    rect = pv.RectilinearGrid(
                        proj_fft_x, proj_fft_y, proj_fft_z
                    ).sample(du_4)
                    array = np.array(
                        rect["color_component"].reshape(
                            pyvista_LR.system_size[0], pyvista_LR.system_size[2]
                        )
                    )

                    proj_fft_xv, proj_fft_zv = np.meshgrid(proj_fft_x, proj_fft_z)
                    coord_fft = np.array(
                        [
                            proj_fft_xv.reshape(
                                pyvista_LR.system_size[0] * pyvista_LR.system_size[2], 1
                            ).squeeze(),
                            np.ones(
                                pyvista_LR.system_size[0] * pyvista_LR.system_size[2]
                            )
                            * proj_fft_y,
                            proj_fft_zv.reshape(
                                pyvista_LR.system_size[0] * pyvista_LR.system_size[2], 1
                            ).squeeze(),
                        ]
                    ).T

                    after_fft = fftn(array)
                    after_fft = fftshift(after_fft)
                    after_fft = np.real(after_fft)
                    point_cloud_arrow_projection_fft = pv.PolyData(coord_fft)
                    point_cloud_arrow_projection_fft["fft"] = after_fft.reshape(
                        pyvista_LR.system_size[0] * pyvista_LR.system_size[2], 1
                    )

                    du_4_fft = point_cloud_arrow_projection_fft.delaunay_2d()

                    actor_list[
                        "projection_plane_4_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    ] = plotter.add_mesh(
                        du_4_fft,
                        name="du_4",
                        scalars="fft",
                        show_scalar_bar=False,
                        cmap="gray",
                        interpolate_before_map=local_state.do_interpolated_projection,
                    )
                    local_state.projection_plane_4_added = True

        if (
            pyvista_LR.add_projection_plane_4 == False
            and (
                local_state.projection_plane_added_4_1
                or local_state.projection_plane_added_4_2
                or local_state.projection_plane_added_4_3
                or local_state.projection_plane_added_4_4
            )
            == True
        ):
            try:
                (
                    eval(
                        "projection_plane_4_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    )
                ).SetVisibility(False)
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.projection_plane_added_4_1 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.projection_plane_added_4_2 = False
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.projection_plane_added_4_3 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.projection_plane_added_4_4 = False
            except:
                print("Oops, projection plane 4 seems not removed")
                pass

        if pyvista_LR.add_projection_plane_5 and local_state.do_warp_sphere == False:
            projection_surface_5 = point_cloud_arrow.project_points_to_plane(
                normal=[0, 0, 1]
            )
            du_5 = projection_surface_5.delaunay_2d()

            if du_5.points.size == 0:
                pass
            else:
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.projection_plane_added_5_1 = True
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.projection_plane_added_5_2 = True
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.projection_plane_added_5_3 = True
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.projection_plane_added_5_4 = True
                if local_state.do_glyph_projection_fft == False:
                    actor_list[
                        "projection_plane_5_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    ] = plotter.add_mesh(
                        du_5,
                        name="du_5",
                        scalars="color_component",
                        show_scalar_bar=False,
                        cmap=pyvista_LR.cmap_record,
                        metallic=pyvista_LR.metallic_record,
                        roughness=pyvista_LR.roughness_record,
                        interpolate_before_map=local_state.do_interpolated_projection,
                    )
                    local_state.projection_plane_5_added = True
                else:
                    proj_fft_z = np.array([du_5.bounds[5]])
                    proj_fft_x = np.linspace(
                        *du_5.bounds[0:2], pyvista_LR.system_size[0]
                    )
                    proj_fft_y = np.linspace(
                        *du_5.bounds[2:4], pyvista_LR.system_size[1]
                    )
                    rect = pv.RectilinearGrid(
                        proj_fft_x, proj_fft_y, proj_fft_z
                    ).sample(du_5)
                    array = np.array(
                        rect["color_component"].reshape(
                            pyvista_LR.system_size[0], pyvista_LR.system_size[1]
                        )
                    )

                    proj_fft_xv, proj_fft_yv = np.meshgrid(proj_fft_x, proj_fft_y)
                    coord_fft = np.array(
                        [
                            proj_fft_xv.reshape(
                                pyvista_LR.system_size[0] * pyvista_LR.system_size[1], 1
                            ).squeeze(),
                            proj_fft_yv.reshape(
                                pyvista_LR.system_size[0] * pyvista_LR.system_size[1], 1
                            ).squeeze(),
                            np.ones(
                                pyvista_LR.system_size[0] * pyvista_LR.system_size[1]
                            )
                            * proj_fft_z,
                        ]
                    ).T

                    after_fft = fftn(array)
                    after_fft = fftshift(after_fft)
                    after_fft = np.real(after_fft)
                    point_cloud_arrow_projection_fft = pv.PolyData(coord_fft)
                    point_cloud_arrow_projection_fft["fft"] = after_fft.reshape(
                        pyvista_LR.system_size[0] * pyvista_LR.system_size[1], 1
                    )

                    du_5_fft = point_cloud_arrow_projection_fft.delaunay_2d()

                    actor_list[
                        "projection_plane_5_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    ] = plotter.add_mesh(
                        du_5_fft,
                        name="du_5",
                        scalars="fft",
                        show_scalar_bar=False,
                        cmap="gray",
                        interpolate_before_map=local_state.do_interpolated_projection,
                    )
                    local_state.projection_plane_5_added = True

        if (
            pyvista_LR.add_projection_plane_5 == False
            and (
                local_state.projection_plane_added_5_1
                or local_state.projection_plane_added_5_2
                or local_state.projection_plane_added_5_3
                or local_state.projection_plane_added_5_4
            )
            == True
        ):
            try:
                (
                    eval(
                        "projection_plane_5_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    )
                ).SetVisibility(False)
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.projection_plane_added_5_1 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.projection_plane_added_5_2 = False
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.projection_plane_added_5_3 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.projection_plane_added_5_4 = False
            except:
                print("Oops, projection plane 5 seems not removed")
                pass

        if pyvista_LR.add_projection_plane_6 and local_state.do_warp_sphere == False:
            projection_surface_6 = point_cloud_arrow.project_points_to_plane(
                normal=[0, 0, -1]
            )
            du_6 = projection_surface_6.delaunay_2d()

            if du_6.points.size == 0:
                pass
            else:
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.projection_plane_added_6_1 = True
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.projection_plane_added_6_2 = True
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.projection_plane_added_6_3 = True
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.projection_plane_added_6_4 = True
                if local_state.do_glyph_projection_fft == False:
                    actor_list[
                        "projection_plane_6_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    ] = plotter.add_mesh(
                        du_6,
                        name="du_6",
                        scalars="color_component",
                        show_scalar_bar=False,
                        cmap=pyvista_LR.cmap_record,
                        metallic=pyvista_LR.metallic_record,
                        roughness=pyvista_LR.roughness_record,
                        interpolate_before_map=local_state.do_interpolated_projection,
                    )
                    local_state.projection_plane_6_added = True
                else:
                    proj_fft_z = np.array([du_6.bounds[5]])
                    proj_fft_x = np.linspace(
                        *du_6.bounds[0:2], pyvista_LR.system_size[0]
                    )
                    proj_fft_y = np.linspace(
                        *du_6.bounds[2:4], pyvista_LR.system_size[1]
                    )
                    rect = pv.RectilinearGrid(
                        proj_fft_x, proj_fft_y, proj_fft_z
                    ).sample(du_6)
                    array = np.array(
                        rect["color_component"].reshape(
                            pyvista_LR.system_size[0], pyvista_LR.system_size[1]
                        )
                    )

                    proj_fft_xv, proj_fft_yv = np.meshgrid(proj_fft_x, proj_fft_y)
                    coord_fft = np.array(
                        [
                            proj_fft_xv.reshape(
                                pyvista_LR.system_size[0] * pyvista_LR.system_size[1], 1
                            ).squeeze(),
                            proj_fft_yv.reshape(
                                pyvista_LR.system_size[0] * pyvista_LR.system_size[1], 1
                            ).squeeze(),
                            np.ones(
                                pyvista_LR.system_size[0] * pyvista_LR.system_size[1]
                            )
                            * proj_fft_z,
                        ]
                    ).T

                    after_fft = fftn(array)
                    after_fft = fftshift(after_fft)
                    after_fft = np.real(after_fft)
                    point_cloud_arrow_projection_fft = pv.PolyData(coord_fft)
                    point_cloud_arrow_projection_fft["fft"] = after_fft.reshape(
                        pyvista_LR.system_size[0] * pyvista_LR.system_size[1], 1
                    )

                    du_6_fft = point_cloud_arrow_projection_fft.delaunay_2d()

                    actor_list[
                        "projection_plane_6_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    ] = plotter.add_mesh(
                        du_6_fft,
                        name="du_6",
                        scalars="fft",
                        show_scalar_bar=False,
                        cmap="gray",
                        interpolate_before_map=local_state.do_interpolated_projection,
                    )
                    local_state.projection_plane_6_added = True

        if (
            pyvista_LR.add_projection_plane_6 == False
            and (
                local_state.projection_plane_added_6_1
                or local_state.projection_plane_added_6_2
                or local_state.projection_plane_added_6_3
                or local_state.projection_plane_added_6_4
            )
            == True
        ):
            try:
                (
                    eval(
                        "projection_plane_6_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    )
                ).SetVisibility(False)
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.projection_plane_added_6_1 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.projection_plane_added_6_2 = False
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.projection_plane_added_6_3 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.projection_plane_added_6_4 = False
            except:
                print("Oops, projection plane 6 seems not removed")
                pass

        #############################################################################################
        # Add glyphs, in this version we offer Cone, Arrow, Plane, Sphere, Box, and User's own Glyphs.
        #############################################################################################

        #########
        # simple_point cubic render_points_as_spheres=True
        #########
        if pyvista_LR.add_simple_point:
            if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                local_state.simple_point_added_1 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                local_state.simple_point_added_2 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "10" or (
                str(subplot_index_list[0]) + str(subplot_index_list[1])
            ) == "02":
                local_state.simple_point_added_3 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                local_state.simple_point_added_4 = True

            # print(point_cloud_arrow['color_component'])
            actor_list[
                "actor_simple_point_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1])
            ] = plotter.add_mesh(
                point_cloud_arrow,
                name="Simple_point"
                + "_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1]),
                scalars="color_component",
                opacity="opacity_component",
                clim=local_state.clim_range,
                show_scalar_bar=pyvista_LR.show_scalar_bar,
                scalar_bar_args={
                    "title": local_state.glyph_scalar_bar_name
                    + "_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                },
                point_size=pyvista_LR.simple_point_size,
                render_points_as_spheres=pyvista_LR.local_rendering_sinmple_point_as_spheres,
                cmap=pyvista_LR.cmap_record,
            )

        if (
            pyvista_LR.add_simple_point == False
            and (
                local_state.simple_point_added_1
                or local_state.simple_point_added_2
                or local_state.simple_point_added_3
                or local_state.simple_point_added_4
            )
            == True
        ):
            try:
                (
                    eval(
                        "actor_simple_point_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    )
                ).SetVisibility(False)
                plotter.remove_scalar_bar(
                    local_state.glyph_scalar_bar_name
                    + "_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                )
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.simple_point_added_1 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.simple_point_added_2 = False
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.simple_point_added_3 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.simple_point_added_4 = False
            except:
                print("Oops, actor: point seems not removed")
                pass
        elif pyvista_LR.add_simple_point == True:
            (
                eval(
                    "actor_simple_point_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                )
            ).SetVisibility(True)

        #########
        # Cone
        #########
        # pyvista_LR.add_cone=True

        if pyvista_LR.add_cone:
            if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                local_state.cone_added_1 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                local_state.cone_added_2 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "10" or (
                str(subplot_index_list[0]) + str(subplot_index_list[1])
            ) == "02":
                local_state.cone_added_3 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                local_state.cone_added_4 = True

            if pyvista_LR.do_scale_cone:
                # if local_state.moment_magintude != None:
                glyph_cone = point_cloud_arrow.glyph(
                    orient="vectors",
                    scale="magnitute",
                    factor=pyvista_LR.Ratio_record,
                    geom=pv.Cone(
                        height=pyvista_LR.cone_highth_record,
                        radius=pyvista_LR.cone_Radius_record,
                        resolution=int(pyvista_LR.resolutions),
                        center=pyvista_LR.Cone_center,
                    ),
                )
                # else:
                #     print(
                #         "No moment magnitude is found, please check your moment file.(Only UppASD support now)"
                #     )

            else:
                glyph_cone = point_cloud_arrow.glyph(
                    orient="vectors",
                    scale=False,
                    factor=pyvista_LR.Ratio_record,
                    geom=pv.Cone(
                        height=pyvista_LR.cone_highth_record,
                        radius=pyvista_LR.cone_Radius_record,
                        resolution=int(pyvista_LR.resolutions),
                        center=pyvista_LR.Cone_center,
                    ),
                )

            actor_list[
                "actor_cone_" + str(subplot_index_list[0]) + str(subplot_index_list[1])
            ] = plotter.add_mesh(
                glyph_cone,
                name="Cone"
                + "_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1]),
                scalars="color_component",
                opacity="opacity_component",
                clim=local_state.clim_range,
                show_scalar_bar=pyvista_LR.show_scalar_bar,
                pbr=pyvista_LR.pbr,
                cmap=pyvista_LR.cmap_record,
                metallic=pyvista_LR.metallic_record,
                roughness=pyvista_LR.roughness_record,
                scalar_bar_args={
                    "title": local_state.glyph_scalar_bar_name
                    + "_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                },
            )

        if (
            pyvista_LR.add_cone == False
            and (
                local_state.cone_added_1
                or local_state.cone_added_2
                or local_state.cone_added_3
                or local_state.cone_added_4
            )
            == True
        ):
            try:
                (
                    eval(
                        "actor_cone_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    )
                ).SetVisibility(False)
                plotter.remove_scalar_bar(
                    local_state.glyph_scalar_bar_name
                    + "_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                )
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.cone_added_1 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.cone_added_2 = False
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.cone_added_3 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.cone_added_4 = False
            except:
                print("Oops, actor: cone seems not removed")
                pass
        elif pyvista_LR.add_cone == True:
            (
                eval(
                    "actor_cone_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                )
            ).SetVisibility(True)

        #########
        # Arrow
        #########
        if pyvista_LR.add_arrow:
            if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                local_state.arrow_added_1 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                local_state.arrow_added_2 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "10" or (
                str(subplot_index_list[0]) + str(subplot_index_list[1])
            ) == "02":
                local_state.arrow_added_3 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                local_state.arrow_added_4 = True

            if pyvista_LR.do_scale_arrow:
                # if local_state.moment_magintude != None:
                glyph_arrow = point_cloud_arrow.glyph(
                    orient="vectors",
                    scale="magnitute",
                    factor=pyvista_LR.Ratio_record_arrow,
                    geom=pv.Arrow(
                        start=pyvista_LR.start_arrow,
                        tip_length=pyvista_LR.tip_length_arrow,
                        tip_radius=pyvista_LR.tip_radius_arrow,
                        tip_resolution=int(pyvista_LR.tip_resolution_arrow),
                        shaft_radius=pyvista_LR.shaft_radius_arrow,
                        shaft_resolution=int(pyvista_LR.shaft_resolution_arrow),
                    ),
                )
                # else:
                #     print(
                #         "No moment magnitude is found, please check your moment file.(Only UppASD support now)"
                #     )

            else:
                glyph_arrow = point_cloud_arrow.glyph(
                    orient="vectors",
                    scale=False,
                    factor=pyvista_LR.Ratio_record_arrow,
                    geom=pv.Arrow(
                        start=pyvista_LR.start_arrow,
                        tip_length=pyvista_LR.tip_length_arrow,
                        tip_radius=pyvista_LR.tip_radius_arrow,
                        tip_resolution=int(pyvista_LR.tip_resolution_arrow),
                        shaft_radius=pyvista_LR.shaft_radius_arrow,
                        shaft_resolution=int(pyvista_LR.shaft_resolution_arrow),
                    ),
                )

            actor_list[
                "actor_arrow_" + str(subplot_index_list[0]) + str(subplot_index_list[1])
            ] = plotter.add_mesh(
                glyph_arrow,
                name="Arrow"
                + "_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1]),
                scalars="color_component",
                opacity="opacity_component",
                clim=local_state.clim_range,
                show_scalar_bar=pyvista_LR.show_scalar_bar,
                pbr=pyvista_LR.pbr_arrow,
                cmap=pyvista_LR.cmap_record,
                metallic=pyvista_LR.metallic_arrow,
                roughness=pyvista_LR.roughness_arrow,
                scalar_bar_args={
                    "title": local_state.glyph_scalar_bar_name
                    + "_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                },
            )

        if (
            pyvista_LR.add_arrow == False
            and (
                local_state.arrow_added_1
                or local_state.arrow_added_2
                or local_state.arrow_added_3
                or local_state.arrow_added_4
            )
            == True
        ):
            try:
                (
                    eval(
                        "actor_arrow_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    )
                ).SetVisibility(False)
                plotter.remove_scalar_bar(
                    local_state.glyph_scalar_bar_name
                    + "_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                )
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.arrow_added_1 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.arrow_added_2 = False
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.arrow_added_3 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.arrow_added_4 = False
            except:
                print("Oops, actor: arrow seems not removed")
                pass
        elif pyvista_LR.add_arrow == True:
            (
                eval(
                    "actor_arrow_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                )
            ).SetVisibility(True)

        #########
        # Sphere
        #########
        if pyvista_LR.add_sphere:
            if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                local_state.sphere_added_1 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                local_state.sphere_added_2 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "10" or (
                str(subplot_index_list[0]) + str(subplot_index_list[1])
            ) == "02":
                local_state.sphere_added_3 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                local_state.sphere_added_4 = True

            if pyvista_LR.do_scale_sphere:
                # if local_state.moment_magintude != None:
                glyph_sphere = point_cloud_arrow.glyph(
                    scale="magnitute",
                    factor=pyvista_LR.Ratio_record_sphere,
                    geom=pv.Sphere(
                        radius=pyvista_LR.radius_sphere,
                        center=pyvista_LR.center_sphere,
                        theta_resolution=int(pyvista_LR.theta_resolution_sphere),
                        phi_resolution=int(pyvista_LR.phi_resolution_sphere),
                    ),
                )

                # else:
                #     print(
                #         "No moment magnitude is found, please check your moment file.(Only UppASD support now)"
                #     )

            else:
                glyph_sphere = point_cloud_arrow.glyph(
                    orient=False,  # it seems no need for sphere to be oriented.
                    scale=False,
                    factor=pyvista_LR.Ratio_record_sphere,
                    geom=pv.Sphere(
                        radius=pyvista_LR.radius_sphere,
                        center=pyvista_LR.center_sphere,
                        theta_resolution=int(pyvista_LR.theta_resolution_sphere),
                        phi_resolution=int(pyvista_LR.phi_resolution_sphere),
                    ),
                )
            # #sphere rescale
            # if pyvista_LR.do_glyph_sphere_rescale:
            #     if pyvista_LR.rescale_sphere_index ==0:
            #         glyph_sphere=glyph_sphere.warp_by_scalar('rescale_x',factor=pyvista_LR.rescale_sphere_factor,normal=pyvista_LR.rescale_sphere_norm)
            #     elif pyvista_LR.rescale_sphere_index ==1:
            #         glyph_sphere=glyph_sphere.warp_by_scalar('rescale_y',factor=pyvista_LR.rescale_sphere_factor,normal=pyvista_LR.rescale_sphere_norm)
            #     elif pyvista_LR.rescale_sphere_index ==2:
            #         glyph_sphere=glyph_sphere.warp_by_scalar('rescale_z',factor=pyvista_LR.rescale_sphere_factor,normal=pyvista_LR.rescale_sphere_norm)
            #     elif pyvista_LR.rescale_sphere_index ==3:
            #         glyph_sphere=glyph_sphere.warp_by_scalar('rescale_phi',factor=pyvista_LR.rescale_sphere_factor,normal=pyvista_LR.rescale_sphere_norm)
            #     elif pyvista_LR.rescale_sphere_index ==4:
            #         glyph_sphere=glyph_sphere.warp_by_scalar('rescale_theta',factor=pyvista_LR.rescale_sphere_factor,normal=pyvista_LR.rescale_sphere_norm)

            actor_list[
                "actor_sphere_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1])
            ] = plotter.add_mesh(
                glyph_sphere,
                name="sphere"
                + "_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1]),
                scalars="color_component",
                opacity="opacity_component",
                clim=local_state.clim_range,
                show_scalar_bar=pyvista_LR.show_scalar_bar,
                pbr=pyvista_LR.pbr_sphere,
                cmap=pyvista_LR.cmap_record,
                metallic=pyvista_LR.metallic_sphere,
                roughness=pyvista_LR.roughness_sphere,
                scalar_bar_args={
                    "title": local_state.glyph_scalar_bar_name
                    + "_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                },
            )

        if (
            pyvista_LR.add_sphere == False
            and (
                local_state.sphere_added_1
                or local_state.sphere_added_2
                or local_state.sphere_added_3
                or local_state.sphere_added_4
            )
            == True
        ):
            try:
                (
                    eval(
                        "actor_sphere_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    )
                ).SetVisibility(False)
                plotter.remove_scalar_bar(
                    local_state.glyph_scalar_bar_name
                    + "_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                )
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.sphere_added_1 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.sphere_added_2 = False
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.sphere_added_3 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.sphere_added_4 = False
            except:
                print("Oops, actor: sphere seems not removed")
                pass
        elif pyvista_LR.add_sphere == True:
            (
                eval(
                    "actor_sphere_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                )
            ).SetVisibility(True)

        #########
        # Plane
        #########
        if pyvista_LR.add_plane:
            if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                local_state.plane_added_1 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                local_state.plane_added_2 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "10" or (
                str(subplot_index_list[0]) + str(subplot_index_list[1])
            ) == "02":
                local_state.plane_added_3 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                local_state.plane_added_4 = True

            if pyvista_LR.do_scale_plane:
                # if local_state.moment_magintude != None:
                glyph_plane = point_cloud_arrow.glyph(
                    orient="vectors",
                    scale="magnitute",
                    factor=pyvista_LR.Ratio_record_plane,
                    geom=pv.Plane(
                        center=pyvista_LR.center_plane,
                        i_resolution=1,  # Here 1*1 should be enough for every case.
                        j_resolution=1,
                    ),
                )

                # else:
                #     print(
                #         "No moment magnitude is found, please check your moment file.(Only UppASD support now)"
                #     )

            else:
                glyph_plane = point_cloud_arrow.glyph(
                    orient=False,
                    scale=False,
                    factor=pyvista_LR.Ratio_record_plane,
                    geom=pv.Plane(
                        center=pyvista_LR.center_plane, i_resolution=1, j_resolution=1
                    ),
                )

            actor_list[
                "actor_plane_" + str(subplot_index_list[0]) + str(subplot_index_list[1])
            ] = plotter.add_mesh(
                glyph_plane,
                name="plane"
                + "_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1]),
                scalars="color_component",
                opacity="opacity_component",
                clim=local_state.clim_range,
                show_scalar_bar=pyvista_LR.show_scalar_bar,
                pbr=pyvista_LR.pbr_plane,
                cmap=pyvista_LR.cmap_record,
                metallic=pyvista_LR.metallic_plane,
                roughness=pyvista_LR.roughness_plane,
                scalar_bar_args={
                    "title": local_state.glyph_scalar_bar_name
                    + "_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                },
            )

        if (
            pyvista_LR.add_plane == False
            and (
                local_state.plane_added_1
                or local_state.plane_added_2
                or local_state.plane_added_3
                or local_state.plane_added_4
            )
            == True
        ):
            try:
                (
                    eval(
                        "actor_plane_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    )
                ).SetVisibility(False)
                plotter.remove_scalar_bar(
                    local_state.glyph_scalar_bar_name
                    + "_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                )
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.plane_added_1 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.plane_added_2 = False
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.plane_added_3 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.plane_added_4 = False
            except:
                print("Oops, actor: plane seems not removed")
                pass
        elif pyvista_LR.add_plane == True:
            (
                eval(
                    "actor_plane_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                )
            ).SetVisibility(True)

        #########
        # Box
        #########
        if pyvista_LR.add_box:
            if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                local_state.box_added_1 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                local_state.box_added_2 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "10" or (
                str(subplot_index_list[0]) + str(subplot_index_list[1])
            ) == "02":
                local_state.box_added_3 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                local_state.box_added_4 = True

            if pyvista_LR.do_scale_box:
                # if local_state.moment_magintude != None:
                glyph_box = point_cloud_arrow.glyph(
                    orient=False,
                    scale="magnitute",
                    factor=pyvista_LR.Ratio_record_box,
                    geom=pv.Box(bounds=pyvista_LR.bounds_box),
                )
                # the bounds_box will not support in the version 0.10.0, will be activated in the future version.
                # else:
                #     print(
                #         "No moment magnitude is found, please check your moment file.(Only UppASD support now)"
                #     )

            else:
                glyph_box = point_cloud_arrow.glyph(
                    orient=False,
                    scale=False,
                    factor=pyvista_LR.Ratio_record_box,
                    geom=pv.Box(bounds=pyvista_LR.bounds_box),
                )

            actor_list[
                "actor_box_" + str(subplot_index_list[0]) + str(subplot_index_list[1])
            ] = plotter.add_mesh(
                glyph_box,
                name="box"
                + "_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1]),
                scalars="color_component",
                opacity="opacity_component",
                clim=local_state.clim_range,
                show_scalar_bar=pyvista_LR.show_scalar_bar,
                pbr=pyvista_LR.pbr_box,
                cmap=pyvista_LR.cmap_record,
                metallic=pyvista_LR.metallic_box,
                roughness=pyvista_LR.roughness_box,
                scalar_bar_args={
                    "title": local_state.glyph_scalar_bar_name
                    + "_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                },
            )

        if (
            pyvista_LR.add_box == False
            and (
                local_state.box_added_1
                or local_state.box_added_2
                or local_state.box_added_3
                or local_state.box_added_4
            )
            == True
        ):
            try:
                (
                    eval(
                        "actor_box_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    )
                ).SetVisibility(False)
                plotter.remove_scalar_bar(
                    local_state.glyph_scalar_bar_name
                    + "_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                )
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.box_added_1 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.box_added_2 = False
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.box_added_3 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.box_added_4 = False
            except:
                print("Oops, actor: box seems not removed")
                pass
        elif pyvista_LR.add_box == True:
            (
                eval(
                    "actor_box_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                )
            ).SetVisibility(True)

        #########
        # User's own Glyphs
        #########

        if pyvista_LR.add_own_glyphs:
            if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                local_state.own_glyphs_added_1 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                local_state.own_glyphs_added_2 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "10" or (
                str(subplot_index_list[0]) + str(subplot_index_list[1])
            ) == "02":
                local_state.own_glyphs_added_3 = True
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                local_state.own_glyphs_added_4 = True

            if local_state.user_input_glyph != None:
                if pyvista_LR.do_scale_own:
                    # if local_state.moment_magintude != None:
                    glyph_own = point_cloud_arrow.glyph(
                        orient="vectors",
                        scale="magnitute",
                        factor=pyvista_LR.Ratio_record_own,
                        geom=local_state.user_input_glyph,
                    )
                    # else:
                    #     print(
                    #         "No moment magnitude is found, please check your moment file.(Only UppASD support now)"
                    #     )

                else:
                    glyph_own = point_cloud_arrow.glyph(
                        orient="vectors",
                        scale=False,
                        factor=pyvista_LR.Ratio_record_own,
                        geom=local_state.user_input_glyph,
                    )

                actor_list[
                    "actor_own_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                ] = plotter.add_mesh(
                    glyph_own,
                    name="own"
                    + "_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1]),
                    scalars="color_component",
                    opacity="opacity_component",
                    clim=local_state.clim_range,
                    show_scalar_bar=pyvista_LR.show_scalar_bar,
                    pbr=pyvista_LR.pbr_own,
                    cmap=pyvista_LR.cmap_record,
                    metallic=pyvista_LR.metallic_own,
                    roughness=pyvista_LR.roughness_own,
                    scalar_bar_args={
                        "title": local_state.glyph_scalar_bar_name
                        + "_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    },
                )

        if (
            pyvista_LR.add_own_glyphs == False
            and (
                local_state.own_glyphs_added_1
                or local_state.own_glyphs_added_2
                or local_state.own_glyphs_added_3
                or local_state.own_glyphs_added_4
            )
            == True
        ):
            try:
                (
                    eval(
                        "actor_own_"
                        + str(subplot_index_list[0])
                        + str(subplot_index_list[1])
                    )
                ).SetVisibility(False)
                plotter.remove_scalar_bar(
                    local_state.glyph_scalar_bar_name
                    + "_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                )
                if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                    local_state.own_glyphs_added_1 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                    local_state.own_glyphs_added_2 = False
                elif (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "10" or (
                    str(subplot_index_list[0]) + str(subplot_index_list[1])
                ) == "02":
                    local_state.own_glyphs_added_3 = False
                elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                    local_state.own_glyphs_added_4 = False
            except:
                print("Oops, actor: own glyph seems not removed")
                pass
        elif pyvista_LR.add_own_glyphs == True:
            (
                eval(
                    "actor_own_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                )
            ).SetVisibility(True)

    else:  # set all glyph invisible
        # remove actor_points:
        sb_1_removed = False
        sb_2_removed = False
        sb_3_removed = False
        sb_4_removed = False
        if local_state.simple_point_added_1 == True:
            try:
                actor_simple_point_00.SetVisibility(False)
                local_state.simple_point_added_1 = False
                if sb_1_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_00")
                    sb_1_removed = True
                else:
                    pass
            except:
                print("Oops, actor: point in subplot 1 seems not removed")
                pass
        if local_state.simple_point_added_2 == True:
            try:
                actor_simple_point_01.SetVisibility(False)
                local_state.simple_point_added_2 = False
                if sb_2_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_01")
                    sb_2_removed = True
                else:
                    pass

            except:
                print("Oops, actor: point in subplot 2 seems not removed")
                pass

        if local_state.simple_point_added_3 == True:
            try:
                actor_simple_point_10.SetVisibility(False)
                local_state.simple_point_added_3 = False
                if sb_3_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_10")
                    sb_3_removed = True
                else:
                    pass

            except:
                actor_simple_point_02.SetVisibility(False)
                local_state.simple_point_added_3 = False
                if sb_3_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_02")
                    sb_3_removed = True
                else:
                    pass

        if local_state.simple_point_added_4 == True:
            try:
                actor_simple_point_11.SetVisibility(False)
                local_state.simple_point_added_4 = False
                if sb_4_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_11")
                    sb_4_removed = True
                else:
                    pass

            except:
                print("Oops, actor: point in subplot 4 seems not removed")
                pass

        # remove actor_cone
        if local_state.cone_added_1 == True:
            try:
                actor_cone_00.SetVisibility(False)
                local_state.cone_added_1 = False
                if sb_1_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_00")
                    sb_1_removed = True
                else:
                    pass

            except:
                print("Oops, actor: cone in subplot 1 seems not removed")
                pass

        if local_state.cone_added_2 == True:
            try:
                actor_cone_01.SetVisibility(False)
                local_state.cone_added_2 = False
                if sb_2_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_01")
                    sb_2_removed = True
                else:
                    pass
            except:
                print("Oops, actor: cone in subplot 2 seems not removed")
                pass
        if local_state.cone_added_3 == True:
            try:
                actor_cone_10.SetVisibility(False)
                local_state.cone_added_3 = False
                if sb_3_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_10")
                    sb_3_removed = True
                else:
                    pass
            except:
                actor_cone_02.SetVisibility(False)
                local_state.cone_added_3 = False
                if sb_3_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_02")
                    sb_3_removed = True
                else:
                    pass

        if local_state.cone_added_4 == True:
            try:
                actor_cone_11.SetVisibility(False)
                local_state.cone_added_4 = False
                if sb_4_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_11")
                    sb_4_removed = True
            except:
                print("Oops, actor: cone in subplot 4 seems not removed")
                pass

        # remove actor_sphere
        if local_state.sphere_added_1 == True:
            try:
                actor_sphere_00.SetVisibility(False)
                local_state.sphere_added_1 = False
                if sb_1_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_00")
                    sb_1_removed = True
                else:
                    pass

            except:
                print("Oops, actor: sphere in subplot1 seems not removed")
                pass

        if local_state.sphere_added_2 == True:
            try:
                actor_sphere_01.SetVisibility(False)
                local_state.sphere_added_2 = False
                if sb_2_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_01")
                    sb_2_removed = True
                else:
                    pass
            except:
                print("Oops, actor: sphere in subplot 2 seems not removed")
                pass
        if local_state.sphere_added_3 == True:
            try:
                actor_sphere_10.SetVisibility(False)
                local_state.sphere_added_3 = False
                if sb_3_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_10")
                    sb_3_removed = True
                else:
                    pass
            except:
                actor_sphere_02.SetVisibility(False)
                local_state.sphere_added_3 = False
                if sb_3_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_02")
                    sb_3_removed = True
                else:
                    pass

        if local_state.sphere_added_4 == True:
            try:
                actor_sphere_11.SetVisibility(False)
                local_state.sphere_added_4 = False
                if sb_4_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_11")
                    sb_4_removed = True
            except:
                print("Oops, actor: sphere in subplot 4 seems not removed")
                pass
        # remove actor_plane

        if local_state.plane_added_1 == True:
            try:
                actor_plane_00.SetVisibility(False)
                local_state.plane_added_1 = False
                if sb_1_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_00")
                    sb_1_removed = True
                else:
                    pass

            except:
                print("Oops, actor: plane in subplot 1 seems not removed")
                pass

        if local_state.plane_added_2 == True:
            try:
                actor_plane_01.SetVisibility(False)
                local_state.plane_added_2 = False
                if sb_2_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_01")
                    sb_2_removed = True
                else:
                    pass
            except:
                print("Oops, actor: plane in subplot 2 seems not removed")
                pass
        if local_state.plane_added_3 == True:
            try:
                actor_plane_10.SetVisibility(False)
                local_state.plane_added_3 = False
                if sb_3_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_10")
                    sb_3_removed = True
                else:
                    pass
            except:
                actor_plane_02.SetVisibility(False)
                local_state.plane_added_3 = False
                if sb_3_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_02")
                    sb_3_removed = True
                else:
                    pass

        if local_state.plane_added_4 == True:
            try:
                actor_plane_11.SetVisibility(False)
                local_state.plane_added_4 = False
                if sb_4_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_11")
                    sb_4_removed = True
            except:
                print("Oops, actor: plane in subplot 4 seems not removed")
                pass
        # remove actor_arrow

        if local_state.arrow_added_1 == True:
            try:
                actor_arrow_00.SetVisibility(False)
                local_state.arrow_added_1 = False
                if sb_1_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_00")
                    sb_1_removed = True
                else:
                    pass
            except:
                print("Oops, actor: arrow in subplot 1 seems not removed")
                pass

        if local_state.arrow_added_2 == True:
            try:
                actor_arrow_01.SetVisibility(False)
                local_state.arrow_added_2 = False
                if sb_2_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_01")
                    sb_2_removed = True
                else:
                    pass
            except:
                print("Oops, actor: arrow in subplot 2 seems not removed")
                pass
        if local_state.arrow_added_3 == True:
            try:
                actor_arrow_10.SetVisibility(False)
                local_state.arrow_added_3 = False
                if sb_3_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_10")
                    sb_3_removed = True
                else:
                    pass
            except:
                actor_arrow_02.SetVisibility(False)
                local_state.arrow_added_3 = False
                if sb_3_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_02")
                    sb_3_removed = True
                else:
                    pass

        if local_state.arrow_added_4 == True:
            try:
                actor_arrow_11.SetVisibility(False)
                local_state.arrow_added_4 = False
                if sb_4_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_11")
                    sb_4_removed = True
            except:
                print("Oops, actor: arrow in subplot 4 seems not removed")
                pass
        # remove actor_own_glyphs
        if local_state.own_glyphs_added_1 == True:
            try:
                actor_own_00.SetVisibility(False)
                local_state.own_glyphs_added_1 = False
                if sb_1_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_00")
                    sb_1_removed = True
                else:
                    pass
            except:
                print("Oops, actor: own glyph in subplot 1 seems not removed")
                pass

        if local_state.own_glyphs_added_2 == True:
            try:
                actor_own_01.SetVisibility(False)
                local_state.own_glyphs_added_2 = False
                if sb_2_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_01")
                    sb_2_removed = True
                else:
                    pass
            except:
                print("Oops, actor: own glyph in subplot 2 seems not removed")
                pass
        if local_state.own_glyphs_added_3 == True:
            try:
                actor_own_10.SetVisibility(False)
                local_state.own_glyphs_added_3 = False
                if sb_3_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_10")
                    sb_3_removed = True
                else:
                    pass
            except:
                actor_own_02.SetVisibility(False)
                local_state.own_glyphs_added_3 = False
                if sb_3_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_02")
                    sb_3_removed = True
                else:
                    pass

        if local_state.own_glyphs_added_4 == True:
            try:
                actor_own_11.SetVisibility(False)
                local_state.own_glyphs_added_4 = False
                if sb_4_removed == False:
                    plotter.remove_scalar_bar(local_state.glyph_scalar_bar_name + "_11")
                    sb_4_removed = True
            except:
                print("Oops, actor: own glyph in subplot 4 seems not removed")
                pass

    #############################################################################################
    # Add meshes
    #############################################################################################

    ###############
    # rectangle mesh
    ###############
    # global grid
    if pyvista_LR.add_rectangle_mesh and local_state.do_warp_sphere == False:
        if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
            local_state.rectangle_mesh_added_1 = True
        elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
            local_state.rectangle_mesh_added_2 = True
        elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "10" or (
            str(subplot_index_list[0]) + str(subplot_index_list[1])
        ) == "02":
            local_state.rectangle_mesh_added_3 = True
        elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
            local_state.rectangle_mesh_added_4 = True

        local_state.nothing_show = False
        input_mesh_lens = (
            pyvista_LR.system_size[0]
            * pyvista_LR.system_size[1]
            * pyvista_LR.system_size[2]
        )
        rtm_data = local_state.rectrangle_mesh_image_data

        rtm_data_lens = len(rtm_data)
        if input_mesh_lens == rtm_data_lens:
            values = rtm_data.reshape(pyvista_LR.system_size)

            grid = pv.ImageData()
            grid.dimensions = values.shape
            grid.spacing = pyvista_LR.rectrangle_spacing
            if (
                pyvista_LR.outputfile_type == "ovf"
                or pyvista_LR.outputfile_type == "Excalibur"
            ):
                grid["x_com"] = (
                    vectors_PolyData_1[0, :]
                    # .reshape(pyvista_LR.system_size)
                    # .flatten(order="F")
                )
                grid["y_com"] = (
                    vectors_PolyData_1[1, :]
                    # .reshape(pyvista_LR.system_size)
                    # .flatten(order="F")
                )
                grid["z_com"] = (
                    vectors_PolyData_1[2, :]
                    # .reshape(pyvista_LR.system_size)
                    # .flatten(order="F")
                )
                grid["phi_com"] = c_phi
                # .reshape(pyvista_LR.system_size).flatten(
                # order="F"
                # )  # range [-180,180]
                grid["theta_com"] = c_theta
                # .reshape(pyvista_LR.system_size).flatten(
                # order="F"
                # )  # range [0,180]

                grid.point_data["rmo"] = local_state.rectrangle_mesh_opacity.reshape(
                    pyvista_LR.system_size
                ).flatten(order="F")
            else:
                grid["x_com"] = vectors_PolyData_1[0, :]
                grid["y_com"] = vectors_PolyData_1[1, :]
                grid["z_com"] = vectors_PolyData_1[2, :]
                grid["phi_com"] = c_phi
                grid["theta_com"] = c_theta
                grid.point_data["color_component"] = rtm_data
                grid.point_data["rmo"] = local_state.rectrangle_mesh_opacity

            #########
            # rectangle mesh
            # Filter contour
            #########

        if pyvista_LR.do_rectangle_mesh_contour:
            if pyvista_LR.do_multi_rectangle_surface_contour:
                grid = grid.copy().contour(
                    isosurfaces=pyvista_LR.rectangle_mesh_contour_isosurface_number,
                    scalars=local_state.rec_mesh_color_scalar,
                    method="contour",
                )
            else:
                if pyvista_LR.rectangle_mesh_contour_method_indicator == 0:
                    grid = grid.copy().contour(
                        isosurfaces=[
                            local_state.rectangle_mesh_contour_isosurface_value_x
                        ],
                        scalars="x_com",
                        method="contour",
                    )
                elif pyvista_LR.rectangle_mesh_contour_method_indicator == 1:
                    grid = grid.copy().contour(
                        isosurfaces=[
                            local_state.rectangle_mesh_contour_isosurface_value_y
                        ],
                        scalars="y_com",
                        method="contour",
                    )
                elif pyvista_LR.rectangle_mesh_contour_method_indicator == 2:
                    grid = grid.copy().contour(
                        isosurfaces=[
                            local_state.rectangle_mesh_contour_isosurface_value_z
                        ],
                        scalars="z_com",
                        method="contour",
                    )
                elif pyvista_LR.rectangle_mesh_contour_method_indicator == 3:
                    grid = grid.copy().contour(
                        isosurfaces=[
                            local_state.rectangle_mesh_contour_isosurface_value_t
                        ],
                        scalars="theta_com",
                        method="contour",
                    )
                elif pyvista_LR.rectangle_mesh_contour_method_indicator == 4:
                    grid = grid.copy().contour(
                        isosurfaces=[
                            local_state.rectangle_mesh_contour_isosurface_value_p
                        ],
                        scalars="phi_com",
                        method="contour",
                    )

        #########
        # rectangle mesh
        # Filter warp_by_scalar
        #########
        if pyvista_LR.do_rectangle_mesh_rescale:
            grid = grid.copy().warp_by_scalar(
                scalars=local_state.rec_mesh_color_scalar,
                factor=pyvista_LR.rescale_rectangle_mesh_factor,
                normal=pyvista_LR.rescale_rectangle_mesh_norm,
            )

        #########
        # rectangle mesh
        # Filter clip_scalar
        #########
        if pyvista_LR.do_rectangle_mesh_clip_scalar:
            grid = grid.copy().clip_scalar(
                progress_bar=True,
                scalars="x_com",
                invert=True,
                value=local_state.rectangle_mesh_clip_scalar_max_x,
            )
            grid = grid.copy().clip_scalar(
                progress_bar=True,
                scalars="x_com",
                invert=False,
                value=local_state.rectangle_mesh_clip_scalar_min_x,
            )
            grid = grid.copy().clip_scalar(
                progress_bar=True,
                scalars="y_com",
                invert=True,
                value=local_state.rectangle_mesh_clip_scalar_max_y,
            )
            grid = grid.copy().clip_scalar(
                progress_bar=True,
                scalars="y_com",
                invert=False,
                value=local_state.rectangle_mesh_clip_scalar_min_y,
            )
            grid = grid.copy().clip_scalar(
                progress_bar=True,
                scalars="z_com",
                invert=True,
                value=local_state.rectangle_mesh_clip_scalar_max_z,
            )
            grid = grid.copy().clip_scalar(
                progress_bar=True,
                scalars="z_com",
                invert=False,
                value=local_state.rectangle_mesh_clip_scalar_min_z,
            )
            grid = grid.copy().clip_scalar(
                progress_bar=True,
                scalars="theta_com",
                invert=True,
                value=pyvista_LR.rectangle_mesh_clip_scalar_max_theta,
            )
            grid = grid.copy().clip_scalar(
                progress_bar=True,
                scalars="theta_com",
                invert=False,
                value=pyvista_LR.rectangle_mesh_clip_scalar_min_theta,
            )
            grid = grid.copy().clip_scalar(
                progress_bar=True,
                scalars="phi_com",
                invert=True,
                value=pyvista_LR.rectangle_mesh_clip_scalar_max_phi,
            )
            grid = grid.copy().clip_scalar(
                progress_bar=True,
                scalars="phi_com",
                invert=False,
                value=pyvista_LR.rectangle_mesh_clip_scalar_min_phi,
            )

        #########
        # rectangle mesh
        # Filter clip
        #########
        if pyvista_LR.do_rectangle_mesh_clip:
            # to aviod error we make sure that max should be larger than min at least 0.1
            if (
                pyvista_LR.rectangle_mesh_clip_plane_x_max
                <= pyvista_LR.rectangle_mesh_clip_plane_x_min
            ):
                pyvista_LR.rectangle_mesh_clip_plane_x_max = (
                    pyvista_LR.rectangle_mesh_clip_plane_x_min + 0.1
                )
            if (
                pyvista_LR.rectangle_mesh_clip_plane_y_max
                <= pyvista_LR.rectangle_mesh_clip_plane_y_min
            ):
                pyvista_LR.rectangle_mesh_clip_plane_y_max = (
                    pyvista_LR.rectangle_mesh_clip_plane_y_min + 0.1
                )
            if (
                pyvista_LR.rectangle_mesh_clip_plane_z_max
                <= pyvista_LR.rectangle_mesh_clip_plane_z_min
            ):
                pyvista_LR.rectangle_mesh_clip_plane_z_max = (
                    pyvista_LR.rectangle_mesh_clip_plane_z_min + 0.1
                )
            if (
                pyvista_LR.rectangle_mesh_clip_plane_x_max
                - pyvista_LR.rectangle_mesh_clip_plane_x_min
                <= 1
            ):  # only max than 1 is valid for clip
                pass
            else:
                grid = grid.copy().clip(
                    "x",
                    invert=False,
                    origin=(grid.bounds[0], grid.bounds[2], grid.bounds[4]),
                    value=pyvista_LR.rectangle_mesh_clip_plane_x_min,
                )
                grid = grid.copy().clip(
                    "x",
                    invert=True,
                    origin=(grid.bounds[0], grid.bounds[2], grid.bounds[4]),
                    value=pyvista_LR.rectangle_mesh_clip_plane_x_max,
                )

            if (
                pyvista_LR.rectangle_mesh_clip_plane_y_max
                - pyvista_LR.rectangle_mesh_clip_plane_y_min
                <= 1
            ):  # only max than 1 is valid for clip
                pass
            else:
                grid = grid.copy().clip(
                    "y",
                    invert=False,
                    origin=(grid.bounds[0], grid.bounds[2], grid.bounds[4]),
                    value=pyvista_LR.rectangle_mesh_clip_plane_y_min,
                )
                grid = grid.copy().clip(
                    "y",
                    invert=True,
                    origin=(grid.bounds[0], grid.bounds[2], grid.bounds[4]),
                    value=pyvista_LR.rectangle_mesh_clip_plane_y_max,
                )
            if (
                pyvista_LR.rectangle_mesh_clip_plane_z_max
                - pyvista_LR.rectangle_mesh_clip_plane_z_min
                <= 1
            ):  # only max than 1 is valid for clip
                pass
            else:
                grid = grid.copy().clip(
                    "z",
                    invert=False,
                    origin=(grid.bounds[0], grid.bounds[2], grid.bounds[4]),
                    value=pyvista_LR.rectangle_mesh_clip_plane_z_min,
                )
                grid = grid.copy().clip(
                    "z",
                    invert=True,
                    origin=(grid.bounds[0], grid.bounds[2], grid.bounds[4]),
                    value=pyvista_LR.rectangle_mesh_clip_plane_z_max,
                )

        if pyvista_LR.do_clip_rectangle_mesh_free_normal:
            # to aviod error we make sure that clip_rectangle_mesh_free_2 should be larger than clip_rectangle_mesh_free_1 at least 0.1
            if (
                pyvista_LR.clip_rectangle_mesh_free_1
                <= pyvista_LR.clip_rectangle_mesh_free_2
            ):
                pyvista_LR.clip_rectangle_mesh_free_2 = (
                    pyvista_LR.clip_rectangle_mesh_free_1 + 0.1
                )
            grid = grid.copy().clip(
                pyvista_LR.rectangle_mesh_clip_plane_free_normal_1,
                invert=False,
                origin=(grid.bounds[0], grid.bounds[2], grid.bounds[4]),
                value=pyvista_LR.clip_rectangle_mesh_free_1,
            )
            grid = grid.copy().clip(
                pyvista_LR.rectangle_mesh_clip_plane_free_normal_2,
                invert=True,
                origin=(grid.bounds[0], grid.bounds[2], grid.bounds[4]),
                value=pyvista_LR.clip_rectangle_mesh_free_2,
            )

        if (
            int(pyvista_LR.rectrangle_opacity_index) == 6
            and local_state.opacity_record_rectangle_mesh == 1
        ):
            actor_list[
                "actor_rectangle_mesh_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1])
            ] = plotter.add_mesh(
                grid,
                scalars=local_state.rec_mesh_color_scalar,
                clim=local_state.rectrangle_clim_range,
                name="rectangle_mesh"
                + "_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1]),
                cmap=pyvista_LR.cmap_record,
                opacity=True,
                show_scalar_bar=pyvista_LR.show_rectangle_mesh_scalar_bar,
                interpolate_before_map=pyvista_LR.rectangle_mesh_interpolate_before_map,
                pbr=pyvista_LR.pbr_rectangle,
                metallic=local_state.metallic_rmesh,
                roughness=local_state.roughness_rmesh,
                scalar_bar_args={
                    "title": local_state.rectangle_mesh_scalar_bar_name
                    + "_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                },
            )
        else:
            actor_list[
                "actor_rectangle_mesh_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1])
            ] = plotter.add_mesh(
                grid,
                scalars=local_state.rec_mesh_color_scalar,
                clim=local_state.rectrangle_clim_range,
                name="rectangle_mesh"
                + "_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1]),
                cmap=pyvista_LR.cmap_record,
                opacity="rmo",
                show_scalar_bar=pyvista_LR.show_rectangle_mesh_scalar_bar,
                interpolate_before_map=pyvista_LR.rectangle_mesh_interpolate_before_map,
                pbr=pyvista_LR.pbr_rectangle,
                metallic=local_state.metallic_rmesh,
                roughness=local_state.roughness_rmesh,
                scalar_bar_args={
                    "title": local_state.rectangle_mesh_scalar_bar_name
                    + "_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                },
            )

    if (pyvista_LR.add_rectangle_mesh == False) and (
        local_state.rectangle_mesh_added_1
        or local_state.rectangle_mesh_added_2
        or local_state.rectangle_mesh_added_3
        or local_state.rectangle_mesh_added_4
    ) == True:
        try:
            (
                eval(
                    "actor_rectangle_mesh_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                )
            ).SetVisibility(False)
            plotter.remove_scalar_bar(
                local_state.rectangle_mesh_scalar_bar_name
                + "_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1])
            )
            if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                local_state.rectangle_mesh_added_1 = False
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                local_state.rectangle_mesh_added_2 = False
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "10" or (
                str(subplot_index_list[0]) + str(subplot_index_list[1])
            ) == "02":
                local_state.rectangle_mesh_added_3 = False
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                local_state.rectangle_mesh_added_4 = False
        except:
            print("Oops, actor: rectangle mesh in subplot 4 seems not removed")
            pass
    elif pyvista_LR.add_rectangle_mesh == True:
        eval(
            "actor_rectangle_mesh_"
            + str(subplot_index_list[0])
            + str(subplot_index_list[1])
        ).SetVisibility(True)

    ###################
    # unstructured mesh
    ###################

    if pyvista_LR.add_unstructured_mesh and local_state.do_warp_sphere == False:
        if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
            local_state.unstructured_mesh_added_1 = True
        elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
            local_state.unstructured_mesh_added_2 = True
        elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "10" or (
            str(subplot_index_list[0]) + str(subplot_index_list[1])
        ) == "02":
            local_state.unstructured_mesh_added_3 = True
        elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
            local_state.unstructured_mesh_added_4 = True

        global surf, surf_for_contour, surf_for_warp, surf_for_clip_scalar, surf_for_clip_filter, surf_for_clip_filter_free_norm, surf_for_filter_slice, surf_for_clip_box, surf_for_clip_along_axis, surf_for_contour_1, surf_for_contour_2, surf_for_contour_3, surf_for_contour_4  # we set this to global to keep it in the memory, so that we can use it in the next time if the frame is not change.
        if local_state.frame_change == True:
            if len(set(coord_xyz[:, 2])) == 1:  # this means we have a 2D system
                print(
                    "[red]2D[/red] system is detected, [yellow]2D delaunay triangulation[/yellow] applied."
                )
                surf = point_cloud_arrow_unstructured.delaunay_2d(progress_bar=True)
            else:
                print(
                    "[red]3D[/red] system is detected, [yellow]3D delaunay triangulation[/yellow] applied."
                )
                surf = point_cloud_arrow_unstructured.delaunay_3d(progress_bar=True)

            if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                surf_for_contour_1 = surf.copy()
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                surf_for_contour_2 = surf.copy()
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "10" or (
                str(subplot_index_list[0]) + str(subplot_index_list[1])
            ) == "02":
                surf_for_contour_3 = surf.copy()
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                surf_for_contour_4 = surf.copy()

            if pyvista_LR.sub_frame_number == 1:
                local_state.frame_change = False

            elif (
                pyvista_LR.sub_frame_number == 2
                and local_state.unstructured_mesh_added_2 == True
            ):
                local_state.frame_change = False
                local_state.unstructured_mesh_added_2 = False
            elif (
                pyvista_LR.sub_frame_number == 3
                and local_state.unstructured_mesh_added_3 == True
            ):
                local_state.frame_change = False
                local_state.unstructured_mesh_added_3 = False
            elif (
                pyvista_LR.sub_frame_number == 4
                and local_state.unstructured_mesh_added_4 == True
            ):
                local_state.frame_change = False
                local_state.unstructured_mesh_added_4 = False

        else:
            pass

        if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
            surf_for_contour = surf_for_contour_1
        elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
            surf_for_contour = surf_for_contour_2
        elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "10" or (
            str(subplot_index_list[0]) + str(subplot_index_list[1])
        ) == "02":
            surf_for_contour = surf_for_contour_3
        elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
            surf_for_contour = surf_for_contour_4

        #########
        # unstructured mesh
        # Filter contour
        #########
        if pyvista_LR.do_unstructured_mesh_contour:
            if pyvista_LR.do_multi_unstructured_surface_contour:
                isosurfaces_parm_us = (
                    pyvista_LR.unstructured_mesh_contour_isosurface_number
                )
                surf = surf_for_contour.copy().contour(
                    isosurfaces=isosurfaces_parm_us,
                    scalars=local_state.unstructured_mesh_scalar_bar_name,
                    method="contour",
                )
                surf_for_warp = surf.copy()
            else:
                if pyvista_LR.unstructured_mesh_contour_method_indicator == 0:
                    surf = surf_for_contour.copy().contour(
                        isosurfaces=[local_state.t_mesh_contour_isosurface_value_x],
                        scalars="UM_x",
                        method="contour",
                    )
                    surf_for_warp = surf.copy()

                elif pyvista_LR.unstructured_mesh_contour_method_indicator == 1:
                    surf = surf_for_contour.copy().contour(
                        isosurfaces=[local_state.t_mesh_contour_isosurface_value_y],
                        scalars="UM_y",
                        method="contour",
                    )
                    surf_for_warp = surf.copy()

                elif pyvista_LR.unstructured_mesh_contour_method_indicator == 2:
                    surf = surf_for_contour.copy().contour(
                        isosurfaces=[local_state.t_mesh_contour_isosurface_value_z],
                        scalars="UM_z",
                        method="contour",
                    )
                    surf_for_warp = surf.copy()

                elif pyvista_LR.unstructured_mesh_contour_method_indicator == 3:
                    surf = surf_for_contour.copy().contour(
                        isosurfaces=[
                            local_state.unstructured_mesh_contour_isosurface_value_t
                        ],
                        scalars="UM_theta",
                        method="contour",
                    )
                    surf_for_warp = surf.copy()

                elif pyvista_LR.unstructured_mesh_contour_method_indicator == 4:
                    surf = surf_for_contour.copy().contour(
                        isosurfaces=[
                            local_state.unstructured_mesh_contour_isosurface_value_p
                        ],
                        scalars="UM_phi",
                        method="contour",
                    )
                    surf_for_warp = surf.copy()
        else:
            surf = surf_for_contour.copy()

        #########
        # unstructured mesh
        # Filter warp_by_scalar
        #########
        if pyvista_LR.do_unstructured_mesh_rescale:
            if pyvista_LR.do_unstructured_mesh_contour:
                surf = surf_for_warp.copy().warp_by_scalar(
                    scalars=local_state.unstructured_mesh_scalar_bar_name,
                    factor=pyvista_LR.rescale_unstructured_mesh_factor,
                    normal=pyvista_LR.rescale_unstructured_mesh_norm,
                )
            else:
                surf = surf_for_contour.copy().warp_by_scalar(
                    scalars=local_state.unstructured_mesh_scalar_bar_name,
                    factor=pyvista_LR.rescale_unstructured_mesh_factor,
                    normal=pyvista_LR.rescale_unstructured_mesh_norm,
                )
            surf_for_clip_scalar = surf.copy()
        else:
            if pyvista_LR.do_unstructured_mesh_contour:
                surf = surf_for_warp.copy()
            else:
                surf = surf_for_contour.copy()

        #########
        # unstructured mesh
        # Filter clip_scalar
        #########
        if pyvista_LR.do_unstructured_mesh_clip_scalar:
            if pyvista_LR.do_unstructured_mesh_rescale:
                surf = surf_for_clip_scalar.copy().clip_scalar(
                    scalars="UM_x",
                    invert=True,
                    value=local_state.t_mesh_clip_scalar_max_x,
                )
                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_x",
                    invert=False,
                    value=local_state.t_mesh_clip_scalar_min_x,
                )

                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_y",
                    invert=True,
                    value=local_state.t_mesh_clip_scalar_max_y,
                )
                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_y",
                    invert=False,
                    value=local_state.t_mesh_clip_scalar_min_y,
                )

                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_z",
                    invert=True,
                    value=local_state.t_mesh_clip_scalar_max_z,
                )
                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_z",
                    invert=False,
                    value=local_state.t_mesh_clip_scalar_min_z,
                )

                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_theta",
                    invert=True,
                    value=pyvista_LR.unstructured_mesh_clip_scalar_max_theta,
                )
                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_theta",
                    invert=False,
                    value=pyvista_LR.unstructured_mesh_clip_scalar_min_theta,
                )

                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_phi",
                    invert=True,
                    value=pyvista_LR.unstructured_mesh_clip_scalar_max_phi,
                )
                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_phi",
                    invert=False,
                    value=pyvista_LR.unstructured_mesh_clip_scalar_min_phi,
                )

                surf_for_clip_filter = surf.copy()

            elif (
                pyvista_LR.do_unstructured_mesh_rescale == False
                and pyvista_LR.do_unstructured_mesh_contour == True
            ):
                surf = surf_for_warp.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_x",
                    invert=True,
                    value=local_state.t_mesh_clip_scalar_max_x,
                )
                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_x",
                    invert=False,
                    value=local_state.t_mesh_clip_scalar_min_x,
                )

                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_y",
                    invert=True,
                    value=local_state.t_mesh_clip_scalar_max_y,
                )
                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_y",
                    invert=False,
                    value=local_state.t_mesh_clip_scalar_min_y,
                )

                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_z",
                    invert=True,
                    value=local_state.t_mesh_clip_scalar_max_z,
                )
                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_z",
                    invert=False,
                    value=local_state.t_mesh_clip_scalar_min_z,
                )

                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="theta_com",
                    invert=True,
                    value=pyvista_LR.unstructured_mesh_clip_scalar_max_theta,
                )
                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="theta_com",
                    invert=False,
                    value=pyvista_LR.unstructured_mesh_clip_scalar_min_theta,
                )

                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_phi",
                    invert=True,
                    value=pyvista_LR.unstructured_mesh_clip_scalar_max_phi,
                )
                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_phi",
                    invert=False,
                    value=pyvista_LR.unstructured_mesh_clip_scalar_min_phi,
                )
                surf_for_clip_filter = surf.copy()
            else:
                surf = surf_for_contour.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_x",
                    invert=True,
                    value=local_state.t_mesh_clip_scalar_max_x,
                )
                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_x",
                    invert=False,
                    value=local_state.t_mesh_clip_scalar_min_x,
                )

                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_y",
                    invert=True,
                    value=local_state.t_mesh_clip_scalar_max_y,
                )
                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_y",
                    invert=False,
                    value=local_state.t_mesh_clip_scalar_min_y,
                )

                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_z",
                    invert=True,
                    value=local_state.t_mesh_clip_scalar_max_z,
                )
                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_z",
                    invert=False,
                    value=local_state.t_mesh_clip_scalar_min_z,
                )

                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_theta",
                    invert=True,
                    value=pyvista_LR.unstructured_mesh_clip_scalar_max_theta,
                )
                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_theta",
                    invert=False,
                    value=pyvista_LR.unstructured_mesh_clip_scalar_min_theta,
                )

                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_phi",
                    invert=True,
                    value=pyvista_LR.unstructured_mesh_clip_scalar_max_phi,
                )
                surf = surf.copy().clip_scalar(
                    progress_bar=True,
                    scalars="UM_phi",
                    invert=False,
                    value=pyvista_LR.unstructured_mesh_clip_scalar_min_phi,
                )
                surf_for_clip_filter = surf.copy()

        else:
            if pyvista_LR.do_unstructured_mesh_rescale:
                surf = surf_for_clip_scalar.copy()
            elif (
                pyvista_LR.do_unstructured_mesh_rescale == False
                and pyvista_LR.do_unstructured_mesh_contour == True
            ):
                surf = surf_for_warp.copy()
            else:
                surf = surf_for_contour.copy()

        #########
        # unstructured mesh
        # Filter clip
        #########
        if pyvista_LR.do_unstructured_mesh_clip:
            if pyvista_LR.do_unstructured_mesh_clip_scalar:
                # to aviod error we make sure that max should be larger than min at least 0.1
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_x_max
                    <= pyvista_LR.unstructured_mesh_clip_plane_x_min
                ):
                    pyvista_LR.unstructured_mesh_clip_plane_x_max = (
                        pyvista_LR.unstructured_mesh_clip_plane_x_min + 0.1
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_y_max
                    <= pyvista_LR.unstructured_mesh_clip_plane_y_min
                ):
                    pyvista_LR.unstructured_mesh_clip_plane_y_max = (
                        pyvista_LR.unstructured_mesh_clip_plane_y_min + 0.1
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_z_max
                    <= pyvista_LR.unstructured_mesh_clip_plane_z_min
                ):
                    pyvista_LR.unstructured_mesh_clip_plane_z_max = (
                        pyvista_LR.unstructured_mesh_clip_plane_z_min + 0.1
                    )
                if (
                    pyvista_LR.clip_unstructured_mesh_free_2
                    <= pyvista_LR.clip_unstructured_mesh_free_1
                ):
                    pyvista_LR.clip_unstructured_mesh_free_2 = (
                        pyvista_LR.clip_unstructured_mesh_free_1 + 0.1
                    )

                if (
                    pyvista_LR.unstructured_mesh_clip_plane_x_max
                    - pyvista_LR.unstructured_mesh_clip_plane_x_min
                    <= 1
                ):  # only max than 1 is valid for clip
                    pass
                else:
                    surf = surf_for_clip_filter.copy().clip(
                        "x",
                        invert=False,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_x_min,
                    )
                    surf = surf.copy().clip(
                        "x",
                        invert=True,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_x_max,
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_y_max
                    - pyvista_LR.unstructured_mesh_clip_plane_y_min
                    <= 1
                ):  # only max than 1 is valid for clip
                    pass
                else:
                    surf = surf.copy().clip(
                        "y",
                        invert=False,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_y_min,
                    )
                    surf = surf.copy().clip(
                        "y",
                        invert=True,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_y_max,
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_z_max
                    - pyvista_LR.unstructured_mesh_clip_plane_z_min
                    <= 1
                ):  # only max than 1 is valid for clip
                    pass
                else:
                    surf = surf.copy().clip(
                        "z",
                        invert=False,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_z_min,
                    )
                    surf = surf.copy().clip(
                        "z",
                        invert=True,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_z_max,
                    )
                surf_for_clip_filter_free_norm = surf.copy()
            elif (
                pyvista_LR.do_unstructured_mesh_clip_scalar == False
                and pyvista_LR.do_unstructured_mesh_rescale == True
            ):
                # to aviod error we make sure that max should be larger than min at least 0.1
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_x_max
                    <= pyvista_LR.unstructured_mesh_clip_plane_x_min
                ):
                    pyvista_LR.unstructured_mesh_clip_plane_x_max = (
                        pyvista_LR.unstructured_mesh_clip_plane_x_min + 0.1
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_y_max
                    <= pyvista_LR.unstructured_mesh_clip_plane_y_min
                ):
                    pyvista_LR.unstructured_mesh_clip_plane_y_max = (
                        pyvista_LR.unstructured_mesh_clip_plane_y_min + 0.1
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_z_max
                    <= pyvista_LR.unstructured_mesh_clip_plane_z_min
                ):
                    pyvista_LR.unstructured_mesh_clip_plane_z_max = (
                        pyvista_LR.unstructured_mesh_clip_plane_z_min + 0.1
                    )
                if (
                    pyvista_LR.clip_unstructured_mesh_free_2
                    <= pyvista_LR.clip_unstructured_mesh_free_1
                ):
                    pyvista_LR.clip_unstructured_mesh_free_2 = (
                        pyvista_LR.clip_unstructured_mesh_free_1 + 0.1
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_x_max
                    - pyvista_LR.unstructured_mesh_clip_plane_x_min
                    <= 1
                ):  # only max than 1 is valid for clip
                    pass
                else:
                    surf = surf_for_clip_scalar.copy().clip(
                        "x",
                        invert=False,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_x_min,
                    )
                    surf = surf.copy().clip(
                        "x",
                        invert=True,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_x_max,
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_y_max
                    - pyvista_LR.unstructured_mesh_clip_plane_y_min
                    <= 1
                ):  # only max than 1 is valid for clip
                    pass
                else:
                    surf = surf.copy().clip(
                        "y",
                        invert=False,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_y_min,
                    )
                    surf = surf.copy().clip(
                        "y",
                        invert=True,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_y_max,
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_z_max
                    - pyvista_LR.unstructured_mesh_clip_plane_z_min
                    <= 1
                ):  # only max than 1 is valid for clip
                    pass
                else:
                    surf = surf.copy().clip(
                        "z",
                        invert=False,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_z_min,
                    )
                    surf = surf.copy().clip(
                        "z",
                        invert=True,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_z_max,
                    )
                surf_for_clip_filter_free_norm = surf.copy()
            elif (
                pyvista_LR.do_unstructured_mesh_clip_scalar == False
                and pyvista_LR.do_unstructured_mesh_rescale == False
                and pyvista_LR.do_unstructured_mesh_contour == True
            ):
                # to aviod error we make sure that max should be larger than min at least 0.1
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_x_max
                    <= pyvista_LR.unstructured_mesh_clip_plane_x_min
                ):
                    pyvista_LR.unstructured_mesh_clip_plane_x_max = (
                        pyvista_LR.unstructured_mesh_clip_plane_x_min + 0.1
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_y_max
                    <= pyvista_LR.unstructured_mesh_clip_plane_y_min
                ):
                    pyvista_LR.unstructured_mesh_clip_plane_y_max = (
                        pyvista_LR.unstructured_mesh_clip_plane_y_min + 0.1
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_z_max
                    <= pyvista_LR.unstructured_mesh_clip_plane_z_min
                ):
                    pyvista_LR.unstructured_mesh_clip_plane_z_max = (
                        pyvista_LR.unstructured_mesh_clip_plane_z_min + 0.1
                    )
                if (
                    pyvista_LR.clip_unstructured_mesh_free_2
                    <= pyvista_LR.clip_unstructured_mesh_free_1
                ):
                    pyvista_LR.clip_unstructured_mesh_free_2 = (
                        pyvista_LR.clip_unstructured_mesh_free_1 + 0.1
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_x_max
                    - pyvista_LR.unstructured_mesh_clip_plane_x_min
                    <= 1
                ):  # only max than 1 is valid for clip
                    pass
                else:
                    surf = surf_for_warp.copy().clip(
                        "x",
                        invert=False,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_x_min,
                    )
                    surf = surf.copy().clip(
                        "x",
                        invert=True,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_x_max,
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_y_max
                    - pyvista_LR.unstructured_mesh_clip_plane_y_min
                    <= 1
                ):  # only max than 1 is valid for clip
                    pass
                else:
                    surf = surf.copy().clip(
                        "y",
                        invert=False,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_y_min,
                    )
                    surf = surf.copy().clip(
                        "y",
                        invert=True,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_y_max,
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_z_max
                    - pyvista_LR.unstructured_mesh_clip_plane_z_min
                    <= 1
                ):  # only max than 1 is valid for clip
                    pass
                else:
                    surf = surf.copy().clip(
                        "z",
                        invert=False,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_z_min,
                    )
                    surf = surf.copy().clip(
                        "z",
                        invert=True,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_z_max,
                    )
                surf_for_clip_filter_free_norm = surf.copy()
            else:
                # to aviod error we make sure that max should be larger than min at least 0.1
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_x_max
                    <= pyvista_LR.unstructured_mesh_clip_plane_x_min
                ):
                    pyvista_LR.unstructured_mesh_clip_plane_x_max = (
                        pyvista_LR.unstructured_mesh_clip_plane_x_min + 0.1
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_y_max
                    <= pyvista_LR.unstructured_mesh_clip_plane_y_min
                ):
                    pyvista_LR.unstructured_mesh_clip_plane_y_max = (
                        pyvista_LR.unstructured_mesh_clip_plane_y_min + 0.1
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_z_max
                    <= pyvista_LR.unstructured_mesh_clip_plane_z_min
                ):
                    pyvista_LR.unstructured_mesh_clip_plane_z_max = (
                        pyvista_LR.unstructured_mesh_clip_plane_z_min + 0.1
                    )
                if (
                    pyvista_LR.clip_unstructured_mesh_free_2
                    <= pyvista_LR.clip_unstructured_mesh_free_1
                ):
                    pyvista_LR.clip_unstructured_mesh_free_2 = (
                        pyvista_LR.clip_unstructured_mesh_free_1 + 0.1
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_x_max
                    - pyvista_LR.unstructured_mesh_clip_plane_x_min
                    <= 1
                ):  # only max than 1 is valid for clip
                    pass
                else:
                    surf = surf_for_contour.copy().clip(
                        "x",
                        invert=False,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_x_min,
                    )
                    surf = surf.copy().clip(
                        "x",
                        invert=True,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_x_max,
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_y_max
                    - pyvista_LR.unstructured_mesh_clip_plane_y_min
                    <= 1
                ):  # only max than 1 is valid for clip
                    pass
                else:
                    surf = surf.copy().clip(
                        "y",
                        invert=False,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_y_min,
                    )
                    surf = surf.copy().clip(
                        "y",
                        invert=True,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_y_max,
                    )
                if (
                    pyvista_LR.unstructured_mesh_clip_plane_z_max
                    - pyvista_LR.unstructured_mesh_clip_plane_z_min
                    <= 1
                ):  # only max than 1 is valid for clip
                    pass
                else:
                    surf = surf.copy().clip(
                        "z",
                        invert=False,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_z_min,
                    )
                    surf = surf.copy().clip(
                        "z",
                        invert=True,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.unstructured_mesh_clip_plane_z_max,
                    )
                surf_for_clip_filter_free_norm = surf.copy()

        if pyvista_LR.do_clip_unstructured_mesh_free_normal:
            if pyvista_LR.do_unstructured_mesh_clip_scalar:
                if (
                    pyvista_LR.clip_unstructured_mesh_free_2
                    - pyvista_LR.clip_unstructured_mesh_free_1
                    <= 1
                ):
                    print(
                        "Free Clip not work, it is too close for two clip planes, please increase the difference between two clip planes"
                    )
                    pass
                else:
                    surf = surf_for_clip_filter_free_norm.copy().clip(
                        pyvista_LR.unstructured_mesh_clip_plane_free_normal_1,
                        invert=False,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.clip_unstructured_mesh_free_1,
                    )
                    surf = surf.copy().clip(
                        pyvista_LR.unstructured_mesh_clip_plane_free_normal_2,
                        invert=True,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.clip_unstructured_mesh_free_2,
                    )
                surf_for_filter_slice = surf.copy()
            elif (
                pyvista_LR.do_unstructured_mesh_clip_scalar == False
                and pyvista_LR.do_unstructured_mesh_rescale == True
            ):
                if (
                    pyvista_LR.clip_unstructured_mesh_free_2
                    - pyvista_LR.clip_unstructured_mesh_free_1
                    <= 1
                ):
                    print(
                        "Free Clip not work, it is too close for two clip planes, please increase the difference between two clip planes"
                    )
                    pass
                else:
                    surf = surf_for_clip_scalar.copy().clip(
                        pyvista_LR.unstructured_mesh_clip_plane_free_normal_1,
                        invert=False,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.clip_unstructured_mesh_free_1,
                    )
                    surf = surf.copy().clip(
                        pyvista_LR.unstructured_mesh_clip_plane_free_normal_2,
                        invert=True,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.clip_unstructured_mesh_free_2,
                    )
                surf_for_filter_slice = surf.copy()
            elif (
                pyvista_LR.do_unstructured_mesh_clip_scalar == False
                and pyvista_LR.do_unstructured_mesh_rescale == False
                and pyvista_LR.do_unstructured_mesh_contour == True
            ):
                if (
                    pyvista_LR.clip_unstructured_mesh_free_2
                    - pyvista_LR.clip_unstructured_mesh_free_1
                    <= 1
                ):
                    print(
                        "Free Clip not work, it is too close for two clip planes, please increase the difference between two clip planes"
                    )
                    pass
                else:
                    surf = surf_for_warp.copy().clip(
                        pyvista_LR.unstructured_mesh_clip_plane_free_normal_1,
                        invert=False,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.clip_unstructured_mesh_free_1,
                    )
                    surf = surf.copy().clip(
                        pyvista_LR.unstructured_mesh_clip_plane_free_normal_2,
                        invert=True,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.clip_unstructured_mesh_free_2,
                    )
                surf_for_filter_slice = surf.copy()
            else:
                if (
                    pyvista_LR.clip_unstructured_mesh_free_2
                    - pyvista_LR.clip_unstructured_mesh_free_1
                    <= 1
                ):
                    print(
                        "Free Clip not work, it is too close for two clip planes, please increase the difference between two clip planes"
                    )
                    pass
                else:
                    surf = surf_for_contour.copy().clip(
                        pyvista_LR.unstructured_mesh_clip_plane_free_normal_1,
                        invert=False,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.clip_unstructured_mesh_free_1,
                    )
                    surf = surf.copy().clip(
                        pyvista_LR.unstructured_mesh_clip_plane_free_normal_2,
                        invert=True,
                        origin=(surf.bounds[0], surf.bounds[2], surf.bounds[4]),
                        value=pyvista_LR.clip_unstructured_mesh_free_2,
                    )
                surf_for_filter_slice = surf.copy()
        if (
            int(pyvista_LR.unstructured_mesh_color_map_opacity_index) == 6
            and local_state.opacity_record_tmesh == 1
        ):
            actor_list[
                "actor_unstructured_mesh_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1])
            ] = plotter.add_mesh(
                surf,
                scalars=local_state.unstructured_mesh_scalar_bar_name,
                clim=local_state.clim_range_unstructured_mesh,
                name="unstructured_mesh"
                + "_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1]),
                cmap=pyvista_LR.cmap_record,
                opacity=True,
                show_scalar_bar=pyvista_LR.show_unstructured_mesh_scalar_bar,
                interpolate_before_map=pyvista_LR.unstructured_mesh_interpolate_before_map,
                pbr=pyvista_LR.pbr_unstructured,
                metallic=local_state.metallic_tmesh,
                roughness=local_state.roughness_tmesh,
                scalar_bar_args={
                    "title": local_state.unstructured_mesh_scalar_bar_name
                    + "_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                },
            )
        else:
            actor_list[
                "actor_unstructured_mesh_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1])
            ] = plotter.add_mesh(
                surf,
                scalars=local_state.unstructured_mesh_scalar_bar_name,
                clim=local_state.clim_range_unstructured_mesh,
                name="unstructured_mesh"
                + "_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1]),
                cmap=pyvista_LR.cmap_record,
                opacity=local_state.tmesh_op_indicator,
                show_scalar_bar=pyvista_LR.show_unstructured_mesh_scalar_bar,
                interpolate_before_map=pyvista_LR.unstructured_mesh_interpolate_before_map,
                pbr=pyvista_LR.pbr_unstructured,
                metallic=local_state.metallic_tmesh,
                roughness=local_state.roughness_tmesh,
                scalar_bar_args={
                    "title": local_state.unstructured_mesh_scalar_bar_name
                    + "_"
                    + str(subplot_index_list[0])
                    + str(subplot_index_list[1])
                },
            )

    if (pyvista_LR.add_unstructured_mesh == False) and (
        local_state.unstructured_mesh_added_1
        or local_state.unstructured_mesh_added_2
        or local_state.unstructured_mesh_added_3
        or local_state.unstructured_mesh_added_4
    ) == True:
        eval(
            "actor_unstructured_mesh_"
            + str(subplot_index_list[0])
            + str(subplot_index_list[1])
        ).SetVisibility(False)
        try:
            eval(
                "actor_unstructured_mesh_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1])
            ).SetVisibility(False)
            plotter.remove_scalar_bar(
                local_state.unstructured_mesh_scalar_bar_name
                + "_"
                + str(subplot_index_list[0])
                + str(subplot_index_list[1])
            )
            if (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "00":
                local_state.unstructured_mesh_added_1 = False
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "01":
                local_state.unstructured_mesh_added_2 = False
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "02" or (
                str(subplot_index_list[0]) + str(subplot_index_list[1])
            ) == "10":
                local_state.unstructured_mesh_added_3 = False
            elif (str(subplot_index_list[0]) + str(subplot_index_list[1])) == "11":
                local_state.unstructured_mesh_added_4 = False
        except:
            print("Oops, actor: T mesh in subplot 4 seems not removed")
            pass
    elif pyvista_LR.add_unstructured_mesh == True:
        eval(
            "actor_unstructured_mesh_"
            + str(subplot_index_list[0])
            + str(subplot_index_list[1])
        ).SetVisibility(True)


def initial_plotter(pyvista_LR, plotter):
    plotter.camera.position = pyvista_LR.camera_position
    plotter.camera.focal_point = pyvista_LR.camera_focal_point
    plotter.camera.up = pyvista_LR.camera_up
    plotter.camera.zoom = pyvista_LR.camera_zoom
    plotter.enable_anti_aliasing(pyvista_LR.antialiasing)


def plot_multiple_meshes(pyvista_LR, plotter, local_state):
    if local_state.sub_frame_number == 1:
        local_state.max_frame = (
            int(len(local_state.mom_states_x) / len(local_state.coord)) - 1
        )

        plotter_add_mesh(
            pyvista_LR,
            local_state.coord,
            local_state.mom_states_x_one_frame,
            local_state.mom_states_y_one_frame,
            local_state.mom_states_z_one_frame,
            plotter,
            local_state=local_state,
        )

    elif local_state.sub_frame_number == 2:
        plotter_add_mesh(
            pyvista_LR,
            local_state.coord,
            local_state.mom_states_x_one_frame,
            local_state.mom_states_y_one_frame,
            local_state.mom_states_z_one_frame,
            plotter,
            subplot_index_list=[0, 0],
            local_state=local_state,
        )
        plotter_add_mesh(
            pyvista_LR,
            local_state.coord,
            local_state.mom_states_x_one_frame1,
            local_state.mom_states_y_one_frame1,
            local_state.mom_states_z_one_frame1,
            plotter,
            subplot_index_list=[0, 1],
            local_state=local_state,
        )

    elif local_state.sub_frame_number == 3:
        plotter_add_mesh(
            pyvista_LR,
            local_state.coord,
            local_state.mom_states_x_one_frame,
            local_state.mom_states_y_one_frame,
            local_state.mom_states_z_one_frame,
            plotter,
            local_state=local_state,
        )
        plotter_add_mesh(
            pyvista_LR,
            local_state.coord,
            local_state.mom_states_x_one_frame1,
            local_state.mom_states_y_one_frame1,
            local_state.mom_states_z_one_frame1,
            plotter,
            subplot_index_list=[0, 1],
            local_state=local_state,
        )
        plotter_add_mesh(
            pyvista_LR,
            local_state.coord,
            local_state.mom_states_x_one_frame2,
            local_state.mom_states_y_one_frame2,
            local_state.mom_states_z_one_frame2,
            plotter,
            subplot_index_list=[0, 2],
            local_state=local_state,
        )

    elif local_state.sub_frame_number == 4:
        plotter_add_mesh(
            pyvista_LR,
            local_state.coord,
            local_state.mom_states_x_one_frame,
            local_state.mom_states_y_one_frame,
            local_state.mom_states_z_one_frame,
            plotter,
            local_state=local_state,
        )
        plotter_add_mesh(
            pyvista_LR,
            local_state.coord,
            local_state.mom_states_x_one_frame1,
            local_state.mom_states_y_one_frame1,
            local_state.mom_states_z_one_frame1,
            plotter,
            subplot_index_list=[0, 1],
            local_state=local_state,
        )
        plotter_add_mesh(
            pyvista_LR,
            local_state.coord,
            local_state.mom_states_x_one_frame2,
            local_state.mom_states_y_one_frame2,
            local_state.mom_states_z_one_frame2,
            plotter,
            subplot_index_list=[1, 0],
            local_state=local_state,
        )
        plotter_add_mesh(
            pyvista_LR,
            local_state.coord,
            local_state.mom_states_x_one_frame3,
            local_state.mom_states_y_one_frame3,
            local_state.mom_states_z_one_frame3,
            plotter,
            subplot_index_list=[1, 1],
            local_state=local_state,
        )
    if local_state.unified_control:
        plotter.link_views()
    else:
        pass
