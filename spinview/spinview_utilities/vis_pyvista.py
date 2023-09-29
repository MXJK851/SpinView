"""
In this file, we have store all the parameters for pyvista rendering, and we can use this file to store the parameters in the database.

Author: Qichen Xu mxjk851@gmail.com/qichenx@kth.se

2023-7-10

Wish you have 'sommartid'(summer time) everyday!

"""


# PyVista
import sqlite3
from os import path
import pyvista as pv

from .profile_DB import (
    check_profile,
    read_property,
    creat_new_table,
    creat_new_keys,
)


def delete_table(db_path, table_name):
    if path.exists(path.expanduser(db_path)):
        con = sqlite3.connect(path.expanduser(db_path))
        cur = con.cursor()
        cur.execute("DROP TABLE {}".format(table_name))
        con.commit()
        con.close()
    else:
        raise Exception("Can not find database {}".format(db_path))


class pyvista_local_rendering:
    # this indicator is used to indicate the code is initilized or not
    # if the code is not initilized, it will not check all tuning parameters, to reduce the cold start time.
    # now we have: cmap frame metallic opacity     roughness resolutions Ratio cone_highth cone_Radius  cs Cut_X Cut_Y Cut_Z fxyzc

    # ToDo :  Read those parameters from database one by one is too slow now, we need to updated to sequencial reading.
    def __init__(self, db_path, table_name):
        self.table_name = eval(read_property(db_path, table_name, "table_name"))[0]
        self.code_init_indicator_cmap = eval(
            read_property(db_path, table_name, "code_init_indicator_cmap")
        )
        self.code_init_indicator_frame = eval(
            read_property(db_path, table_name, "code_init_indicator_frame")
        )
        self.code_init_indicator_metallic = eval(
            read_property(db_path, table_name, "code_init_indicator_metallic")
        )
        self.code_init_indicator_opacity = eval(
            read_property(db_path, table_name, "code_init_indicator_opacity")
        )
        self.code_init_indicator_roughness = eval(
            read_property(db_path, table_name, "code_init_indicator_roughness")
        )
        self.code_init_indicator_resolutions = eval(
            read_property(db_path, table_name, "code_init_indicator_resolutions")
        )
        self.code_init_indicator_Ratio = eval(
            read_property(db_path, table_name, "code_init_indicator_Ratio")
        )
        self.code_init_indicator_cone_highth = eval(
            read_property(db_path, table_name, "code_init_indicator_cone_highth")
        )
        self.code_init_indicator_cone_Radius = eval(
            read_property(db_path, table_name, "code_init_indicator_cone_Radius")
        )
        self.code_init_indicator_cs = eval(
            read_property(db_path, table_name, "code_init_indicator_cs")
        )
        self.code_init_indicator_Cut_X = eval(
            read_property(db_path, table_name, "code_init_indicator_Cut_X")
        )
        self.code_init_indicator_Cut_Y = eval(
            read_property(db_path, table_name, "code_init_indicator_Cut_Y")
        )
        self.code_init_indicator_Cut_Z = eval(
            read_property(db_path, table_name, "code_init_indicator_Cut_Z")
        )
        self.code_init_indicator_fxyzc = eval(
            read_property(db_path, table_name, "code_init_indicator_fxyzc")
        )
        self.frame_number = eval(read_property(db_path, table_name, "frame_number"))
        self.color_map_index = eval(
            read_property(db_path, table_name, "color_map_index")
        )
        self.antialiasing = eval(read_property(db_path, table_name, "antialiasing"))[
            0
        ]  # to extra the str, because we warp the value in a list
        self.x_compoment_filter_min = eval(
            read_property(db_path, table_name, "x_compoment_filter_min")
        )
        self.x_compoment_filter_max = eval(
            read_property(db_path, table_name, "x_compoment_filter_max")
        )
        self.y_compoment_filter_min = eval(
            read_property(db_path, table_name, "y_compoment_filter_min")
        )
        self.y_compoment_filter_max = eval(
            read_property(db_path, table_name, "y_compoment_filter_max")
        )
        self.z_compoment_filter_min = eval(
            read_property(db_path, table_name, "z_compoment_filter_min")
        )
        self.z_compoment_filter_max = eval(
            read_property(db_path, table_name, "z_compoment_filter_max")
        )
        self.a1_plane_slicer = eval(
            read_property(db_path, table_name, "a1_plane_slicer")
        )
        self.a1_clip_plane_x = eval(
            read_property(db_path, table_name, "a1_clip_plane_x")
        )
        self.a1_clip_plane_y = eval(
            read_property(db_path, table_name, "a1_clip_plane_y")
        )
        self.a1_clip_plane_z = eval(
            read_property(db_path, table_name, "a1_clip_plane_z")
        )
        self.a2_plane_slicer = eval(
            read_property(db_path, table_name, "a2_plane_slicer")
        )
        self.a2_clip_plane_x = eval(
            read_property(db_path, table_name, "a2_clip_plane_x")
        )
        self.a2_clip_plane_y = eval(
            read_property(db_path, table_name, "a2_clip_plane_y")
        )
        self.a2_clip_plane_z = eval(
            read_property(db_path, table_name, "a2_clip_plane_z")
        )
        self.b1_plane_slicer = eval(
            read_property(db_path, table_name, "b1_plane_slicer")
        )
        self.b1_clip_plane_x = eval(
            read_property(db_path, table_name, "b1_clip_plane_x")
        )
        self.b1_clip_plane_y = eval(
            read_property(db_path, table_name, "b1_clip_plane_y")
        )
        self.b1_clip_plane_z = eval(
            read_property(db_path, table_name, "b1_clip_plane_z")
        )
        self.b2_plane_slicer = eval(
            read_property(db_path, table_name, "b2_plane_slicer")
        )
        self.b2_clip_plane_x = eval(
            read_property(db_path, table_name, "b2_clip_plane_x")
        )
        self.b2_clip_plane_y = eval(
            read_property(db_path, table_name, "b2_clip_plane_y")
        )
        self.b2_clip_plane_z = eval(
            read_property(db_path, table_name, "b2_clip_plane_z")
        )
        self.c1_plane_slicer = eval(
            read_property(db_path, table_name, "c1_plane_slicer")
        )
        self.c1_clip_plane_x = eval(
            read_property(db_path, table_name, "c1_clip_plane_x")
        )
        self.c1_clip_plane_y = eval(
            read_property(db_path, table_name, "c1_clip_plane_y")
        )
        self.c1_clip_plane_z = eval(
            read_property(db_path, table_name, "c1_clip_plane_z")
        )
        self.c2_plane_slicer = eval(
            read_property(db_path, table_name, "c2_plane_slicer")
        )
        self.c2_clip_plane_x = eval(
            read_property(db_path, table_name, "c2_clip_plane_x")
        )
        self.c2_clip_plane_y = eval(
            read_property(db_path, table_name, "c2_clip_plane_y")
        )
        self.c2_clip_plane_z = eval(
            read_property(db_path, table_name, "c2_clip_plane_z")
        )
        self.resolutions = eval(read_property(db_path, table_name, "resolutions"))
        self.radius_record = eval(read_property(db_path, table_name, "radius_record"))
        self.height_record = eval(read_property(db_path, table_name, "height_record"))
        self.metallic_record = eval(
            read_property(db_path, table_name, "metallic_record")
        )
        self.opacity_record = eval(read_property(db_path, table_name, "opacity_record"))
        self.roughness_record = eval(
            read_property(db_path, table_name, "roughness_record")
        )
        self.Ratio_record = eval(read_property(db_path, table_name, "Ratio_record"))
        self.cmap_record = eval(read_property(db_path, table_name, "cmap_record"))[
            0
        ]  # to extra the str, because we warp the value in a list
        self.cone_highth_record = eval(
            read_property(db_path, table_name, "cone_highth_record")
        )
        self.cone_Radius_record = eval(
            read_property(db_path, table_name, "cone_Radius_record")
        )
        self.cs_record = eval(read_property(db_path, table_name, "cs_record"))
        self.camera_position = eval(
            read_property(db_path, table_name, "camera_position")
        )
        self.camera_focal_point = eval(
            read_property(db_path, table_name, "camera_focal_point")
        )
        self.camera_up = eval(read_property(db_path, table_name, "camera_up"))
        self.camera_zoom = eval(read_property(db_path, table_name, "camera_zoom"))
        try:
            self.pbr = eval(read_property(db_path, table_name, "pbr"))[
                0
            ]  # to extra the str, because we warp the value in a list
        except:
            self.pbr = eval(read_property(db_path, table_name, "pbr"))
        self.Cone_center = eval(read_property(db_path, table_name, "Cone_center"))
        self.Arrow_center = eval(read_property(db_path, table_name, "Arrow_center"))
        try:
            self.add_cone = eval(read_property(db_path, table_name, "add_cone"))[0]
        except:
            self.add_cone = eval(read_property(db_path, table_name, "add_cone"))
        try:
            self.coord_name = eval(read_property(db_path, table_name, "coord_name"))[0]
        except:
            self.coord_name = str(read_property(db_path, table_name, "coord_name"))
        try:
            self.mom_name = eval(read_property(db_path, table_name, "mom_name"))[0]
        except:
            self.mom_name = str(read_property(db_path, table_name, "mom_name"))
        try:
            self.ovf_name = eval(read_property(db_path, table_name, "ovf_name"))[0]
        except:
            self.ovf_name = str(read_property(db_path, table_name, "ovf_name"))

        try:
            self.outputfile_type = eval(
                read_property(db_path, table_name, "outputfile_type")
            )[0]
        except:
            self.outputfile_type = str(
                read_property(db_path, table_name, "outputfile_type")
            )
        try:
            self.bgc = eval(read_property(db_path, table_name, "bgc"))[0]
        except:
            self.bgc = str(read_property(db_path, table_name, "bgc"))
        self.moment_file_indicator = eval(
            read_property(db_path, table_name, "moment_file_indicator")
        )
        self.coord_file_indicator = eval(
            read_property(db_path, table_name, "coord_file_indicator")
        )
        self.ovf_file_indicator = eval(
            read_property(db_path, table_name, "ovf_file_indicator")
        )
        self.bgc_indicator = eval(read_property(db_path, table_name, "bgc_indicator"))
        self.pbr_indicator = eval(read_property(db_path, table_name, "pbr_indicator"))
        try:
            self.add_glyphs = eval(read_property(db_path, table_name, "add_glyphs"))[0]
        except:
            self.add_glyphs = eval(read_property(db_path, table_name, "add_glyphs"))
        try:
            self.add_arrow = eval(read_property(db_path, table_name, "add_arrow"))[0]
        except:
            self.add_arrow = eval(read_property(db_path, table_name, "add_arrow"))
        self.start_arrow = eval(read_property(db_path, table_name, "start_arrow"))
        self.tip_length_arrow = eval(
            read_property(db_path, table_name, "tip_length_arrow")
        )
        self.tip_radius_arrow = eval(
            read_property(db_path, table_name, "tip_radius_arrow")
        )
        self.tip_resolution_arrow = eval(
            read_property(db_path, table_name, "tip_resolution_arrow")
        )
        self.shaft_radius_arrow = eval(
            read_property(db_path, table_name, "shaft_radius_arrow")
        )
        self.shaft_resolution_arrow = eval(
            read_property(db_path, table_name, "shaft_resolution_arrow")
        )
        self.Ratio_record_arrow = eval(
            read_property(db_path, table_name, "Ratio_record_arrow")
        )
        try:
            self.pbr_arrow = eval(read_property(db_path, table_name, "pbr_arrow"))[0]
        except:
            self.pbr_arrow = eval(read_property(db_path, table_name, "pbr_arrow"))
        self.metallic_arrow = eval(read_property(db_path, table_name, "metallic_arrow"))
        self.roughness_arrow = eval(
            read_property(db_path, table_name, "roughness_arrow")
        )
        try:
            self.do_clip_component = eval(
                read_property(db_path, table_name, "do_clip_component")
            )[0]
        except:
            self.do_clip_component = eval(
                read_property(db_path, table_name, "do_clip_component")
            )
        try:
            self.do_clip_plane_fix_origin_and_normal = eval(
                read_property(
                    db_path, table_name, "do_clip_plane_fix_origin_and_normal"
                )
            )[0]
        except:
            self.do_clip_plane_fix_origin_and_normal = eval(
                read_property(
                    db_path, table_name, "do_clip_plane_fix_origin_and_normal"
                )
            )

        try:
            self.do_clip_box = eval(read_property(db_path, table_name, "do_clip_box"))[
                0
            ]
        except:
            self.do_clip_box = eval(read_property(db_path, table_name, "do_clip_box"))
        self.clip_plane_x_min = eval(
            read_property(db_path, table_name, "clip_plane_x_min")
        )
        self.clip_plane_x_max = eval(
            read_property(db_path, table_name, "clip_plane_x_max")
        )
        self.clip_plane_y_min = eval(
            read_property(db_path, table_name, "clip_plane_y_min")
        )
        self.clip_plane_y_max = eval(
            read_property(db_path, table_name, "clip_plane_y_max")
        )
        self.clip_plane_z_min = eval(
            read_property(db_path, table_name, "clip_plane_z_min")
        )
        self.clip_plane_z_max = eval(
            read_property(db_path, table_name, "clip_plane_z_max")
        )
        try:
            self.do_scale_arrow = eval(
                read_property(db_path, table_name, "do_scale_arrow")
            )[0]
        except:
            self.do_scale_arrow = eval(
                read_property(db_path, table_name, "do_scale_arrow")
            )
        try:
            self.do_scale_cone = eval(
                read_property(db_path, table_name, "do_scale_cone")
            )[0]
        except:
            self.do_scale_cone = eval(
                read_property(db_path, table_name, "do_scale_cone")
            )

        try:
            self.do_scale_sphere = eval(
                read_property(db_path, table_name, "do_scale_sphere")
            )[0]
            self.do_scale_plane = eval(
                read_property(db_path, table_name, "do_scale_plane")
            )[0]
            self.do_scale_box = eval(
                read_property(db_path, table_name, "do_scale_box")
            )[0]
            self.do_scale_own = eval(
                read_property(db_path, table_name, "do_scale_own")
            )[0]
            self.show_scalar_bar = eval(
                read_property(db_path, table_name, "show_scalar_bar")
            )[0]
            self.add_sphere = eval(read_property(db_path, table_name, "add_sphere"))[0]
            self.pbr_sphere = eval(read_property(db_path, table_name, "pbr_sphere"))[0]
            self.add_plane = eval(read_property(db_path, table_name, "add_plane"))[0]
            self.pbr_plane = eval(read_property(db_path, table_name, "pbr_plane"))[0]
            self.add_box = eval(read_property(db_path, table_name, "add_box"))[0]
            self.pbr_box = eval(read_property(db_path, table_name, "pbr_box"))[0]
            self.add_own_glyphs = eval(
                read_property(db_path, table_name, "add_own_glyphs")
            )[0]
            self.pbr_own = eval(read_property(db_path, table_name, "pbr_own"))[0]
            self.add_rectangle_mesh = eval(
                read_property(db_path, table_name, "add_rectangle_mesh")
            )[0]
            self.rectangle_mesh_interpolate_before_map = eval(
                read_property(
                    db_path, table_name, "rectangle_mesh_interpolate_before_map"
                )
            )[0]

            self.show_rectangle_mesh_scalar_bar = eval(
                read_property(db_path, table_name, "show_rectangle_mesh_scalar_bar")
            )[0]
            self.add_unstructured_mesh = eval(
                read_property(db_path, table_name, "add_unstructured_mesh")
            )[0]
            self.show_unstructured_mesh_scalar_bar = eval(
                read_property(db_path, table_name, "show_unstructured_mesh_scalar_bar")
            )[0]
            self.unstructured_mesh_interpolate_before_map = eval(
                read_property(
                    db_path, table_name, "unstructured_mesh_interpolate_before_map"
                )
            )[0]
            self.do_glyph_cone_rescale = eval(
                read_property(db_path, table_name, "do_glyph_cone_rescale")
            )[0]
            self.do_glyph_sphere_rescale = eval(
                read_property(db_path, table_name, "do_glyph_sphere_rescale")
            )[0]
            self.do_glyph_plane_rescale = eval(
                read_property(db_path, table_name, "do_glyph_plane_rescale")
            )[0]
            self.do_glyph_box_rescale = eval(
                read_property(db_path, table_name, "do_glyph_box_rescale")
            )[0]
            self.do_glyph_own_rescale = eval(
                read_property(db_path, table_name, "do_glyph_own_rescale")
            )[0]
            self.do_glyph_arrow_rescale = eval(
                read_property(db_path, table_name, "do_glyph_arrow_rescale")
            )[0]
            self.add_projection_plane_1 = eval(
                read_property(db_path, table_name, "add_projection_plane_1")
            )[0]
            self.add_projection_plane_2 = eval(
                read_property(db_path, table_name, "add_projection_plane_2")
            )[0]
            self.add_projection_plane_3 = eval(
                read_property(db_path, table_name, "add_projection_plane_3")
            )[0]
            self.add_projection_plane_4 = eval(
                read_property(db_path, table_name, "add_projection_plane_4")
            )[0]
            self.add_projection_plane_5 = eval(
                read_property(db_path, table_name, "add_projection_plane_5")
            )[0]
            self.add_projection_plane_6 = eval(
                read_property(db_path, table_name, "add_projection_plane_6")
            )[0]
            self.interpolate_plane_1 = eval(
                read_property(db_path, table_name, "interpolate_plane_1")
            )[0]
            self.interpolate_plane_2 = eval(
                read_property(db_path, table_name, "interpolate_plane_2")
            )[0]
            self.interpolate_plane_3 = eval(
                read_property(db_path, table_name, "interpolate_plane_3")
            )[0]
            self.interpolate_plane_4 = eval(
                read_property(db_path, table_name, "interpolate_plane_4")
            )[0]
            self.interpolate_plane_5 = eval(
                read_property(db_path, table_name, "interpolate_plane_5")
            )[0]
            self.interpolate_plane_6 = eval(
                read_property(db_path, table_name, "interpolate_plane_6")
            )[0]
            self.do_rectangle_mesh_contour = eval(
                read_property(db_path, table_name, "do_rectangle_mesh_contour")
            )[0]
            self.do_multi_rectangle_surface_contour = eval(
                read_property(db_path, table_name, "do_multi_rectangle_surface_contour")
            )[0]
            self.do_unstructured_mesh_contour = eval(
                read_property(db_path, table_name, "do_unstructured_mesh_contour")
            )[0]
            self.do_multi_unstructured_surface_contour = eval(
                read_property(
                    db_path, table_name, "do_multi_unstructured_surface_contour"
                )
            )[0]
            self.do_rectangle_mesh_slice_along_axis = eval(
                read_property(db_path, table_name, "do_rectangle_mesh_slice_along_axis")
            )[0]
            self.do_unstructured_mesh_slice_along_axis = eval(
                read_property(
                    db_path, table_name, "do_unstructured_mesh_slice_along_axis"
                )
            )[0]
            self.do_rectangle_mesh_rescale = eval(
                read_property(db_path, table_name, "do_rectangle_mesh_rescale")
            )[0]
            self.do_unstructured_mesh_rescale = eval(
                read_property(db_path, table_name, "do_unstructured_mesh_rescale")
            )[0]
            self.do_rectangle_mesh_clip_scalar = eval(
                read_property(db_path, table_name, "do_rectangle_mesh_clip_scalar")
            )[0]
            self.do_clip_rectangle_mesh_free_normal = eval(
                read_property(db_path, table_name, "do_clip_rectangle_mesh_free_normal")
            )[0]
            self.do_unstructured_mesh_clip_scalar = eval(
                read_property(db_path, table_name, "do_unstructured_mesh_clip_scalar")
            )[0]
            self.do_rectangle_mesh_clip = eval(
                read_property(db_path, table_name, "do_rectangle_mesh_clip")
            )[0]
            self.do_unstructured_mesh_clip = eval(
                read_property(db_path, table_name, "do_unstructured_mesh_clip")
            )[0]
            self.do_clip_unstructured_mesh_free_normal = eval(
                read_property(
                    db_path, table_name, "do_clip_unstructured_mesh_free_normal"
                )
            )[0]
            self.do_rectangle_mesh_slice = eval(
                read_property(db_path, table_name, "do_rectangle_mesh_slice")
            )[0]
            self.rectangle_mesh_slice_contour_option = eval(
                read_property(
                    db_path, table_name, "rectangle_mesh_slice_contour_option"
                )
            )[0]
            self.do_unstructured_mesh_slice = eval(
                read_property(db_path, table_name, "do_unstructured_mesh_slice")
            )[0]
            self.unstructured_mesh_slice_contour_option = eval(
                read_property(
                    db_path, table_name, "unstructured_mesh_slice_contour_option"
                )
            )[0]
            self.do_rectangle_mesh_clip_box = eval(
                read_property(db_path, table_name, "do_rectangle_mesh_clip_box")
            )[0]
            self.invert_rectangle_mesh_clip_box = eval(
                read_property(db_path, table_name, "invert_rectangle_mesh_clip_box")
            )[0]
            self.rectangle_mesh_clip_implicit_or_explict = eval(
                read_property(
                    db_path, table_name, "rectangle_mesh_clip_implicit_or_explict"
                )
            )[0]
            self.do_unstructured_mesh_clip_box = eval(
                read_property(db_path, table_name, "do_unstructured_mesh_clip_box")
            )[0]
            self.invert_unstructured_mesh_clip_box = eval(
                read_property(db_path, table_name, "invert_unstructured_mesh_clip_box")
            )[0]
            self.unstructured_mesh_clip_implicit_or_explict = eval(
                read_property(
                    db_path, table_name, "unstructured_mesh_clip_implicit_or_explict"
                )
            )[0]
            self.do_clip_plane_free_normal = eval(
                read_property(db_path, table_name, "do_clip_plane_free_normal")
            )[0]
            self.pbr_rectangle = eval(
                read_property(db_path, table_name, "pbr_rectangle")
            )[0]
            self.pbr_unstructured = eval(
                read_property(db_path, table_name, "pbr_unstructured")
            )[0]
            self.add_simple_point = eval(
                read_property(db_path, table_name, "add_simple_point")
            )[0]
            self.do_glyph_simple_point_rescale = eval(
                read_property(db_path, table_name, "do_glyph_simple_point_rescale")
            )[0]
            self.local_rendering_sinmple_point_as_spheres = eval(
                read_property(
                    db_path, table_name, "local_rendering_sinmple_point_as_spheres"
                )
            )[0]
            self.mom_name1 = eval(read_property(db_path, table_name, "mom_name1"))[0]
            self.mom_name2 = eval(read_property(db_path, table_name, "mom_name2"))[0]
            self.mom_name3 = eval(read_property(db_path, table_name, "mom_name3"))[0]
            self.do_delaunay = eval(read_property(db_path, table_name, "do_delaunay"))[
                0
            ]
            self.excu_from_other_place = eval(
                read_property(db_path, table_name, "excu_from_other_place")
            )[0]
            self.nothing_show = eval(
                read_property(db_path, table_name, "nothing_show")
            )[0]
            self.frame_change = eval(
                read_property(db_path, table_name, "frame_change")
            )[0]
            self.projection_plane_1_added = eval(
                read_property(db_path, table_name, "projection_plane_1_added")
            )[0]
            self.projection_plane_2_added = eval(
                read_property(db_path, table_name, "projection_plane_2_added")
            )[0]
            self.projection_plane_3_added = eval(
                read_property(db_path, table_name, "projection_plane_3_added")
            )[0]
            self.projection_plane_4_added = eval(
                read_property(db_path, table_name, "projection_plane_4_added")
            )[0]
            self.projection_plane_5_added = eval(
                read_property(db_path, table_name, "projection_plane_5_added")
            )[0]
            self.projection_plane_6_added = eval(
                read_property(db_path, table_name, "projection_plane_6_added")
            )[0]
            self.cone_added_1 = eval(
                read_property(db_path, table_name, "cone_added_1")
            )[0]
            self.cone_added_2 = eval(
                read_property(db_path, table_name, "cone_added_2")
            )[0]
            self.cone_added_3 = eval(
                read_property(db_path, table_name, "cone_added_3")
            )[0]
            self.cone_added_4 = eval(
                read_property(db_path, table_name, "cone_added_4")
            )[0]
            self.arrow_added_1 = eval(
                read_property(db_path, table_name, "arrow_added_1")
            )[0]
            self.arrow_added_2 = eval(
                read_property(db_path, table_name, "arrow_added_2")
            )[0]
            self.arrow_added_3 = eval(
                read_property(db_path, table_name, "arrow_added_3")
            )[0]
            self.arrow_added_4 = eval(
                read_property(db_path, table_name, "arrow_added_4")
            )[0]
            self.sphere_added_1 = eval(
                read_property(db_path, table_name, "sphere_added_1")
            )[0]
            self.sphere_added_2 = eval(
                read_property(db_path, table_name, "sphere_added_2")
            )[0]
            self.sphere_added_3 = eval(
                read_property(db_path, table_name, "sphere_added_3")
            )[0]
            self.sphere_added_4 = eval(
                read_property(db_path, table_name, "sphere_added_4")
            )[0]
            self.box_added_1 = eval(read_property(db_path, table_name, "box_added_1"))[
                0
            ]
            self.box_added_2 = eval(read_property(db_path, table_name, "box_added_2"))[
                0
            ]
            self.box_added_3 = eval(read_property(db_path, table_name, "box_added_3"))[
                0
            ]
            self.box_added_4 = eval(read_property(db_path, table_name, "box_added_4"))[
                0
            ]
            self.own_glyphs_added_1 = eval(
                read_property(db_path, table_name, "own_glyphs_added_1")
            )[0]
            self.own_glyphs_added_2 = eval(
                read_property(db_path, table_name, "own_glyphs_added_2")
            )[0]
            self.own_glyphs_added_3 = eval(
                read_property(db_path, table_name, "own_glyphs_added_3")
            )[0]
            self.own_glyphs_added_4 = eval(
                read_property(db_path, table_name, "own_glyphs_added_4")
            )[0]
            self.plane_added_1 = eval(
                read_property(db_path, table_name, "plane_added_1")
            )[0]
            self.plane_added_2 = eval(
                read_property(db_path, table_name, "plane_added_2")
            )[0]
            self.plane_added_3 = eval(
                read_property(db_path, table_name, "plane_added_3")
            )[0]
            self.plane_added_4 = eval(
                read_property(db_path, table_name, "plane_added_4")
            )[0]
            self.unstructured_mesh_added_1 = eval(
                read_property(db_path, table_name, "unstructured_mesh_added_1")
            )[0]
            self.unstructured_mesh_added_2 = eval(
                read_property(db_path, table_name, "unstructured_mesh_added_2")
            )[0]
            self.unstructured_mesh_added_3 = eval(
                read_property(db_path, table_name, "unstructured_mesh_added_3")
            )[0]
            self.unstructured_mesh_added_4 = eval(
                read_property(db_path, table_name, "unstructured_mesh_added_4")
            )[0]
            self.rectangle_mesh_added_1 = eval(
                read_property(db_path, table_name, "rectangle_mesh_added_1")
            )[0]
            self.rectangle_mesh_added_2 = eval(
                read_property(db_path, table_name, "rectangle_mesh_added_2")
            )[0]
            self.rectangle_mesh_added_3 = eval(
                read_property(db_path, table_name, "rectangle_mesh_added_3")
            )[0]
            self.rectangle_mesh_added_4 = eval(
                read_property(db_path, table_name, "rectangle_mesh_added_4")
            )[0]
            self.simple_point_added_1 = eval(
                read_property(db_path, table_name, "simple_point_added_1")
            )[0]
            self.simple_point_added_2 = eval(
                read_property(db_path, table_name, "simple_point_added_2")
            )[0]
            self.simple_point_added_3 = eval(
                read_property(db_path, table_name, "simple_point_added_3")
            )[0]
            self.simple_point_added_4 = eval(
                read_property(db_path, table_name, "simple_point_added_4")
            )[0]
            self.excu_from_other_place_welcome_image = eval(
                read_property(
                    db_path, table_name, "excu_from_other_place_welcome_image"
                )
            )[0]
            self.nothing_show_welcome_image = eval(
                read_property(db_path, table_name, "nothing_show_welcome_image")
            )[0]
            self.first_time_nothing_show = eval(
                read_property(db_path, table_name, "first_time_nothing_show")
            )[0]
            self.cubemap_exist = eval(
                read_property(db_path, table_name, "cubemap_exist")
            )[0]
            self.welcome_image_not_created = eval(
                read_property(db_path, table_name, "welcome_image_not_created")
            )[0]
            self.add_warpped_sphere_kernel = eval(
                read_property(db_path, table_name, "add_warpped_sphere_kernel")
            )[0]
            self.do_warp_sphere = eval(
                read_property(db_path, table_name, "do_warp_sphere")
            )[0]
            self.swk_added = eval(read_property(db_path, table_name, "swk_added"))[0]
            self.warp_kernel_color_changed = eval(
                read_property(db_path, table_name, "warp_kernel_color_changed")
            )[0]
            self.projection_plane_added_1_1 = eval(
                read_property(db_path, table_name, "projection_plane_added_1_1")
            )[0]
            self.projection_plane_added_1_2 = eval(
                read_property(db_path, table_name, "projection_plane_added_1_2")
            )[0]
            self.projection_plane_added_1_3 = eval(
                read_property(db_path, table_name, "projection_plane_added_1_3")
            )[0]
            self.projection_plane_added_1_4 = eval(
                read_property(db_path, table_name, "projection_plane_added_1_4")
            )[0]
            self.projection_plane_added_2_1 = eval(
                read_property(db_path, table_name, "projection_plane_added_2_1")
            )[0]
            self.projection_plane_added_2_2 = eval(
                read_property(db_path, table_name, "projection_plane_added_2_2")
            )[0]
            self.projection_plane_added_2_3 = eval(
                read_property(db_path, table_name, "projection_plane_added_2_3")
            )[0]
            self.projection_plane_added_2_4 = eval(
                read_property(db_path, table_name, "projection_plane_added_2_4")
            )[0]
            self.projection_plane_added_3_1 = eval(
                read_property(db_path, table_name, "projection_plane_added_3_1")
            )[0]
            self.projection_plane_added_3_2 = eval(
                read_property(db_path, table_name, "projection_plane_added_3_2")
            )[0]
            self.projection_plane_added_3_3 = eval(
                read_property(db_path, table_name, "projection_plane_added_3_3")
            )[0]
            self.projection_plane_added_3_4 = eval(
                read_property(db_path, table_name, "projection_plane_added_3_4")
            )[0]
            self.projection_plane_added_4_1 = eval(
                read_property(db_path, table_name, "projection_plane_added_4_1")
            )[0]
            self.projection_plane_added_4_2 = eval(
                read_property(db_path, table_name, "projection_plane_added_4_2")
            )[0]
            self.projection_plane_added_4_3 = eval(
                read_property(db_path, table_name, "projection_plane_added_4_3")
            )[0]
            self.projection_plane_added_4_4 = eval(
                read_property(db_path, table_name, "projection_plane_added_4_4")
            )[0]
            self.projection_plane_added_5_1 = eval(
                read_property(db_path, table_name, "projection_plane_added_5_1")
            )[0]
            self.projection_plane_added_5_2 = eval(
                read_property(db_path, table_name, "projection_plane_added_5_2")
            )[0]
            self.projection_plane_added_5_3 = eval(
                read_property(db_path, table_name, "projection_plane_added_5_3")
            )[0]
            self.projection_plane_added_5_4 = eval(
                read_property(db_path, table_name, "projection_plane_added_5_4")
            )[0]
            self.projection_plane_added_6_1 = eval(
                read_property(db_path, table_name, "projection_plane_added_6_1")
            )[0]
            self.projection_plane_added_6_2 = eval(
                read_property(db_path, table_name, "projection_plane_added_6_2")
            )[0]
            self.projection_plane_added_6_3 = eval(
                read_property(db_path, table_name, "projection_plane_added_6_3")
            )[0]
            self.projection_plane_added_6_4 = eval(
                read_property(db_path, table_name, "projection_plane_added_6_4")
            )[0]
            self.do_glyph_projection_fft = eval(
                read_property(db_path, table_name, "do_glyph_projection_fft")
            )[0]
            self.do_interpolated_projection = eval(
                read_property(db_path, table_name, "do_interpolated_projection")
            )[0]

        except:
            self.do_scale_sphere = eval(
                read_property(db_path, table_name, "do_scale_sphere")
            )
            self.do_scale_plane = eval(
                read_property(db_path, table_name, "do_scale_plane")
            )
            self.do_scale_box = eval(read_property(db_path, table_name, "do_scale_box"))
            self.do_scale_own = eval(read_property(db_path, table_name, "do_scale_own"))
            self.show_scalar_bar = eval(
                read_property(db_path, table_name, "show_scalar_bar")
            )
            self.add_sphere = eval(read_property(db_path, table_name, "add_sphere"))
            self.pbr_sphere = eval(read_property(db_path, table_name, "pbr_sphere"))
            self.add_plane = eval(read_property(db_path, table_name, "add_plane"))
            self.pbr_plane = eval(read_property(db_path, table_name, "pbr_plane"))
            self.add_box = eval(read_property(db_path, table_name, "add_box"))
            self.pbr_box = eval(read_property(db_path, table_name, "pbr_box"))
            self.add_own_glyphs = eval(
                read_property(db_path, table_name, "add_own_glyphs")
            )
            self.pbr_own = eval(read_property(db_path, table_name, "pbr_own"))
            self.add_rectangle_mesh = eval(
                read_property(db_path, table_name, "add_rectangle_mesh")
            )
            self.rectangle_mesh_interpolate_before_map = eval(
                read_property(
                    db_path, table_name, "rectangle_mesh_interpolate_before_map"
                )
            )

            self.show_rectangle_mesh_scalar_bar = eval(
                read_property(db_path, table_name, "show_rectangle_mesh_scalar_bar")
            )
            self.add_unstructured_mesh = eval(
                read_property(db_path, table_name, "add_unstructured_mesh")
            )
            self.show_unstructured_mesh_scalar_bar = eval(
                read_property(db_path, table_name, "show_unstructured_mesh_scalar_bar")
            )
            self.unstructured_mesh_interpolate_before_map = eval(
                read_property(
                    db_path, table_name, "unstructured_mesh_interpolate_before_map"
                )
            )
            self.do_glyph_cone_rescale = eval(
                read_property(db_path, table_name, "do_glyph_cone_rescale")
            )
            self.do_glyph_sphere_rescale = eval(
                read_property(db_path, table_name, "do_glyph_sphere_rescale")
            )
            self.do_glyph_plane_rescale = eval(
                read_property(db_path, table_name, "do_glyph_plane_rescale")
            )
            self.do_glyph_box_rescale = eval(
                read_property(db_path, table_name, "do_glyph_box_rescale")
            )
            self.do_glyph_own_rescale = eval(
                read_property(db_path, table_name, "do_glyph_own_rescale")
            )
            self.do_glyph_arrow_rescale = eval(
                read_property(db_path, table_name, "do_glyph_arrow_rescale")
            )
            self.add_projection_plane_1 = eval(
                read_property(db_path, table_name, "add_projection_plane_1")
            )
            self.add_projection_plane_2 = eval(
                read_property(db_path, table_name, "add_projection_plane_2")
            )
            self.add_projection_plane_3 = eval(
                read_property(db_path, table_name, "add_projection_plane_3")
            )
            self.add_projection_plane_4 = eval(
                read_property(db_path, table_name, "add_projection_plane_4")
            )
            self.add_projection_plane_5 = eval(
                read_property(db_path, table_name, "add_projection_plane_5")
            )
            self.add_projection_plane_6 = eval(
                read_property(db_path, table_name, "add_projection_plane_6")
            )
            self.interpolate_plane_1 = eval(
                read_property(db_path, table_name, "interpolate_plane_1")
            )
            self.interpolate_plane_2 = eval(
                read_property(db_path, table_name, "interpolate_plane_2")
            )
            self.interpolate_plane_3 = eval(
                read_property(db_path, table_name, "interpolate_plane_3")
            )
            self.interpolate_plane_4 = eval(
                read_property(db_path, table_name, "interpolate_plane_4")
            )
            self.interpolate_plane_5 = eval(
                read_property(db_path, table_name, "interpolate_plane_5")
            )
            self.interpolate_plane_6 = eval(
                read_property(db_path, table_name, "interpolate_plane_6")
            )
            self.do_rectangle_mesh_contour = eval(
                read_property(db_path, table_name, "do_rectangle_mesh_contour")
            )
            self.do_multi_rectangle_surface_contour = eval(
                read_property(db_path, table_name, "do_multi_rectangle_surface_contour")
            )
            self.do_unstructured_mesh_contour = eval(
                read_property(db_path, table_name, "do_unstructured_mesh_contour")
            )
            self.do_multi_unstructured_surface_contour = eval(
                read_property(
                    db_path, table_name, "do_multi_unstructured_surface_contour"
                )
            )
            self.do_rectangle_mesh_slice_along_axis = eval(
                read_property(db_path, table_name, "do_rectangle_mesh_slice_along_axis")
            )
            self.do_unstructured_mesh_slice_along_axis = eval(
                read_property(
                    db_path, table_name, "do_unstructured_mesh_slice_along_axis"
                )
            )
            self.do_rectangle_mesh_rescale = eval(
                read_property(db_path, table_name, "do_rectangle_mesh_rescale")
            )
            self.do_unstructured_mesh_rescale = eval(
                read_property(db_path, table_name, "do_unstructured_mesh_rescale")
            )
            self.do_rectangle_mesh_clip_scalar = eval(
                read_property(db_path, table_name, "do_rectangle_mesh_clip_scalar")
            )
            self.do_clip_rectangle_mesh_free_normal = eval(
                read_property(db_path, table_name, "do_clip_rectangle_mesh_free_normal")
            )
            self.do_unstructured_mesh_clip_scalar = eval(
                read_property(db_path, table_name, "do_unstructured_mesh_clip_scalar")
            )
            self.do_rectangle_mesh_clip = eval(
                read_property(db_path, table_name, "do_rectangle_mesh_clip")
            )
            self.do_unstructured_mesh_clip = eval(
                read_property(db_path, table_name, "do_unstructured_mesh_clip")
            )
            self.do_clip_unstructured_mesh_free_normal = eval(
                read_property(
                    db_path, table_name, "do_clip_unstructured_mesh_free_normal"
                )
            )
            self.do_rectangle_mesh_slice = eval(
                read_property(db_path, table_name, "do_rectangle_mesh_slice")
            )
            self.rectangle_mesh_slice_contour_option = eval(
                read_property(
                    db_path, table_name, "rectangle_mesh_slice_contour_option"
                )
            )
            self.do_unstructured_mesh_slice = eval(
                read_property(db_path, table_name, "do_unstructured_mesh_slice")
            )
            self.unstructured_mesh_slice_contour_option = eval(
                read_property(
                    db_path, table_name, "unstructured_mesh_slice_contour_option"
                )
            )
            self.do_rectangle_mesh_clip_box = eval(
                read_property(db_path, table_name, "do_rectangle_mesh_clip_box")
            )
            self.invert_rectangle_mesh_clip_box = eval(
                read_property(db_path, table_name, "invert_rectangle_mesh_clip_box")
            )
            self.rectangle_mesh_clip_implicit_or_explict = eval(
                read_property(
                    db_path, table_name, "rectangle_mesh_clip_implicit_or_explict"
                )
            )
            self.do_unstructured_mesh_clip_box = eval(
                read_property(db_path, table_name, "do_unstructured_mesh_clip_box")
            )
            self.invert_unstructured_mesh_clip_box = eval(
                read_property(db_path, table_name, "invert_unstructured_mesh_clip_box")
            )
            self.unstructured_mesh_clip_implicit_or_explict = eval(
                read_property(
                    db_path, table_name, "unstructured_mesh_clip_implicit_or_explict"
                )
            )
            self.do_clip_plane_free_normal = eval(
                read_property(db_path, table_name, "do_clip_plane_free_normal")
            )
            self.pbr_rectangle = eval(
                read_property(db_path, table_name, "pbr_rectangle")
            )
            self.pbr_unstructured = eval(
                read_property(db_path, table_name, "pbr_unstructured")
            )
            self.add_simple_point = eval(
                read_property(db_path, table_name, "add_simple_point")
            )
            self.do_glyph_simple_point_rescale = eval(
                read_property(db_path, table_name, "do_glyph_simple_point_rescale")
            )
            self.local_rendering_sinmple_point_as_spheres = eval(
                read_property(
                    db_path, table_name, "local_rendering_sinmple_point_as_spheres"
                )
            )
            self.mom_name1 = str(read_property(db_path, table_name, "mom_name1"))
            self.mom_name2 = str(read_property(db_path, table_name, "mom_name2"))
            self.mom_name3 = str(read_property(db_path, table_name, "mom_name3"))
            self.do_delaunay = eval(read_property(db_path, table_name, "do_delaunay"))
            self.excu_from_other_place = eval(
                read_property(db_path, table_name, "excu_from_other_place")
            )
            self.nothing_show = eval(read_property(db_path, table_name, "nothing_show"))
            self.frame_change = eval(read_property(db_path, table_name, "frame_change"))
            self.projection_plane_1_added = eval(
                read_property(db_path, table_name, "projection_plane_1_added")
            )
            self.projection_plane_2_added = eval(
                read_property(db_path, table_name, "projection_plane_2_added")
            )
            self.projection_plane_3_added = eval(
                read_property(db_path, table_name, "projection_plane_3_added")
            )
            self.projection_plane_4_added = eval(
                read_property(db_path, table_name, "projection_plane_4_added")
            )
            self.projection_plane_5_added = eval(
                read_property(db_path, table_name, "projection_plane_5_added")
            )
            self.projection_plane_6_added = eval(
                read_property(db_path, table_name, "projection_plane_6_added")
            )
            self.cone_added_1 = eval(read_property(db_path, table_name, "cone_added_1"))
            self.cone_added_2 = eval(read_property(db_path, table_name, "cone_added_2"))
            self.cone_added_3 = eval(read_property(db_path, table_name, "cone_added_3"))
            self.cone_added_4 = eval(read_property(db_path, table_name, "cone_added_4"))
            self.arrow_added_1 = eval(
                read_property(db_path, table_name, "arrow_added_1")
            )
            self.arrow_added_2 = eval(
                read_property(db_path, table_name, "arrow_added_2")
            )
            self.arrow_added_3 = eval(
                read_property(db_path, table_name, "arrow_added_3")
            )
            self.arrow_added_4 = eval(
                read_property(db_path, table_name, "arrow_added_4")
            )
            self.sphere_added_1 = eval(
                read_property(db_path, table_name, "sphere_added_1")
            )
            self.sphere_added_2 = eval(
                read_property(db_path, table_name, "sphere_added_2")
            )
            self.sphere_added_3 = eval(
                read_property(db_path, table_name, "sphere_added_3")
            )
            self.sphere_added_4 = eval(
                read_property(db_path, table_name, "sphere_added_4")
            )
            self.box_added_1 = eval(read_property(db_path, table_name, "box_added_1"))
            self.box_added_2 = eval(read_property(db_path, table_name, "box_added_2"))
            self.box_added_3 = eval(read_property(db_path, table_name, "box_added_3"))
            self.box_added_4 = eval(read_property(db_path, table_name, "box_added_4"))
            self.own_glyphs_added_1 = eval(
                read_property(db_path, table_name, "own_glyphs_added_1")
            )
            self.own_glyphs_added_2 = eval(
                read_property(db_path, table_name, "own_glyphs_added_2")
            )
            self.own_glyphs_added_3 = eval(
                read_property(db_path, table_name, "own_glyphs_added_3")
            )
            self.own_glyphs_added_4 = eval(
                read_property(db_path, table_name, "own_glyphs_added_4")
            )
            self.plane_added_1 = eval(
                read_property(db_path, table_name, "plane_added_1")
            )
            self.plane_added_2 = eval(
                read_property(db_path, table_name, "plane_added_2")
            )
            self.plane_added_3 = eval(
                read_property(db_path, table_name, "plane_added_3")
            )
            self.plane_added_4 = eval(
                read_property(db_path, table_name, "plane_added_4")
            )
            self.unstructured_mesh_added_1 = eval(
                read_property(db_path, table_name, "unstructured_mesh_added_1")
            )
            self.unstructured_mesh_added_2 = eval(
                read_property(db_path, table_name, "unstructured_mesh_added_2")
            )
            self.unstructured_mesh_added_3 = eval(
                read_property(db_path, table_name, "unstructured_mesh_added_3")
            )
            self.unstructured_mesh_added_4 = eval(
                read_property(db_path, table_name, "unstructured_mesh_added_4")
            )
            self.rectangle_mesh_added_1 = eval(
                read_property(db_path, table_name, "rectangle_mesh_added_1")
            )
            self.rectangle_mesh_added_2 = eval(
                read_property(db_path, table_name, "rectangle_mesh_added_2")
            )
            self.rectangle_mesh_added_3 = eval(
                read_property(db_path, table_name, "rectangle_mesh_added_3")
            )
            self.rectangle_mesh_added_4 = eval(
                read_property(db_path, table_name, "rectangle_mesh_added_4")
            )
            self.simple_point_added_1 = eval(
                read_property(db_path, table_name, "simple_point_added_1")
            )
            self.simple_point_added_2 = eval(
                read_property(db_path, table_name, "simple_point_added_2")
            )
            self.simple_point_added_3 = eval(
                read_property(db_path, table_name, "simple_point_added_3")
            )
            self.simple_point_added_4 = eval(
                read_property(db_path, table_name, "simple_point_added_4")
            )
            self.excu_from_other_place_welcome_image = eval(
                read_property(
                    db_path, table_name, "excu_from_other_place_welcome_image"
                )
            )
            self.nothing_show_welcome_image = eval(
                read_property(db_path, table_name, "nothing_show_welcome_image")
            )
            self.first_time_nothing_show = eval(
                read_property(db_path, table_name, "first_time_nothing_show")
            )
            self.cubemap_exist = eval(
                read_property(db_path, table_name, "cubemap_exist")
            )
            self.welcome_image_not_created = eval(
                read_property(db_path, table_name, "welcome_image_not_created")
            )
            self.add_warpped_sphere_kernel = eval(
                read_property(db_path, table_name, "add_warpped_sphere_kernel")
            )
            self.do_warp_sphere = eval(
                read_property(db_path, table_name, "do_warp_sphere")
            )
            self.swk_added = eval(read_property(db_path, table_name, "swk_added"))
            self.warp_kernel_color_changed = eval(
                read_property(db_path, table_name, "warp_kernel_color_changed")
            )
            self.projection_plane_added_1_1 = eval(
                read_property(db_path, table_name, "projection_plane_added_1_1")
            )
            self.projection_plane_added_1_2 = eval(
                read_property(db_path, table_name, "projection_plane_added_1_2")
            )
            self.projection_plane_added_1_3 = eval(
                read_property(db_path, table_name, "projection_plane_added_1_3")
            )
            self.projection_plane_added_1_4 = eval(
                read_property(db_path, table_name, "projection_plane_added_1_4")
            )
            self.projection_plane_added_2_1 = eval(
                read_property(db_path, table_name, "projection_plane_added_2_1")
            )
            self.projection_plane_added_2_2 = eval(
                read_property(db_path, table_name, "projection_plane_added_2_2")
            )
            self.projection_plane_added_2_3 = eval(
                read_property(db_path, table_name, "projection_plane_added_2_3")
            )
            self.projection_plane_added_2_4 = eval(
                read_property(db_path, table_name, "projection_plane_added_2_4")
            )
            self.projection_plane_added_3_1 = eval(
                read_property(db_path, table_name, "projection_plane_added_3_1")
            )
            self.projection_plane_added_3_2 = eval(
                read_property(db_path, table_name, "projection_plane_added_3_2")
            )
            self.projection_plane_added_3_3 = eval(
                read_property(db_path, table_name, "projection_plane_added_3_3")
            )
            self.projection_plane_added_3_4 = eval(
                read_property(db_path, table_name, "projection_plane_added_3_4")
            )
            self.projection_plane_added_4_1 = eval(
                read_property(db_path, table_name, "projection_plane_added_4_1")
            )
            self.projection_plane_added_4_2 = eval(
                read_property(db_path, table_name, "projection_plane_added_4_2")
            )
            self.projection_plane_added_4_3 = eval(
                read_property(db_path, table_name, "projection_plane_added_4_3")
            )
            self.projection_plane_added_4_4 = eval(
                read_property(db_path, table_name, "projection_plane_added_4_4")
            )
            self.projection_plane_added_5_1 = eval(
                read_property(db_path, table_name, "projection_plane_added_5_1")
            )
            self.projection_plane_added_5_2 = eval(
                read_property(db_path, table_name, "projection_plane_added_5_2")
            )
            self.projection_plane_added_5_3 = eval(
                read_property(db_path, table_name, "projection_plane_added_5_3")
            )
            self.projection_plane_added_5_4 = eval(
                read_property(db_path, table_name, "projection_plane_added_5_4")
            )
            self.projection_plane_added_6_1 = eval(
                read_property(db_path, table_name, "projection_plane_added_6_1")
            )
            self.projection_plane_added_6_2 = eval(
                read_property(db_path, table_name, "projection_plane_added_6_2")
            )
            self.projection_plane_added_6_3 = eval(
                read_property(db_path, table_name, "projection_plane_added_6_3")
            )
            self.projection_plane_added_6_4 = eval(
                read_property(db_path, table_name, "projection_plane_added_6_4")
            )
            self.do_glyph_projection_fft = eval(
                read_property(db_path, table_name, "do_glyph_projection_fft")
            )
            self.do_interpolated_projection = eval(
                read_property(db_path, table_name, "do_interpolated_projection")
            )

        self.opacity_index = eval(read_property(db_path, table_name, "opacity_index"))

        self.radius_sphere = eval(read_property(db_path, table_name, "radius_sphere"))
        self.center_sphere = eval(read_property(db_path, table_name, "center_sphere"))
        self.theta_resolution_sphere = eval(
            read_property(db_path, table_name, "theta_resolution_sphere")
        )
        self.phi_resolution_sphere = eval(
            read_property(db_path, table_name, "phi_resolution_sphere")
        )
        self.Ratio_record_sphere = eval(
            read_property(db_path, table_name, "Ratio_record_sphere")
        )

        self.metallic_sphere = eval(
            read_property(db_path, table_name, "metallic_sphere")
        )
        self.roughness_sphere = eval(
            read_property(db_path, table_name, "roughness_sphere")
        )

        self.center_plane = eval(read_property(db_path, table_name, "center_plane"))

        self.metallic_plane = eval(read_property(db_path, table_name, "metallic_plane"))
        self.roughness_plane = eval(
            read_property(db_path, table_name, "roughness_plane")
        )
        self.Ratio_record_plane = eval(
            read_property(db_path, table_name, "Ratio_record_plane")
        )

        self.bounds_box = eval(read_property(db_path, table_name, "bounds_box"))
        self.Ratio_record_box = eval(
            read_property(db_path, table_name, "Ratio_record_box")
        )

        self.metallic_box = eval(read_property(db_path, table_name, "metallic_box"))
        self.roughness_box = eval(read_property(db_path, table_name, "roughness_box"))

        self.Ratio_record_own = eval(
            read_property(db_path, table_name, "Ratio_record_own")
        )

        self.metallic_own = eval(read_property(db_path, table_name, "metallic_own"))
        self.roughness_own = eval(read_property(db_path, table_name, "roughness_own"))

        self.system_size = eval(read_property(db_path, table_name, "system_size"))
        self.rectrangle_color_index = eval(
            read_property(db_path, table_name, "rectrangle_color_index")
        )
        self.rectrangle_spacing = eval(
            read_property(db_path, table_name, "rectrangle_spacing")
        )
        self.rectrangle_opacity_index = eval(
            read_property(db_path, table_name, "rectrangle_opacity_index")
        )

        self.unstructured_mesh_color_map_index = eval(
            read_property(db_path, table_name, "unstructured_mesh_color_map_index")
        )
        self.unstructured_mesh_color_map_opacity_index = eval(
            read_property(
                db_path, table_name, "unstructured_mesh_color_map_opacity_index"
            )
        )

        self.phi_compoment_filter_max = eval(
            read_property(db_path, table_name, "phi_compoment_filter_max")
        )
        self.phi_compoment_filter_min = eval(
            read_property(db_path, table_name, "phi_compoment_filter_min")
        )
        self.theta_compoment_filter_max = eval(
            read_property(db_path, table_name, "theta_compoment_filter_max")
        )
        self.theta_compoment_filter_min = eval(
            read_property(db_path, table_name, "theta_compoment_filter_min")
        )

        self.rescale_cone_factor = eval(
            read_property(db_path, table_name, "rescale_cone_factor")
        )
        self.rescale_sphere_factor = eval(
            read_property(db_path, table_name, "rescale_sphere_factor")
        )
        self.rescale_plane_factor = eval(
            read_property(db_path, table_name, "rescale_plane_factor")
        )
        self.rescale_box_factor = eval(
            read_property(db_path, table_name, "rescale_box_factor")
        )
        self.rescale_own_factor = eval(
            read_property(db_path, table_name, "rescale_own_factor")
        )
        self.rescale_arrow_factor = eval(
            read_property(db_path, table_name, "rescale_arrow_factor")
        )
        self.rescale_arrow_index = eval(
            read_property(db_path, table_name, "rescale_arrow_index")
        )
        self.rescale_cone_index = eval(
            read_property(db_path, table_name, "rescale_cone_index")
        )
        self.rescale_sphere_index = eval(
            read_property(db_path, table_name, "rescale_sphere_index")
        )
        self.rescale_plane_index = eval(
            read_property(db_path, table_name, "rescale_plane_index")
        )
        self.rescale_box_index = eval(
            read_property(db_path, table_name, "rescale_box_index")
        )
        self.rescale_own_index = eval(
            read_property(db_path, table_name, "rescale_own_index")
        )
        self.rescale_arrow_norm = eval(
            read_property(db_path, table_name, "rescale_arrow_norm")
        )
        self.rescale_cone_norm = eval(
            read_property(db_path, table_name, "rescale_cone_norm")
        )
        self.rescale_sphere_norm = eval(
            read_property(db_path, table_name, "rescale_sphere_norm")
        )
        self.rescale_plane_norm = eval(
            read_property(db_path, table_name, "rescale_plane_norm")
        )
        self.rescale_box_norm = eval(
            read_property(db_path, table_name, "rescale_box_norm")
        )
        self.rescale_own_norm = eval(
            read_property(db_path, table_name, "rescale_own_norm")
        )

        self.rectangle_mesh_contour_isosurface_number = eval(
            read_property(
                db_path, table_name, "rectangle_mesh_contour_isosurface_number"
            )
        )
        self.rectangle_mesh_contour_isosurface_value = eval(
            read_property(
                db_path, table_name, "rectangle_mesh_contour_isosurface_value"
            )
        )
        self.rectangle_mesh_contour_method_indicator = eval(
            read_property(
                db_path, table_name, "rectangle_mesh_contour_method_indicator"
            )
        )

        self.unstructured_mesh_contour_isosurface_value = eval(
            read_property(
                db_path, table_name, "unstructured_mesh_contour_isosurface_value"
            )
        )
        self.unstructured_mesh_contour_isosurface_number = eval(
            read_property(
                db_path, table_name, "unstructured_mesh_contour_isosurface_number"
            )
        )
        self.unstructured_mesh_contour_method_indicator = eval(
            read_property(
                db_path, table_name, "unstructured_mesh_contour_method_indicator"
            )
        )
        self.rectangle_number_of_slice_along_axis = eval(
            read_property(db_path, table_name, "rectangle_number_of_slice_along_axis")
        )
        self.rectangle_axis_of_slice_along_axis = eval(
            read_property(db_path, table_name, "rectangle_axis_of_slice_along_axis")
        )
        self.unstructured_number_of_slice_along_axis = eval(
            read_property(
                db_path, table_name, "unstructured_number_of_slice_along_axis"
            )
        )
        self.unstructured_axis_of_slice_along_axis = eval(
            read_property(db_path, table_name, "unstructured_axis_of_slice_along_axis")
        )
        self.rescale_rectangle_mesh_factor = eval(
            read_property(db_path, table_name, "rescale_rectangle_mesh_factor")
        )
        self.rescale_rectangle_mesh_norm = eval(
            read_property(db_path, table_name, "rescale_rectangle_mesh_norm")
        )
        self.rescale_unstructured_mesh_factor = eval(
            read_property(db_path, table_name, "rescale_unstructured_mesh_factor")
        )
        self.rescale_unstructured_mesh_norm = eval(
            read_property(db_path, table_name, "rescale_unstructured_mesh_norm")
        )
        self.rectangle_mesh_clip_scalar_max_xyz = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_scalar_max_xyz")
        )
        self.rectangle_mesh_clip_scalar_min_xyz = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_scalar_min_xyz")
        )
        self.rectangle_mesh_clip_scalar_max_theta = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_scalar_max_theta")
        )
        self.rectangle_mesh_clip_scalar_min_theta = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_scalar_min_theta")
        )
        self.rectangle_mesh_clip_scalar_max_phi = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_scalar_max_phi")
        )
        self.rectangle_mesh_clip_scalar_min_phi = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_scalar_min_phi")
        )
        self.unstructured_mesh_clip_scalar_max_xyz = eval(
            read_property(db_path, table_name, "unstructured_mesh_clip_scalar_max_xyz")
        )
        self.unstructured_mesh_clip_scalar_min_xyz = eval(
            read_property(db_path, table_name, "unstructured_mesh_clip_scalar_min_xyz")
        )
        self.unstructured_mesh_clip_scalar_max_theta = eval(
            read_property(
                db_path, table_name, "unstructured_mesh_clip_scalar_max_theta"
            )
        )
        self.unstructured_mesh_clip_scalar_min_theta = eval(
            read_property(
                db_path, table_name, "unstructured_mesh_clip_scalar_min_theta"
            )
        )
        self.unstructured_mesh_clip_scalar_max_phi = eval(
            read_property(db_path, table_name, "unstructured_mesh_clip_scalar_max_phi")
        )
        self.unstructured_mesh_clip_scalar_min_phi = eval(
            read_property(db_path, table_name, "unstructured_mesh_clip_scalar_min_phi")
        )
        self.dataset_clip_plane_free_normal_1 = eval(
            read_property(db_path, table_name, "dataset_clip_plane_free_normal_1")
        )
        self.dataset_clip_plane_free_normal_2 = eval(
            read_property(db_path, table_name, "dataset_clip_plane_free_normal_2")
        )
        self.clip_plane_free_1 = eval(
            read_property(db_path, table_name, "clip_plane_free_1")
        )
        self.clip_plane_free_2 = eval(
            read_property(db_path, table_name, "clip_plane_free_2")
        )
        self.rectangle_mesh_clip_plane_x_min = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_plane_x_min")
        )
        self.rectangle_mesh_clip_plane_x_max = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_plane_x_max")
        )
        self.rectangle_mesh_clip_plane_y_min = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_plane_y_min")
        )
        self.rectangle_mesh_clip_plane_y_max = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_plane_y_max")
        )
        self.rectangle_mesh_clip_plane_z_min = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_plane_z_min")
        )
        self.rectangle_mesh_clip_plane_z_max = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_plane_z_max")
        )
        self.rectangle_mesh_clip_plane_free_normal_1 = eval(
            read_property(
                db_path, table_name, "rectangle_mesh_clip_plane_free_normal_1"
            )
        )
        self.rectangle_mesh_clip_plane_free_normal_2 = eval(
            read_property(
                db_path, table_name, "rectangle_mesh_clip_plane_free_normal_2"
            )
        )
        self.clip_rectangle_mesh_free_1 = eval(
            read_property(db_path, table_name, "clip_rectangle_mesh_free_1")
        )
        self.clip_rectangle_mesh_free_2 = eval(
            read_property(db_path, table_name, "clip_rectangle_mesh_free_2")
        )
        self.unstructured_mesh_clip_plane_x_min = eval(
            read_property(db_path, table_name, "unstructured_mesh_clip_plane_x_min")
        )
        self.unstructured_mesh_clip_plane_x_max = eval(
            read_property(db_path, table_name, "unstructured_mesh_clip_plane_x_max")
        )
        self.unstructured_mesh_clip_plane_y_min = eval(
            read_property(db_path, table_name, "unstructured_mesh_clip_plane_y_min")
        )
        self.unstructured_mesh_clip_plane_y_max = eval(
            read_property(db_path, table_name, "unstructured_mesh_clip_plane_y_max")
        )
        self.unstructured_mesh_clip_plane_z_min = eval(
            read_property(db_path, table_name, "unstructured_mesh_clip_plane_z_min")
        )
        self.unstructured_mesh_clip_plane_z_max = eval(
            read_property(db_path, table_name, "unstructured_mesh_clip_plane_z_max")
        )
        self.unstructured_mesh_clip_plane_free_normal_1 = eval(
            read_property(
                db_path, table_name, "unstructured_mesh_clip_plane_free_normal_1"
            )
        )
        self.unstructured_mesh_clip_plane_free_normal_2 = eval(
            read_property(
                db_path, table_name, "unstructured_mesh_clip_plane_free_normal_2"
            )
        )

        self.clip_unstructured_mesh_free_1 = eval(
            read_property(db_path, table_name, "clip_unstructured_mesh_free_1")
        )
        self.clip_unstructured_mesh_free_2 = eval(
            read_property(db_path, table_name, "clip_unstructured_mesh_free_2")
        )

        self.rectangle_mesh_slice_origin = eval(
            read_property(db_path, table_name, "rectangle_mesh_slice_origin")
        )
        self.rectangle_mesh_slice_normal = eval(
            read_property(db_path, table_name, "rectangle_mesh_slice_normal")
        )

        self.unstructured_mesh_slice_origin = eval(
            read_property(db_path, table_name, "unstructured_mesh_slice_origin")
        )
        self.unstructured_mesh_slice_normal = eval(
            read_property(db_path, table_name, "unstructured_mesh_slice_normal")
        )
        self.rectangle_mesh_clip_box_x_min = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_box_x_min")
        )
        self.rectangle_mesh_clip_box_x_max = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_box_x_max")
        )
        self.rectangle_mesh_clip_box_y_min = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_box_y_min")
        )
        self.rectangle_mesh_clip_box_y_max = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_box_y_max")
        )
        self.rectangle_mesh_clip_box_z_min = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_box_z_min")
        )
        self.rectangle_mesh_clip_box_z_max = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_box_z_max")
        )

        self.rectangle_mesh_clip_box_factor = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_box_factor")
        )
        self.unstructured_mesh_clip_box_x_min = eval(
            read_property(db_path, table_name, "unstructured_mesh_clip_box_x_min")
        )
        self.unstructured_mesh_clip_box_x_max = eval(
            read_property(db_path, table_name, "unstructured_mesh_clip_box_x_max")
        )
        self.unstructured_mesh_clip_box_y_min = eval(
            read_property(db_path, table_name, "unstructured_mesh_clip_box_y_min")
        )
        self.unstructured_mesh_clip_box_y_max = eval(
            read_property(db_path, table_name, "unstructured_mesh_clip_box_y_max")
        )
        self.unstructured_mesh_clip_box_z_min = eval(
            read_property(db_path, table_name, "unstructured_mesh_clip_box_z_min")
        )
        self.unstructured_mesh_clip_box_z_max = eval(
            read_property(db_path, table_name, "unstructured_mesh_clip_box_z_max")
        )

        self.unstructured_mesh_clip_box_factor = eval(
            read_property(db_path, table_name, "unstructured_mesh_clip_box_factor")
        )

        self.rescale_simple_point_index = eval(
            read_property(db_path, table_name, "rescale_simple_point_index")
        )
        self.simple_point_size = eval(
            read_property(db_path, table_name, "simple_point_size")
        )
        self.rescale_simple_point_factor = eval(
            read_property(db_path, table_name, "rescale_simple_point_factor")
        )
        self.rescale_simple_point_norm = eval(
            read_property(db_path, table_name, "rescale_simple_point_norm")
        )

        self.antialiasing_indicator = eval(
            read_property(db_path, table_name, "antialiasing_indicator")
        )
        self.download_screenshot_resolution = eval(
            read_property(db_path, table_name, "download_screenshot_resolution")
        )
        self.download_screenshot_indicator = eval(
            read_property(db_path, table_name, "download_screenshot_indicator")
        )
        self.activate_glyphs_indicator = eval(
            read_property(db_path, table_name, "activate_glyphs_indicator")
        )
        self.activate_rectangle_mesh_indicator = eval(
            read_property(db_path, table_name, "activate_rectangle_mesh_indicator")
        )
        self.activate_unstructured_mesh_indicator = eval(
            read_property(db_path, table_name, "activate_unstructured_mesh_indicator")
        )

        self.tmesh_op_indicator = eval(
            read_property(db_path, table_name, "tmesh_op_indicator")
        )

        self.rectangle_mesh_contour_isosurface_value_x = eval(
            read_property(
                db_path, table_name, "rectangle_mesh_contour_isosurface_value_x"
            )
        )
        self.rectangle_mesh_contour_isosurface_value_y = eval(
            read_property(
                db_path, table_name, "rectangle_mesh_contour_isosurface_value_y"
            )
        )
        self.rectangle_mesh_contour_isosurface_value_z = eval(
            read_property(
                db_path, table_name, "rectangle_mesh_contour_isosurface_value_z"
            )
        )

        self.activate_cone_indicator = eval(
            read_property(db_path, table_name, "activate_cone_indicator")
        )
        self.activate_arrow_indicator = eval(
            read_property(db_path, table_name, "activate_arrow_indicator")
        )
        self.activate_sphere_indicator = eval(
            read_property(db_path, table_name, "activate_sphere_indicator")
        )
        self.activate_box_indicator = eval(
            read_property(db_path, table_name, "activate_box_indicator")
        )
        self.activate_own_glyphs_indicator = eval(
            read_property(db_path, table_name, "activate_own_glyphs_indicator")
        )
        self.activate_plane_indicator = eval(
            read_property(db_path, table_name, "activate_plane_indicator")
        )
        self.sub_frame_number = eval(
            read_property(db_path, table_name, "sub_frame_number")
        )
        self.scalar_bar_indicator = eval(
            read_property(db_path, table_name, "scalar_bar_indicator")
        )
        self.moive_size_x = eval(read_property(db_path, table_name, "moive_size_x"))
        self.moive_size_y = eval(read_property(db_path, table_name, "moive_size_y"))
        self.cone_cmap_index_indicator = eval(
            read_property(db_path, table_name, "cone_cmap_index_indicator")
        )
        self.glyph_cmap_vbtn = eval(
            read_property(db_path, table_name, "glyph_cmap_vbtn")
        )
        self.glyph_opaciy_vbtn = eval(
            read_property(db_path, table_name, "glyph_opaciy_vbtn")
        )
        self.do_clip_component_indicator = eval(
            read_property(db_path, table_name, "do_clip_component_indicator")
        )
        self.activate_point_indicator = eval(
            read_property(db_path, table_name, "activate_point_indicator")
        )
        self.point_rescale_indicator = eval(
            read_property(db_path, table_name, "point_rescale_indicator")
        )
        self.point_size_indicator = eval(
            read_property(db_path, table_name, "point_size_indicator")
        )
        self.point_rescale_factor_indicator = eval(
            read_property(db_path, table_name, "point_rescale_factor_indicator")
        )
        self.warp_sphere_radius = eval(
            read_property(db_path, table_name, "warp_sphere_radius")
        )
        self.warpped_sphere_kernel = eval(
            read_property(db_path, table_name, "warpped_sphere_kernel")
        )
        self.warp_kernel_color = eval(
            read_property(db_path, table_name, "warp_kernel_color")
        )
        self.swk_c_indicator = eval(
            read_property(db_path, table_name, "swk_c_indicator")
        )
        self.warp_sphere_radius_indicator = eval(
            read_property(db_path, table_name, "warp_sphere_radius_indicator")
        )
        self.skw_ratio_indicator = eval(
            read_property(db_path, table_name, "skw_ratio_indicator")
        )
        self.start_desoning_filter_index = eval(
            read_property(db_path, table_name, "start_desoning_filter_index")
        )
        self.low_pass_filter_order = eval(
            read_property(db_path, table_name, "low_pass_filter_order")
        )
        self.low_pass_normalized_freq = eval(
            read_property(db_path, table_name, "low_pass_normalized_freq")
        )
        self.fft_rec_windows_X = eval(
            read_property(db_path, table_name, "fft_rec_windows_X")
        )
        self.fft_rec_windows_Y = eval(
            read_property(db_path, table_name, "fft_rec_windows_Y")
        )
        self.fft_rec_windows_Z = eval(
            read_property(db_path, table_name, "fft_rec_windows_Z")
        )

        self.do_glyph_projection_fft_indicator = eval(
            read_property(db_path, table_name, "do_glyph_projection_fft_indicator")
        )
        self.cut_phi_indicator = eval(
            read_property(db_path, table_name, "cut_phi_indicator")
        )
        self.cut_theta_indicator = eval(
            read_property(db_path, table_name, "cut_theta_indicator")
        )
        self.rectangle_cmap_vbtn = eval(
            read_property(db_path, table_name, "rectangle_cmap_vbtn")
        )
        self.rectangle_opaciy_vbtn = eval(
            read_property(db_path, table_name, "rectangle_opaciy_vbtn")
        )
        self.Tmesh_cmap_vbtn = eval(
            read_property(db_path, table_name, "Tmesh_cmap_vbtn")
        )
        self.Tmesh_opaciy_vbtn = eval(
            read_property(db_path, table_name, "Tmesh_opaciy_vbtn")
        )
        self.rectangle_mesh_contour_isosurface_value_t = eval(
            read_property(
                db_path, table_name, "rectangle_mesh_contour_isosurface_value_t"
            )
        )
        self.rectangle_mesh_contour_isosurface_value_p = eval(
            read_property(
                db_path, table_name, "rectangle_mesh_contour_isosurface_value_p"
            )
        )
        self.unstructured_mesh_contour_isosurface_value_t = eval(
            read_property(
                db_path, table_name, "unstructured_mesh_contour_isosurface_value_t"
            )
        )
        self.unstructured_mesh_contour_isosurface_value_p = eval(
            read_property(
                db_path, table_name, "unstructured_mesh_contour_isosurface_value_p"
            )
        )
        self.opacity_record_tmesh = eval(
            read_property(db_path, table_name, "opacity_record_tmesh")
        )
        self.opacity_record_rectangle_mesh = eval(
            read_property(db_path, table_name, "opacity_record_rectangle_mesh")
        )
        self.change_mom1 = eval(read_property(db_path, table_name, "change_mom1"))
        self.change_mom2 = eval(read_property(db_path, table_name, "change_mom2"))
        self.change_mom3 = eval(read_property(db_path, table_name, "change_mom3"))
        self.change_mom4 = eval(read_property(db_path, table_name, "change_mom4"))
        self.rec_mesh_color_scalar = eval(
            read_property(db_path, table_name, "rec_mesh_color_scalar")
        )
        self.rectangle_mesh_clip_scalar_max_x = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_scalar_max_x")
        )
        self.rectangle_mesh_clip_scalar_min_x = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_scalar_min_x")
        )
        self.rectangle_mesh_clip_scalar_max_y = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_scalar_max_y")
        )
        self.rectangle_mesh_clip_scalar_min_y = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_scalar_min_y")
        )
        self.rectangle_mesh_clip_scalar_max_z = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_scalar_max_z")
        )
        self.rectangle_mesh_clip_scalar_min_z = eval(
            read_property(db_path, table_name, "rectangle_mesh_clip_scalar_min_z")
        )
        self.roughness_rmesh = eval(
            read_property(db_path, table_name, "roughness_rmesh")
        )
        self.metallic_rmesh = eval(read_property(db_path, table_name, "metallic_rmesh"))
        self.metallic_tmesh = eval(read_property(db_path, table_name, "metallic_tmesh"))
        self.roughness_tmesh = eval(
            read_property(db_path, table_name, "roughness_tmesh")
        )
        self.pyvista_backend_interactive_ratio = eval(
            read_property(db_path, table_name, "pyvista_backend_interactive_ratio")
        )
        self.pyvista_backend_still_ratio = eval(
            read_property(db_path, table_name, "pyvista_backend_still_ratio")
        )
        self.t_mesh_contour_isosurface_value_x = eval(
            read_property(db_path, table_name, "t_mesh_contour_isosurface_value_x")
        )
        self.t_mesh_contour_isosurface_value_y = eval(
            read_property(db_path, table_name, "t_mesh_contour_isosurface_value_y")
        )
        self.t_mesh_contour_isosurface_value_z = eval(
            read_property(db_path, table_name, "t_mesh_contour_isosurface_value_z")
        )
        self.t_mesh_clip_scalar_max_x = eval(
            read_property(db_path, table_name, "t_mesh_clip_scalar_max_x")
        )
        self.t_mesh_clip_scalar_min_x = eval(
            read_property(db_path, table_name, "t_mesh_clip_scalar_min_x")
        )
        self.t_mesh_clip_scalar_max_y = eval(
            read_property(db_path, table_name, "t_mesh_clip_scalar_max_y")
        )
        self.t_mesh_clip_scalar_min_y = eval(
            read_property(db_path, table_name, "t_mesh_clip_scalar_min_y")
        )
        self.t_mesh_clip_scalar_max_z = eval(
            read_property(db_path, table_name, "t_mesh_clip_scalar_max_z")
        )
        self.t_mesh_clip_scalar_min_z = eval(
            read_property(db_path, table_name, "t_mesh_clip_scalar_min_z")
        )

    def store_profile(self, table_name_store, db_path):
        try:
            delete_table(db_path, table_name=table_name_store)
        except:
            # print(
            #     'No table named "{}" in database "{}"'.format(table_name_store, db_path)
            # )
            pass
        creat_new_table(db_path, table_name=table_name_store)
        name_list = [
            "table_name",
            "code_init_indicator_cmap",
            "code_init_indicator_frame",
            "code_init_indicator_metallic",
            "code_init_indicator_opacity",
            "code_init_indicator_roughness",
            "code_init_indicator_resolutions",
            "code_init_indicator_Ratio",
            "code_init_indicator_cone_highth",
            "code_init_indicator_cone_Radius",
            "code_init_indicator_cs",
            "code_init_indicator_Cut_X",
            "code_init_indicator_Cut_Y",
            "code_init_indicator_Cut_Z",
            "code_init_indicator_fxyzc",
            "frame_number",
            "color_map_index",
            "antialiasing",
            "x_compoment_filter_min",
            "x_compoment_filter_max",
            "y_compoment_filter_min",
            "y_compoment_filter_max",
            "z_compoment_filter_min",
            "z_compoment_filter_max",
            "a1_plane_slicer",
            "a1_clip_plane_x",
            "a1_clip_plane_y",
            "a1_clip_plane_z",
            "a2_plane_slicer",
            "a2_clip_plane_x",
            "a2_clip_plane_y",
            "a2_clip_plane_z",
            "b1_plane_slicer",
            "b1_clip_plane_x",
            "b1_clip_plane_y",
            "b1_clip_plane_z",
            "b2_plane_slicer",
            "b2_clip_plane_x",
            "b2_clip_plane_y",
            "b2_clip_plane_z",
            "c1_plane_slicer",
            "c1_clip_plane_x",
            "c1_clip_plane_y",
            "c1_clip_plane_z",
            "c2_plane_slicer",
            "c2_clip_plane_x",
            "c2_clip_plane_y",
            "c2_clip_plane_z",
            "resolutions",
            "radius_record",
            "height_record",
            "metallic_record",
            "opacity_record",
            "roughness_record",
            "Ratio_record",
            "cmap_record",
            "cone_highth_record",
            "cone_Radius_record",
            "cs_record",
            "camera_position",
            "camera_focal_point",
            "camera_up",
            "camera_zoom",
            "pbr",
            "Cone_center",
            "Arrow_center",
            "add_cone",
            "coord_name",
            "mom_name",
            "ovf_name",
            "outputfile_type",
            "bgc",
            "moment_file_indicator",
            "coord_file_indicator",
            "ovf_file_indicator",
            "bgc_indicator",
            "pbr_indicator",
            "add_glyphs",
            "add_arrow",
            "start_arrow",
            "tip_length_arrow",
            "tip_radius_arrow",
            "tip_resolution_arrow",
            "shaft_radius_arrow",
            "shaft_resolution_arrow",
            "Ratio_record_arrow",
            "pbr_arrow",
            "metallic_arrow",
            "roughness_arrow",
            "do_clip_component",
            "do_clip_plane_fix_origin_and_normal",
            "do_clip_box",
            "clip_plane_x_min",
            "clip_plane_x_max",
            "clip_plane_y_min",
            "clip_plane_y_max",
            "clip_plane_z_min",
            "clip_plane_z_max",
            "do_scale_arrow",
            "do_scale_cone",
            "do_scale_sphere",
            "do_scale_plane",
            "do_scale_box",
            "do_scale_own",
            "show_scalar_bar",
            "opacity_index",
            "add_sphere",
            "radius_sphere",
            "center_sphere",
            "theta_resolution_sphere",
            "phi_resolution_sphere",
            "Ratio_record_sphere",
            "pbr_sphere",
            "metallic_sphere",
            "roughness_sphere",
            "add_plane",
            "center_plane",
            "pbr_plane",
            "metallic_plane",
            "roughness_plane",
            "Ratio_record_plane",
            "add_box",
            "bounds_box",
            "Ratio_record_box",
            "pbr_box",
            "metallic_box",
            "roughness_box",
            "add_own_glyphs",
            "Ratio_record_own",
            "pbr_own",
            "metallic_own",
            "roughness_own",
            "add_rectangle_mesh",
            "rectangle_mesh_interpolate_before_map",
            "system_size",
            "rectrangle_color_index",
            "rectrangle_spacing",
            "rectrangle_opacity_index",
            "show_rectangle_mesh_scalar_bar",
            "add_unstructured_mesh",
            "unstructured_mesh_color_map_index",
            "unstructured_mesh_color_map_opacity_index",
            "show_unstructured_mesh_scalar_bar",
            "unstructured_mesh_interpolate_before_map",
            "phi_compoment_filter_max",
            "phi_compoment_filter_min",
            "theta_compoment_filter_max",
            "theta_compoment_filter_min",
            "do_glyph_cone_rescale",
            "do_glyph_sphere_rescale",
            "do_glyph_plane_rescale",
            "do_glyph_box_rescale",
            "do_glyph_own_rescale",
            "do_glyph_arrow_rescale",
            "rescale_cone_factor",
            "rescale_sphere_factor",
            "rescale_plane_factor",
            "rescale_box_factor",
            "rescale_own_factor",
            "rescale_arrow_factor",
            "rescale_arrow_index",
            "rescale_cone_index",
            "rescale_sphere_index",
            "rescale_plane_index",
            "rescale_box_index",
            "rescale_own_index",
            "rescale_arrow_norm",
            "rescale_cone_norm",
            "rescale_sphere_norm",
            "rescale_plane_norm",
            "rescale_box_norm",
            "rescale_own_norm",
            "add_projection_plane_1",
            "add_projection_plane_2",
            "add_projection_plane_3",
            "add_projection_plane_4",
            "add_projection_plane_5",
            "add_projection_plane_6",
            "interpolate_plane_1",
            "interpolate_plane_2",
            "interpolate_plane_3",
            "interpolate_plane_4",
            "interpolate_plane_5",
            "interpolate_plane_6",
            "do_rectangle_mesh_contour",
            "do_multi_rectangle_surface_contour",
            "rectangle_mesh_contour_isosurface_number",
            "rectangle_mesh_contour_isosurface_value",
            "rectangle_mesh_contour_method_indicator",
            "do_unstructured_mesh_contour",
            "do_multi_unstructured_surface_contour",
            "unstructured_mesh_contour_isosurface_value",
            "unstructured_mesh_contour_isosurface_number",
            "unstructured_mesh_contour_method_indicator",
            "do_rectangle_mesh_slice_along_axis",
            "rectangle_number_of_slice_along_axis",
            "rectangle_axis_of_slice_along_axis",
            "do_unstructured_mesh_slice_along_axis",
            "unstructured_number_of_slice_along_axis",
            "unstructured_axis_of_slice_along_axis",
            "do_rectangle_mesh_rescale",
            "rescale_rectangle_mesh_factor",
            "rescale_rectangle_mesh_norm",
            "do_unstructured_mesh_rescale",
            "rescale_unstructured_mesh_factor",
            "rescale_unstructured_mesh_norm",
            "do_rectangle_mesh_clip_scalar",
            "rectangle_mesh_clip_scalar_max_xyz",
            "rectangle_mesh_clip_scalar_min_xyz",
            "rectangle_mesh_clip_scalar_max_theta",
            "rectangle_mesh_clip_scalar_min_theta",
            "rectangle_mesh_clip_scalar_max_phi",
            "rectangle_mesh_clip_scalar_min_phi",
            "do_unstructured_mesh_clip_scalar",
            "unstructured_mesh_clip_scalar_max_xyz",
            "unstructured_mesh_clip_scalar_min_xyz",
            "unstructured_mesh_clip_scalar_max_theta",
            "unstructured_mesh_clip_scalar_min_theta",
            "unstructured_mesh_clip_scalar_max_phi",
            "unstructured_mesh_clip_scalar_min_phi",
            "dataset_clip_plane_free_normal_1",
            "dataset_clip_plane_free_normal_2",
            "clip_plane_free_1",
            "clip_plane_free_2",
            "do_rectangle_mesh_clip",
            "rectangle_mesh_clip_plane_x_min",
            "rectangle_mesh_clip_plane_x_max",
            "rectangle_mesh_clip_plane_y_min",
            "rectangle_mesh_clip_plane_y_max",
            "rectangle_mesh_clip_plane_z_min",
            "rectangle_mesh_clip_plane_z_max",
            "do_clip_rectangle_mesh_free_normal",
            "rectangle_mesh_clip_plane_free_normal_1",
            "rectangle_mesh_clip_plane_free_normal_2",
            "clip_rectangle_mesh_free_1",
            "clip_rectangle_mesh_free_2",
            "do_unstructured_mesh_clip",
            "unstructured_mesh_clip_plane_x_min",
            "unstructured_mesh_clip_plane_x_max",
            "unstructured_mesh_clip_plane_y_min",
            "unstructured_mesh_clip_plane_y_max",
            "unstructured_mesh_clip_plane_z_min",
            "unstructured_mesh_clip_plane_z_max",
            "do_clip_unstructured_mesh_free_normal",
            "unstructured_mesh_clip_plane_free_normal_1",
            "unstructured_mesh_clip_plane_free_normal_2",
            "clip_unstructured_mesh_free_1",
            "clip_unstructured_mesh_free_2",
            "do_rectangle_mesh_slice",
            "rectangle_mesh_slice_contour_option",
            "rectangle_mesh_slice_origin",
            "rectangle_mesh_slice_normal",
            "do_unstructured_mesh_slice",
            "unstructured_mesh_slice_contour_option",
            "unstructured_mesh_slice_origin",
            "unstructured_mesh_slice_normal",
            "do_rectangle_mesh_clip_box",
            "rectangle_mesh_clip_box_x_min",
            "rectangle_mesh_clip_box_x_max",
            "rectangle_mesh_clip_box_y_min",
            "rectangle_mesh_clip_box_y_max",
            "rectangle_mesh_clip_box_z_min",
            "rectangle_mesh_clip_box_z_max",
            "invert_rectangle_mesh_clip_box",
            "rectangle_mesh_clip_implicit_or_explict",
            "rectangle_mesh_clip_box_factor",
            "do_unstructured_mesh_clip_box",
            "unstructured_mesh_clip_box_x_min",
            "unstructured_mesh_clip_box_x_max",
            "unstructured_mesh_clip_box_y_min",
            "unstructured_mesh_clip_box_y_max",
            "unstructured_mesh_clip_box_z_min",
            "unstructured_mesh_clip_box_z_max",
            "invert_unstructured_mesh_clip_box",
            "unstructured_mesh_clip_implicit_or_explict",
            "unstructured_mesh_clip_box_factor",
            "do_clip_plane_free_normal",
            "pbr_rectangle",
            "pbr_unstructured",
            "add_simple_point",
            "do_glyph_simple_point_rescale",
            "rescale_simple_point_index",
            "simple_point_size",
            "local_rendering_sinmple_point_as_spheres",
            "rescale_simple_point_factor",
            "rescale_simple_point_norm",
            "mom_name1",
            "mom_name2",
            "mom_name3",
            "do_delaunay",
            "antialiasing_indicator",
            "download_screenshot_resolution",
            "download_screenshot_indicator",
            "activate_glyphs_indicator",
            "activate_rectangle_mesh_indicator",
            "activate_unstructured_mesh_indicator",
            "excu_from_other_place",
            "nothing_show",
            "frame_change",
            "projection_plane_1_added",
            "projection_plane_2_added",
            "projection_plane_3_added",
            "projection_plane_4_added",
            "projection_plane_5_added",
            "projection_plane_6_added",
            "cone_added_1",
            "cone_added_2",
            "cone_added_3",
            "cone_added_4",
            "arrow_added_1",
            "arrow_added_2",
            "arrow_added_3",
            "arrow_added_4",
            "sphere_added_1",
            "sphere_added_2",
            "sphere_added_3",
            "sphere_added_4",
            "box_added_1",
            "box_added_2",
            "box_added_3",
            "box_added_4",
            "own_glyphs_added_1",
            "own_glyphs_added_2",
            "own_glyphs_added_3",
            "own_glyphs_added_4",
            "plane_added_1",
            "plane_added_2",
            "plane_added_3",
            "plane_added_4",
            "tmesh_op_indicator",
            "unstructured_mesh_added_1",
            "unstructured_mesh_added_2",
            "unstructured_mesh_added_3",
            "unstructured_mesh_added_4",
            "rectangle_mesh_added_1",
            "rectangle_mesh_added_2",
            "rectangle_mesh_added_3",
            "rectangle_mesh_added_4",
            "rectangle_mesh_contour_isosurface_value_x",
            "rectangle_mesh_contour_isosurface_value_y",
            "rectangle_mesh_contour_isosurface_value_z",
            "simple_point_added_1",
            "simple_point_added_2",
            "simple_point_added_3",
            "simple_point_added_4",
            "excu_from_other_place_welcome_image",
            "nothing_show_welcome_image",
            "first_time_nothing_show",
            "cubemap_exist",
            "activate_cone_indicator",
            "activate_arrow_indicator",
            "activate_sphere_indicator",
            "activate_box_indicator",
            "activate_own_glyphs_indicator",
            "activate_plane_indicator",
            "sub_frame_number",
            "scalar_bar_indicator",
            "moive_size_x",
            "moive_size_y",
            "welcome_image_not_created",
            "cone_cmap_index_indicator",
            "glyph_cmap_vbtn",
            "glyph_opaciy_vbtn",
            "do_clip_component_indicator",
            "activate_point_indicator",
            "point_rescale_indicator",
            "point_size_indicator",
            "point_rescale_factor_indicator",
            "warp_sphere_radius",
            "do_warp_sphere",
            "add_warpped_sphere_kernel",
            "warpped_sphere_kernel",
            "warp_kernel_color",
            "swk_c_indicator",
            "swk_added",
            "warp_sphere_radius_indicator",
            "skw_ratio_indicator",
            "warp_kernel_color_changed",
            "start_desoning_filter_index",
            "low_pass_filter_order",
            "low_pass_normalized_freq",
            "fft_rec_windows_X",
            "fft_rec_windows_Y",
            "fft_rec_windows_Z",
            "projection_plane_added_1_1",
            "projection_plane_added_1_2",
            "projection_plane_added_1_3",
            "projection_plane_added_1_4",
            "projection_plane_added_2_1",
            "projection_plane_added_2_2",
            "projection_plane_added_2_3",
            "projection_plane_added_2_4",
            "projection_plane_added_3_1",
            "projection_plane_added_3_2",
            "projection_plane_added_3_3",
            "projection_plane_added_3_4",
            "projection_plane_added_4_1",
            "projection_plane_added_4_2",
            "projection_plane_added_4_3",
            "projection_plane_added_4_4",
            "projection_plane_added_5_1",
            "projection_plane_added_5_2",
            "projection_plane_added_5_3",
            "projection_plane_added_5_4",
            "projection_plane_added_6_1",
            "projection_plane_added_6_2",
            "projection_plane_added_6_3",
            "projection_plane_added_6_4",
            "do_glyph_projection_fft",
            "do_glyph_projection_fft_indicator",
            "cut_phi_indicator",
            "cut_theta_indicator",
            "rectangle_cmap_vbtn",
            "rectangle_opaciy_vbtn",
            "Tmesh_cmap_vbtn",
            "Tmesh_opaciy_vbtn",
            "rectangle_mesh_contour_isosurface_value_t",
            "rectangle_mesh_contour_isosurface_value_p",
            "unstructured_mesh_contour_isosurface_value_t",
            "unstructured_mesh_contour_isosurface_value_p",
            "opacity_record_tmesh",
            "opacity_record_rectangle_mesh",
            "change_mom1",
            "change_mom2",
            "change_mom3",
            "change_mom4",
            "rec_mesh_color_scalar",
            "rectangle_mesh_clip_scalar_max_x",
            "rectangle_mesh_clip_scalar_min_x",
            "rectangle_mesh_clip_scalar_max_y",
            "rectangle_mesh_clip_scalar_min_y",
            "rectangle_mesh_clip_scalar_max_z",
            "rectangle_mesh_clip_scalar_min_z",
            "roughness_rmesh",
            "metallic_rmesh",
            "metallic_tmesh",
            "roughness_tmesh",
            "pyvista_backend_interactive_ratio",
            "pyvista_backend_still_ratio",
            "do_interpolated_projection",
            "t_mesh_contour_isosurface_value_x",
            "t_mesh_contour_isosurface_value_y",
            "t_mesh_contour_isosurface_value_z",
            "t_mesh_clip_scalar_max_x",
            "t_mesh_clip_scalar_min_x",
            "t_mesh_clip_scalar_max_y",
            "t_mesh_clip_scalar_min_y",
            "t_mesh_clip_scalar_max_z",
            "t_mesh_clip_scalar_min_z",
        ]

        default_value_list = [
            '["{}"]'.format(self.table_name),
            self.code_init_indicator_cmap,
            self.code_init_indicator_frame,
            self.code_init_indicator_metallic,
            self.code_init_indicator_opacity,
            self.code_init_indicator_roughness,
            self.code_init_indicator_resolutions,
            self.code_init_indicator_Ratio,
            self.code_init_indicator_cone_highth,
            self.code_init_indicator_cone_Radius,
            self.code_init_indicator_cs,
            self.code_init_indicator_Cut_X,
            self.code_init_indicator_Cut_Y,
            self.code_init_indicator_Cut_Z,
            self.code_init_indicator_fxyzc,
            self.frame_number,
            self.color_map_index,
            '["{}"]'.format(self.antialiasing),
            self.x_compoment_filter_min,
            self.x_compoment_filter_max,
            self.y_compoment_filter_min,
            self.y_compoment_filter_max,
            self.z_compoment_filter_min,
            self.z_compoment_filter_max,
            self.a1_plane_slicer,
            self.a1_clip_plane_x,
            self.a1_clip_plane_y,
            self.a1_clip_plane_z,
            self.a2_plane_slicer,
            self.a2_clip_plane_x,
            self.a2_clip_plane_y,
            self.a2_clip_plane_z,
            self.b1_plane_slicer,
            self.b1_clip_plane_x,
            self.b1_clip_plane_y,
            self.b1_clip_plane_z,
            self.b2_plane_slicer,
            self.b2_clip_plane_x,
            self.b2_clip_plane_y,
            self.b2_clip_plane_z,
            self.c1_plane_slicer,
            self.c1_clip_plane_x,
            self.c1_clip_plane_y,
            self.c1_clip_plane_z,
            self.c2_plane_slicer,
            self.c2_clip_plane_x,
            self.c2_clip_plane_y,
            self.c2_clip_plane_z,
            self.resolutions,
            self.radius_record,
            self.height_record,
            self.metallic_record,
            self.opacity_record,
            self.roughness_record,
            self.Ratio_record,
            '["{}"]'.format(self.cmap_record),
            self.cone_highth_record,
            self.cone_Radius_record,
            self.cs_record,
            self.camera_position,
            self.camera_focal_point,
            self.camera_up,
            self.camera_zoom,
            self.pbr,
            self.Cone_center,
            self.Arrow_center,
            self.add_cone,
            self.coord_name,
            self.mom_name,
            self.ovf_name,
            self.outputfile_type,
            self.bgc,
            self.moment_file_indicator,
            self.coord_file_indicator,
            self.ovf_file_indicator,
            self.bgc_indicator,
            self.pbr_indicator,
            self.add_glyphs,
            self.add_arrow,
            self.start_arrow,
            self.tip_length_arrow,
            self.tip_radius_arrow,
            self.tip_resolution_arrow,
            self.shaft_radius_arrow,
            self.shaft_resolution_arrow,
            self.Ratio_record_arrow,
            self.pbr_arrow,
            self.metallic_arrow,
            self.roughness_arrow,
            self.do_clip_component,
            self.do_clip_plane_fix_origin_and_normal,
            self.do_clip_box,
            self.clip_plane_x_min,
            self.clip_plane_x_max,
            self.clip_plane_y_min,
            self.clip_plane_y_max,
            self.clip_plane_z_min,
            self.clip_plane_z_max,
            self.do_scale_arrow,
            self.do_scale_cone,
            self.do_scale_sphere,
            self.do_scale_plane,
            self.do_scale_box,
            self.do_scale_own,
            self.show_scalar_bar,
            self.opacity_index,
            self.add_sphere,
            self.radius_sphere,
            self.center_sphere,
            self.theta_resolution_sphere,
            self.phi_resolution_sphere,
            self.Ratio_record_sphere,
            self.pbr_sphere,
            self.metallic_sphere,
            self.roughness_sphere,
            self.add_plane,
            self.center_plane,
            self.pbr_plane,
            self.metallic_plane,
            self.roughness_plane,
            self.Ratio_record_plane,
            self.add_box,
            self.bounds_box,
            self.Ratio_record_box,
            self.pbr_box,
            self.metallic_box,
            self.roughness_box,
            self.add_own_glyphs,
            self.Ratio_record_own,
            self.pbr_own,
            self.metallic_own,
            self.roughness_own,
            self.add_rectangle_mesh,
            self.rectangle_mesh_interpolate_before_map,
            self.system_size,
            self.rectrangle_color_index,
            self.rectrangle_spacing,
            self.rectrangle_opacity_index,
            self.show_rectangle_mesh_scalar_bar,
            self.add_unstructured_mesh,
            self.unstructured_mesh_color_map_index,
            self.unstructured_mesh_color_map_opacity_index,
            self.show_unstructured_mesh_scalar_bar,
            self.unstructured_mesh_interpolate_before_map,
            self.phi_compoment_filter_max,
            self.phi_compoment_filter_min,
            self.theta_compoment_filter_max,
            self.theta_compoment_filter_min,
            self.do_glyph_cone_rescale,
            self.do_glyph_sphere_rescale,
            self.do_glyph_plane_rescale,
            self.do_glyph_box_rescale,
            self.do_glyph_own_rescale,
            self.do_glyph_arrow_rescale,
            self.rescale_cone_factor,
            self.rescale_sphere_factor,
            self.rescale_plane_factor,
            self.rescale_box_factor,
            self.rescale_own_factor,
            self.rescale_arrow_factor,
            self.rescale_arrow_index,
            self.rescale_cone_index,
            self.rescale_sphere_index,
            self.rescale_plane_index,
            self.rescale_box_index,
            self.rescale_own_index,
            self.rescale_arrow_norm,
            self.rescale_cone_norm,
            self.rescale_sphere_norm,
            self.rescale_plane_norm,
            self.rescale_box_norm,
            self.rescale_own_norm,
            self.add_projection_plane_1,
            self.add_projection_plane_2,
            self.add_projection_plane_3,
            self.add_projection_plane_4,
            self.add_projection_plane_5,
            self.add_projection_plane_6,
            self.interpolate_plane_1,
            self.interpolate_plane_2,
            self.interpolate_plane_3,
            self.interpolate_plane_4,
            self.interpolate_plane_5,
            self.interpolate_plane_6,
            self.do_rectangle_mesh_contour,
            self.do_multi_rectangle_surface_contour,
            self.rectangle_mesh_contour_isosurface_number,
            self.rectangle_mesh_contour_isosurface_value,
            self.rectangle_mesh_contour_method_indicator,
            self.do_unstructured_mesh_contour,
            self.do_multi_unstructured_surface_contour,
            self.unstructured_mesh_contour_isosurface_value,
            self.unstructured_mesh_contour_isosurface_number,
            self.unstructured_mesh_contour_method_indicator,
            self.do_rectangle_mesh_slice_along_axis,
            self.rectangle_number_of_slice_along_axis,
            self.rectangle_axis_of_slice_along_axis,
            self.do_unstructured_mesh_slice_along_axis,
            self.unstructured_number_of_slice_along_axis,
            self.unstructured_axis_of_slice_along_axis,
            self.do_rectangle_mesh_rescale,
            self.rescale_rectangle_mesh_factor,
            self.rescale_rectangle_mesh_norm,
            self.do_unstructured_mesh_rescale,
            self.rescale_unstructured_mesh_factor,
            self.rescale_unstructured_mesh_norm,
            self.do_rectangle_mesh_clip_scalar,
            self.rectangle_mesh_clip_scalar_max_xyz,
            self.rectangle_mesh_clip_scalar_min_xyz,
            self.rectangle_mesh_clip_scalar_max_theta,
            self.rectangle_mesh_clip_scalar_min_theta,
            self.rectangle_mesh_clip_scalar_max_phi,
            self.rectangle_mesh_clip_scalar_min_phi,
            self.do_unstructured_mesh_clip_scalar,
            self.unstructured_mesh_clip_scalar_max_xyz,
            self.unstructured_mesh_clip_scalar_min_xyz,
            self.unstructured_mesh_clip_scalar_max_theta,
            self.unstructured_mesh_clip_scalar_min_theta,
            self.unstructured_mesh_clip_scalar_max_phi,
            self.unstructured_mesh_clip_scalar_min_phi,
            self.dataset_clip_plane_free_normal_1,
            self.dataset_clip_plane_free_normal_2,
            self.clip_plane_free_1,
            self.clip_plane_free_2,
            self.do_rectangle_mesh_clip,
            self.rectangle_mesh_clip_plane_x_min,
            self.rectangle_mesh_clip_plane_x_max,
            self.rectangle_mesh_clip_plane_y_min,
            self.rectangle_mesh_clip_plane_y_max,
            self.rectangle_mesh_clip_plane_z_min,
            self.rectangle_mesh_clip_plane_z_max,
            self.do_clip_rectangle_mesh_free_normal,
            self.rectangle_mesh_clip_plane_free_normal_1,
            self.rectangle_mesh_clip_plane_free_normal_2,
            self.clip_rectangle_mesh_free_1,
            self.clip_rectangle_mesh_free_2,
            self.do_unstructured_mesh_clip,
            self.unstructured_mesh_clip_plane_x_min,
            self.unstructured_mesh_clip_plane_x_max,
            self.unstructured_mesh_clip_plane_y_min,
            self.unstructured_mesh_clip_plane_y_max,
            self.unstructured_mesh_clip_plane_z_min,
            self.unstructured_mesh_clip_plane_z_max,
            self.do_clip_unstructured_mesh_free_normal,
            self.unstructured_mesh_clip_plane_free_normal_1,
            self.unstructured_mesh_clip_plane_free_normal_2,
            self.clip_unstructured_mesh_free_1,
            self.clip_unstructured_mesh_free_2,
            self.do_rectangle_mesh_slice,
            self.rectangle_mesh_slice_contour_option,
            self.rectangle_mesh_slice_origin,
            self.rectangle_mesh_slice_normal,
            self.do_unstructured_mesh_slice,
            self.unstructured_mesh_slice_contour_option,
            self.unstructured_mesh_slice_origin,
            self.unstructured_mesh_slice_normal,
            self.do_rectangle_mesh_clip_box,
            self.rectangle_mesh_clip_box_x_min,
            self.rectangle_mesh_clip_box_x_max,
            self.rectangle_mesh_clip_box_y_min,
            self.rectangle_mesh_clip_box_y_max,
            self.rectangle_mesh_clip_box_z_min,
            self.rectangle_mesh_clip_box_z_max,
            self.invert_rectangle_mesh_clip_box,
            self.rectangle_mesh_clip_implicit_or_explict,
            self.rectangle_mesh_clip_box_factor,
            self.do_unstructured_mesh_clip_box,
            self.unstructured_mesh_clip_box_x_min,
            self.unstructured_mesh_clip_box_x_max,
            self.unstructured_mesh_clip_box_y_min,
            self.unstructured_mesh_clip_box_y_max,
            self.unstructured_mesh_clip_box_z_min,
            self.unstructured_mesh_clip_box_z_max,
            self.invert_unstructured_mesh_clip_box,
            self.unstructured_mesh_clip_implicit_or_explict,
            self.unstructured_mesh_clip_box_factor,
            self.do_clip_plane_free_normal,
            self.pbr_rectangle,
            self.pbr_unstructured,
            self.add_simple_point,
            self.do_glyph_simple_point_rescale,
            self.rescale_simple_point_index,
            self.simple_point_size,
            self.local_rendering_sinmple_point_as_spheres,
            self.rescale_simple_point_factor,
            self.rescale_simple_point_norm,
            self.mom_name1,
            self.mom_name2,
            self.mom_name3,
            self.do_delaunay,
            self.antialiasing_indicator,
            self.download_screenshot_resolution,
            self.download_screenshot_indicator,
            self.activate_glyphs_indicator,
            self.activate_rectangle_mesh_indicator,
            self.activate_unstructured_mesh_indicator,
            self.excu_from_other_place,
            self.nothing_show,
            self.frame_change,
            self.projection_plane_1_added,
            self.projection_plane_2_added,
            self.projection_plane_3_added,
            self.projection_plane_4_added,
            self.projection_plane_5_added,
            self.projection_plane_6_added,
            self.cone_added_1,
            self.cone_added_2,
            self.cone_added_3,
            self.cone_added_4,
            self.arrow_added_1,
            self.arrow_added_2,
            self.arrow_added_3,
            self.arrow_added_4,
            self.sphere_added_1,
            self.sphere_added_2,
            self.sphere_added_3,
            self.sphere_added_4,
            self.box_added_1,
            self.box_added_2,
            self.box_added_3,
            self.box_added_4,
            self.own_glyphs_added_1,
            self.own_glyphs_added_2,
            self.own_glyphs_added_3,
            self.own_glyphs_added_4,
            self.plane_added_1,
            self.plane_added_2,
            self.plane_added_3,
            self.plane_added_4,
            self.tmesh_op_indicator,
            self.unstructured_mesh_added_1,
            self.unstructured_mesh_added_2,
            self.unstructured_mesh_added_3,
            self.unstructured_mesh_added_4,
            self.rectangle_mesh_added_1,
            self.rectangle_mesh_added_2,
            self.rectangle_mesh_added_3,
            self.rectangle_mesh_added_4,
            self.rectangle_mesh_contour_isosurface_value_x,
            self.rectangle_mesh_contour_isosurface_value_y,
            self.rectangle_mesh_contour_isosurface_value_z,
            self.simple_point_added_1,
            self.simple_point_added_2,
            self.simple_point_added_3,
            self.simple_point_added_4,
            self.excu_from_other_place_welcome_image,
            self.nothing_show_welcome_image,
            self.first_time_nothing_show,
            self.cubemap_exist,
            self.activate_cone_indicator,
            self.activate_arrow_indicator,
            self.activate_sphere_indicator,
            self.activate_box_indicator,
            self.activate_own_glyphs_indicator,
            self.activate_plane_indicator,
            self.sub_frame_number,
            self.scalar_bar_indicator,
            self.moive_size_x,
            self.moive_size_y,
            self.welcome_image_not_created,
            self.cone_cmap_index_indicator,
            self.glyph_cmap_vbtn,
            self.glyph_opaciy_vbtn,
            self.do_clip_component_indicator,
            self.activate_point_indicator,
            self.point_rescale_indicator,
            self.point_size_indicator,
            self.point_rescale_factor_indicator,
            self.warp_sphere_radius,
            self.do_warp_sphere,
            self.add_warpped_sphere_kernel,
            self.warpped_sphere_kernel,
            '["{}"]'.format(self.warp_kernel_color[0]),
            self.swk_c_indicator,
            self.swk_added,
            self.warp_sphere_radius_indicator,
            self.skw_ratio_indicator,
            self.warp_kernel_color_changed,
            self.start_desoning_filter_index,
            self.low_pass_filter_order,
            self.low_pass_normalized_freq,
            self.fft_rec_windows_X,
            self.fft_rec_windows_Y,
            self.fft_rec_windows_Z,
            self.projection_plane_added_1_1,
            self.projection_plane_added_1_2,
            self.projection_plane_added_1_3,
            self.projection_plane_added_1_4,
            self.projection_plane_added_2_1,
            self.projection_plane_added_2_2,
            self.projection_plane_added_2_3,
            self.projection_plane_added_2_4,
            self.projection_plane_added_3_1,
            self.projection_plane_added_3_2,
            self.projection_plane_added_3_3,
            self.projection_plane_added_3_4,
            self.projection_plane_added_4_1,
            self.projection_plane_added_4_2,
            self.projection_plane_added_4_3,
            self.projection_plane_added_4_4,
            self.projection_plane_added_5_1,
            self.projection_plane_added_5_2,
            self.projection_plane_added_5_3,
            self.projection_plane_added_5_4,
            self.projection_plane_added_6_1,
            self.projection_plane_added_6_2,
            self.projection_plane_added_6_3,
            self.projection_plane_added_6_4,
            self.do_glyph_projection_fft,
            self.do_glyph_projection_fft_indicator,
            self.cut_phi_indicator,
            self.cut_theta_indicator,
            self.rectangle_cmap_vbtn,
            self.rectangle_opaciy_vbtn,
            self.Tmesh_cmap_vbtn,
            self.Tmesh_opaciy_vbtn,
            self.rectangle_mesh_contour_isosurface_value_t,
            self.rectangle_mesh_contour_isosurface_value_p,
            self.unstructured_mesh_contour_isosurface_value_t,
            self.unstructured_mesh_contour_isosurface_value_p,
            self.opacity_record_tmesh,
            self.opacity_record_rectangle_mesh,
            self.change_mom1,
            self.change_mom2,
            self.change_mom3,
            self.change_mom4,
            '["{}"]'.format(self.rec_mesh_color_scalar[0]),
            self.rectangle_mesh_clip_scalar_max_x,
            self.rectangle_mesh_clip_scalar_min_x,
            self.rectangle_mesh_clip_scalar_max_y,
            self.rectangle_mesh_clip_scalar_min_y,
            self.rectangle_mesh_clip_scalar_max_z,
            self.rectangle_mesh_clip_scalar_min_z,
            self.roughness_rmesh,
            self.metallic_rmesh,
            self.metallic_tmesh,
            self.roughness_tmesh,
            self.pyvista_backend_interactive_ratio,
            self.pyvista_backend_still_ratio,
            self.do_interpolated_projection,
            self.t_mesh_contour_isosurface_value_x,
            self.t_mesh_contour_isosurface_value_y,
            self.t_mesh_contour_isosurface_value_z,
            self.t_mesh_clip_scalar_max_x,
            self.t_mesh_clip_scalar_min_x,
            self.t_mesh_clip_scalar_max_y,
            self.t_mesh_clip_scalar_min_y,
            self.t_mesh_clip_scalar_max_z,
            self.t_mesh_clip_scalar_min_z,
        ]
        for i in range(len(name_list)):
            creat_new_keys(
                db_path, table_name_store, name_list[i], default_value_list[i]
            )


