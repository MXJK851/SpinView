import typer
from rich import print
from .main import webui_realspace
from typing_extensions import Annotated
from typing import Optional
from .spinview_utilities.profile_DB import check_profile, initial_profile
import os
import pathlib

welcome_words = f"""
            😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀
            😆                                😆
            😉       Welcome to [bold red]S[/bold red][#FFA500]p[/#FFA500][bold Yellow]i[/bold Yellow][bold green]n[/bold green][bold Blue]V[/bold Blue][bold green]i[/bold green][#FF1493]e[/#FF1493][bold Purple]w [/bold Purple]     😉
            😆                                😆
            😉        欢迎使用 [bold red]S[/bold red][#FFA500]p[/#FFA500][bold Yellow]i[/bold Yellow][bold green]n[/bold green][bold Blue]V[/bold Blue][bold green]i[/bold green][#FF1493]e[/#FF1493][bold Purple]w [/bold Purple]      😉 
            😆                                😆
            😉     Willkommen zu [bold red]S[/bold red][#FFA500]p[/#FFA500][bold Yellow]i[/bold Yellow][bold green]n[/bold green][bold Blue]V[/bold Blue][bold green]i[/bold green][#FF1493]e[/#FF1493][bold Purple]w [/bold Purple]    😉
            😆                                😆
            😉    Välkommen till [bold red]S[/bold red][#FFA500]p[/#FFA500][bold Yellow]i[/bold Yellow][bold green]n[/bold green][bold Blue]V[/bold Blue][bold green]i[/bold green][#FF1493]e[/#FF1493][bold Purple]w [/bold Purple]    😉
            😆                                😆
            😉      Bienvenue à [bold red]S[/bold red][#FFA500]p[/#FFA500][bold Yellow]i[/bold Yellow][bold green]n[/bold green][bold Blue]V[/bold Blue][bold green]i[/bold green][#FF1493]e[/#FF1493][bold Purple]w [/bold Purple]     😉
            😆                                😆
            😉      へようこそ [bold red]S[/bold red][#FFA500]p[/#FFA500][bold Yellow]i[/bold Yellow][bold green]n[/bold green][bold Blue]V[/bold Blue][bold green]i[/bold green][#FF1493]e[/#FF1493][bold Purple]w [/bold Purple]      😉
            😆                                😆
            😉      Bienvenido a [bold red]S[/bold red][#FFA500]p[/#FFA500][bold Yellow]i[/bold Yellow][bold green]n[/bold green][bold Blue]V[/bold Blue][bold green]i[/bold green][#FF1493]e[/#FF1493][bold Purple]w [/bold Purple]    😉
            😆                                😆
            😉   사용을 환영합니다 [bold red]S[/bold red][#FFA500]p[/#FFA500][bold Yellow]i[/bold Yellow][bold green]n[/bold green][bold Blue]V[/bold Blue][bold green]i[/bold green][#FF1493]e[/#FF1493][bold Purple]w [/bold Purple]  😉
            😆                                😆
            😉           @Qichen Xu           😉
            😆      -KTH Royal Institute      😆
            😉         of Technology          😉
            🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩🤩

         SpinView V1 Copyright (C) 2023  Qichen Xu
                            GPL V3
"""


spinview_cli = typer.Typer()


@spinview_cli.command()
def check_database(
    db_name: Annotated[
        Optional[str],
        typer.Option(
            metavar="📁database name",
            help="The path of the database file. If not specified, the default database will be used. which is (PATH of SpinView)/DB/default.db",
        ),
    ] = "default.db",
    table_name: Annotated[
        Optional[str],
        typer.Option(
            metavar="📙database table name",
            help="The name of the table that store all variables",
        ),
    ] = "Initial_profile",
):
    print(welcome_words)
    filepath = pathlib.Path(__file__).resolve().parent
    db_path = os.path.join(filepath, "DB")
    db_path = os.path.join(db_path, db_name)
    exist_table_in_db = check_profile(db_path=db_path)
    print(
        "[bold red]S[/bold red][#FFA500]p[/#FFA500][bold Yellow]i[/bold Yellow][bold green]n[/bold green][bold Blue]V[/bold Blue][bold green]i[/bold green][#FF1493]e[/#FF1493][bold Purple]w [/bold Purple] database include following tables: \n"
    )
    for i in exist_table_in_db:
        print("[green]{}[/green] \n".format(i[0]))


@spinview_cli.command()
def initial_database():
    print(welcome_words)
    filepath = pathlib.Path(__file__).resolve().parent
    db_path = os.path.join(filepath, "DB")
    db_path = os.path.join(db_path, "default.db")
    # print(db_path)
    try:
        os.remove(db_path)
    except:
        print("Can not delete exist database, please check if the database is in use")
    initial_profile(
        db_path=db_path,
        table_name="Initial_profile",
        table_name_store="Initial_profile_store",
    )
    print(
        "[bold red]S[/bold red][#FFA500]p[/#FFA500][bold Yellow]i[/bold Yellow][bold green]n[/bold green][bold Blue]V[/bold Blue][bold green]i[/bold green][#FF1493]e[/#FF1493][bold Purple]w [/bold Purple] database initialized with table named 'Initial_profile'"
    )


