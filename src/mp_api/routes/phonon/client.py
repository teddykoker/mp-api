from mp_api.core.client import BaseRester
from mp_api.routes.phonon.models import PhononBSDoc, PhononImgDoc


class PhononRester(BaseRester):

    suffix = "phonon"
    document_model = PhononBSDoc  # type: ignore


class PhononImgRester(BaseRester):

    suffix = "phonon_img"
    document_model = PhononImgDoc  # type: ignore
