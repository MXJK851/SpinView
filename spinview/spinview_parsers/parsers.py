import pandas as pd
import numpy as np
import os
import glob
import struct


import numpy as np
import re


"""
Spirit output file parser
"""


# def Ovf_file_checking(filename):
#     with open(filename, "rb") as f:
#         chunk = f.read(10240)
#     return b"\0" in chunk


def ovf_spirit_parser(OVF_file_name):
    """
    Parser for the OVF file
    Test with Spirit code output OVF file
    """
    try:
        # this case it is a ascii file
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
    except:
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
        with open(OVF_file_name, "rb") as f:
            while True:
                line = f.readline().strip()
                if line == b"# Begin: Data Binary 4":
                    break
                else:
                    for name in list_ovf_key:
                        if line.decode("ascii").lstrip().startswith(name):
                            dict_ovf_keys[name.lstrip("# ").rstrip(":")] = float(
                                line.decode("ascii").lstrip(name)
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
        #  @MathieuMoalic from https://github.com/MathieuMoalic
        #  Qichen Thanks MathieuMoalic for sharing the code to parse the binary ovf file. Cheers!
        #  Now it should works.
        with open(OVF_file_name, "rb") as f:
            dims = np.array([0, 0, 0, 0])
            while True:
                line = f.readline().strip().decode("ASCII")
                if "valuedim" in line:
                    dims[3] = int(line.split(" ")[-1])
                if "xnodes" in line:
                    dims[2] = int(line.split(" ")[-1])
                if "ynodes" in line:
                    dims[1] = int(line.split(" ")[-1])
                if "znodes" in line:
                    dims[0] = int(line.split(" ")[-1])
                if "Begin: Data" in line:
                    break
            count = int(dims[0] * dims[1] * dims[2] * dims[3] + 1)
            moment = np.fromfile(f, "<f4", count=count)[1:].reshape(dims)
        mom_states_x = moment[:, :, :, 0].flatten()
        mom_states_y = moment[:, :, :, 1].flatten()
        mom_states_z = moment[:, :, :, 2].flatten()

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


def parse_Excalibur_bin_to_numpy(filename):
    """
    Parse a binary-output from the Excalibur code into numpy array.

    The binary file should contain a sequence of 64-bit floats,
    organized as triplets (mx, my, mz) for each point in a 3D grid.
    The dimensions of the grid are extracted from the filename,
    which should be in the format '..._3xNxMxL.bin'.

    The full description of this code can be find in Phillip's nature physics paper:
    https://www-nature-com.focus.lib.kth.se/articles/s41567-022-01638-4
    or directly in the zenodo repo here:
    https://zenodo.org/records/5930353
    You can find the node file in the zenodo repo, which is the description file for output file.

    Parameters:
    filename (str): The name of the binary file to parse.

    Returns:
    numpy.ndarray: A 4D array with shape (3, N, M, L), where the first
    dimension represents the component (0=mx, 1=my, 2=mz) and the other
    three dimensions represent the position in the grid.

    Raises:
    ValueError: If the dimensions cannot be extracted from the filename.


    """
    match = re.search(r"(\d+)x(\d+)x(\d+)x(\d+)", filename)
    if match is None:
        raise ValueError("Could not extract dimensions from filename")
    d, x, y, z = map(int, match.groups())
    mom_output = np.fromfile(filename, dtype=np.double)
    mom_output = mom_output.reshape(x, y, z, d)

    mom_x = mom_output[:, :, :, 0].flatten()
    mom_y = mom_output[:, :, :, 1].flatten()
    mom_z = mom_output[:, :, :, 2].flatten()
    mom_states_x = np.array(mom_x).astype(np.float32)
    mom_states_y = np.array(mom_y).astype(np.float32)
    mom_states_z = np.array(mom_z).astype(np.float32)

    X, Y, Z = np.mgrid[0:x:1, 0:y:1, 0:z:1]
    x_c = (X.flatten(order="F").astype(np.float32),)
    y_c = (Y.flatten(order="F").astype(np.float32),)
    z_c = (Z.flatten(order="F").astype(np.float32),)
    coord = np.vstack([x_c, y_c, z_c]).T

    return mom_states_x, mom_states_y, mom_states_z, coord


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
    try:
        with open(ovfpath) as f:
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
    except:
        with open(ovfpath, "rb") as f:
            for line in f:
                line = line.strip()
                if line == b"# Begin: Data Binary 4":
                    break
                else:
                    for name in list_ovf_key:
                        if line.lstrip().decode("ascii").startswith(name):
                            dict_ovf_keys[name.lstrip("# ").rstrip(":")] = float(
                                line.decode("ascii").lstrip(name)
                            )
                    moment_start_index = moment_start_index + 1

    gap_x = dict_ovf_keys["xstepsize"]
    gap_y = dict_ovf_keys["ystepsize"]
    gap_z = dict_ovf_keys["zstepsize"]

    system_size_x = int(dict_ovf_keys["xnodes"])
    system_size_y = int(dict_ovf_keys["ynodes"])
    system_size_z = int(dict_ovf_keys["znodes"])

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
    elif outputfile_type == "Excalibur":
        default_mom_path_list = glob.glob(
            os.path.abspath(os.path.join(working_dir, mom_name + "*.bin"))
        )

        if len(default_mom_path_list) == 1:
            (
                mom_states_x,
                mom_states_y,
                mom_states_z,
                coord,
            ) = parse_Excalibur_bin_to_numpy(default_mom_path_list[0])
        else:
            (
                mom_states_x,
                mom_states_y,
                mom_states_z,
                coord,
            ) = parse_Excalibur_bin_to_numpy(default_mom_path_list[0])
            for i in range(1, len(default_mom_path_list)):
                (
                    mom_states_x_temp,
                    mom_states_y_temp,
                    mom_states_z_temp,
                    coord_temp,
                ) = parse_Excalibur_bin_to_numpy(default_mom_path_list[i])
                mom_states_x = np.concatenate((mom_states_x, mom_states_x_temp))
                mom_states_y = np.concatenate((mom_states_y, mom_states_y_temp))
                mom_states_z = np.concatenate((mom_states_z, mom_states_z_temp))
        magnitudes = np.ones(len(mom_states_z))
    else:
        raise Exception(
            " Make sure you execute SpinView in the simulation folder, if not you can change your current path to the simulation folder or add '--wp' combine with absoult path of your sumulation folder to 'spinview start'. Current outputfile_type support UppASD, vampire(partly) and .ovf, more is coming soon"
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
    elif outputfile_type == "Excalibur":
        default_mom_path_list = glob.glob(
            os.path.abspath(os.path.join(working_dir, mom_name + "*.bin"))
        )

        if len(default_mom_path_list) == 1:
            (
                mom_states_x,
                mom_states_y,
                mom_states_z,
                coord,
            ) = parse_Excalibur_bin_to_numpy(default_mom_path_list[0])
        else:
            (
                mom_states_x,
                mom_states_y,
                mom_states_z,
                coord,
            ) = parse_Excalibur_bin_to_numpy(default_mom_path_list[0])
            for i in range(1, len(default_mom_path_list)):
                (
                    mom_states_x_temp,
                    mom_states_y_temp,
                    mom_states_z_temp,
                    coord_temp,
                ) = parse_Excalibur_bin_to_numpy(default_mom_path_list[i])
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
    elif outputfile_type == "Excalibur":
        default_mom_path_list = glob.glob(
            os.path.abspath(os.path.join(working_dir, mom_name + "*.bin"))
        )

        if len(default_mom_path_list) == 1:
            (
                mom_states_x,
                mom_states_y,
                mom_states_z,
                coord,
            ) = parse_Excalibur_bin_to_numpy(default_mom_path_list[0])
        else:
            (
                mom_states_x,
                mom_states_y,
                mom_states_z,
                coord,
            ) = parse_Excalibur_bin_to_numpy(default_mom_path_list[0])
            for i in range(1, len(default_mom_path_list)):
                (
                    mom_states_x_temp,
                    mom_states_y_temp,
                    mom_states_z_temp,
                    coord_temp,
                ) = parse_Excalibur_bin_to_numpy(default_mom_path_list[i])
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
    elif outputfile_type == "Excalibur":
        default_mom_path_list = glob.glob(
            os.path.abspath(os.path.join(working_dir, mom_name + "*.bin"))
        )

        if len(default_mom_path_list) == 1:
            (
                mom_states_x,
                mom_states_y,
                mom_states_z,
                coord,
            ) = parse_Excalibur_bin_to_numpy(default_mom_path_list[0])
        else:
            (
                mom_states_x,
                mom_states_y,
                mom_states_z,
                coord,
            ) = parse_Excalibur_bin_to_numpy(default_mom_path_list[0])
            for i in range(1, len(default_mom_path_list)):
                (
                    mom_states_x_temp,
                    mom_states_y_temp,
                    mom_states_z_temp,
                    coord_temp,
                ) = parse_Excalibur_bin_to_numpy(default_mom_path_list[i])
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
    if pyvista_LR.outputfile_type == "Excalibur":
        default_mom_path_list = glob.glob(
            os.path.abspath(os.path.join(working_dir, "*.bin"))
        )
        filename = default_mom_path_list[0]
        # we try to read the inpsd.dat file to get the system size
        match = re.search(r"(\d+)x(\d+)x(\d+)x(\d+)", filename)
        if match is None:
            raise ValueError("Could not extract dimensions from filename")
        d, x, y, z = map(int, match.groups())
        pyvista_LR.system_size = (x, y, z)
        pyvista_LR.rectrangle_spacing = (1, 1, 1)
