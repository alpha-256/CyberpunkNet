import math
import sys
from time import sleep as delay
from functionset import functions

class loadingAnim:
    def menuAnimLoad():
        print("            ______      __                                __   _   __     __ ")
        delay(0.3)
        print("           / ______  __/ /_  ___  _________  __  ______  / /__/ | / ___  / /_")
        delay(0.3)
        print("          / /   / / / / __ \/ _ \/ ___/ __ \/ / / / __ \/ //_/  |/ / _ \/ __/")
        delay(0.3)
        print("         / /___/ /_/ / /_/ /  __/ /  / /_/ / /_/ / / / / ,< / /|  /  __/ /_  ")
        delay(0.3)
        print("         \____/\__, /_.___/\___/_/  / .___/\__,_/_/ /_/_/|_/_/ |_/\___/\__/  ")
        delay(0.3)
        print("              /____/               /_/                                       ")
        functions.clearTerm()

        animRepeat = 1
        while animRepeat < 3 :
            print("            ______      __                                __   _   __     __ ")
            print("           / ______  __/ /_  ___  _________  __  ______  / /__/ | / ___  / /_")
            print("          / /   / / / / __ \/ _ \/ ___/ __ \/ / / / __ \/ //_/  |/ / _ \/ __/")
            print("         / /___/ /_/ / /_/ /  __/ /  / /_/ / /_/ / / / / ,< / /|  /  __/ /_  ")
            print("         \____/\__, /_.___/\___/_/  / .___/\__,_/_/ /_/_/|_/_/ |_/\___/\__/  ")
            print("              /____/               /_/                                       ")
            functions.spacing8()
            delay(0.3)
            functions.clearTerm()
            delay(0.3)
            animRepeat = animRepeat + 1

        print("            ______      __                                __   _   __     __ ")
        print("           / ______  __/ /_  ___  _________  __  ______  / /__/ | / ___  / /_")
        print("          / /   / / / / __ \/ _ \/ ___/ __ \/ / / / __ \/ //_/  |/ / _ \/ __/")
        print("         / /___/ /_/ / /_/ /  __/ /  / /_/ / /_/ / / / / ,< / /|  /  __/ /_  ")
        print("         \____/\__, /_.___/\___/_/  / .___/\__,_/_/ /_/_/|_/_/ |_/\___/\__/  ")
        print("              /____/               /_/                                       ")


        functions.spacing8()
        print("loading operting system...")
        functions.progressBar()
        delay(1)
        functions.spacing8()
        functions.clearTerm()
        print("██╗    ██╗    ███████╗    ██╗          ██████╗     ██████╗     ███╗   ███╗    ███████╗")
        print("██║    ██║    ██╔════╝    ██║         ██╔════╝    ██╔═══██╗    ████╗ ████║    ██╔════╝")
        print("██║ █╗ ██║    █████╗      ██║         ██║         ██║   ██║    ██╔████╔██║    █████╗  ")
        print("██║███╗██║    ██╔══╝      ██║         ██║         ██║   ██║    ██║╚██╔╝██║    ██╔══╝  ")
        print("╚███╔███╔╝    ███████╗    ███████╗    ╚██████╗    ╚██████╔╝    ██║ ╚═╝ ██║    ███████╗")
        print(" ╚══╝╚══╝     ╚══════╝    ╚══════╝     ╚═════╝     ╚═════╝     ╚═╝     ╚═╝    ╚══════╝")
        print("")
        print("████████╗ ██████╗")
        print("╚══██╔══╝██╔═══██╗")
        print("   ██║   ██║   ██║")
        print("   ██║   ██║   ██║")
        print("   ██║   ╚██████╔╝")
        print("   ╚═╝    ╚═════╝ ")

        print(" @@@@@@@  @@@ @@@  @@@@@@@   @@@@@@@@  @@@@@@@   @@@@@@@   @@@  @@@  @@@  @@@  @@@  @@@    @@@  @@@  @@@@@@@@  @@@@@@@  ")
        print("@@@@@@@@  @@@ @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@ @@@  @@@  @@@    @@@@ @@@  @@@@@@@@  @@@@@@@  ")
        print("!@@       @@! !@@  @@!  @@@  @@!       @@!  @@@  @@!  @@@  @@!  @@@  @@!@!@@@  @@!  !@@    @@!@!@@@  @@!         @@!    ")
        print("!@!       !@! @!!  !@   @!@  !@!       !@!  @!@  !@!  @!@  !@!  @!@  !@!!@!@!  !@!  @!!    !@!!@!@!  !@!         !@!    ")
        print("!@!        !@!@!   @!@!@!@   @!!!:!    @!@!!@!   @!@@!@!   @!@  !@!  @!@ !!@!  @!@@!@!     @!@ !!@!  @!!!:!      @!!    ")
        print("!!!         @!!!   !!!@!!!!  !!!!!:    !!@!@!    !!@!!!    !@!  !!!  !@!  !!!  !!@!!!      !@!  !!!  !!!!!:      !!!    ")
        print(":!!         !!:    !!:  !!!  !!:       !!: :!!   !!:       !!:  !!!  !!:  !!!  !!: :!!     !!:  !!!  !!:         !!:    ")
        print(":!:         :!:    :!:  !:!  :!:       :!:  !:!  :!:       :!:  !:!  :!:  !:!  :!:  !:!    :!:  !:!  :!:         :!:    ")
        print(" ::: :::     ::     :: ::::   :: ::::  ::   :::   ::       ::::: ::   ::   ::   ::  :::    ::   ::   :: ::::     ::    ")
        print(" :: :: :     :     :: : ::   : :: ::    :   : :   :         : :  :   ::    :    :   :::    ::    :   : :: ::      :     ")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
        print("\n")