@spinview_cli.command()
def start(
    dn: Annotated[
        Optional[str],
        typer.Option(
            metavar="📁database name",
            help="The path of the database file. If not specified, the default database will be used. which is (PATH of SpinView)/DB/default.db",
        ),
    ] = "default.db",
    tn: Annotated[
        Optional[str],
        typer.Option(
            metavar="📙database table name",
            help="The name of the table that store all variables",
        ),
    ] = "Initial_profile",
    ft: Annotated[
        Optional[str],
        typer.Option(
            metavar="📜file type",
            help="Currently, SpinView support .out(UppASD) .data(Vampire, partly support)and non-binary .ovf(Spirit,Mumax3,OOMMF), choose from ['auto','uppasd', 'vampire', and, 'ovf']",
        ),
    ] = "auto",
    wp: Annotated[
        Optional[str],
        typer.Option(
            metavar="🧭Path of the working folder that store simulation file",
            help=" 1. For UppASD it must includes inpsd.dat, coord file and moments file. 2. for OVF files, different trajectorys must have different names, e.g., (trajectory 1) skyrmions0001.ovf, skyrmions0002.ovf, skyrmions0003.ovf,(trajectory 2) ss0001.ovf,ss0002.ovf,ss0003.ovf",
        ),
    ] = None,
    hi: Annotated[
        Optional[str],
        typer.Option(
            metavar="🌐Host IP",
            help="Enter your IP address to activate the server for online device visit. If you are using localhost, use 'localhost' ",
        ),
    ] = "localhost",
    ucm: Annotated[
        Optional[str],
        typer.Option(
            metavar="😝UI contol model",
            help="Choose the control model of the UI, currently, SpinView support client, trame, or server (Same as Pyvista))",
        ),
    ] = "trame",
    tem: Annotated[
        Optional[str],
        typer.Option(
            metavar="🚀Execution mode",
            help="Choose the Trame model from main and desktop, main means webui and desktop using a pywebview container",
        ),
    ] = "main",
    sf: Annotated[
        Optional[int],
        typer.Option(
            metavar="📖Subframe number",
            help="Choose subframe numbers, SpinView currently support maximum to 4 subframes in comparison mode",
        ),
    ] = 1,
    pn: Annotated[
        Optional[int],
        typer.Option(
            metavar="port number",
            help="the port number, it should be different when you are using different SpinView instances",
        ),
    ] = 9000,
    pwx: Annotated[
        Optional[int],
        typer.Option(
            metavar="📏Pywebview container windows length",
            help="Set the SpinView desktop mode windows size length",
        ),
    ] = 1920,
    pwy: Annotated[
        Optional[int],
        typer.Option(
            metavar="📏Pywebview container windows heigth",
            help="Set the SpinView desktop mode windows size heigth",
        ),
    ] = 1080,
    psr: Annotated[
        Optional[int],
        typer.Option(
            metavar="🖐️Pyvista still ratio",
            help="The image quality in server mode when no operations take, currently we only support > 1 value when using server mode. Recommand to use 0.1 when only use the VTKjs model, not that VTKjs model needs manuel reload when function not works properly",
        ),
    ] = 1,
    pir: Annotated[
        Optional[int],
        typer.Option(
            metavar="👋Pyvista interactive ratio",
            help="The image quality in server mode during operations, currently we only support > 1 value when using server mode.  Recommand to use 0.1 when only use the VTKjs model, not that VTKjs model needs manuel reload when function not works properly",
        ),
    ] = 1,
    tom: Annotated[
        Optional[bool],
        typer.Option(
            metavar="💻Auto open browser",
            help="Auto open the brower with the IP address, but it will gives a no related suggestion when activate.",
        ),
    ] = False,
):
    print(welcome_words)
    print(
        "Using ctrl + C to stop [bold red]S[/bold red][#FFA500]p[/#FFA500][bold Yellow]i[/bold Yellow][bold green]n[/bold green][bold Blue]V[/bold Blue][bold green]i[/bold green][#FF1493]e[/#FF1493][bold Purple]w [/bold Purple]"
    )
    print("\n")
    if tom == False and tem == "main":
        print(
            "[green]Using ctrl(windows)/cmd(macos) + left click the IP address below to open your browser or type the IP address into your browser [/green]"
        )

    webui_realspace(
        db_name=dn,
        table_name=tn,
        subframes=sf,
        file_type=ft,
        port_number=pn,
        trame_host=hi,
        ui_control_model=ucm,
        trame_exec_mode=tem,
        trame_open_browser=tom,
        pywebview_windows_size_x=pwx,
        pywebview_windows_size_y=pwy,
        path_from_user=wp,
        pyvista_still_ratio=psr,
        pyvista_interactive_ratio=pir,
    )

    print(
        "[bold red]S[/bold red][#FFA500]p[/#FFA500][bold Yellow]i[/bold Yellow][bold green]n[/bold green][bold Blue]V[/bold Blue][bold green]i[/bold green][#FF1493]e[/#FF1493][bold Purple]w [/bold Purple] stopped"
    )


if __name__ == "__main__":
    spinview_cli()
