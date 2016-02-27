from pyanaconda.installclasses.korora import KororaBaseInstallClass


class KororaWorkstationInstallClass(KororaBaseInstallClass):
    name = "Korora"
    stylesheet = "/usr/share/anaconda/korora-workstation.css"
    defaultPackageEnvironment = "workstation-product-environment"
