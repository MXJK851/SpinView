import pandas as pd
import numpy as np
import os
import glob

"""
Spirit output file parser
"""


def ovf_spirit_parser(OVF_file_name):
    """
    Parser for the OVF file
    Test with Spirit code output OVF file
    """
    # Find out which one is not start with #
    list_ovf_key = [
        "# xmin:",
        "# ymin:",
        "# zmin:",
        "# xmax:",
        "# ymax:",
        "# zmax:",
        "# xnodes:",
        "# ynodes:",
        "# znodes:",
        "# xstepsize:",
        "# ystepsize:",
        "# zstepsize:",
    ]

    dict_ovf_keys = {}

    moment_start_index = 0
    with open(OVF_file_name) as f:
        for line in f:
            if not line.lstrip().startswith("#"):
                break
            else:
                for name in list_ovf_key:
                    if line.lstrip().startswith(name):
                        dict_ovf_keys[name.lstrip("# ").rstrip(":")] = float(
                            line.lstrip(name)
                        )
                moment_start_index = moment_start_index + 1

    a0 = dict_ovf_keys["xmin"]
    a1 = dict_ovf_keys["xmax"]
    b0 = dict_ovf_keys["ymin"]
    b1 = dict_ovf_keys["ymax"]
    c0 = dict_ovf_keys["zmin"]
    c1 = dict_ovf_keys["zmax"]
    gap_x = dict_ovf_keys["xstepsize"]
    gap_y = dict_ovf_keys["ystepsize"]
    gap_z = dict_ovf_keys["zstepsize"]
    normal_helper = min(gap_x, gap_y, gap_z)
    a0 = a0 / normal_helper
    a1 = a1 / normal_helper
    b0 = b0 / normal_helper
    b1 = b1 / normal_helper
    c0 = c0 / normal_helper
    c1 = c1 / normal_helper

    a_r = int(dict_ovf_keys["xnodes"])
    b_r = int(dict_ovf_keys["ynodes"])
    c_r = int(dict_ovf_keys["znodes"])

    Z, Y, X = np.mgrid[c0 : c1 : c_r * 1j, b0 : b1 : b_r * 1j, a0 : a1 : a_r * 1j]
    x = (X.flatten(),)
    y = (Y.flatten(),)
    z = (Z.flatten(),)
    coord = np.vstack([x, y, z]).T

    mom_output = pd.read_csv(
        OVF_file_name,
        sep="\s+",
        header=None,
        skiprows=moment_start_index,
        skipfooter=2,
        engine="python",
    ).values
    # replace 0,0,0 to np.nan
    # mom_output.astype(np.float32)
    # for i in range(len(mom_output)):
    #     print(mom_output[i].all())
    #     print(mom_output[i] == "[0 0 0]")
    #     print(mom_output[i] == ["0 0 0"])
    #     break
    # if mom_output[i]== [0 0 0]:
    #     mom_output[i] = [np.nan, np.nan, np.nan]
    if 0 in mom_output.sum(axis=1):
        print(
            "There is [0, 0, 0] in the ovf file, we will replace it with np.nan to hiden those sites (Specially meshes detected)"
        )

        mom_output = mom_output.T
        mom_x = mom_output[0]
        mom_y = mom_output[1]
        mom_z = mom_output[2]
        mom_states_x = np.array(mom_x).astype(np.float32)
        mom_states_y = np.array(mom_y).astype(np.float32)
        mom_states_z = np.array(mom_z).astype(np.float32)
        for i in range(len(mom_states_x)):
            if (
                mom_states_x[i] == 0.0
                and mom_states_y[i] == 0.0
                and mom_states_z[i] == 0.0
            ):
                mom_states_x[i] = np.nan
                mom_states_y[i] = np.nan
                mom_states_z[i] = np.nan
    else:
        mom_output = mom_output.T
        mom_x = mom_output[0]
        mom_y = mom_output[1]
        mom_z = mom_output[2]
        mom_states_x = np.array(mom_x).astype(np.float32)
        mom_states_y = np.array(mom_y).astype(np.float32)
        mom_states_z = np.array(mom_z).astype(np.float32)

    return mom_states_x, mom_states_y, mom_states_z, coord