class local_state_class:
    def __init__(self, pyvista_LR):
        # We store some indicator here, which should not be stored in the database.
        # for saving time, we also store trajectory which have very big size in the memory. so it only need to be loaded once.
        self.mom_states_x = None
        self.mom_states_x1 = None
        self.mom_states_x2 = None
        self.mom_states_x3 = None
        self.mom_states_y = None
        self.mom_states_y1 = None
        self.mom_states_y2 = None
        self.mom_states_y3 = None
        self.mom_states_z = None
        self.mom_states_z1 = None
        self.mom_states_z2 = None
        self.mom_states_z3 = None
        self.coord = None
        self.ui_control_model = "trame"
        self.max_frame = (50,)
        self.moment_magintude = None
        self.mom_states_x_one_frame = None
        self.mom_states_x_one_frame1 = None
        self.mom_states_x_one_frame2 = None
        self.mom_states_x_one_frame3 = None
        self.mom_states_y_one_frame = None
        self.mom_states_y_one_frame1 = None
        self.mom_states_y_one_frame2 = None
        self.mom_states_y_one_frame3 = None
        self.mom_states_z_one_frame = None
        self.mom_states_z_one_frame1 = None
        self.mom_states_z_one_frame2 = None
        self.mom_states_z_one_frame3 = None
        self.calculated_unstructured_mesh_single_frame = None
        self.calculated_unstructured_mesh_whole_trajectory = None
        self.clim_range = [-1, 1]
        self.user_input_glyph = None
        self.rectrangle_mesh_image_data = None
        self.rectrangle_clim_range = None
        self.moment_magintude_all = None
        self.user_bgc_image = None
        self.glyph_scalar_bar_name = None
        self.rectangle_mesh_scalar_bar_name = None
        self.unstructured_mesh_scalar_bar_name = None
        self.point_cloud_arrow_for_face_cut = pv.PolyData()
        self.face_clip_index = []
        self.face_clip_index_r = []
        self.face_clip_index_t = []
        self.glyph_projection_plane = []
        self.cubemap_folder_names_list = []
        self.do_warp_sphere_vbtn_light = []
        self.file_select_1 = None
        self.file_select_2 = None
        self.file_select_3 = None
        self.file_select_4 = None
        self.moive_fps = 5
        self.roughness_arrow_indicator = 0
        self.new_profile_name = "newtable"
        self.unified_control = True
        self.metallic_arrow_indicator = 0
        self.metallic_sphere_indicator = 0
        self.metallic_box_indicator = 0
        self.metallic_own_indicator = 0
        self.metallic_plane_indicator = 0
        self.pbr_arrow_indicator = 0
        self.pbr_sphere_indicator = 0
        self.pbr_plane_indicator = 0
        self.do_interpolated_projection_indicator = 0
        self.pbr_box_indicator = 0
        self.pbr_own_indicator = 0
        self.do_scale_cone_indicator = 0
        self.do_scale_arrow_indicator = 0
        self.do_scale_box_indicator = 0
        self.do_scale_sphere_indicator = 0
        self.do_scale_plane_indicator = 0
        self.do_scale_own_indicator = 0
        self.roughness_sphere_indicator = 0
        self.roughness_box_indicator = 0
        self.metallic_arrow_indicator = 0
        self.roughness_plane_indicator = 0
        self.roughness_own_indicator = 0
        self.Ratio_record_arrow_indicator = 0
        self.tip_length_arrow_indicator = 0
        self.tip_radius_arrow_indicator = 0
        self.tip_resolution_arrow_indicator = 0
        self.shaft_radius_arrow_indicator = 0
        self.shaft_resolution_arrow_indicator = 0
        self.Ratio_record_box_indicator = 0
        self.Ratio_record_sphere_indicator = 0
        self.radius_sphere_indicator = 0
        self.theta_resolution_sphere_indicator = 0
        self.phi_resolution_sphere_indicator = 0
        self.Ratio_record_plane_indicator = 0
        self.Ratio_record_own_indicator = 0
        self.clip_plane_x_min_indicator = 0
        self.clip_plane_x_max_indicator = 0
        self.clip_plane_y_min_indicator = 0
        self.clip_plane_y_max_indicator = 0
        self.clip_plane_z_min_indicator = 0
        self.clip_plane_z_max_indicator = 0
        self.clip_plane_free_min_indicator = 0
        self.clip_plane_free_max_indicator = 0
        self.point_rescale_factor_indicator = 0
        self.do_clip_component_recmesh_indicator = 0
        self.rectangle_mesh_rescale_indicator = 0
        self.rescale_rectangle_mesh_factor_indicator = 0
        self.metallic_rmesh_indicator = 0
        self.pbr_rectangle_indicator = 0
        self.do_rectangle_mesh_contour_indicator = 0
        self.rectangle_mesh_interpolate_before_map_indicator = 0
        self.do_multi_rectangle_surface_contour_indicator = 0
        self.opacity_record_rectangle_mesh_indicator = 0
        self.roughness_rmesh_indicator = 0
        self.rectangle_mesh_contour_isosurface_number_indicator = 0
        self.rectangle_mesh_contour_isosurface_value_t_indicator = 0
        self.rectangle_mesh_contour_isosurface_value_p_indicator = 0
        self.rectangle_mesh_contour_isosurface_value_x_indicator = 0
        self.rectangle_mesh_contour_isosurface_value_y_indicator = 0
        self.rectangle_mesh_contour_isosurface_value_z_indicator = 0
        self.Cut_X_indicator = 0
        self.Cut_Y_indicator = 0
        self.Cut_Z_indicator = 0
        self.Cut_theta_indicator = 0
        self.Cut_phi_indicator = 0
        self.rectangle_mesh_clip_plane_x_min_indicator = 0
        self.rectangle_mesh_clip_plane_x_max_indicator = 0
        self.rectangle_mesh_clip_plane_y_max_indicator = 0
        self.rectangle_mesh_clip_plane_y_min_indicator = 0
        self.rectangle_mesh_clip_plane_z_min_indicator = 0
        self.rectangle_mesh_clip_plane_z_max_indicator = 0
        self.clip_rectangle_mesh_free_1_indicator = 0
        self.clip_rectangle_mesh_free_2_indicator = 0
        self.do_clip_component_Tmesh_indicator = 0
        self.unstructured_mesh_rescale_indicator = 0
        self.rescale_unstructured_mesh_factor_indicator = 0
        self.metallic_tmesh_indicator = 0
        self.roughness_tmesh_indicator = 0
        self.pbr_unstructured_indicator = 0
        self.do_multi_unstructured_surface_contour_indicator = 0
        self.unstructured_mesh_interpolate_before_map_indicator = 0
        self.do_unstructured_mesh_contour_indicator = 0
        self.opacity_record_tmesh_indicator = 0
        self.roughness_tmesh_indicator = 0
        self.unstructured_mesh_contour_isosurface_number_indicator = 0
        self.t_mesh_contour_isosurface_value_x_indicator = 0
        self.t_mesh_contour_isosurface_value_y_indicator = 0
        self.t_mesh_contour_isosurface_value_z_indicator = 0
        self.unstructured_mesh_contour_isosurface_value_indicator = 0
        self.unstructured_mesh_contour_isosurface_value_t_indicator = 0
        self.unstructured_mesh_contour_isosurface_value_p_indicator = 0
        self.Cut_X_tmesh_indicator = 0
        self.Cut_phi_Tmesh_indicator = 0
        self.Cut_theta_tmesh_indicator = 0
        self.Cut_Z_tmesh_indicator = 0
        self.Cut_Y_tmesh_indicator = 0
        self.unstructured_mesh_clip_plane_x_min_indicator = 0
        self.unstructured_mesh_clip_plane_x_max_indicator = 0
        self.unstructured_mesh_clip_plane_y_max_indicator = 0
        self.unstructured_mesh_clip_plane_y_min_indicator = 0
        self.unstructured_mesh_clip_plane_z_min_indicator = 0
        self.unstructured_mesh_clip_plane_z_max_indicator = 0
        self.clip_unstructured_mesh_free_1_indicator = 0
        self.clip_unstructured_mesh_free_2_indicator = 0
        self.low_pass_filter_order_indicator = 0
        self.low_pass_normalized_freq_indicator = 0
        self.fft_rec_windows_X_indicator = 0
        self.fft_rec_windows_Y_indicator = 0
        self.fft_rec_windows_Z_indicator = 0
        self.unified_control_indicator = 0

        self.do_delaunay = pyvista_LR.do_delaunay
        self.antialiasing_indicator = pyvista_LR.antialiasing_indicator
        self.download_screenshot_resolution = pyvista_LR.download_screenshot_resolution
        self.download_screenshot_indicator = pyvista_LR.download_screenshot_indicator
        self.activate_glyphs_indicator = pyvista_LR.activate_glyphs_indicator
        self.activate_rectangle_mesh_indicator = (
            pyvista_LR.activate_rectangle_mesh_indicator
        )
        self.activate_unstructured_mesh_indicator = (
            pyvista_LR.activate_unstructured_mesh_indicator
        )
        self.excu_from_other_place = pyvista_LR.excu_from_other_place
        self.nothing_show = pyvista_LR.nothing_show
        self.frame_change = pyvista_LR.frame_change
        self.projection_plane_1_added = pyvista_LR.projection_plane_1_added
        self.projection_plane_2_added = pyvista_LR.projection_plane_2_added
        self.projection_plane_3_added = pyvista_LR.projection_plane_3_added
        self.projection_plane_4_added = pyvista_LR.projection_plane_4_added
        self.projection_plane_5_added = pyvista_LR.projection_plane_5_added
        self.projection_plane_6_added = pyvista_LR.projection_plane_6_added
        self.cone_added_1 = pyvista_LR.cone_added_1
        self.cone_added_2 = pyvista_LR.cone_added_2
        self.cone_added_3 = pyvista_LR.cone_added_3
        self.cone_added_4 = pyvista_LR.cone_added_4
        self.arrow_added_1 = pyvista_LR.arrow_added_1
        self.arrow_added_2 = pyvista_LR.arrow_added_2
        self.arrow_added_3 = pyvista_LR.arrow_added_3
        self.arrow_added_4 = pyvista_LR.arrow_added_4
        self.sphere_added_1 = pyvista_LR.sphere_added_1
        self.sphere_added_2 = pyvista_LR.sphere_added_2
        self.sphere_added_3 = pyvista_LR.sphere_added_3
        self.sphere_added_4 = pyvista_LR.sphere_added_4
        self.box_added_1 = pyvista_LR.box_added_1
        self.box_added_2 = pyvista_LR.box_added_2
        self.box_added_3 = pyvista_LR.box_added_3
        self.box_added_4 = pyvista_LR.box_added_4
        self.own_glyphs_added_1 = pyvista_LR.own_glyphs_added_1
        self.own_glyphs_added_2 = pyvista_LR.own_glyphs_added_2
        self.own_glyphs_added_3 = pyvista_LR.own_glyphs_added_3
        self.own_glyphs_added_4 = pyvista_LR.own_glyphs_added_4
        self.plane_added_1 = pyvista_LR.plane_added_1
        self.plane_added_2 = pyvista_LR.plane_added_2
        self.plane_added_3 = pyvista_LR.plane_added_3
        self.plane_added_4 = pyvista_LR.plane_added_4
        self.tmesh_op_indicator = pyvista_LR.tmesh_op_indicator
        self.unstructured_mesh_added_1 = pyvista_LR.unstructured_mesh_added_1
        self.unstructured_mesh_added_2 = pyvista_LR.unstructured_mesh_added_2
        self.unstructured_mesh_added_3 = pyvista_LR.unstructured_mesh_added_3
        self.unstructured_mesh_added_4 = pyvista_LR.unstructured_mesh_added_4
        self.rectangle_mesh_added_1 = pyvista_LR.rectangle_mesh_added_1
        self.rectangle_mesh_added_2 = pyvista_LR.rectangle_mesh_added_2
        self.rectangle_mesh_added_3 = pyvista_LR.rectangle_mesh_added_3
        self.rectangle_mesh_added_4 = pyvista_LR.rectangle_mesh_added_4
        self.rectangle_mesh_contour_isosurface_value_x = (
            pyvista_LR.rectangle_mesh_contour_isosurface_value_x
        )
        self.rectangle_mesh_contour_isosurface_value_y = (
            pyvista_LR.rectangle_mesh_contour_isosurface_value_y
        )
        self.rectangle_mesh_contour_isosurface_value_z = (
            pyvista_LR.rectangle_mesh_contour_isosurface_value_z
        )
        self.simple_point_added_1 = pyvista_LR.simple_point_added_1
        self.simple_point_added_2 = pyvista_LR.simple_point_added_2
        self.simple_point_added_3 = pyvista_LR.simple_point_added_3
        self.simple_point_added_4 = pyvista_LR.simple_point_added_4
        self.excu_from_other_place_welcome_image = (
            pyvista_LR.excu_from_other_place_welcome_image
        )
        self.nothing_show_welcome_image = pyvista_LR.nothing_show_welcome_image
        self.first_time_nothing_show = pyvista_LR.first_time_nothing_show
        self.cubemap_exist = pyvista_LR.cubemap_exist
        self.activate_cone_indicator = pyvista_LR.activate_cone_indicator
        self.activate_arrow_indicator = pyvista_LR.activate_arrow_indicator
        self.activate_sphere_indicator = pyvista_LR.activate_sphere_indicator
        self.activate_box_indicator = pyvista_LR.activate_box_indicator
        self.activate_own_glyphs_indicator = pyvista_LR.activate_own_glyphs_indicator
        self.activate_plane_indicator = pyvista_LR.activate_plane_indicator
        self.sub_frame_number = pyvista_LR.sub_frame_number
        self.scalar_bar_indicator = pyvista_LR.scalar_bar_indicator
        self.moive_size_x = pyvista_LR.moive_size_x
        self.moive_size_y = pyvista_LR.moive_size_y
        self.welcome_image_not_created = pyvista_LR.welcome_image_not_created
        self.cone_cmap_index_indicator = pyvista_LR.cone_cmap_index_indicator
        self.glyph_cmap_vbtn = pyvista_LR.glyph_cmap_vbtn
        self.glyph_opaciy_vbtn = pyvista_LR.glyph_opaciy_vbtn
        self.do_clip_component_indicator = pyvista_LR.do_clip_component_indicator
        self.activate_point_indicator = pyvista_LR.activate_point_indicator
        self.point_rescale_indicator = pyvista_LR.point_rescale_indicator
        self.point_size_indicator = pyvista_LR.point_size_indicator
        self.point_rescale_factor_indicator = pyvista_LR.point_rescale_factor_indicator
        self.warp_sphere_radius = pyvista_LR.warp_sphere_radius
        self.do_warp_sphere = pyvista_LR.do_warp_sphere
        self.add_warpped_sphere_kernel = pyvista_LR.add_warpped_sphere_kernel
        self.warpped_sphere_kernel = pyvista_LR.warpped_sphere_kernel
        self.warp_kernel_color = pyvista_LR.warp_kernel_color
        self.swk_c_indicator = pyvista_LR.swk_c_indicator
        self.swk_added = pyvista_LR.swk_added
        self.warp_sphere_radius_indicator = pyvista_LR.warp_sphere_radius_indicator
        self.skw_ratio_indicator = pyvista_LR.skw_ratio_indicator
        self.warp_kernel_color_changed = pyvista_LR.warp_kernel_color_changed
        self.start_desoning_filter_index = pyvista_LR.start_desoning_filter_index
        self.low_pass_filter_order = pyvista_LR.low_pass_filter_order
        self.low_pass_normalized_freq = pyvista_LR.low_pass_normalized_freq
        self.fft_rec_windows_X = pyvista_LR.fft_rec_windows_X
        self.fft_rec_windows_Y = pyvista_LR.fft_rec_windows_Y
        self.fft_rec_windows_Z = pyvista_LR.fft_rec_windows_Z
        self.projection_plane_added_1_1 = pyvista_LR.projection_plane_added_1_1
        self.projection_plane_added_1_2 = pyvista_LR.projection_plane_added_1_2
        self.projection_plane_added_1_3 = pyvista_LR.projection_plane_added_1_3
        self.projection_plane_added_1_4 = pyvista_LR.projection_plane_added_1_4
        self.projection_plane_added_2_1 = pyvista_LR.projection_plane_added_2_1
        self.projection_plane_added_2_2 = pyvista_LR.projection_plane_added_2_2
        self.projection_plane_added_2_3 = pyvista_LR.projection_plane_added_2_3
        self.projection_plane_added_2_4 = pyvista_LR.projection_plane_added_2_4
        self.projection_plane_added_3_1 = pyvista_LR.projection_plane_added_3_1
        self.projection_plane_added_3_2 = pyvista_LR.projection_plane_added_3_2
        self.projection_plane_added_3_3 = pyvista_LR.projection_plane_added_3_3
        self.projection_plane_added_3_4 = pyvista_LR.projection_plane_added_3_4
        self.projection_plane_added_4_1 = pyvista_LR.projection_plane_added_4_1
        self.projection_plane_added_4_2 = pyvista_LR.projection_plane_added_4_2
        self.projection_plane_added_4_3 = pyvista_LR.projection_plane_added_4_3
        self.projection_plane_added_4_4 = pyvista_LR.projection_plane_added_4_4
        self.projection_plane_added_5_1 = pyvista_LR.projection_plane_added_5_1
        self.projection_plane_added_5_2 = pyvista_LR.projection_plane_added_5_2
        self.projection_plane_added_5_3 = pyvista_LR.projection_plane_added_5_3
        self.projection_plane_added_5_4 = pyvista_LR.projection_plane_added_5_4
        self.projection_plane_added_6_1 = pyvista_LR.projection_plane_added_6_1
        self.projection_plane_added_6_2 = pyvista_LR.projection_plane_added_6_2
        self.projection_plane_added_6_3 = pyvista_LR.projection_plane_added_6_3
        self.projection_plane_added_6_4 = pyvista_LR.projection_plane_added_6_4
        self.do_glyph_projection_fft = pyvista_LR.do_glyph_projection_fft
        self.do_glyph_projection_fft_indicator = (
            pyvista_LR.do_glyph_projection_fft_indicator
        )
        self.cut_phi_indicator = pyvista_LR.cut_phi_indicator
        self.cut_theta_indicator = pyvista_LR.cut_theta_indicator
        self.rectangle_cmap_vbtn = pyvista_LR.rectangle_cmap_vbtn
        self.rectangle_opaciy_vbtn = pyvista_LR.rectangle_opaciy_vbtn
        self.Tmesh_cmap_vbtn = pyvista_LR.Tmesh_cmap_vbtn
        self.Tmesh_opaciy_vbtn = pyvista_LR.Tmesh_opaciy_vbtn
        self.rectangle_mesh_contour_isosurface_value_t = (
            pyvista_LR.rectangle_mesh_contour_isosurface_value_t
        )
        self.rectangle_mesh_contour_isosurface_value_p = (
            pyvista_LR.rectangle_mesh_contour_isosurface_value_p
        )
        self.unstructured_mesh_contour_isosurface_value_t = (
            pyvista_LR.unstructured_mesh_contour_isosurface_value_t
        )
        self.unstructured_mesh_contour_isosurface_value_p = (
            pyvista_LR.unstructured_mesh_contour_isosurface_value_p
        )
        self.opacity_record_tmesh = pyvista_LR.opacity_record_tmesh
        self.opacity_record_rectangle_mesh = pyvista_LR.opacity_record_rectangle_mesh
        self.change_mom1 = pyvista_LR.change_mom1
        self.change_mom2 = pyvista_LR.change_mom2
        self.change_mom3 = pyvista_LR.change_mom3
        self.change_mom4 = pyvista_LR.change_mom4
        self.rec_mesh_color_scalar = pyvista_LR.rec_mesh_color_scalar
        self.rectangle_mesh_clip_scalar_max_x = (
            pyvista_LR.rectangle_mesh_clip_scalar_max_x
        )
        self.rectangle_mesh_clip_scalar_min_x = (
            pyvista_LR.rectangle_mesh_clip_scalar_min_x
        )
        self.rectangle_mesh_clip_scalar_max_y = (
            pyvista_LR.rectangle_mesh_clip_scalar_max_y
        )
        self.rectangle_mesh_clip_scalar_min_y = (
            pyvista_LR.rectangle_mesh_clip_scalar_min_y
        )
        self.rectangle_mesh_clip_scalar_max_z = (
            pyvista_LR.rectangle_mesh_clip_scalar_max_z
        )
        self.rectangle_mesh_clip_scalar_min_z = (
            pyvista_LR.rectangle_mesh_clip_scalar_min_z
        )
        self.roughness_rmesh = pyvista_LR.roughness_rmesh
        self.metallic_rmesh = pyvista_LR.metallic_rmesh
        self.metallic_tmesh = pyvista_LR.metallic_tmesh
        self.roughness_tmesh = pyvista_LR.roughness_tmesh
        self.pyvista_backend_interactive_ratio = (
            pyvista_LR.pyvista_backend_interactive_ratio
        )
        self.pyvista_backend_still_ratio = pyvista_LR.pyvista_backend_still_ratio
        self.do_interpolated_projection = pyvista_LR.do_interpolated_projection
        self.t_mesh_contour_isosurface_value_x = (
            pyvista_LR.t_mesh_contour_isosurface_value_x
        )
        self.t_mesh_contour_isosurface_value_y = (
            pyvista_LR.t_mesh_contour_isosurface_value_y
        )
        self.t_mesh_contour_isosurface_value_z = (
            pyvista_LR.t_mesh_contour_isosurface_value_z
        )
        self.t_mesh_clip_scalar_max_x = pyvista_LR.t_mesh_clip_scalar_max_x
        self.t_mesh_clip_scalar_min_x = pyvista_LR.t_mesh_clip_scalar_min_x
        self.t_mesh_clip_scalar_max_y = pyvista_LR.t_mesh_clip_scalar_max_y
        self.t_mesh_clip_scalar_min_y = pyvista_LR.t_mesh_clip_scalar_min_y
        self.t_mesh_clip_scalar_max_z = pyvista_LR.t_mesh_clip_scalar_max_z
        self.t_mesh_clip_scalar_min_z = pyvista_LR.t_mesh_clip_scalar_min_z
