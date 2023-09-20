
# Help functions


## Main help function:

## 1. To get help on the main function use the following command: 

<div class="termy">
```console
$ spinview --help

╭─ Options ────────────────────────────────────╮
│ --install-comple…       Install           │
│                         completion for    │
│                         the current       │
│                         shell.            │
│ --show-completion       Show completion   │
│                         for the current   │
│                         shell, to copy it │
│                         or customize the  │
│                         installation.     │
│ --help                  Show this message │
│                         and exit.         │
╰───────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────╮
│ check-database                            │
│ initial-database                          │
│ start                                     │
╰───────────────────────────────────────────────╯
```
</div>


## 2. Help function of each command:

### 1. Help function of `check-database`, the `.......` in the content is used for replace the real help content.
<div class="termy">
```console
$  spinview check-database --help


 Usage: spinview check-database
            [OPTIONS]
╭─ Options ────────────────────────────────────╮
│ --db-name        📁database        .......│
│                  name              .......│
│ --table-name     📙database        .......│
│                  table name        .......│
│ --help                             .......│
╰───────────────────────────────────────────────╯
```
</div>
### 2. Help function of `initial-database`.

<div class="termy">
```console
$  spinview initial-database --help


 Usage: spinview initial-database
            [OPTIONS]

╭─ Options ────────────────────────────────────╮
│ --help       Show this message and exit.  │
╰──────────────────────────────────────────────╯
```
</div>
### 3. Help function of `start`.

<div class="termy">
```console
$  spinview start --help


 Usage: spinview start
            [OPTIONS]
╭─ Options ────────────────────────────────────╮
│ --dn               📁database  ...........│
│                    name        ...........│
│ --tn               📙database  ...........│
│                    table name  ...........│
│ --ft               📜file      ...........│
│                    type        ...........│
│ --wp               🧭Path of   ...........│
│                    the         ...........│
│                    working     ...........│
│                    folder      ...........│
│                    that store  ...........│
│                    simulation  ...........│
│                    file        ...........│
│ --hi               🌐Host IP   ...........│
│ --ucm              😝UI        ...........│
│                    contol      ...........│
│                    model       ...........│
│ --tem              🚀Executio  ...........│
│                     mode       ...........│
│ --sf               📖Subframe  ...........│
│                    number      ...........│
│ --pn               port        ...........│
│                    number      ...........│
│ --pwx              📏Pywebvie  ...........│
│                                ...........│
│                    container   ...........│
│                    windows     ...........│
│                    length      ...........│
│ --pwy              📏Pywebvie  ...........│
│                                ...........│
│                    container   ...........│
│                    windows     ...........│
│                    heigth      ...........│
│ --psr              🖐️Pyvista   ........... │
│                    still       ...........│
│                    ratio       ...........│
│ --pir              👋Pyvista   ...........│
│                    interactiv  ...........│
│                    e ratio     ...........│
│                                ...........│
│ --tom  --no-tom    💻Auto      ...........│
│                    open        ...........│
│                    browser     ...........│
│                                ...........│
│ --help                         ...........│
╰──────────────────────────────────────────────╯

```
</div>