"""
UppASD Parser
"""


def coord_file_parser(file_name_of_coord):
    """
    :param file_name_of_coord coord file
    :type file_name_of_coord opened output file
    :return: np array
    """

    # this matrix includes series number: the first C
    result = pd.read_csv(file_name_of_coord, sep="\s+", header=None)
    coord = np.array(result)[:, 1:4]
    return coord


def moment_out_parser(mom_out_file):
    """
    :param mom_out_file moment file
    :type mom_out_file opened output file
    :return: np.array
    """

    mom_output = pd.read_csv(mom_out_file, sep="\s+", header=None, skiprows=7)
    magnitudes = mom_output[3]
    mom_x = mom_output[4]
    mom_y = mom_output[5]
    mom_z = mom_output[6]
    mom_states_x = np.array(mom_x)
    mom_states_y = np.array(mom_y)
    mom_states_z = np.array(mom_z)
    return mom_states_x, mom_states_y, mom_states_z, magnitudes


def total_energy_file_paser(file_name_of_total_energy):
    # here the inputfile name should be totenergy.SCsurf_T.out
    result = pd.read_csv(file_name_of_total_energy, sep="\s+", header=None).drop([0])
    Iter_num_totenergy = np.array(list(result[0]))
    Tot = np.array(list(result[1])).astype(float)
    Exc = np.array(list(result[2])).astype(float)
    Ani = np.array(list(result[3])).astype(float)
    DM = np.array(list(result[4])).astype(float)
    PD = np.array(list(result[5])).astype(float)
    BiqDM = np.array(list(result[6])).astype(float)
    BQ = np.array(list(result[7])).astype(float)
    Dip = np.array(list(result[8])).astype(float)
    Zeeman = np.array(list(result[9])).astype(float)
    LSF = np.array(list(result[10])).astype(float)
    Chir = np.array(list(result[11])).astype(float)
    return Iter_num_totenergy, Tot, Exc, Ani, DM, PD, BiqDM, BQ, Dip, Zeeman, LSF, Chir


def averages_file_paser(file_name_of_averages):
    result = pd.read_csv(file_name_of_averages, sep="\s+", header=None).drop([0])
    Iter_num_average = np.array(list(np.array(result)[:, 0]))
    M_x = np.array(list(np.array(result)[:, 1])).astype(float)
    M_y = np.array(list(np.array(result)[:, 2])).astype(float)
    M_z = np.array(list(np.array(result)[:, 3])).astype(float)
    M = np.array(list(np.array(result)[:, 4])).astype(float)
    M_stdv = np.array(list(np.array(result)[:, 5])).astype(float)
    return Iter_num_average, M_x, M_y, M_z, M, M_stdv


def moment_csv_parser(mom_out_file):
    """
    This parser works for the csv file generated by UppASD(Qichen's version), i.e., moment.csv
    """

    mom_output = pd.read_csv(mom_out_file, header=None, skiprows=7, engine="pyarrow")
    magnitudes = mom_output[3]
    mom_x = mom_output[4]
    mom_y = mom_output[5]
    mom_z = mom_output[6]
    mom_states_x = np.array(mom_x)
    mom_states_y = np.array(mom_y)
    mom_states_z = np.array(mom_z)
    return mom_states_x, mom_states_y, mom_states_z, magnitudes


def coord_csv_parser(file_name_of_coord):
    """
    :param file_name_of_coord coord file
    :type file_name_of_coord opened output file
    :return: np array
    """

    # this matrix includes series number: the first C
    result = pd.read_csv(file_name_of_coord, header=None, engine="pyarrow")
    coord = np.array(result)[:, 1:4]
    return coord


def vampire_moment_parser(mom_out_file):
    """
    This parser works vampire spin file
    """

    mom_output = pd.read_csv(
        mom_out_file,
        header=None,
        skiprows=1,
        sep="\s+",
    )
    mom_x = mom_output[0]
    mom_y = mom_output[1]
    mom_z = mom_output[2]
    mom_states_x = np.array(mom_x)
    mom_states_y = np.array(mom_y)
    mom_states_z = np.array(mom_z)
    return mom_states_x, mom_states_y, mom_states_z


def vampire_coord_parser(file_name_of_coord):
    """
    parsers for vampire coord file
    """

    # this matrix includes series number: the first C
    result = pd.read_csv(
        file_name_of_coord,
        header=None,
        skiprows=1,
        sep="\s+",
    )
    coord = np.array(result)[:, 2:]
    return coord


def system_size_uppasd_parser(inpasd_path):
    with open(inpasd_path, "r") as infile:
        lines = infile.readlines()
        for idx, line in enumerate(lines):
            line_data = line.rstrip("\n").split()
            if len(line_data) > 0:
                if line_data[0] == "ncell":
                    system_size_x = int(line_data[1])
                    system_size_y = int(line_data[2])
                    system_size_z = int(line_data[3])
                    break
    return system_size_x, system_size_y, system_size_z


def system_size_ovf_parser(ovfpath):
    with open(ovfpath, "r") as infile:
        lines = infile.readlines()
        stop_i = 0
        for idx, line in enumerate(lines):
            stop_i = stop_i + 1
            line_data = line.rstrip("\n")
            if len(line_data) > 0:
                if "# xnodes:" in line_data:
                    system_size_x = int(line_data.lstrip("# xnodes:"))
                if "# ynodes:" in line_data:
                    system_size_y = int(line_data.lstrip("# ynodes:"))
                if "# znodes:" in line_data:
                    system_size_z = int(line_data.lstrip("# znodes:"))
                if "# xstepsize:" in line_data:
                    gap_x = float(line_data.lstrip("# xstepsize:"))
                if "# ystepsize:" in line_data:
                    gap_y = float(line_data.lstrip("# ystepsize:"))
                if "# zstepsize:" in line_data:
                    gap_z = float(line_data.lstrip("# zstepsize:"))

            if stop_i == 200:
                break

    return system_size_x, system_size_y, system_size_z, gap_x, gap_y, gap_z


def parse_moment_and_coord_file(pyvista_LR, working_dir=os.getcwd()):
    # working path will not store in the databse, since we mostly want to use the current working path.
    coord_name = pyvista_LR.coord_name
    mom_name = (
        pyvista_LR.mom_name
    )  # We default to use the restart file, but when the mom_name changed in the WebUI or the CLI it will automatically use the given file.
    outputfile_type = pyvista_LR.outputfile_type

    if outputfile_type == "uppasd":
        """
        Highlight: now we suppose UppASD has no ovf file, but it could be changed in the future.
        """
        default_coord_path = glob.glob(
            os.path.abspath(os.path.join(working_dir, coord_name))
        )
        default_mom_path = glob.glob(
            os.path.abspath(os.path.join(working_dir, mom_name))
        )
        if default_coord_path[0][-4:] == ".out":
            coord = coord_file_parser(
                default_coord_path[0]
            )  # we use the first one that find
        elif default_coord_path[0][-4:] == ".csv":
            coord = coord_csv_parser(default_coord_path[0])
        else:
            raise Exception(
                "The UppASD coord file should be either .out or .csv.  If this is a first running, please check if restart file or coord file is in the working directory. If not, please check the path in the database."
            )

        if default_mom_path[0][-4:] == ".out":
            mom_states_x, mom_states_y, mom_states_z, magnitudes = moment_out_parser(
                default_mom_path[0]
            )
        elif default_mom_path[0][-4:] == ".csv":
            mom_states_x, mom_states_y, mom_states_z, magnitudes = moment_csv_parser(
                default_mom_path[0]
            )
        else:
            raise Exception(
                "The UppASD coord file should be either .out or .csv.  If this is a first running, please check if restart file or coord file is in the working directory. If not, please check the path in the database."
            )

    elif outputfile_type == "ovf":
        default_mom_path_list = glob.glob(
            os.path.abspath(os.path.join(working_dir, mom_name + "*.ovf"))
        )

        if len(default_mom_path_list) == 1:
            mom_states_x, mom_states_y, mom_states_z, coord = ovf_spirit_parser(
                default_mom_path_list[0]
            )
        else:
            mom_states_x, mom_states_y, mom_states_z, coord = ovf_spirit_parser(
                default_mom_path_list[0]
            )
            for i in range(1, len(default_mom_path_list)):
                (
                    mom_states_x_temp,
                    mom_states_y_temp,
                    mom_states_z_temp,
                    coord_temp,
                ) = ovf_spirit_parser(default_mom_path_list[i])
                mom_states_x = np.concatenate((mom_states_x, mom_states_x_temp))
                mom_states_y = np.concatenate((mom_states_y, mom_states_y_temp))
                mom_states_z = np.concatenate((mom_states_z, mom_states_z_temp))
        magnitudes = np.ones(len(mom_states_z))
    elif outputfile_type == "vampire":
        default_mom_path_list = glob.glob(
            os.path.abspath(os.path.join(working_dir, mom_name + "*.data"))
        )
        default_coord_path = glob.glob(
            os.path.abspath(os.path.join(working_dir, "*coords.data"))
        )
        if len(default_mom_path_list) == 1:
            coord = vampire_coord_parser(
                default_coord_path[0]
            )  # we use the first one that find
            mom_states_x, mom_states_y, mom_states_z = vampire_moment_parser(
                default_mom_path_list[0]
            )
        else:
            coord = vampire_coord_parser(
                default_coord_path[0]
            )  # we use the first one that find
            mom_states_x, mom_states_y, mom_states_z = vampire_moment_parser(
                default_mom_path_list[0]
            )
            for i in range(1, len(default_mom_path_list)):
                (
                    mom_states_x_temp,
                    mom_states_y_temp,
                    mom_states_z_temp,
                ) = vampire_moment_parser(default_mom_path_list[i])

                mom_states_x = np.concatenate((mom_states_x, mom_states_x_temp))
                mom_states_y = np.concatenate((mom_states_y, mom_states_y_temp))
                mom_states_z = np.concatenate((mom_states_z, mom_states_z_temp))
        magnitudes = np.ones(len(mom_states_z))
    else:
        raise Exception(
            "Current outputfile_type support UppASD, vampire(partly) and .ovf, more is coming soon"
        )

    return coord, mom_states_x, mom_states_y, mom_states_z, magnitudes


def parse_moment_and_coord_file1(pyvista_LR, working_dir=os.getcwd()):
    # working path will not store in the databse, since we mostly want to use the current working path.
    coord_name = pyvista_LR.coord_name
    mom_name = (
        pyvista_LR.mom_name1
    )  # We default to use the restart file, but when the mom_name changed in the WebUI or the CLI it will automatically use the given file.
    outputfile_type = pyvista_LR.outputfile_type

    if outputfile_type == "uppasd":
        """
        Highlight: now we suppose UppASD has no ovf file, but it could be changed in the future.
        """
        default_coord_path = glob.glob(
            os.path.abspath(os.path.join(working_dir, coord_name))
        )
        default_mom_path = glob.glob(
            os.path.abspath(os.path.join(working_dir, mom_name))
        )
        if default_coord_path[0][-4:] == ".out":
            coord = coord_file_parser(
                default_coord_path[0]
            )  # we use the first one that find
        elif default_coord_path[0][-4:] == ".csv":
            coord = coord_csv_parser(default_coord_path[0])
        else:
            raise Exception(
                "The UppASD coord file should be either .out or .csv.  If this is a first running, please check if restart file or coord file is in the working directory. If not, please check the path in the database."
            )

        if default_mom_path[0][-4:] == ".out":
            mom_states_x, mom_states_y, mom_states_z, magnitudes = moment_out_parser(
                default_mom_path[0]
            )
        elif default_mom_path[0][-4:] == ".csv":
            mom_states_x, mom_states_y, mom_states_z, magnitudes = moment_csv_parser(
                default_mom_path[0]
            )
        else:
            raise Exception(
                "The UppASD coord file should be either .out or .csv.  If this is a first running, please check if restart file or coord file is in the working directory. If not, please check the path in the database."
            )

    elif outputfile_type == "ovf":
        default_mom_path_list = glob.glob(
            os.path.abspath(os.path.join(working_dir, mom_name + "*.ovf"))
        )

        if len(default_mom_path_list) == 1:
            mom_states_x, mom_states_y, mom_states_z, coord = ovf_spirit_parser(
                default_mom_path_list[0]
            )
        else:
            mom_states_x, mom_states_y, mom_states_z, coord = ovf_spirit_parser(
                default_mom_path_list[0]
            )
            for i in range(1, len(default_mom_path_list)):
                (
                    mom_states_x_temp,
                    mom_states_y_temp,
                    mom_states_z_temp,
                    coord_temp,
                ) = ovf_spirit_parser(default_mom_path_list[i])
                mom_states_x = np.concatenate((mom_states_x, mom_states_x_temp))
                mom_states_y = np.concatenate((mom_states_y, mom_states_y_temp))
                mom_states_z = np.concatenate((mom_states_z, mom_states_z_temp))
        magnitudes = np.ones(len(mom_states_z))
    elif outputfile_type == "vampire":
        default_mom_path_list = glob.glob(
            os.path.abspath(os.path.join(working_dir, mom_name + "*.data"))
        )
        default_coord_path = glob.glob(
            os.path.abspath(os.path.join(working_dir, "*coords.data"))
        )
        if len(default_mom_path_list) == 1:
            coord = vampire_coord_parser(
                default_coord_path[0]
            )  # we use the first one that find
            mom_states_x, mom_states_y, mom_states_z = vampire_moment_parser(
                default_mom_path[0]
            )
        else:
            coord = vampire_coord_parser(
                default_coord_path[0]
            )  # we use the first one that find
            mom_states_x, mom_states_y, mom_states_z = vampire_moment_parser(
                default_mom_path[0]
            )
            for i in range(1, len(default_mom_path_list)):
                (
                    mom_states_x_temp,
                    mom_states_y_temp,
                    mom_states_z_temp,
                ) = vampire_moment_parser(default_mom_path_list[i])

                mom_states_x = np.concatenate((mom_states_x, mom_states_x_temp))
                mom_states_y = np.concatenate((mom_states_y, mom_states_y_temp))
                mom_states_z = np.concatenate((mom_states_z, mom_states_z_temp))
        magnitudes = np.ones(len(mom_states_z))
    else:
        raise Exception(
            "Current outputfile_type support UppASD, vampire(partly) and .ovf, more is coming soon"
        )

    return coord, mom_states_x, mom_states_y, mom_states_z, magnitudes


def parse_moment_and_coord_file2(pyvista_LR, working_dir=os.getcwd()):
    # working path will not store in the databse, since we mostly want to use the current working path.
    coord_name = pyvista_LR.coord_name
    mom_name = (
        pyvista_LR.mom_name2
    )  # We default to use the restart file, but when the mom_name changed in the WebUI or the CLI it will automatically use the given file.
    outputfile_type = pyvista_LR.outputfile_type

    if outputfile_type == "uppasd":
        """
        Highlight: now we suppose UppASD has no ovf file, but it could be changed in the future.
        """
        default_coord_path = glob.glob(
            os.path.abspath(os.path.join(working_dir, coord_name))
        )
        default_mom_path = glob.glob(
            os.path.abspath(os.path.join(working_dir, mom_name))
        )
        if default_coord_path[0][-4:] == ".out":
            coord = coord_file_parser(
                default_coord_path[0]
            )  # we use the first one that find
        elif default_coord_path[0][-4:] == ".csv":
            coord = coord_csv_parser(default_coord_path[0])
        else:
            raise Exception(
                "The UppASD coord file should be either .out or .csv.  If this is a first running, please check if restart file or coord file is in the working directory. If not, please check the path in the database."
            )

        if default_mom_path[0][-4:] == ".out":
            mom_states_x, mom_states_y, mom_states_z, magnitudes = moment_out_parser(
                default_mom_path[0]
            )
        elif default_mom_path[0][-4:] == ".csv":
            mom_states_x, mom_states_y, mom_states_z, magnitudes = moment_csv_parser(
                default_mom_path[0]
            )
        else:
            raise Exception(
                "The UppASD coord file should be either .out or .csv.  If this is a first running, please check if restart file or coord file is in the working directory. If not, please check the path in the database."
            )

    elif outputfile_type == "ovf":
        default_mom_path_list = glob.glob(
            os.path.abspath(os.path.join(working_dir, mom_name + "*.ovf"))
        )

        if len(default_mom_path_list) == 1:
            mom_states_x, mom_states_y, mom_states_z, coord = ovf_spirit_parser(
                default_mom_path_list[0]
            )
        else:
            mom_states_x, mom_states_y, mom_states_z, coord = ovf_spirit_parser(
                default_mom_path_list[0]
            )
            for i in range(1, len(default_mom_path_list)):
                (
                    mom_states_x_temp,
                    mom_states_y_temp,
                    mom_states_z_temp,
                    coord_temp,
                ) = ovf_spirit_parser(default_mom_path_list[i])
                mom_states_x = np.concatenate((mom_states_x, mom_states_x_temp))
                mom_states_y = np.concatenate((mom_states_y, mom_states_y_temp))
                mom_states_z = np.concatenate((mom_states_z, mom_states_z_temp))
        magnitudes = np.ones(len(mom_states_z))
    elif outputfile_type == "vampire":
        default_mom_path_list = glob.glob(
            os.path.abspath(os.path.join(working_dir, mom_name + "*.data"))
        )
        default_coord_path = glob.glob(
            os.path.abspath(os.path.join(working_dir, "*coords.data"))
        )
        if len(default_mom_path_list) == 1:
            coord = vampire_coord_parser(
                default_coord_path[0]
            )  # we use the first one that find
            mom_states_x, mom_states_y, mom_states_z = vampire_moment_parser(
                default_mom_path[0]
            )
        else:
            coord = vampire_coord_parser(
                default_coord_path[0]
            )  # we use the first one that find
            mom_states_x, mom_states_y, mom_states_z = vampire_moment_parser(
                default_mom_path[0]
            )
            for i in range(1, len(default_mom_path_list)):
                (
                    mom_states_x_temp,
                    mom_states_y_temp,
                    mom_states_z_temp,
                ) = vampire_moment_parser(default_mom_path_list[i])

                mom_states_x = np.concatenate((mom_states_x, mom_states_x_temp))
                mom_states_y = np.concatenate((mom_states_y, mom_states_y_temp))
                mom_states_z = np.concatenate((mom_states_z, mom_states_z_temp))
        magnitudes = np.ones(len(mom_states_z))
    else:
        raise Exception(
            "Current outputfile_type support UppASD, vampire(partly) and .ovf, more is coming soon"
        )

    return coord, mom_states_x, mom_states_y, mom_states_z, magnitudes


def parse_moment_and_coord_file3(pyvista_LR, working_dir=os.getcwd()):
    # working path will not store in the databse, since we mostly want to use the current working path.
    coord_name = pyvista_LR.coord_name
    mom_name = (
        pyvista_LR.mom_name3
    )  # We default to use the restart file, but when the mom_name changed in the WebUI or the CLI it will automatically use the given file.
    outputfile_type = pyvista_LR.outputfile_type

    if outputfile_type == "uppasd":
        """
        Highlight: now we suppose UppASD has no ovf file, but it could be changed in the future.
        """
        default_coord_path = glob.glob(
            os.path.abspath(os.path.join(working_dir, coord_name))
        )
        default_mom_path = glob.glob(
            os.path.abspath(os.path.join(working_dir, mom_name))
        )
        if default_coord_path[0][-4:] == ".out":
            coord = coord_file_parser(
                default_coord_path[0]
            )  # we use the first one that find
        elif default_coord_path[0][-4:] == ".csv":
            coord = coord_csv_parser(default_coord_path[0])
        else:
            raise Exception(
                "The UppASD coord file should be either .out or .csv.  If this is a first running, please check if restart file or coord file is in the working directory. If not, please check the path in the database."
            )

        if default_mom_path[0][-4:] == ".out":
            mom_states_x, mom_states_y, mom_states_z, magnitudes = moment_out_parser(
                default_mom_path[0]
            )
        elif default_mom_path[0][-4:] == ".csv":
            mom_states_x, mom_states_y, mom_states_z, magnitudes = moment_csv_parser(
                default_mom_path[0]
            )
        else:
            raise Exception(
                "The UppASD coord file should be either .out or .csv.  If this is a first running, please check if restart file or coord file is in the working directory. If not, please check the path in the database."
            )

    elif outputfile_type == "ovf":
        default_mom_path_list = glob.glob(
            os.path.abspath(os.path.join(working_dir, mom_name + "*.ovf"))
        )

        if len(default_mom_path_list) == 1:
            mom_states_x, mom_states_y, mom_states_z, coord = ovf_spirit_parser(
                default_mom_path_list[0]
            )
        else:
            mom_states_x, mom_states_y, mom_states_z, coord = ovf_spirit_parser(
                default_mom_path_list[0]
            )
            for i in range(1, len(default_mom_path_list)):
                (
                    mom_states_x_temp,
                    mom_states_y_temp,
                    mom_states_z_temp,
                    coord_temp,
                ) = ovf_spirit_parser(default_mom_path_list[i])
                mom_states_x = np.concatenate((mom_states_x, mom_states_x_temp))
                mom_states_y = np.concatenate((mom_states_y, mom_states_y_temp))
                mom_states_z = np.concatenate((mom_states_z, mom_states_z_temp))
        magnitudes = np.ones(len(mom_states_z))
    elif outputfile_type == "vampire":
        default_mom_path_list = glob.glob(
            os.path.abspath(os.path.join(working_dir, mom_name + "*.data"))
        )
        default_coord_path = glob.glob(
            os.path.abspath(os.path.join(working_dir, "*coords.data"))
        )
        if len(default_mom_path_list) == 1:
            coord = vampire_coord_parser(
                default_coord_path[0]
            )  # we use the first one that find
            mom_states_x, mom_states_y, mom_states_z = vampire_moment_parser(
                default_mom_path[0]
            )
        else:
            coord = vampire_coord_parser(
                default_coord_path[0]
            )  # we use the first one that find
            mom_states_x, mom_states_y, mom_states_z = vampire_moment_parser(
                default_mom_path[0]
            )
            for i in range(1, len(default_mom_path_list)):
                (
                    mom_states_x_temp,
                    mom_states_y_temp,
                    mom_states_z_temp,
                ) = vampire_moment_parser(default_mom_path_list[i])

                mom_states_x = np.concatenate((mom_states_x, mom_states_x_temp))
                mom_states_y = np.concatenate((mom_states_y, mom_states_y_temp))
                mom_states_z = np.concatenate((mom_states_z, mom_states_z_temp))
        magnitudes = np.ones(len(mom_states_z))
    else:
        raise Exception(
            "Current outputfile_type support UppASD, vampire(partly) and .ovf, more is coming soon"
        )

    return coord, mom_states_x, mom_states_y, mom_states_z, magnitudes


def system_size_reader(pyvista_LR, working_dir=os.getcwd()):
    if pyvista_LR.outputfile_type == "uppasd":
        # we try to read the inpsd.dat file to get the system size
        inpasd_path = glob.glob(os.path.abspath(os.path.join(working_dir, "inpsd.dat")))
        if inpasd_path == []:
            raise Exception("The inpsd.dat file is not found, please check the path.")
        else:
            system_size_x, system_size_y, system_size_z = system_size_uppasd_parser(
                inpasd_path[0]
            )
            pyvista_LR.system_size = (system_size_x, system_size_y, system_size_z)
        # since the UppASD file are not rec mesh, we set the rec mesh to be 1,1,1 here.
        # Will update if needed.
        pyvista_LR.rectrangle_spacing = (1, 1, 1)
    if pyvista_LR.outputfile_type == "ovf":
        ovfpath = glob.glob(
            os.path.abspath(os.path.join(working_dir, pyvista_LR.ovf_name))
        )
        if ovfpath == []:
            raise Exception("The ovf file is not found, please check the path.")
        else:
            (
                system_size_x,
                system_size_y,
                system_size_z,
                gap_x,
                gap_y,
                gap_z,
            ) = system_size_ovf_parser(ovfpath[0])

            pyvista_LR.system_size = (system_size_x, system_size_y, system_size_z)

        # normalize the distance, since ovf user want to use different unit, e.g., nm, um, even m!!!!
        normal_helper = min(gap_x, gap_y, gap_z)
        gap_x = gap_x / normal_helper
        gap_y = gap_y / normal_helper
        gap_z = gap_z / normal_helper
        pyvista_LR.rectrangle_spacing = (gap_x, gap_y, gap_z)
